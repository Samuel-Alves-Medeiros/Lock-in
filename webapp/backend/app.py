import os
from dotenv import load_dotenv
from flask import Flask, request,jsonify, session
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

load_dotenv()
app = Flask(__name__)
CORS(
    app,
    origins=["http://127.0.0.1:5500"],
    supports_credentials=True
)

secret_key = os.getenv("FLASK_SECRET_KEY")

if not secret_key:
    raise RuntimeError("FLASK_SECRET_KEY não foi definida")

app.config["SECRET_KEY"] = secret_key


# Cria a tabela 'users' no banco de dados
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
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
        # O with garante que o banco de dados sempre será fechado 
        with sqlite3.connect('database.db') as conn:
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


# --> Permite acessar as colunas pelo nome. Ex.: user['pssword']
def connect_database():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

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
            
        saved_hash = user['password']

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



if __name__ == "__main__":
    init_db()
    app.run(debug = True)