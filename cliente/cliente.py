import socket

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

            # A comunicação de imagens será implementada depois.

        except OSError as e:
            print("Erro ao conectar com o servidor:", e)

        finally:
            self.__tcp.close()
