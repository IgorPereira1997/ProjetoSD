import random
from datetime import datetime
from io import BytesIO
from django.core.files import File
from PIL import Image


def gerarCodigoUnico(extensao):
    alfabeto = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tamanho = 15
    resultado = "_"
    for i in range(1, tamanho):
        resultado += random.choice(alfabeto)
    date_agora = datetime.now().strftime('%d_%m_%Y%H%M%S')
    return "foto_" + date_agora + resultado + extensao[-4::]


def gerarConhecimento():
    alfabeto = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tamanho = 7
    resultado = ''
    for i in range(1, tamanho):
        resultado += random.choice(alfabeto)
    return resultado


def resize_image(image, size, mod_image=0):
    """Resize image of given size from given image"""
    im = Image.open(image)
    im.load()
    im = im.convert('RGB')  # convert mode
    im = im.resize(size)  # resize image
    output = BytesIO()  # create a BytesIO object
    im.save(output, 'JPEG', quality=100)  # save image to BytesIO object
    if mod_image:
        new_image = File(output, name=(gerarCodigoUnico(image)))
    else:
        new_image = File(output, name=(gerarCodigoUnico(image.name)))  # create a django friendly File object (create new name)
    return new_image
