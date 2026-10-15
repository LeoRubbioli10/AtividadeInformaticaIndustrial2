# Funções para receber e enviar bytes, com o cabeçalho do tamanho.
# Esse módulo não precisa conhecer OpenCV nem a classe Image, apenas manipula bytes.

def enviar_imagem(sock, dados):

    # Envia os bytes da imagem com um cabeçalho de 4 bytes, indicando seu tamanho.
    tamanho = len(dados).to_bytes(4, 'big')

    sock.sendall(tamanho)
    sock.sendall(dados)

def receber_imagem_completo(sock, tamanho): 

    dados = b''

    while len(dados) < tamanho:
        pacote = sock.recv(tamanho - len(dados))
        if not pacote:
            raise ConnectionError("Conexão encerrada antes do recebimento completo")
        
        dados += pacote

    return dados

def receber_imagem(sock):
    # Recebe os 4 bytes do cabeçalho.
    cabecalho = receber_imagem_completo(sock, 4)
    tamanho = int.from_bytes(cabecalho, 'big')

    # Recebe os bytes da imagem.
    dados = receber_imagem_completo(sock, tamanho)

    return dados