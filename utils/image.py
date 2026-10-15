import cv2
import numpy as np

class Imagem:
    def __init__(self):
        # Mantém a matriz em um atributo do objeto
        self.matriz = None 

    def ler(self, caminho):
        # Lê um arquivo[cite: 1]
        self.matriz = cv2.imread(caminho)
        if self.matriz is None:
            print(f"Erro ao carregar a imagem: {caminho}")

    def codificar(self):
        # Codifica em JPEG[cite: 1]
        if self.matriz is None:
            raise ValueError("Não há imagem para codificar.")
            
        _, img_bytes = cv2.imencode('.jpg', self.matriz) 
        return bytes(img_bytes)
        
    def decodificar(self, dados):
        # Decodifica bytes JPEG[cite: 1]
        array_numpy = np.frombuffer(dados, np.uint8)
        self.matriz = cv2.imdecode(array_numpy, cv2.IMREAD_COLOR)