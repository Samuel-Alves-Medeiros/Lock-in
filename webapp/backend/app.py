import os
from dotenv import load_dotenv
from flask import Flask, request,jsonify, session
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
CORS(
    app,
    origins=["http://127.0.0.1:5500"],
    supports_credentials=True
)

load_dotenv()
secret_key = os.getenv("FLASK_SECRET_KEY")

if not secret_key:
    raise RuntimeError("FLASK_SECRET_KEY não foi definida")
    
app.config["SECRET_KEY"] = secret_key



# --> Permite acessar as colunas pelo nome. Ex.: user['pssword']
def connect_database():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn



# Cria a tabela 'users' no banco de dados
def init_db():
    conn = connect_database()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    query = """CREATE TABLE IF NOT EXISTS pomo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    duration INTEGER NOT NULL,
    completed_at TEXT DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
      )"""
    
    cursor.execute(query)
    conn.commit()
    conn.close()



@app.route('/signup', methods=['POST'])
def signup_user():
    dados = request.get_json()
    email = dados.get('email')
    name = dados.get('name')
    password = dados.get('password')

    if not email or not name or not password:
        return jsonify({"erro": "preencha todos os campos"}), 400

    #Criptografa a senha criando um hash
    hashed_password = generate_password_hash(password)

    try:
        conn = connect_database()    
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (email, name, password) VALUES (?, ?, ?)",
                       (email, name, hashed_password))
        conn.commit()

        return jsonify({"message":"Usuário cadastrado com sucesso!!"}), 201
    
    except sqlite3.IntegrityError:
        return jsonify({"erro":"Conta já exite no banco de dados"}), 400
    except Exception as e:
        print(repr(e))
        return jsonify({"erro": "Erro interno no servidor"}), 500
    finally:
        conn.close()

@app.route('/login', methods=['POST'])
def check_user():

    dados = request.get_json(silent=True)
    email = dados.get('email')
    password = dados.get('password')

    if not email or not password:
        return jsonify({"erro": "Email and password field must be fufilled"}), 400

    conn = connect_database()

    try:

        user = conn.execute("SELECT id, name, password FROM users WHERE email = ? ", (email,)
        ).fetchone()

        if user is None:
            return jsonify({"erro": "Email or passwor are incorrects"}), 401
            
        saved_hash = user["password"]

        if not check_password_hash(saved_hash, password):
            return jsonify({"erro": "Email or password are incorrects"}), 401

        session.clear()
        session["user_id"] = user["id"]
            
        return jsonify({
            "message" : "Login aproved",
            "id" : user['id'],
            "name" : user['name'],
            "email" : email
        }), 200
        
    except Exception as e:
        print(repr(e))
        return jsonify({"erro": "Erro interno no servidor"}), 500
    
    finally:
        conn.close()

@app.route("/api/me", methods=["GET"])
def get_current_user():
    user_id = session.get("user_id")
    if user_id == None:
        return jsonify({"erro": "usuário não autenticado"}), 401
    
    return jsonify({
       "authenticated" : True,
        "user_id": user_id
    }), 200

@app.route("/sessions", methods=["POST"])
def cadastrar_sessions():

    user_id = session.get("user_id")

    if user_id is None:
        return jsonify({"erro": "Usuário não autenticado"}), 401

    dados = request.get_json()

    if dados == None:
        return jsonify({"Falha ao enviar sessões"}), 400

    mode = dados.get("mode")
    duration = dados.get("duration")

    if mode != "focus":
        return jsonify({"erro": "Somente sessões de foco são registradas"}), 400

    if not isinstance(duration, int) or duration <= 0:
        return jsonify({"erro": "Duração inválida"}), 400

    conn = connect_database()

    try:
        cursor = conn.cursor()
        query = "INSERT INTO pomo (user_id, duration) VALUES (?,?)"
        cursor.execute(query, (user_id, duration,))
        conn.commit()

        return jsonify({"message": "Sessão registrada com sucesso"}), 201
    
    except sqlite3.Error:
        app.logger.exception("Erro ao registrar sessão")

        return jsonify({"erro": "Erro ao registrar sessão"}), 500
    
    finally:
        conn.close()


@app.route("/sessions", methods=["GET"])
def get_sessions():

    user_id = session.get("user_id")

    if user_id is None:
        return jsonify({"erro": "Usuário não autenticado"}), 401

    conn = connect_database()

    try:
        result = conn.execute("""
            SELECT COUNT (*) AS total
            FROM pomo WHERE user_id = ?
        """, (user_id,)).fetchone()

        return jsonify({"completed_sessions": result["total"]}), 200
    finally:
        conn.close()



if __name__ == "__main__":
    init_db()
    app.run(debug = True)