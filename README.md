# API RESTful para gerenciar de eventos

**Autores:** [Lucas Lima](https://github.com/lucasouzamil) e [Luiz Pini](https://github.com/luizehp)

[Vídeo de apresentação](https://youtu.be/odRsZW2olWc)

Este projeto é uma API RESTful construída com FastAPI.

## Requisitos

- Python 3.8+

## Instalação e Configuração

Na raiz do projeto siga os seguintes passos:

### 1. Criar um ambiente virtual

#### Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

#### MacOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Instalar dependências:

```bash
pip install -r requirements.txt
```

### 3. Executar a API:

```bash
fastapi dev main.py
```

Acesse a API em [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 4. Documentação da API:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
