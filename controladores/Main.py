# coding=utf-8
import urllib

import html2text
import requests
from bs4 import BeautifulSoup
from nltk import sent_tokenize
from nltk.corpus import stopwords

from controladores.ControladorBase import ControladorBase
from libs.Traductor import Traductor
from libs.Utiles import inicializar_y_capturar_excepciones
from vistas.Main import MainView


class MainController(ControladorBase):

    def __init__(self):
        super(MainController, self).__init__()
        self.view = MainView()
        self.view.initUi()
        self.conectarWidgets()

    def conectarWidgets(self):
        self.view.btnCerrar.clicked.connect(self.view.Cerrar)
        self.view.btnTraducir.clicked.connect(self.onClickBtnTraducir)

    @inicializar_y_capturar_excepciones
    def onClickBtnTraducir(self, *args, **kwargs):

        if self.view.textURL.text(): #si tiene algo en la url primero bajo el contenido
            self.BajarTextoURL()

        traduccion = Traductor()
        traduccion.Traduccion(text=self.view.textTextoTraducir.toPlainText(),
                              source=self.view.cboIdiomaDesde.text(),
                              target=self.view.cboIdiomaHasta.text())
        if traduccion.traducido:
            self.view.textTraducido.setText(
                traduccion.traducido
            )

    @inicializar_y_capturar_excepciones
    def BajarTextoURL(self, *args, **kwargs):
        # response = urllib.request.urlopen(self.view.textURL.text())
        # html = response.read()
        # soup = BeautifulSoup(html, "html.parser")
        # text = soup.get_text(strip=True)
        # # # tokens = [t for t in text.split()]

        res = requests.get(self.view.textURL.text())
        h = html2text.HTML2Text()
        h.ignore_links = True
        self.view.textTextoTraducir.setText(
            h.handle(res.text)
        )
        # stopWords = set(stopwords.words('english'))
        # texto = ''
        # tokens = sent_tokenize(text)
        # for t in  tokens:
        #     texto += t
        # self.view.textTextoTraducir.setText(
        #     texto
        # )