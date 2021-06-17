From python:3.7-slim-buster
RUN apt-get update && apt-get install g++ gcc  cmake -y
RUN pip install --upgrade pip && pip install face_recognition flask numpy flask_restful werkzeug pybase64
RUN apt-get update && apt-get install -y  libglib2.0-0 libsm6 libxrender1 libfontconfig1 libxext6 libgl1-mesa-glx
RUN pip install opencv-python 
RUN pip install imutils pillow
COPY . /app
WORKDIR /app
EXPOSE 5000
CMD ["python","app.py"]