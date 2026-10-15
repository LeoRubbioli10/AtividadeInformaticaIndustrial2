import socket
import threading
import cv2
import os
from imagem import Imagem
import protocolo

def processar_imagem(img_obj):
    """
    Recebe um objeto Imagem, detecta faces e desenha retângulos verdes.
    Retorna o próprio objeto atualizado.
    """
    # Cada thread deve instanciar seu próprio classificador[cite: 2]
    caminho_base_cv2 = os.path.dirname(cv2.__file__)
    xml_classificador = os.path.join(caminho_base_cv2, 'data', 'haarcascade_frontalface_default.xml')
    
    face_cascade = cv2.CascadeClassifier(xml_classificador)
    
    # Processa a imagem usando o atributo 'matriz' do objeto
    gray = cv2.cvtColor(img_obj.matriz, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Desenha retângulos nas áreas onde as faces foram detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(img_obj.matriz, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    return img_obj

class ServidorMT():
    """
    Classe Servidor MultiThread - API Socket
    """
    #Classe construtora
    def __init__(self, host, port):

    def start(self):
        """
        Método que inicializa a execução do servidor
        """

    def _service(self, con, client):
        """
        Método que atende cada cliente em uma thread isolada.
        :param con: objeto socket utilizado para enviar e receber dados
        :param client: é o endereço do cliente
        """