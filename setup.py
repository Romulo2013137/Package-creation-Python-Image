# image_processor/__init__.py

from .upload import upload_image
from .processing import process_image
from .filters import apply_filter

# image_processor/upload.py

import os

def upload_image(file_path: str, destination_folder: str):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    destination_path = os.path.join(destination_folder, os.path.basename(file_path))
    with open(file_path, 'rb') as fsrc:
        with open(destination_path, 'wb') as fdst:
            fdst.write(fsrc.read())
    return destination_path

# image_processor/processing.py

from PIL import Image

def process_image(image_path: str, size: tuple):
    with Image.open(image_path) as img:
        img = img.resize(size)
        processed_image_path = f"processed_{size[0]}x{size[1]}_{image_path}"
        img.save(processed_image_path)
    return processed_image_path

# image_processor/filters.py

from PIL import ImageFilter

def apply_filter(image_path: str, filter_type: str):
    with Image.open(image_path) as img:
        if filter_type == 'blur':
            img = img.filter(ImageFilter.BLUR)
        elif filter_type == 'sharpen':
            img = img.filter(ImageFilter.SHARPEN)
        elif filter_type == 'edge_enhance':
            img = img.filter(ImageFilter.EDGE_ENHANCE)
        else:
            raise ValueError("Filter type not recognized. Use 'blur', 'sharpen', or 'edge_enhance'.")
        
        filtered_image_path = f"filtered_{filter_type}_{image_path}"
        img.save(filtered_image_path)
    return filtered_image_path
# setup.py

from setuptools import setup, find_packages

setup(
    name='image_processor',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    description='A simple image processing package',
    author='Seu Nome',
    author_email='seuemail@exemplo.com',
    url='https://github.com/seunome/image_processor',  # Atualize com o URL do seu repositório
)
# Image Processor

Este é um pacote simples para processamento de imagens.

## Instalação

```bash
pip install image_processor

from image_processor import upload_image, process_image, apply_filter

# Fazer upload da imagem
upload_image('caminho/para/imagem.jpg', 'caminho/para/pasta')

# Processar a imagem
process_image('caminho/para/imagem.jpg', (800, 600))

# Aplicar filtro
apply_filter('caminho/para/imagem.jpg', 'blur')


### Instruções

1. Crie os arquivos e pastas conforme a estrutura mencionada.
2. Instale a biblioteca `Pillow` usando `pip install Pillow`.
3. Após criar o pacote, você pode usar o comando `python setup.py sdist` para criar o pacote e, em seguida, subir para o Test PyPI.

Sinta-se à vontade para modificar as funções conforme necessário! Se precisar de mais alguma coisa, estou aqui para ajudar!
