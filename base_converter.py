##################################################################################
# Codigo para converter numero (inteiro ou fracionario) entre duas bases quaisquer
# INPE, Sao Jose dos Campos, SP, Brasil - 14 de Marco de 2020
# Leonardo Sattler Cassara - leocassara@igeo.ufrj.br
##################################################################################
#=================================================================================
#                                 IMPORTACOES
#---------------------------------------------------------------------------------
import sys
#=================================================================================
#                                   INPUTS
#---------------------------------------------------------------------------------
# x = numero a ser convertido da base alpha para a base beta (restricao: x deve
#     ser float ou int)
# alpha = base inicial do numero x (restricao: todo digito de x
#         precisa ser menor que alpha e alpha <= 10)
# beta = base final do numero x (restricao: beta <= 10)
#---------------------------------------------------------------------------------
x = 0.101
alpha = 4
beta = 2
#=================================================================================
#                              FUNCOES AUXILIARES
#---------------------------------------------------------------------------------
# Funcao para converter numero x > 1 na base 10 para uma base qualquer.
# inputs:
# - x (inteiro positivo)
# - base (inteiro positivo menor que 10)
# output:
# - resultado (string representando numero x na base desejada)
#---------------------------------------------------------------------------------
def conversor_int_decimal_base(x, base):
    x_base = []    # lista auxiliar para representar algarismo x na base b
    numerador = x  # variavel auxiliar para conversao
    #----------------------------------------
    # Iniciando conversao
    while numerador != 0:                          # condicao para encerrar conversao (divisao = 0)
        x_base.append(int(float(numerador)%base))  # guardando digito da base beta (resto da divisao)
        numerador = int(float(numerador)/base)     # atualizando numerador
    #----------------------------------------
    # Preparando output (string)
    x_base.reverse()        # Invertendo lista x_beta para exibir resultado
    if x==0:
        resultado_inteiro = '0'  # variavel auxiliar para exibir resultado (caso x=0)
    else:
        resultado_inteiro = ''   # variavel auxiliar para exibir resultado (qualquer outro caso)
    for i in x_base:
        resultado_inteiro = resultado_inteiro + str(i)
    return resultado_inteiro
#---------------------------------------------------------------------------------
# Funcao para converter numero 0 < x < 1 na base 10 para uma base qualquer.
# inputs:
# - x (float positivo)
# - base (inteiro positivo menor que 10)
# output:
# - resultado (string representando numero x na base desejada)
#---------------------------------------------------------------------------------
def conversor_frac_decimal_base(x, base):
    x_base = []    # lista auxiliar para representar algarismo x na base b
    num_multiplicado = x  # variavel auxiliar para conversao
    detalhe = ''          # detalhe extra a ser adicionado ao output caso representacao seja infinita
    check_repeticao = [] # lista auxiliar para checar se conversao sera infinita
    #----------------------------------------
    # Iniciando conversao
    while num_multiplicado != 0:                                             # condicao para encerrar conversao (parte fracionaria da multiplicacao = 0)
        check_repeticao.append(num_multiplicado)                             # guardando valor da multiplicacao para check de repeticao
        num_multiplicado = num_multiplicado * base                           # realizando multiplicacao
        digito = int(num_multiplicado)                                       # digito de interese eh a parte inteira da multiplicacao
        #print(num_multiplicado, '->', digito)
        num_multiplicado = float('0.'+str(num_multiplicado).split('.')[-1])  # encontrando parte fracionaria da multiplicacao
        #print('prox.:', num_multiplicado)
        x_base.append(int(digito))                                           # guardando digito da base beta        
        if check_repeticao.count(num_multiplicado)==2 or len(x_base)>14:     # checando se multiplicacao ja ocorreu num loop anterior (pelo menos 2x)
            detalhe = '...'
            break                                                            # saindo do oop caso sim
    #----------------------------------------
    # Preparando output (string)
    resultado_fracionario = ''  # variavel auxiliar para exibir resultado
    for i in x_base:
        resultado_fracionario = resultado_fracionario + str(i)
    resultado_fracionario = resultado_fracionario + detalhe
    return resultado_fracionario
#=================================================================================
#                                   CHECKS
#---------------------------------------------------------------------------------
# Configurando avisos de inputs nao aceitos dadas as restricoes acima. Nesses
# casos, o programa terminara sem realizar calculo algum.
#---------------------------------------------------------------------------------
# Restricao de x 
if type(x) not in [type(10), type(10.)]:
    print('Aviso:')
    print('x deve ser float ou inteiro.')
    print('Escolha outros valores.')
    sys.exit()
# Checando se x eh negativo para adicionar sinal apenas ao final:
sinal=''
if x < 0:
    x = abs(x)
    sinal = '-'
