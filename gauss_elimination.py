##################################################################################
# Codigo para converter numero (inteiro ou fracionario) entre duas bases quaisquer
# INPE, Sao Jose dos Campos, SP, Brasil - 14 de Marco de 2020
# Leonardo Sattler Cassara - leocassara@igeo.ufrj.br
##################################################################################
#=================================================================================
#                                 IMPORTACOES
#---------------------------------------------------------------------------------
import sys
import numpy as np
#=================================================================================
#                                   INPUTS
#---------------------------------------------------------------------------------
# x = numero a ser convertido da base alpha para a base beta (restricao: x deve
#     ser float ou int)
# alpha = base inicial do numero x (restricao: todo dgiito de x
#         precisa ser menor que alpha e alpha <= 10)
# beta = base final do numero x (restricao: beta <= 10)
#---------------------------------------------------------------------------------
matriz_de_coeficientes = \
                         [[2, 1, -3], \
                          [-1, 3, 2], \
                          [3, 1, -3]]
lado_direito = [-1, 12, 0]
#=================================================================================
#                                    MEG
#---------------------------------------------------------------------------------
# Encontrando matriz triangular conforme algoritmo de eliminacao de Gauss
#---------------------------------------------------------------------------------
n = len(matriz_de_coeficientes)
A = np.array(matriz_de_coeficientes,dtype=float)
b = np.array(lado_direito,dtype=float)
for line in range(1,n):
    for pivot in range(line):
        if A[pivot,pivot]!=0:
            factor = -float(A[line,pivot])/A[pivot,pivot]        
            for col in range(n):
                A[line,col] = A[line,col] + factor * A[pivot,col]
            #
            b[line] = b[line] + factor * b[pivot]
#=================================================================================
#                                   CHECKS
#---------------------------------------------------------------------------------
# Checando se matriz e trianguar superior, ajeitando caso nao seja, e retornando
# 'sistema sem solucao' caso numero de pivos nao nulos nao seja o esperado
#---------------------------------------------------------------------------------
# Guardando numero de zeros em cada linha
c=[]
for i in range(n):
    c.append(list(A[i,:]).count(0))
# checando se numero de zeros na matriz e ideal, ou seja, se numero de zeros
# aumenta em 1 da primeira linha em diante; equivalente a saber se o sistema
# tem solucao. Caso contrario, o programa termina sem retornar as reaizes.
if sum(c) != np.sum(np.arange(n)):
    print('Sistema sem solucao!')
    sys.exit()
#
# Acertando a matriz caso numero de zeros seja o esperado mas nao aumenta
# conforme esperado
A2 = np.zeros(np.shape(A))
b2 = []
for i in range(n):
    indx = c.index(i)
    A2[i,:] = A[indx,:]
    b2.append(b[indx])
#=================================================================================
#                                ENCONTRANDO RAIZES
#---------------------------------------------------------------------------------
x = np.zeros(n) # lista auxiliar para guardar raizes
for i in -np.arange(-n+1,1):
    x_i = b2[i]
    for j in np.arange(i,n-1):
        x_i = x_i - A2[i,j+1] * x[j+1]
    x[i] = x_i/A2[i,i]
# Printando solucao
print('Raizes do sistema:')
print(x)
#=================================================================================
#                                      FIM
#=================================================================================
