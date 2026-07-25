🧪 FastAPI Todo App — Testes Automatizados com Playwright

Projeto desenvolvido para demonstrar a implementação de testes automatizados End-to-End (E2E) utilizando Playwright em uma aplicação web construída com FastAPI.

A aplicação consiste em um sistema de gerenciamento de tarefas (Todo App), com autenticação de usuários, CRUD de tarefas e persistência em banco de dados PostgreSQL. O foco deste projeto é validar o comportamento da aplicação por meio de testes automatizados que simulam a interação real de um usuário.

🌐 Aplicação Online

A aplicação está disponível para acesso em:

https://ph-todoapp.onrender.com/auth/login-page

🎯 Objetivos do Projeto
Desenvolver uma aplicação web utilizando FastAPI.
Implementar autenticação baseada em JWT.
Validar funcionalidades através de testes End-to-End.
Aplicar boas práticas de automação de testes.
Demonstrar conhecimentos em QA e Testes de Software.
🚀 Tecnologias Utilizadas
Backend
Python
FastAPI
SQLAlchemy
PostgreSQL
Alembic
Jinja2
Testes
Playwright
Pytest
FastAPI TestClient
✅ Funcionalidades Testadas

Os cenários automatizados cobrem funcionalidades essenciais da aplicação, como:

Login de usuários
Cadastro de usuários
Logout
Criação de tarefas
Atualização de tarefas
Exclusão de tarefas
Validação de campos obrigatórios
Fluxos de autenticação
Controle de acesso às páginas protegidas
🧪 Automação com Playwright

Os testes End-to-End foram desenvolvidos utilizando o Playwright, simulando a navegação de um usuário real na aplicação.

Entre as validações realizadas estão:

Navegação entre páginas
Preenchimento de formulários
Cliques em botões e links
Verificação de mensagens de sucesso e erro
Validação de redirecionamentos
Fluxos completos de autenticação
Validação do comportamento esperado da interface
▶️ Executando os Testes

Instale as dependências:

pip install -r requirements.txt

Execute os testes automatizados:

pytest

Caso utilize apenas os testes do Playwright:

pytest tests/

Ou execute diretamente pelo Playwright:

playwright test
📂 Estrutura do Projeto
FastAPI-TodoApp/
│
├── TodoApp/
│   ├── routers/
│   ├── templates/
│   ├── static/
│   ├── alembic/
│   └── ...
│
├── tests/
│
├── requirements.txt
├── README.md
└── .env.example
📖 Documentação da API

O FastAPI disponibiliza documentação automática.

Swagger:

http://127.0.0.1:8000/docs

ReDoc:

http://127.0.0.1:8000/redoc
📌 Competências Demonstradas

Este projeto demonstra conhecimentos em:

Desenvolvimento Backend com FastAPI
Arquitetura REST
SQLAlchemy ORM
PostgreSQL
Autenticação JWT
Testes automatizados End-to-End
Automação com Playwright
Testes com Pytest
Versionamento com Git e GitHub
Boas práticas de Engenharia de Software
💡 Próximas Evoluções
Integração Contínua (GitHub Actions)
Execução automática dos testes a cada push
Relatórios de cobertura
Geração de relatórios HTML do Playwright
Docker e Docker Compose
Testes de desempenho
👨‍💻 Autor

Projeto desenvolvido com foco em estudos de Desenvolvimento Backend e Automação de Testes, utilizando FastAPI e Playwright para demonstrar a implementação de testes automatizados em uma aplicação web real.
