# coding=utf-8
import html2text
import requests

from controladores.ControladorBase import ControladorBase
from libs.Traductor import Traductor
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

    def onClickBtnTraducir(self):

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

    def BajarTextoURL(self):
        res = requests.get(self.view.textURL.text())
        h = html2text.HTML2Text()
        h.ignore_links = True
        self.view.textTextoTraducir.setText(
            h.handle(res.text)
        )