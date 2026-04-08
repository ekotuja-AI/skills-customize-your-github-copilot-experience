# 📘 Assignment: Construindo APIs REST com framework FastAPI

## 🎯 Objective

Aprender a construir APIs REST utilizando o framework FastAPI em Python, incluindo a criação de endpoints, manipulação de dados e documentação automática.

## 📝 Tasks

### 🛠️ Configurar Aplicação FastAPI Básica

#### Description
Instale o FastAPI e crie uma aplicação simples com um endpoint raiz que retorna uma mensagem de boas-vindas.

#### Requirements
Completed program should:

- Instalar FastAPI e Uvicorn usando pip
- Criar uma instância de FastAPI
- Definir um endpoint GET na rota "/" que retorna um dicionário com uma mensagem de boas-vindas
- Executar a aplicação usando Uvicorn

### 🛠️ Adicionar Endpoints para Gerenciar Itens

#### Description
Adicione endpoints para listar, criar e obter itens específicos, utilizando uma lista em memória para armazenar os dados.

#### Requirements
Completed program should:

- Criar uma lista ou dicionário para armazenar itens (ex: [{"id": 1, "name": "Item 1"}])
- Definir endpoint GET "/items" que retorna a lista de itens
- Definir endpoint POST "/items" que aceita JSON com "name" e adiciona um novo item com ID único
- Definir endpoint GET "/items/{item_id}" que retorna o item com o ID especificado ou erro 404 se não encontrado
- Usar Pydantic para validar os dados de entrada no POST

### 🛠️ Implementar Documentação e Testes

#### Description
Utilize a documentação automática do FastAPI e teste os endpoints criados.

#### Requirements
Completed program should:

- Acessar a documentação interativa em /docs
- Testar todos os endpoints usando a interface ou ferramentas como curl/Postman
- Adicionar descrições aos endpoints usando docstrings ou parâmetros
- Garantir que a API retorne respostas apropriadas para casos de erro