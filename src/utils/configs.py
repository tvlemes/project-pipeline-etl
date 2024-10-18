from pathlib import Path

try:
    PASTA_ROOT = Path(__file__).parent.parent.parent # obtém o diretório raiz, o parent equivale a '../'
except:
    raise NotADirectoryError('Diretório não encontrado!')

PASTA_SRC = PASTA_ROOT / "src"
PASTA_LOGS = PASTA_SRC / "logs"
PASTA_DADOS = PASTA_SRC / "dados"
PASTA_UTILS = PASTA_SRC / "utils"
# PASTA_ENTRADA_AQUISICAO = f"{PASTA_DADOS}/externo"
# PASTA_SAIDA_AQUISICAO = f"{PASTA_DADOS}/aquisicao"


# Formas de obter o diretório com path os
# Obter o diretório atual
# current_dir = os.path.dirname(os.path.abspath(__file__))

# Subir para o diretório raiz (ajuste o número de '..' conforme necessário)
# project_root = os.path.abspath(os.path.join(current_dir, '..'))