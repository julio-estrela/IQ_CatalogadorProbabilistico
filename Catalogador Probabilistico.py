from iqoptionapi.stable_api import IQ_Option
from datetime import datetime
from colorama import init, Fore
from time import time, sleep
import sys, os
init(convert=True, autoreset=False)
API = IQ_Option('seu email', 'sua senha')
API.connect()
if API.check_connect():
    print(' ')
else:
    print(Fore.RED + 'verifique se voce colocou a senha ou e-mail correto \n no app de configuraçao')
    input(Fore.RED + 'Aperte [ enter ] para fechar o robo')
    sys.exit()
print(Fore.GREEN + '||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n')
print(Fore.GREEN + ' ANALISE MEGA AVANÇADA DE MERCADO PARA MG-TRADER TELEGRAM \n')
dias = int(input(' QUANTOS DIAS DESEJA ANALISAR  1 ATE 30: '))
print('\n')
print('\n')
timiframe = int(input(' QUAL TIMEFRAME DE OPERAÇAO : '))
print('\n')
entrada = float(input(' VALOR DE ENTRADA : '))
print(Fore.GREEN + '\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n')
if dias == 1:
    qt_velas = 288
if dias == 2:
    qt_velas = 576
if dias == 3:
    qt_velas = 864
if dias == 4:
    qt_velas = 1152
if dias == 5:
    qt_velas = 1728
if dias == 6:
    qt_velas = 2016
if dias == 7:
    qt_velas = 2304
if dias == 8:
    qt_velas = 2592
if dias == 9:
    qt_velas = 2880
if dias == 10:
    qt_velas = 3168
if dias == 11:
    qt_velas = 3456
if dias == 12:
    qt_velas = 3744
if dias == 13:
    qt_velas = 4032
if dias == 14:
    qt_velas = 4320
if dias == 15:
    qt_velas = 4608
if dias == 16:
    qt_velas = 4896
if dias == 17:
    qt_velas = 5184
if dias == 18:
    qt_velas = 5472
if dias == 19:
    qt_velas = 5760
if dias == 20:
    qt_velas = 6048
if dias == 21:
    qt_velas = 6336
if dias == 22:
    qt_velas = 6624
if dias == 23:
    qt_velas = 6912
if dias == 24:
    qt_velas = 7200
if dias == 25:
    qt_velas = 7488
if dias == 26:
    qt_velas = 7776
if dias == 27:
    qt_velas = 8064
if dias == 28:
    qt_velas = 8352
if dias == 29:
    qt_velas = 8640
if dias == 30:
    qt_velas = 18640
