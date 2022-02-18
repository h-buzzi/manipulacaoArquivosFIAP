# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:23:39 2022

@author: hbuzzi
"""
from Funcoes import *

inventario={}
opcao= chamarMenu()
while opcao>0 and opcao<4:
    if opcao==1:
        registrar(inventario)
    elif opcao==2:
        adicionar(inventario)
    elif opcao==3:
        exibir()
    opcao= chamarMenu()