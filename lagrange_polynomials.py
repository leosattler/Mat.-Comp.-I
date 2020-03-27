##################################################################################
# Codigo para interpolar pares de pontos (x,y) via Lagrange. Retorna a forma
# literal do polinomio interpolador e gera uma funcao (def) deste mesmo polinomio
# INPE, Sao Jose dos Campos, SP, Brasil - 21 de Marco de 2020
# Leonardo Sattler Cassara - leocassara@igeo.ufrj.br
##################################################################################
#=================================================================================
#                                 IMPORTACOES
#---------------------------------------------------------------------------------
import numpy as np
from sympy import Symbol
import sympy as sym
#=================================================================================
#                                   INPUTS
#---------------------------------------------------------------------------------
X = [-1, 0, 3]
Y = [15, 8, -1]
#=================================================================================
#                        ENCONTRANDO POLINOMIO DE LAGRANGE
#---------------------------------------------------------------------------------
# Passando inputs para array de floats
X=np.array(X,dtype=float)
Y=np.array(Y,dtype=float)
# Definindo variavel simbolica 'x'
x = Symbol('x')
# Numero de coeficientes 
n_coefs = len(X)
# Definindo coef.s de Lagrange usando a variavel simbolica 'x' e pontos X_i
L = [] # lista para guardar os coeficientes (L_i's) do polinomio
# Loop sobre cada coeficiente
for i in range(n_coefs):
    #X_i = X[i] # guardando X_i
    # Variaveis auxiliares para deifinir coeficiente L_i 
    num_L_i = 1
    den_L_i = 1
    # Removendo X_i da lista de coeficientes  
    coefs = np.arange(n_coefs)
    coefs = list(coefs)
    coefs.remove(i)
    # Valores iniciais do numerador e denominador do coef. L_i de Lagrange
    num_L_i = 1
    den_L_i = 1
    # Loop sobre os membros de X menos menos X_i
    for j in coefs:
        num_L_i = num_L_i * (x - X[j])
        den_L_i = den_L_i * (X[i] - X[j])
    L_i = num_L_i / den_L_i
    L.append(sym.expand(L_i)) # expandindo representacao simbolica e adicionando
                              # L_i a lista de coeficientes de Lagrange
#---------------------------------------------------------------------------------
# Multiplicando y_i por Li e somando os termos para encontrar polinomio final
p = np.sum(Y*np.array(L))
#=================================================================================
#                                PRINTANDO RESULTADO
#---------------------------------------------------------------------------------
print('Polinomio interpolador:')
print(p)
#=================================================================================
#                          CRIANDO FUNCAO DO POLINOMIO
#--------------------------------------------------------------------------------
def f(var):
    funcao = p.subs(x, var)
    return funcao
#=================================================================================
#                                      FIM
#=================================================================================
