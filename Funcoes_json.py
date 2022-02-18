# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:44:08 2022

@author: hbuzzi
"""
import json
import os

def chamarMenu():
    escolha = int(input("Digite: \n<1> para registrar ativo\n<2> para exibir ativos armazenados\n:"))
    return escolha

def ler_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo,'r') as arq_json:
            dicionario = json.load(arq_json)
    else: dicionario = {}
    return dicionario

def registrar(dicionario,arquivo):
    resp="S"
    while resp=="S":
        dicionario[input("Digite o número patrimonial: ")]=[
        input("Digite a data da última atualização: "),
        input("Digite a descrição: "),
        input("Digite o departamento: ")]
        resp=input("Digite <S> para continuar: ").upper()
        gravar_arquivo(dicionario, arquivo)
        print('JSON Gerado!!')
    return

def gravar_arquivo(dicionario,arquivo):
    with open(arquivo,'w') as arq_json:
        json.dump(dicionario, arq_json)
    return
        
            
def exibir(arquivo):
    with open(arquivo, "r") as arq_json:
        conteudo = json.load(arq_json)
        for chave,dado in conteudo.items():
            print('Data: ', dado[0])
            print('Descrição: ', dado[1])
            print('Departamento: ', dado[2])
    return
