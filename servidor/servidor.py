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
        self._host = host
        self._port = port
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """
        Método que inicializa a execução do servidor
        """
        endpoint = (self._host, self._port)
        try:
            self.__tcp.bind(endpoint)
            self.__tcp.listen(5) # Permite enfileirar algumas conexões
            print(f"Servidor iniciado em {self._host}:{self._port}")
            
            # Laço de accept que inicia a thread e volta a esperar, sem join()[cite: 2]
            while True:
                con, client = self.__tcp.accept()
                
                # Inicia uma nova thread para atender o cliente[cite: 1]
                t = threading.Thread(target=self._service, args=(con, client))
                t.start()

        except Exception as e:
            print("Erro ao inicializar o servidor:", e.args)
        finally:
            self.__tcp.close()

    def _service(self, con, client):
        """
        Método que atende cada cliente em uma thread isolada.
        :param con: objeto socket utilizado para enviar e receber dados
        :param client: é o endereço do cliente
        """
        print(f"[{client}] Iniciou o atendimento.")
        
        try:
            # IMPORTANTE: Para o teste 3, você deve colocar o time.sleep(5) AQUI.
            # import time; time.sleep(5)
            
            # 1. Recebe os bytes da imagem enviada pelo cliente usando o protocolo
            dados_recebidos = protocolo.receber_mensagem(con)
            if not dados_recebidos:
                print(f"[{client}] Nenhum dado recebido.")
                return

            # 2. Instancia a imagem e decodifica[cite: 2]
            img = Imagem()
            img.decodificar(dados_recebidos)

            # 3. Executa o processamento[cite: 2]
            img_processada = processar_imagem(img)

            # 4. Codifica a imagem processada para bytes JPEG[cite: 2]
            dados_resposta = img_processada.codificar()

            # 5. Envia a resposta de volta ao cliente usando o protocolo
            protocolo.enviar_mensagem(con, dados_resposta)
            
            print(f"[{client}] Terminou. Imagem processada e enviada.")
            
        except Exception as e:
            # Uma falha em um atendimento não deve encerrar o servidor[cite: 2]
            print(f"[{client}] Erro durante o atendimento: {e}")
        finally:
            # Fecha os sockets ao terminar[cite: 2]
            con.close()