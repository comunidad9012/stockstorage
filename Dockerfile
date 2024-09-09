FROM python:3
 #directorio que se crea en el contendor
WORKDIR /app

#variables de flask, indicamos donde esta el archivo principal
ENV FLASK_APP app.py 
ENV FLASK_RUN_HOST 0.0.0.0

#ruta donde se encuentra el requirements y ruta a donde sera copiado (/app/)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

#copia todos los demas archivos al contenedor
COPY . /app 
EXPOSE 5000
CMD ["python", "app.py"]