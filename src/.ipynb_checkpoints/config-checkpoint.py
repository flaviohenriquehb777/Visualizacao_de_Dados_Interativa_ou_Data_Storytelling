import os

# Define o diretório base do projeto (um nível acima da pasta 'src')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define os caminhos para as pastas principais
DATA_DIR = os.path.join(BASE_DIR, 'data')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')
NOTEBOOKS_DIR = os.path.join(BASE_DIR, 'notebooks') # Apenas para referência, não será usado diretamente no notebook

# Garante que as pastas existam
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(MEDIA_DIR, exist_ok=True)