#---------------------------------------------------------------------------------
# Restricao de alpha (nesse caso sao duas)
if alpha <= 10 and alpha >1:
    for i in str(x):
        if i != '.':
            if int(i) >= alpha:  # checando cada digito de x para a restricao
                print('Aviso:')
                print('x nao pode ser representado pela base alpha escolhida.')
                print('Escolha outros valores.')
                sys.exit()
else:
    print('Aviso:')
    print('Escolha bases entre 2 e 10.')
    sys.exit()
#---------------------------------------------------------------------------------
# Restricao de beta
if beta > 10 or beta <=1:
    print('Aviso:')
    print('Escolha bases entre 2 e 10.')
    sys.exit()
#=================================================================================
#                                  CONVERSAO
#---------------------------------------------------------------------------------
# Metodo: converte-se x da base alpha para base 10 e em seguida da base 10 para a
# base beta. Antes checo se alpha = 10 e depois se beta = 10 (para evitar
# redundancias no script). O script divide conversoes das partes inteira e
# fracionaria e concatena os resultados numa string.
# obs.:
if alpha == beta:
    print(sinal + str(x) + ' (base ' +str(alpha) + ') = ' + str(x) + ' (base ' + str(beta) + ')')
    sys.exit()
#---------------------------------------------------------------------------------
# Se alpha diferente de 10, converto x para base 10
if alpha != 10:
    # CALCULANDO CONVERSAO DA PARTE INTEIRA
    x_int = int(x)
    x_int_10 = 0  # variavel auxiliar para representar algarismo x na base 10
    # Convertendo para base 10
    for i in range(len(str(x_int))):  # loop sobre numero de digitos de x
        digito = int(str(x_int)[i])              
        expoente = (len(str(x_int))-i-1)
        x_int_10 = x_int_10 + digito * (alpha ** expoente)  # calculando x_int na base 10
        #print(digito, expoente, x_10_int)
    #----------------------------------------
    # CASO FRACIONARIO, CALCULANDO CONVERSAO
    if x != int(x):
        x_frac = str(x).split('.')[-1]
        x_frac_10 = 0  # variavel auxiliar para representar algarismo x na base 10
        # Convertendo para base 10
        for i in range(len(x_frac)):  # loop sobre numero de digitos de x
            digito = int(x_frac[i])      
            expoente = -i-1
            x_frac_10 = x_frac_10 + digito * (alpha ** expoente)  # calculando x_frac na base 10
            #print(digito, expoente, x_frac_10)
    #----------------------------------------
    # Se beta igual a 10, printo resultado e programa encerra
    if beta == 10:
        # CASO FRACIONARIO
        if x != int(x):
            resultado_int = str(x_int_10)
            resultado_frac = str(x_frac_10).split('.')[-1]  # manipulando string fracionaria para exibicao do resultado
            resultado = resultado_int + '.' + resultado_frac
        # CASO INTEIRO
        else:
            resultado = str(x_int_10)
        # Exibindo resultado
        print(sinal + str(x) + ' (base ' +str(alpha) + ') = ' + sinal + resultado + ' (base ' + str(beta) + ')')
    #----------------------------------------
    # Se beta diferente de 10, utilizo cada x_10 encontrado acima e converto x para base beta
    else:
        # CASO FRACIONARIO
        if x != int(x):
            resultado_int = conversor_int_decimal_base(x_int_10, beta)     # chamando funcao de conversao para inteiros
            resultado_frac = conversor_frac_decimal_base(x_frac_10, beta)  # chamando funcao de conversao para fracionarios
            resultado = resultado_int + '.' + resultado_frac
        # CASO INTEIRO
        else:
            resultado = conversor_int_decimal_base(x_int_10, beta)     # chamando funcao de conversao para inteiros
        # Exibindo resultado
        print(sinal + str(x) + ' (base ' +str(alpha) + ') = ' + sinal + resultado + ' (base ' + str(beta) + ')')
#---------------------------------------------------------------------------------
# Se alpha igual a 10, x ja esta na base decimal entao simplesmente converto x para base beta
else:
    # CASO FRACIONARIO
    if x != int(x):
        x_int = int(x)
        x_frac = float('0.'+str(x).split('.')[-1])
        resultado_int = conversor_int_decimal_base(x_int, beta)     # chamando funcao de conversao para inteiros
        resultado_frac = conversor_frac_decimal_base(x_frac, beta)  # chamando funcao de conversao para fracionarios
        resultado = resultado_int + '.' + resultado_frac
    # CASO INTEIRO
    else:
        x = int(x)
        resultado = conversor_int_decimal_base(x, beta)     # chamando funcao de conversao para inteiros
    # Exibindo resultado
    print(sinal + str(x) + ' (base ' +str(alpha) + ') = ' + sinal + resultado + ' (base ' + str(beta) + ')')
#=================================================================================
#                                      FIM
#=================================================================================
