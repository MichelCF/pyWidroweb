#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:45:10 2019

@author: Michel Vieira Caiafa
"""

import os
from tkinter import *
from tkinter import filedialog
import sys
import pyHidroweb

# By Vitor

# ABRE ARQUIVO DE ENTRADA
root    = Tk()
entrada = filedialog.askopenfile(mode='r')
root.destroy()
if (entrada == None):
    sair = raw_input('\tArquivo de entrada nao selecionado. \n\t\tPressione enter para sair.\n')
    sys.exit()
pathname = os.path.dirname(entrada.name) #define o path de trabalho igual ao do arquivo de entrada
os.chdir(pathname)  #muda caminho de trabalho.

conteudo_linha = entrada.read().split("\n")#pega todos os ids das estacoes e coloca em uma lista
conteudo_linha.remove('')
print(conteudo_linha, "\n")

for estacao in conteudo_linha:
    pyHidroweb.download_hidroweb(estacao)