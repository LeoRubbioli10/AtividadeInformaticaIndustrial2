import sys
import os
# Adiciona a pasta principal ao caminho de busca do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cliente import Cliente

c = Cliente("127.0.0.1", 9000)
c.start()