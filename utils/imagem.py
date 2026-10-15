import cv2
import os
import numpy as np

class Imagem:

    #Método construtor da classe
    def __init__(self, caminho_imagem = None):
        self.img = None #Atributo que se guarda pixels da imagem

        #Se um caminho for passado na criação do objeto, a imagem será lida
        if caminho_imagem:
            self.lerArquivo(caminho_imagem)

    #Método para ler arquivo de imagem
    def lerArquivo(self, caminho_imagem):
        self.img = cv2.imread(caminho_imagem)
        if self.img is None:
            print(f"Erro ao carregar a imagem: {caminho_imagem}")

    #Método para codificação de imagem
    def codificarImagem(self):

        if self.img is None:
            print("Nenhuma imagem carregada para codificação.")
            raise ValueError("Nenhuma imagem carregada para codificação. Leia um arquivo primeiro.")
        
        _, img_bytes = cv2.imencode('.jpg', self.img) 
        img_bytes = bytes(img_bytes)

        # O tamanho (4 bytes) geralmente é usado para rede. 
        # Como a classe não faz comunicação, retornamos os bytes e o tamanho separadamente.
        tamanho_da_imagem_codificado = len(img_bytes).to_bytes(4, 'big')
        
        return img_bytes, tamanho_da_imagem_codificado
        
    #Classe para decodificar a imagem a partir de bytes
    def decodificaBytes(self, img_bytes):
        # Transforma os bytes de volta em uma matriz numpy e decodifica para pixels
        array_numpy = np.frombuffer(img_bytes, np.uint8)
        self.img = cv2.imdecode(array_numpy, cv2.IMREAD_COLOR)