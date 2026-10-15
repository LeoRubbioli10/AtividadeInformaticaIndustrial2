# Atividade Prática — Informática Industrial (ENE118)

## 1. Descrição

Atividade desenvolvida na disciplina de Informática Industrial (ENE118), do curso de Engenharia Elétrica da Universidade Federal de Juiz de Fora (UFJF).

O projeto consiste em uma aplicação cliente-servidor em Python.

O cliente envia uma imagem JPEG ao servidor, que realiza a detecção de faces utilizando OpenCV, desenha retângulos verdes sobre as faces identificadas e retorna a imagem processada ao cliente.

O desenvolvimento foi realizado em dupla, utilizando Git e GitHub para versionamento, organização e integração do código.

## 2. Integrantes e atribuições

**Lucas de Faria Cristofaro**
- Implementação do módulo `protocolo.py`, responsável pelo envio e recebimento de bytes.
- Desenvolvimento do `cliente.py`, responsável pela conexão, envio da imagem, recebimento e exibição do resultado.

**Leonardo Nunes Rubbioli Cordeiro**
- Adaptação do exemplo de processamento de imagens para a classe `Imagem`, em `image.py`.
- Desenvolvimento do `servidor.py`, incluindo atendimento concorrente de clientes e detecção de faces.

## 3. Organização do projeto

- `cliente.py`: implementação da classe Cliente.
- `servidor.py`: implementação do servidor TCP multithread.
- `utils/image.py`: classe para leitura, codificação e decodificação de imagens.
- `utils/protocolo.py`: funções de envio e recebimento de mensagens TCP.
- `tests/`: imagens de teste e capturas dos resultados.
- `requirements.txt`: dependências Python necessárias.
- `.gitignore`: arquivos e diretórios excluídos do versionamento.

## 4. Funcionamento do protocolo

A comunicação utiliza TCP e mensagens compostas por um cabeçalho de 4 bytes, contendo o tamanho da imagem, seguido pelos bytes JPEG.

A função `enviar_imagem()` utiliza `sendall()` para transmitir o cabeçalho e os dados.

A função `receber_imagem_completo()` utiliza um laço `while` para acumular os bytes recebidos por `recv()` até completar o tamanho esperado. Caso a conexão seja encerrada antecipadamente, uma exceção é gerada.

A função `receber_imagem()` utiliza essa leitura completa primeiro para o cabeçalho e depois para a imagem.

## 5. Programação concorrente

O servidor utiliza `threading.Thread()` para criar uma thread de atendimento para cada cliente conectado.

Dessa forma, o servidor pode continuar aceitando novas conexões enquanto outras threads realizam o processamento das imagens.

Cada atendimento utiliza seu próprio socket de comunicação e realiza o processamento da imagem recebida.

## 7. Testes realizados

Os seguintes testes estão previstos no enunciado:

**Teste 1 — Imagem com face**

Resultado: *A preencher após a execução.*

**Teste 2 — Imagem sem face**

Resultado: *A preencher após a execução.*

**Teste 3 — Dois clientes simultâneos**

Resultado: *A preencher após a execução.*
