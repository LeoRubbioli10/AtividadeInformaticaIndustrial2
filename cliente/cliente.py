import socket

from utils.protocolo import enviar_imagem as enviar

class Cliente:
    """
    Classe Cliente - API Socket
    """
    def __init__(self, server_ip, port):
        """
        Construtor da classe Cliente.
        """
        self.__server_ip = server_ip
        self.__port = port
        self.__tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """
        Inicializa a conexão TCP com o servidor.
        """
        endpoint = (self.__server_ip, self.__port)

        try:
            self.__tcp.connect(endpoint)
            print("Conexão realizada com sucesso!")

            self.__envia_imagem("tests/image_001.jpg")

        except OSError as e:
            print("Erro ao conectar com o servidor:", e)

        finally:
            self.__tcp.close()

    def __envia_imagem(self, image_path):
        """
        Envia uma imagem JPEG para o servidor.
        """
        with open(image_path, 'rb') as f:
            dados = f.read()

        enviar(self.__tcp, dados)
        print("Imagem enviada com sucesso!")