while True:
    win = 0
    loss = 0
    doji = 0
    mg1 = 0
    mg2 = 0
    mg3 = 0
    mg4 = 0
    mg5 = 0
    mg6 = 0
    mg7 = 0
    mg8 = 0
    print(Fore.YELLOW + '\n\n QUAL A PARIDADE QUE DESEJA TESTAR A ASSERTIVIDADE: ')
    print(' ')
    print(Fore.YELLOW + ' \n----[ MERCADO NORMAL ]---- \n [01] EURGBP | [02] GBPJPY | [03] GBPUSD | [04] AUDCAD \n [05] USDCHF | [06] AUDUSD | [07] USDCAD | [08] AUDJPY \n [09] GBPCAD | [10] GBPCHF | [11] GBPAUD | [12] EURCAD | [13] EURAUD [14] EURUSD \n----[ MERCADO OTC ]---- \n [15] EURUSD-OTC | [16] EURGBP-OTC | [17] USDCHF-OTC | [18] EURJPY-OTC \n [19] NZDUSD-OTC | [20] GBPUSD-OTC | [21] USDJPY-OTC | [22] AUDCAD-OTC')
    paridade = str(input(' DIGITE AQUI NUMERO DA PARIDADE:  ').strip()).upper()
    if paridade == '01':
        par = 'EURGBP'
    else:
        if paridade == '02':
            par = 'GBPJPY'
        if paridade == '03':
            par = 'GBPUSD'
        if paridade == '04':
            par = 'AUDCAD'
        if paridade == '05':
            par = 'USDCHF'
        if paridade == '06':
            par = 'AUDUSD'
        if paridade == '07':
            par = 'USDCAD'
        if paridade == '08':
            par = 'AUDJPY'
        if paridade == '09':
            par = 'GBPCAD'
        if paridade == '10':
            par = 'GBPCHF'
        if paridade == '11':
            par = 'GBPAUD'
        if paridade == '12':
            par = 'EURCAD'
        if paridade == '13':
            par = 'EURAUD'
        if paridade == '14':
            par = 'EURUSD'
        if paridade == '15':
            par = 'EURUSD-OTC'
        if paridade == '16':
            par = 'EURGBP-OTC'
        if paridade == '17':
            par = 'USDCHF-OTC'
        if paridade == '18':
            par = 'EURJPY-OTC'
        if paridade == '19':
            par = 'NZDUSD-OTC'
        if paridade == '20':
            par = 'GBPUSD-OTC'
        if paridade == '21':
            par = 'USDJPY-OTC'
        if paridade == '22':
            par = 'AUDCAD-OTC'
        print('\n')
        candles = API.get_candles(par, timiframe * 60, qt_velas, int(time()))
        for index, vela in enumerate(candles):
            min = int(datetime.fromtimestamp(int(vela['from'])).strftime('%M')[1:])
            if not min == 5:
                if min == 0:
                    pass
            cor_operacao = 'g' if vela['open'] < vela['close'] else 'r' if vela['open'] > vela['close'] else 'd'
            entrada_analise = ['g' if candles[(index - i)]['open'] < candles[(index - i)]['close'] else 'r' if candles[(index - i)]['open'] > candles[(index - i)]['close'] else 'd' for i in range(1, 4)]
            entrada_analise = 'g' if False if entrada_analise.count('d') > 0 else entrada_analise.count('r') > entrada_analise.count('g') else 'r' if entrada_analise.count('g') > entrada_analise.count('r') else False
            if entrada_analise != False:
                if entrada_analise == cor_operacao:
                    win += 1
                else:
                    try:
                        mg1_res = 'g' if candles[(index + 1)]['open'] < candles[(index + 1)]['close'] else 'r' if candles[(index + 1)]['open'] > candles[(index + 1)]['close'] else 'd'
                    except:
                        mg1_res = False

                    try:
                        mg2_res = 'g' if candles[(index + 2)]['open'] < candles[(index + 2)]['close'] else 'r' if candles[(index + 2)]['open'] > candles[(index + 2)]['close'] else 'd'
                    except:
                        mg2_res = False

                    try:
                        mg3_res = 'g' if candles[(index + 3)]['open'] < candles[(index + 3)]['close'] else 'r' if candles[(index + 3)]['open'] > candles[(index + 3)]['close'] else 'd'
                    except:
                        mg3_res = False

                    try:
                        mg4_res = 'g' if candles[(index + 4)]['open'] < candles[(index + 4)]['close'] else 'r' if candles[(index + 4)]['open'] > candles[(index + 4)]['close'] else 'd'
                    except:
                        mg4_res = False

                    try:
                        mg5_res = 'g' if candles[(index + 5)]['open'] < candles[(index + 5)]['close'] else 'r' if candles[(index + 5)]['open'] > candles[(index + 5)]['close'] else 'd'
                    except:
                        mg5_res = False

                    try:
                        mg6_res = 'g' if candles[(index + 6)]['open'] < candles[(index + 6)]['close'] else 'r' if candles[(index + 6)]['open'] > candles[(index + 6)]['close'] else 'd'
                    except:
                        mg6_res = False

                    try:
                        mg7_res = 'g' if candles[(index + 7)]['open'] < candles[(index + 7)]['close'] else 'r' if candles[(index + 7)]['open'] > candles[(index + 7)]['close'] else 'd'
                    except:
                        mg7_res = False

                    try:
                        mg8_res = 'g' if candles[(index + 8)]['open'] < candles[(index + 8)]['close'] else 'r' if candles[(index + 8)]['open'] > candles[(index + 8)]['close'] else 'd'
                    except:
                        mg8_res = False

                    if mg1_res == cor_operacao and mg1_res != False:
                        mg1 += 1
                    elif mg2_res == cor_operacao and mg1_res != False:
                        mg2 += 1
                    elif mg3_res == cor_operacao and mg1_res != False:
                        mg3 += 1
                    elif mg4_res == cor_operacao and mg1_res != False:
                        mg4 += 1
                    elif mg5_res == cor_operacao and mg1_res != False:
                        mg5 += 1
                    elif mg6_res == cor_operacao and mg1_res != False:
                        mg6 += 1
                    elif mg7_res == cor_operacao and mg1_res != False:
                        mg7 += 1
                    elif mg8_res == cor_operacao and mg1_res != False:
                        mg8 += 1
                    else:
                        loss += 1
            else:
                doji += 1

        total = win + mg1 + mg2 + mg3 + mg4 + mg5 + mg6 + mg7 + mg8
        loss_sem_gale = total - win
        loss_gale11 = win + mg1
        loss_gale21 = win + mg1 + mg2
        loss_gale31 = win + mg1 + mg2 + mg3
        loss_gale41 = win + mg1 + mg2 + mg3 + mg4
        loss_gale51 = win + mg1 + mg2 + mg3 + mg4 + mg5
        loss_gale52 = win + mg1 + mg2 + mg3 + mg4 + mg5 + mg6
        loss_gale53 = win + mg1 + mg2 + mg3 + mg4 + mg5 + mg6 + mg7
        loss_gale54 = win + mg1 + mg2 + mg3 + mg4 + mg5 + mg6 + mg7 + mg8
        loss_gale1 = total - loss_gale11
        loss_gale2 = total - loss_gale21
        loss_gale3 = total - loss_gale31
        loss_gale4 = total - loss_gale41
        loss_gale5 = total - loss_gale51
        loss_gale6 = total - loss_gale52
        loss_gale7 = total - loss_gale53
        loss_gale8 = total - loss_gale54
        perca_din = entrada * loss_sem_gale
        ganho_din = entrada * win
        ganho_total = ganho_din - perca_din
        perca_din1 = entrada * loss_gale1
        ganho_din1 = entrada * loss_gale11
        ganho_total1 = ganho_din1 - perca_din1
        perca_din2 = entrada * loss_gale2
        ganho_din2 = entrada * loss_gale21
        ganho_total2 = ganho_din2 - perca_din2
        perca_din3 = entrada * loss_gale3
        ganho_din3 = entrada * loss_gale31
        ganho_total3 = ganho_din3 - perca_din3
        perca_din4 = entrada * loss_gale4
        ganho_din4 = entrada * loss_gale41
        ganho_total4 = ganho_din4 - perca_din4
        perca_din5 = entrada * loss_gale5
        ganho_din5 = entrada * loss_gale51
        ganho_total5 = ganho_din5 - perca_din5
        perca_din6 = entrada * loss_gale6
        ganho_din6 = entrada * loss_gale52
        ganho_total6 = ganho_din6 - perca_din6
        perca_din7 = entrada * loss_gale7
        ganho_din7 = entrada * loss_gale53
        ganho_total7 = ganho_din7 - perca_din7
        perca_din8 = entrada * loss_gale8
        ganho_din8 = entrada * loss_gale54
        ganho_total8 = ganho_din8 - perca_din8
        print('--------- [ RESULTADO DO BACKTEST ] --------- ')
        print(Fore.GREEN + ' | WIN GALE 0  : ' + str(win) + Fore.RED + ' | LOSS : ' + str(loss_sem_gale) + Fore.GREEN + ' | GANHO : ' + str(ganho_total) + Fore.CYAN + ' | ASSERTIVIDADE : ', round(100 * (win / (win + mg1 + mg2 + mg3 + mg4 + mg5 + mg6 + mg7 + mg8 + loss_sem_gale))), '%')
        print(Fore.GREEN + ' | WIN GALE 1  : ' + str(loss_gale11) + Fore.RED + ' | LOSS : ' + str(loss_gale1) + Fore.GREEN + ' | GANHO : ' + str(ganho_total1) + Fore.CYAN + ' | ASSERTIVIDADE : ', round(100 * ((win + mg1) / (win + mg1 + mg2 + mg3 + mg4 + mg5 + mg6 + mg7 + mg8 + loss_gale1))), '%')
        print(Fore.GREEN + ' | WIN GALE 2  : ' + str(loss_gale21) + Fore.RED + ' | LOSS : ' + str(loss_gale2) + Fore.GREEN + ' | GANHO : ' + str(ganho_total2) + Fore.CYAN + ' | ASSERTIVIDADE : ', round(100 * ((win + mg1 + mg2) / (win + mg1 + mg2 + mg3 + mg4 + mg5 + mg6 + mg7 + mg8 + loss_gale2))), '%')
        print(Fore.GREEN + ' | WIN GALE 3  : ' + str(loss_gale31) + Fore.RED + ' | LOSS : ' + str(loss_gale3) + Fore.GREEN + ' | GANHO : ' + str(ganho_total3) + Fore.CYAN + ' | ASSERTIVIDADE : ', round(100 * ((win + mg1 + mg2 + mg3) / (win + mg1 + mg2 + mg3 + mg4 + mg5 + mg6 + mg7 + mg8 + loss_gale3))), '%')
        print(Fore.GREEN + ' | WIN GALE 4  : ' + str(loss_gale41) + Fore.RED + ' | LOSS : ' + str(loss_gale4) + Fore.GREEN + ' | GANHO : ' + str(ganho_total4) + Fore.CYAN + ' | ASSERTIVIDADE : ', round(100 * ((win + mg1 + mg2 + mg3 + mg4) / (win + mg1 + mg2 + mg3 + mg4 + mg5 + mg6 + mg7 + mg8 + loss_gale4))), '%')
        print(Fore.GREEN + ' | WIN GALE 5  : ' + str(loss_gale51) + Fore.RED + ' | LOSS : ' + str(loss_gale5) + Fore.GREEN + ' | GANHO : ' + str(ganho_total5) + Fore.CYAN + ' | ASSERTIVIDADE : ', round(100 * ((win + mg1 + mg2 + mg3 + mg4 + mg5) / (win + mg1 + mg2 + mg3 + mg4 + mg5 + mg6 + mg7 + mg8 + loss_gale5))), '%')
        print(Fore.GREEN + ' | WIN GALE 6  : ' + str(loss_gale52) + Fore.RED + ' | LOSS : ' + str(loss_gale6) + Fore.GREEN + ' | GANHO : ' + str(ganho_total6) + Fore.CYAN + ' | ASSERTIVIDADE : ', round(100 * ((win + mg1 + mg2 + mg3 + mg4 + mg5 + mg6) / (win + mg1 + mg2 + mg3 + mg4 + mg5 + mg6 + mg7 + mg8 + loss_gale6))), '%')
        print(Fore.GREEN + ' | WIN GALE 7  : ' + str(loss_gale53) + Fore.RED + ' | LOSS : ' + str(loss_gale7) + Fore.GREEN + ' | GANHO : ' + str(ganho_total7) + Fore.CYAN + ' | ASSERTIVIDADE : ', round(100 * ((win + mg1 + mg2 + mg3 + mg4 + mg5 + mg6 + mg7) / (win + mg1 + mg2 + mg3 + mg4 + mg5 + mg6 + mg7 + mg8 + loss_gale7))), '%')
        print(Fore.GREEN + ' | WIN GALE 8  : ' + str(loss_gale54) + Fore.RED + ' | LOSS : ' + str(loss_gale8) + Fore.GREEN + ' | GANHO : ' + str(ganho_total8) + Fore.CYAN + ' | ASSERTIVIDADE : ', round(100 * ((win + mg1 + mg2 + mg3 + mg4 + mg5 + mg6 + mg7 + mg8) / (win + mg1 + mg2 + mg3 + mg4 + mg5 + mg6 + mg7 + mg8 + loss_gale8))), '%')
        print(Fore.GREEN + '\n TOTAL DE ENTRADAS : ', total)
        print(Fore.GREEN + ' PARIDADE : ', par)