# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:44:08 2022

@author: hbuzzi
"""

def chamarMenu():
    escolha = int(input("Digite: \n<1> para registrar ativo\n<2> para persistir em arquivo\n<3> para exibir ativos armazenados\n:"))
    return escolha

def registrar(dicionario):
    resp="S"
    while resp=="S":
        dicionario[input("Digite o número patrimonial: ")]=[
        input("Digite a data da última atualização: "),
        input("Digite a descrição: "),
        input("Digite o departamento: ")]
        resp=input("Digite <S> para continuar: ").upper()
    return
        
def adicionar(dicionario):
    with open("inventario.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" + 
	valor[1] + ";" + valor[2] +"\n")
    print("Adicionado com sucesso!")
    return
            
def exibir():
    with open("inventario.csv", "r") as inv:
        conteudo = inv.readlines()
        for linha in conteudo:
            separacao = linha[linha.find(';')+1:]
            data = separacao[0:separacao.find(';')]
            separacao = separacao[separacao.find(';')+1:]
            desc = separacao[0:separacao.find(';')]
            dep = separacao[separacao.find(';')+1:]
            print('Data: ', data)
            print('Descrição: ', desc)
            print('Departamento: ', dep)
    return
