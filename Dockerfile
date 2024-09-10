#para hacerlo andar:
#docker build -t flaskapp .

FROM alpine:3.19

RUN apk add --no-cache python3 py3-pip
RUN pip3 install --no-cache-dir --upgrade pip

#directorio que se crea dentro del contenedor
WORKDIR /app 

#copia todo dentro del directorio app del contenedor
COPY . /app

RUN pip3 install --no-cache-dir install -r requirements.txt

CMD [ "python", "backend/app.py" ]