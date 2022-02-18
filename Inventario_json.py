# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:23:39 2022

@author: hbuzzi
"""
from Funcoes_json import *
import json

arquivo = 'inventario_json.json'
inventario = ler_arquivo(arquivo)

opcao= chamarMenu()
while opcao>0 and opcao<3:
    if opcao==1:
        registrar(inventario,arquivo)
    elif opcao==2:
        exibir(arquivo)
    opcao= chamarMenu()