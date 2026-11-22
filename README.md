# Lock in space
## English
Lock in space is a personal project designed for daily organization and task management. I combined the main productivity and study tools into a single simple, intuitive, and useful application.

    🚧 ongoing.... 🛠️

##

## Technologies

[![My Skills](https://skillicons.dev/icons?i=html,css,js,py,flask,sqlite&theme=dark)](https://skillicons.dev)

## Funcionalidades

- [x] Cadastro e autenticação de usuários.
- [x] Temporizador Pomodoro.
- [ ] Gerenciamento de tarefas.
- [ ] Quadro Kanban.
- [ ] Anotações pessoais.
- [ ] Checklists.
- [ ] Estatísticas de produtividade.

## Português
Lock in space é um projeto pessoal feito para a organização do dia a dia e o gerenciamento de projetos pessoais. A ideia é combinar as principais ferramentas de estudos e organização pessoal em uma aplicação única, simples e intuitiva.

status: 🚧 Em construção 🚧 </br>
![](https://geps.dev/progress/40) 


### Preview

![página completa](<webapp/frontend/images/Lockin space photos/pagina-inteira.png>)
--
**Logos e imagens de template provisórias geradas com IA.** ***(Posteriormente a logo e as imagens de template serão substituídas por um design feito por pessoas reais (eu) ***
![página de cadastro](<webapp/frontend/images/Lockin space photos/Criação-de-conta.png>)
![página de login](<webapp/frontend/images/Lockin space photos/Login.png>)
![pomodoro](<webapp/frontend/images/Lockin space photos/pomodoro.png>)
![quadro kanban](<webapp/frontend/images/Lockin space photos/kanban.png>)

### Como rodar localmente?

- **primeiro passo**: Instale a pasta com todos os arquivos do projeto e abra ela no seu editor de código (VS code é a minha recomendação pessoal). Depois, crie um arquivo chamado .env na raiz do projeto e dentro dela escreva "FLASK_SECRET_KEY=chave_super_secreta" (troque o "chave_super_secreta" por uma chave forte que vai servir para assinar as sessões de usuário [Use o comando: python -c "import secrets; print(secrets.token_hex(32))" no terminal para gerar uma chave aleatória.])

- **segundo passo**: tenha certeza de ter a extensão live server instalada no seu vscode para conseguir executar o frontend. Para que a extensão funcione corretamente, crie uma pasta chamada ".vscode" com um arquivo "settings.json" dentro dela. Dentro do arquivo cole o seguinte comando: {
    "python.terminal.useEnvFile": true,

    "liveServer.settings.root": "/webapp/frontend",
    "liveServer.settings.ignoreFiles": [
        ".vscode/**",
        "**/*.scss",
        "**/*.sass",
        "**/*.ts",
        "**/database.db",
        "**/*.sqlite",
        "**/*.sqlite3"
    ]
}

- **terceiro passo**: instale as bibliotecas necessárias para o funcionamento do backend. Para isso, primeiro crie um virtual environment "venv" dentro na raiz do projeto:
#### Linux
- execute o comando: python -m venv .venv -> Criar venv
- source .venv/bin/activate -> Executar venv

#### Windows
- execute o comando: python -m venv .venv -> Criar venv
- .\.venv\Scripts\Activate.ps1 -> Executar venv

Após isso instale as bibliotecas e módulos necessários
Digite o seguinte comandos no terminal: 

- python -m pip install -r requirements.txt

- **quarto e ultimo passo**: execute o backend clicando no botão run pyhthon file no seu vscode (tenha certeza de ter o python intalado corretamente e suas extensões no vscode). Assim que o backend iniciar, abara o arquivo index.html (./webapp/frontend/pages/index.html) usando o live server. Crie sua conta e faça login. Pronto, se tudo der certo você conseguirar experimentar o aplicativo Lock in space :)

### Atenção! A instalação e execução do aplicativo por enquanto é bastante complicada e exige muito esforço, isso se deve ao fato de ele ainda estar em desenvolvimento, futuramente eu planejo transformar ele em uma aplicação executada nativamente no pc com apenas um clique, e em um site disponível no meu github pages onde você só precisara executar o backend de forma manual. 
