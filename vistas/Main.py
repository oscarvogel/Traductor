# coding=utf-8
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

from libs.BarraProgreso import Avance
from libs.Botones import BotonCerrarFormulario, Boton
from libs.ComboBox import ComboIdiomas
from libs.EntradaTexto import TextEdit, EntradaTexto
from libs.Etiquetas import EtiquetaTitulo, Etiqueta
from libs.Grillas import Grilla
from libs.Utiles import LeerIni, imagen
from vistas.VistaBase import VistaBase


class MainView(VistaBase):

    def initUi(self):
        self.setGeometry(150, 150, 650, 450)
        layoutPpal = QVBoxLayout(self)

        layoutIdiomas = QHBoxLayout()
        lblDesde = Etiqueta(texto="Desde")
        self.cboIdiomaDesde = ComboIdiomas()
        lblHasta = Etiqueta(texto="Hasta")
        self.cboIdiomaHasta = ComboIdiomas()
        layoutIdiomas.addWidget(lblDesde)
        layoutIdiomas.addWidget(self.cboIdiomaDesde)
        layoutIdiomas.addWidget(lblHasta)
        layoutIdiomas.addWidget(self.cboIdiomaHasta)
        layoutPpal.addLayout(layoutIdiomas)

        layoutPagina = QHBoxLayout()
        lblPagina = Etiqueta(texto="URL de la pagina")
        self.textURL = EntradaTexto()
        layoutPagina.addWidget(lblPagina)
        layoutPagina.addWidget(self.textURL)
        layoutPpal.addLayout(layoutPagina)

        self.textTextoTraducir = TextEdit(placeholdertext="Texto a traducir")
        layoutPpal.addWidget(self.textTextoTraducir)

        self.textTraducido = TextEdit(placeholdertext="Texto traducido")
        layoutPpal.addWidget(self.textTraducido)

        layoutBotones = QHBoxLayout()
        self.btnTraducir = Boton(texto="Tradudir",
                                 imagen=imagen("iconfinder_logo_brand_brands_logos_translate_google_2230965.png"))
        self.btnCerrar = Boton(texto="Salir", imagen=imagen("iconfinder_free-29_618316.png"))
        layoutBotones.addWidget(self.btnTraducir)
        layoutBotones.addWidget(self.btnCerrar)
        layoutPpal.addLayout(layoutBotones)
