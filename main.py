# coding=utf-8
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 3, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTIBILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.
import sys

from PyQt5.QtWidgets import QApplication

from controladores.Main import MainController


def inicio():
    args = []
    app = QApplication(args)
    ex = MainController()
    ex.run()
    sys.exit(app.exec_())

if __name__ == "__main__":
    inicio()