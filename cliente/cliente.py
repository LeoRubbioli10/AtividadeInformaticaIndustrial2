import socket

from utils.protocolo import enviar_imagem as enviar
from utils.protocolo import receber_imagem as receber
from utils.image import Imagem

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

            # Envia a imagem para o servidor
            self.__envia_imagem("tests/image_001.jpg")

            # Recebe a imagem processada do servidor
            dados = self.__recebe_imagem()

            # Decodifica os bytes recebidos em uma imagem
            img = self.__decodifica_imagem(dados)

            # Exibe a imagem decodificada
            self.__exibir_imagem(img)

        except (OSError, ValueError) as e:
            print("Erro durante a comunicação:", e)

        finally:
            self.__tcp.close()

    def __envia_imagem(self, image_path):
        """
        Envia uma imagem JPEG para o servidor.
        """
        dados, _ = Imagem(image_path).codificarImagem()

        enviar(self.__tcp, dados)
        print("Imagem enviada com sucesso!")

    def __recebe_imagem(self):
        """
        Recebe os bytes da imagem processada.
        """
        dados = receber(self.__tcp)
        return dados

    def __decodifica_imagem(self, dados):
        """
        Decodifica os dados da imagem.
        """
        img = Imagem()
        img.decodificaBytes(dados)

        return img

    def __exibir_imagem(self, img):
        """
        Exibe a imagem processada.
        """
        img.mostrar_imagem()