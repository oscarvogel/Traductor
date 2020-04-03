# coding=utf-8
"""
Traducto de palabras realizado con Python
"""

# Importamos la libreria request
import requests
from googletrans import Translator


class Traductor:

    traducido = '' # texto traducido
    a_traducir = '' #texto a traducir
    error = '' #mensaje error

    def Traduccion(self, source = '', target = '', text = ''):
        # params:
        # source: idioma origen
        # target: idioma destino
        # text: texto a traducir
        self.error = ''
        self.traducido = ''
        translator = Translator()
        translated = translator.translate(text, dest=target, src=source)
        self.traducido = translated.text
        return self.traducido