# Imagem base do Python
FROM python:3.13-slim

# Criar diretório de trabalho dentro do container
WORKDIR /app

# Copiar requirements.txt e instalar dependências
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação
COPY . .

# Expõe a porta 8000 (padrão do FastAPI/Uvicorn)
EXPOSE 8010

# Comando para rodar a API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8010"]
