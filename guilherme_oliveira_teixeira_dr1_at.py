# -*- coding: utf-8 -*-
"""Guilherme_Oliveira_Teixeira_DR1_AT

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LnyMpHzOgCFNOE5mMpE495qOjwCnMcdT
"""

def calculaGastos ():
  rendaMensalTotal = int(input("Renda Mensal total: R$"))
  gastos = []
  gastos.append(int(input("Gastos totais com moradia: R$")))
  gastos.append(int(input("Gastos totais com educação: R$")))
  gastos.append(int(input("Gastos totais com transporte: R$")))

  porcentagemGastaComMoradia = int((rendaMensalTotal*30) / 100)
  porcentagemGastaComEducacao = int((rendaMensalTotal*20) / 100)
  porcentagemGastaComTransporte = int((rendaMensalTotal*15) / 100)

  diagnostico =""

  print(gastos[0],porcentagemGastaComMoradia)
  if porcentagemGastaComMoradia < gastos[0] :
    porcentagem = int((gastos[0]/rendaMensalTotal) * 100)
    diagnostico += f"Seus gastos totais com moradia comprometem  {porcentagem}% de sua renda total. O máximo recomendado é de 30%. Portanto, idealmente o máximo de sua renda comprometida com moradia deveria ser de R$ {porcentagemGastaComMoradia}"
  else:
    porcentagem = int((gastos[0]/rendaMensalTotal) * 100)
    diagnostico += f"\n Seus gastos totais com moradia comprometem {2}% de sua renda total. O máximo recomendado é de 30%. Seus gastos estão dentro da margem recomendada."
  
  
  if porcentagemGastaComEducacao < gastos[1] :
    porcentagem = int((gastos[1]/rendaMensalTotal) * 100)
    diagnostico += f"\n Seus gastos totais com educação comprometem  {porcentagem}% de sua renda total. O máximo recomendado é de 20%. Portanto, idealmente o máximo de sua renda comprometida com educação deveria ser de R$ {porcentagemGastaComEducacao}"
  else: 
    porcentagem = int((gastos[1]/rendaMensalTotal) * 100)
    diagnostico += f"\n Seus gastos totais com educação comprometem {porcentagem}% de sua renda total. O máximo recomendado é de 20%. Seus gastos estão dentro da margem recomendada."


  if porcentagemGastaComTransporte < gastos[2] :
    porcentagem = int((gastos[2]/rendaMensalTotal) * 100)
    diagnostico += f"\n Seus gastos totais com educação comprometem R$ {porcentagem}% de sua renda total. O máximo recomendado é de 15%. Portanto, idealmente o máximo de sua renda comprometida com transporte deveria ser de R$ {porcentagemGastaComTransporte}"
  else: 
    porcentagem = int((gastos[2]/rendaMensalTotal) * 100)
    diagnostico += f"\n Seus gastos totais com educação comprometem {porcentagem}% de sua renda total. O máximo recomendado é de 15%. Seus gastos estão dentro da margem recomendada."

  print('Diagnóstico')
  print(diagnostico)

calculaGastos()

#Valor inicial: R$ 10000
#Rendimento por período (%): 0.54
#Aporte a cada período: R$ 1000
#Total de períodos: 120 

#Após 1 períodos(s), o montante será de R$11054.00.
#Após 2 períodos(s), o montante será de R$12113.69.
#Após 3 períodos(s), o montante será de R$13179.11.
#Após 4 períodos(s), o montante será de R$14250.27.
#Após 5 períodos(s), o montante será de R$15327.22.
#(...)
#Após 115 períodos(s), o montante será de R$177406.76.
#Após 116 períodos(s), o montante será de R$179364.76.
#Após 117 períodos(s), o montante será de R$181333.33.
#Após 118 períodos(s), o montante será de R$183312.53.
#Após 119 períodos(s), o montante será de R$185302.42.
#Após 120 períodos(s), o montante será de R$187303.05.

import matplotlib.pyplot

def jurosCompostos():
  valorInicial = int(input("Valor inicial: R$"))
  rendimentoPorMes = float(input("Rendimento por mês (%): "))
  aportePorMes = int(input("Aporte por mês: "))
  totalMes = int(input("total de meses: "))
  montante = []
  meses = []

  for i in range(totalMes):
    porcentagemJuros = (valorInicial*rendimentoPorMes) / 100
    valorInicial += porcentagemJuros
    valorInicial += aportePorMes
    montante.append(valorInicial)
    meses.append(i+1)
    print(f"Após {i+1} Meses, o montante será de R${valorInicial:.2f}")

  matplotlib.pyplot.plot(meses,montante)
  matplotlib.pyplot.ylabel("Montante")
  matplotlib.pyplot.xlabel("Períodos")
jurosCompostos()



import matplotlib.pyplot
import pandas as pd
import numpy as np 


def pibGrafico():
  pais = input('Entre com o nome do País: ')

  paises = pd.read_csv (r'./Assessment_PIBs - Planilha1.csv')
  
  df = pd.read_csv (r'./Assessment_PIBs - Planilha1.csv')
  headers = pd.read_csv(r'./Assessment_PIBs - Planilha1.csv', index_col=0, nrows=0).columns.tolist()
  paisAnalise = []
  for i in df.values:
    if i[0] == pais:
      paisAnalise.append(i)

  paisAnalise = np.array(paisAnalise)
  index = np.argwhere(paisAnalise==pais)
  y = np.delete(paisAnalise, index)
  matplotlib.pyplot.plot(headers,y)
  matplotlib.pyplot.ylabel("PIB")
  matplotlib.pyplot.xlabel("Anos")

pibGrafico()