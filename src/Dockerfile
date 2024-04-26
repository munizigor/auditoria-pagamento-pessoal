# Use a imagem oficial do Python
FROM python:3.9-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt requirements.txt

# Instala as dependências listadas no arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do código-fonte para o diretório de trabalho
COPY . .

# Expõe a porta 5000 para que o Flask possa ser acessado de fora do contêiner
EXPOSE 5000

# Comando para iniciar a aplicação quando o contêiner for iniciado
CMD ["python", "app.py"]
