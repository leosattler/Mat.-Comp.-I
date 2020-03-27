##################################################################################
# Script para solucao de Problemas de Valor Inicial (PVIs) definidos por Equacoes
# Diferenciais Ordinarias (EDOs). Metodos empregados sao Metodo de Euler e
# Metodo de Runge-Kutta de segunda, terceira e quarta ordem.
# INPE, Sao Jose dos Campos, SP, Brasil - 27 de Marco de 2020
# Leonardo Sattler Cassara - leocassara@igeo.ufrj.br
##################################################################################
#=================================================================================
#                                  IMPORTACOES
#---------------------------------------------------------------------------------
import numpy as np
#=================================================================================
#                                    INPUTS
#---------------------------------------------------------------------------------
# y_0 = valor inicial de y
# x_0 = valor inicial de x
# x_final = valor final de x
# h = passo de avanco da variavel x
#---------------------------------------------------------------------------------
y_0 = 3.
x_0 = 0.
x_final = 2.
h = .125
#---------------------------------------------------------------------------------
# Definicao da funcao f(x,y) = y' (primeira derivada de y)
#---------------------------------------------------------------------------------
def f(x, y):
    return (2.*y)/(x+1) + (x+1.)**3.
#=================================================================================
#               PREPARANDO INPUTS E DEFININDO VARIAVEIS AUXILIARES
#---------------------------------------------------------------------------------
y_0 = float(y_0)
x_0 = float(x_0)
x_final = float(x_final)
h = float(h)
n_digits = int(str(h).split('.')[-1])
#=================================================================================
#                                METODO DE EULER
#                        (ou metodo de Taylor de ordem 1)
#---------------------------------------------------------------------------------
def euler(y_0, x_0, x_final, h, f):
    # Condicoes iniciais
    x = x_0
    y = y_0
    # Calculando y(x_final)
    while x < x_final:
        y = y + h*f(x, y)
        x = round(x + h, n_digits)
    # 
    return y
#=================================================================================
#                          METODO DE RUNGE-KUTTA DE ORDEM 2
#---------------------------------------------------------------------------------
def runge_kutta_2(y_0, x_0, x_final, h, f):
    # Condicoes iniciais
    x = x_0
    y = y_0
    # coeficientes do RK-2
    a1 = 1/2.
    a2 = 1/2.
    b1 = 1.
    b2 = 1.
    # Calculando y(x_final)
    while x < x_final:
        # Avancando no tempo
        y = y + h*a1*f(x, y) + h*a2*f(x + b1*h, y + b2*h*f(x,y))        
        x = round(x + h, n_digits)
    #
    return y
#=================================================================================
#                       METODO DE RUNGE-KUTTA DE ORDEM 3
#---------------------------------------------------------------------------------
def runge_kutta_3(y_0, x_0, x_final, h, f):
    # Condicoes iniciais
    x = x_0
    y = y_0
    # Calculando y(x_final)
    while x < x_final:
        # coeficientes do RK-3
        k1 = h*f(x, y)
        k2 = h*f((x + h/2.), (y + k1/2.))
        k3 = h*f((x + h*(3./4.)), (y + k2*(3./4.)))
        # Avancando no tempo
        y = y + k1*(2./9.) + k2*(1./3.) + k3*(4./9.)        
        x = round(x + h, n_digits)
    #
    return y
#=================================================================================
#                       METODO DE RUNGE-KUTTA DE ORDEM 4
#---------------------------------------------------------------------------------
def runge_kutta_4(y_0, x_0, x_final, h, f):
    # Condicoes iniciais
    x = x_0
    y = y_0
    # Calculando y(x_final)
    while x < x_final:
        # coeficientes do RK-4
        k1 = h*f(x, y)
        k2 = h*f(x + h/2., y + k1/2.)
        k3 = h*f(x + h/2., y + k2/2.)
        k4 = h*f(x + h, y + k3)
        # Avancando no tempo
        y = y + (k1 + 2*k2 + 2*k3 + k4)/6.
        x = round(x + h, n_digits)        
    #
    return y
#=================================================================================
#                            PRINTANDO RESULTADOS
#---------------------------------------------------------------------------------
print('Euler: ', euler(y_0, x_0, x_final, h, f))
print('RK-2: ', runge_kutta_2(y_0, x_0, x_final, h, f))
print('RK-3: ', runge_kutta_3(y_0, x_0, x_final, h, f))
print('RK-4: ', runge_kutta_4(y_0, x_0, x_final, h, f))
#=================================================================================
#                                      FIM
#=================================================================================
