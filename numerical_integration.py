##################################################################################
# Script para aproximacao de integral por somas finitas dados pares (x,y).
# Metodos empregados sao Regra do Retangulo, Regra do Trapezio e 1/3 de Simpson.
# INPE, Sao Jose dos Campos, SP, Brasil - 27 de Marco de 2020
# Leonardo Sattler Cassara - leocassara@igeo.ufrj.br
##################################################################################
#=================================================================================
#                                  IMPORTACOES
#---------------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
#=================================================================================
#                                    INPUTS
#---------------------------------------------------------------------------------
# X = pontos x0, x1, ..., xn
# Y = pontos y0, y1, ..., yn
#---------------------------------------------------------------------------------
X = [ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20]
Y = [0, 1.8, 2, 4, 4, 6, 4, 3.6, 3.4, 2.8, 0]
#=================================================================================
#                              REGRA DO RETANGULO 
#---------------------------------------------------------------------------------
# Soma de Riemman pela direita
#---------------------------------------------------------------------------------
def retangulo_direita(X,Y):
    X = np.array(X, dtype=float)
    Y = np.array(Y, dtype=float)
    #
    integral = 0
    for indx in range(len(X)-1):
        delta_x = (X[indx+1] - X[indx])
        integral = integral + (Y[indx+1] * delta_x)
        #print(X[indx], X[indx+1], Y[indx+1])
    return integral
#---------------------------------------------------------------------------------
# Soma de Riemman pela esquerda
#---------------------------------------------------------------------------------
def retangulo_esquerda(X,Y):
    X = np.array(X, dtype=float)
    Y = np.array(Y, dtype=float)
    #
    integral = 0
    for indx in range(len(X)-1):
        delta_x = (X[indx+1] - X[indx])
        integral = integral + (Y[indx] * delta_x)
        #print(X[indx], X[indx+1], Y[indx])
    return integral
#=================================================================================
#                                REGRA DO TRAPEZIO
#---------------------------------------------------------------------------------
#     (ou formula fechada de Newton-Cotes para polinomios de primeiro grau)
#---------------------------------------------------------------------------------
def trapezio(X, Y):
    X = np.array(X, dtype=float)
    Y = np.array(Y, dtype=float)
    # definindo passo h
    h = abs(X[0] - X[1])
    # somando termos de x_1 ate x_(n-1)
    termos_do_meio = 0
    for yi in Y[1:-1]:
        termos_do_meio = termos_do_meio + yi
    termos_do_meio = 2 * termos_do_meio
    #
    integral = (h/2.) * (Y[0] + termos_do_meio + Y[-1])
    #
    return integral
#=================================================================================
#                              REGRA 1/3 DE SIMPSON
#---------------------------------------------------------------------------------
#     (ou formula fechada de Newton-Cotes para polinomios de segundo grau)
#---------------------------------------------------------------------------------
def um_terco_Simpson(X, Y):
    X = np.array(X, dtype=float)
    Y = np.array(Y, dtype=float)
    # definindo passo h
    h = abs(X[0] - X[1])
    # somando termos de x_1 ate x_(n-1)
    termos_2 = np.arange(2,len(Y)-1,2)
    termos_4 = np.arange(1,len(Y)-1,2)
    #
    integral_2 = np.sum(Y[termos_2])
    integral_4 = np.sum(Y[termos_4])
    integral = (h/3.)*(Y[0] + 4*integral_4 + 2*integral_2 + Y[-1])
    #
    return integral
#=================================================================================
#                             PRINTANDO RESULTADOS
#---------------------------------------------------------------------------------
print('Retangulo (direita): ',  retangulo_direita(X,Y))
print('Retangulo (esquerda): ', retangulo_esquerda(X,Y))
print('Trapezio: ', trapezio(X, Y))
print('Um terco de Simpson: ', um_terco_Simpson(X, Y))
#=================================================================================
#                                      FIM
#=================================================================================
