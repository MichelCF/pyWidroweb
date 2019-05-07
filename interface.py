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

#****************---------------correcao de bug--------------********************
if (entrada == None):
    sair = raw_input('\tArquivo de entrada nao selecionado. \n\t\tPressione enter para sair.\n')
    sys.exit()
#****************---------------fim da correcao--------------********************

pathname = os.path.dirname(entrada.name) #define o path de trabalho igual ao do arquivo de entrada
os.chdir(pathname)  #muda caminho de trabalho.

# By Jean
conteudo_linha = entrada.read().split("\n")
conteudo_linha.remove('')

print(conteudo_linha, "\n")

for estacao in conteudo_linha:
    pyHidroweb.download_hidroweb(estacao)[0]