from __future__ import division
from __future__ import print_function
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import requests
import json
import urllib
import numpy as np 
import matplotlib.pyplot as plt 
from docplex.mp.model import Model
import sys
import cplex
from cplex.exceptions import CplexError

# FUNCOES PARA CRIACAO DA MATRIZ DE DISTANCIAS
def getEnderecos(dia):
    """Cria uma lista com as cidades de visitacao para cada dia da semana."""
    cidades = {}
    cidades['chave_API'] = 'YourAPIKey'
    # 16 lugares, adaptar para mais caso necessario
    if dia == 0:  # segunda
        cidades['enderecos'] = ['824F+56+Maripa+de+Minas+MG',  # Oxetil, pontoDePartida
                                # MG
                                'Belo+Horizonte+MG',  # BELO HORIZONTE
                                'Bicas+MG',  # BICAS
                                'Juiz+de+Fora+MG',  # Juiz de Fora
                                'Lima+Duarte+MG',  # LIMA DUARTE
                                # RJ
                                'Barra+Mansa+RJ',  # BARRA MANSA
                                'Rio+de+Janeiro+RJ',  # RIO DE JANEIRO
                                'Valenca+RJ',  # VALENCA
                                'Vassouras+RJ',  # VASSOURAS
                                'Volta+Redonda+RJ'  # VOLTA REDONDA
                                ]
    elif dia == 1:  # terca
        cidades['enderecos'] = ['824F+56+Maripa+de+Minas+MG',  # Oxetil, pontoDePartida
                                # MG
                                'Alem+Paraiba+MG',  # Alem Paraiba
                                'Belo+Horizonte+MG',  # BELO HORIZONTE
                                # RJ
                                'Bom+Jardim+RJ',  # BOM JARDIM
                                'Cabo+Frio+RJ',  # CABO FRIO
                                'Campos+dos+Goytacazes+RJ',  # CAMPOS DOS GOYTACAZES
                                'Cantagalo+RJ',  # CANTAGALO
                                'Carmo+RJ',  # CARMO
                                'Cordeiro+RJ',  # CORDEIRO
                                'Itaperuna+RJ',  # ITAPERUNA
                                'Macae+RJ',  # MACAE
                                'Nova+Friburgo+RJ',  # NOVA FRIBURGO
                                'Santo+Antonio+de+Padua+RJ'  # SANTO ANTONIO DE PADUA
                                ]
    elif dia == 2:  # quarta
        cidades['enderecos'] = ['824F+56+Maripa+de+Minas+MG',  # Oxetil, pontoDePartida
                                # MG
                                'Barbacena+MG',  # BARBACENA
                                'Barroso+MG',  # BARROSO
                                'Carangola+MG',  # CARANGOLA
                                'Cataguases+MG',  # CATAGUASES
                                'Governador+Valadares+MG',  # GOVERNADOR VALADARES
                                'Juiz+de+Fora+MG',  # Juiz de Fora
                                'Muriae+MG',  # MURIAE
                                'Ponte+Nova+MG',  # PONTE NOVA
                                'Rio+Pomba+MG',  # RIO POMBA
                                'Santos+Dumont+MG',  # SANTOS DUMONT
                                'Uba+MG',  # UBA
                                'Vicosa+MG',  # VICOSA
                                'Visconde+do+Rio+Branco+MG',  # VISCONDE DO RIO BRANCO
                                # RJ
                                'Manhuacu+RJ',  # MANHUACU
                                'Niteroi+RJ',  # NITEROI
                                'Petropolis+RJ',  # PETROPOLIS
                                'Rio+de+Janeiro+RJ'  # RIO DE JANEIRO
                                ]
    elif dia == 3:  # quinta
        cidades['enderecos'] = ['824F+56+Maripa+de+Minas+MG',  # Oxetil, pontoDePartida
                                # MG
                                'Belo+Horizonte+MG',  # BELO HORIZONTE
                                'Bicas+MG',  # BICAS
                                'Juiz+de+Fora+MG',  # Juiz de Fora
                                'Lima+Duarte+MG',  # LIMA DUARTE
                                # RJ
                                'Barra+Mansa+RJ',  # BARRA MANSA
                                'Rio+de+Janeiro+RJ',  # RIO DE JANEIRO
                                'Valenca+RJ',  # VALENCA
                                'Vassouras+RJ',  # VASSOURAS
                                'Volta+Redonda+RJ'  # VOLTA REDONDA
                                ]
    elif dia == 4:  # sexta
        cidades['enderecos'] = ['824F+56+Maripa+de+Minas+MG',  # Oxetil, pontoDePartida
                                # MG
                                'Alem+Paraiba+MG',  # Alem Paraiba
                                'Belo+Horizonte+MG',  # BELO HORIZONTE
                                'Muriae+MG',  # MURIAE
                                # RJ
                                'Bom+Jardim+RJ',  # BOM JARDIM
                                'Cabo+Frio+RJ',  # CABO FRIO
                                'Campos+dos+Goytacazes+RJ',  # CAMPOS DOS GOYTACAZES
                                'Cantagalo+RJ',  # CANTAGALO
                                'Carmo+RJ',  # CARMO
                                'Cordeiro+RJ',  # CORDEIRO
                                'Itaperuna+RJ',  # ITAPERUNA
                                'Macae+RJ',  # MACAE
                                'Nova+Friburgo+RJ',  # NOVA FRIBURGO
                                'Rio+de+Janeiro+RJ',  # RIO DE JANEIRO
                                'Santo+Antonio+de+Padua+RJ'  # SANTO ANTONIO DE PADUA
                                ]
    elif dia == 5:  # sabado
        cidades['enderecos'] = ['824F+56+Maripa+de+Minas+MG',  # Oxetil, pontoDePartida
                                # MG
                                'Barbacena+MG',  # BARBACENA
                                'Barroso+MG',  # BARROSO
                                'Carangola+MG',  # CARANGOLA
                                'Cataguases+MG',  # CATAGUASES
                                'Governador+Valadares+MG',  # GOVERNADOR VALADARES
                                'Juiz+de+Fora+MG',  # Juiz de Fora
                                'Muriae+MG',  # MURIAE
                                'Ponte+Nova+MG',  # PONTE NOVA
                                'Rio+Pomba+MG',  # RIO POMBA
                                'Santos+Dumont+MG',  # SANTOS DUMONT
                                'Uba+MG',  # UBA
                                'Vicosa+MG',  # VICOSA
                                'Visconde+do+Rio+Branco+MG',  # VISCONDE DO RIO BRANCO
                                # RJ
                                'Manhuacu+RJ',  # MANHUACU
                                'Niteroi+RJ',  # NITEROI
                                'Petropolis+RJ',  # PETROPOLIS
                                'Rio+de+Janeiro+RJ'  # RIO DE JANEIRO
                                ]
    else:  # matriz de enderecos completa
        cidades['enderecos'] = ['824F+56+Maripa+de+Minas+MG',  # Oxetil, pontoDePartida
                                # MG
                                'Alem+Paraiba+MG',  # Alem Paraiba
                                'Barbacena+MG',  # BARBACENA
                                'Barroso+MG',  # BARROSO
                                'Belo+Horizonte+MG',  # BELO HORIZONTE
                                'Betim+MG',  # BETIM
                                'Bicas+MG',  # BICAS
                                'Campo+Belo+MG',  # CAMPO BELO
                                'Carangola+MG',  # CARANGOLA
                                'Caratinga+MG',  # CARATINGA
                                'Cataguases+MG',  # CATAGUASES
                                'Congonhas+MG',  # CONGONHAS
                                'Conselheiro+Lafaiete+MG',  # CONSELHEIRO LAFAIETE
                                'Contagem+MG',  # CONTAGEM
                                'Governador+Valadares+MG',  # GOVERNADOR VALADARES
                                'Guarani+MG',  # GUARANI
                                'Iapu+MG',  # IAPU
                                'Ituiutaba+MG',  # ITUIUTABA
                                'Juiz+de+Fora+MG',  # Juiz de Fora
                                'Leopoldina+MG',  # LEOPOLDINA
                                'Lima+Duarte+MG',  # LIMA DUARTE
                                'Manhumirim+MG',  # MANHUMIRIM
                                'Mar+de+Espanha+MG',  # MAR DE ESPANHA
                                'Maripa+de+Minas+MG',  # MARIPA DE MINAS
                                'Matias+Barbosa+MG',  # MATIAS BARBOSA
                                'Minas+Nova+MG',  # MINAS NOVA
                                'Mirai+MG',  # MIRAI
                                'Muriae+MG',  # MURIAE
                                'Ouro+Branco+MG',  # OURO BRANCO
                                'Ponte+Nova+MG',  # PONTE NOVA
                                'Recreio+MG',  # RECREIO
                                'Rio+Pomba+MG',  # RIO POMBA
                                'Salinas+MG',  # SALINAS
                                'Santos+Dumont+MG',  # SANTOS DUMONT
                                'Sao+Joao+Nepomuceno+MG',  # SAO JOAO NEPOMUCENO
                                'Senador+Firmino+MG',  # SENADOR FIRMINO
                                'Tocantins+MG',  # TOCANTINS
                                'Uba+MG',  # UBA
                                'Vicosa+MG',  # VICOSA
                                'Visconde+do+Rio+Branco+MG',  # VISCONDE DO RIO BRANCO
                                # RJ
                                'Araruama+RJ',  # ARARUAMA
                                'Barra+do+Pirai+RJ',  # BARRA DO PIRAI
                                'Barra+Mansa+RJ',  # BARRA MANSA
                                'Bom+Jardim+RJ',  # BOM JARDIM
                                'Cabo+Frio+RJ',  # CABO FRIO
                                'Campos+dos+Goytacazes+RJ',  # CAMPOS DOS GOYTACAZES
                                'Cantagalo+RJ',  # CANTAGALO
                                'Carmo+RJ',  # CARMO
                                'Cordeiro+RJ',  # CORDEIRO
                                'Duas+Barras+RJ',  # DUAS BARRAS
                                'Duque+de+Caxias+RJ',  # DUQUE DE CAXIAS
                                'Itaguai+RJ',  # ITAGUAI
                                'Itaocara+RJ',  # ITAOCARA
                                'Itaperuna+RJ',  # ITAPERUNA
                                'Japeri+RJ',  # JAPERI
                                'Macae+RJ',  # MACAE
                                'Mage+RJ',  # MAGE
                                'Manhuacu+RJ',  # MANHUACU
                                'Niteroi+RJ',  # NITEROI
                                'Nova+Friburgo+RJ',  # NOVA FRIBURGO
                                'Nova+Iguacu+RJ',  # NOVA IGUACU
                                'Paraiba+do+Sul+RJ',  # PARAIBA DO SUL
                                'Petropolis+RJ',  # PETROPOLIS
                                'Queimados+RJ',  # QUEIMADOS
                                'Rio+de+Janeiro+RJ',  # RIO DE JANEIRO
                                'Santa+Maria+Madalena+RJ',  # SANTA MARIA MADALENA
                                'Santo+Antonio+de+Padua+RJ',  # SANTO ANTONIO DE PADUA
                                'Sao+Goncalo+RJ',  # SAO GONCALO
                                'Sao+Joao+de+Meriti+RJ',  # SAO JOAO DE MERITI
                                'Teresopolis+RJ',  # TERESOPOLIS
                                'Tres+Rios+RJ',  # TRES RIOS
                                'Valenca+RJ',  # VALENCA
                                'Varre-Sai+RJ',  # VARRE - SAI
                                'Vassouras+RJ',  # VASSOURAS
                                'Volta+Redonda+RJ'  # VOLTA REDONDA
                                ]
    return cidades


def criaMatrizDeDistancias(dados):
    enderecos = dados["enderecos"]
    chave_API = dados["chave_API"]

    # A API de Matriz de Distancia do google so aceita 100 elementos por requisicao, entao faremos multiplas requisicoes.
    numMaxElementos = 100
    numEnderecos = len(enderecos)

    # O numero maximo de linhas que pode ser computado por requisicao.
    maxLinhas = numMaxElementos // numEnderecos

    # numEnderecos = q * maxLinhas + r.
    q, r = divmod(numEnderecos, maxLinhas)
    enderecosDestino = enderecos
    matrizDeDistancias = []

    # Envia q requisicoes, retornando maxLinhas por requisicao.
    for i in range(q):
        enderecosOrigem = enderecos[i * maxLinhas: (i + 1) * maxLinhas]
        resposta = enviaRequisicao(enderecosOrigem, enderecosDestino, chave_API)
        matrizDeDistancias += montaMatrizDeDistancias(resposta)

    # Pega o restante r de linhas se necessario.
    if r > 0:
        enderecosOrigem = enderecos[q * maxLinhas: q * maxLinhas + r]
        resposta = enviaRequisicao(enderecosOrigem, enderecosDestino, chave_API)
        matrizDeDistancias += montaMatrizDeDistancias(resposta)
    return matrizDeDistancias


def enviaRequisicao(enderecosOrigem, enderecosDestino, chave_API):
    """ Monta e envia requisicoes para os enderecos de origem e destino passados."""

    def montaStringEndereco(enderecos):
        # Monta a string com os enderecos separadas por 'pipe(|)'
        stringEndereco = ''
        for i in range(len(enderecos) - 1):
            stringEndereco += enderecos[i] + '|'
        stringEndereco += enderecos[-1]
        return stringEndereco

    requisicao = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=metric'
    stringEnderecoOrigem = montaStringEndereco(enderecosOrigem)
    stringEnderecoDestino = montaStringEndereco(enderecosDestino)
    requisicao = requisicao + '&origins=' + stringEnderecoOrigem + '&destinations=' + \
                 stringEnderecoDestino + '&key=' + chave_API
    resultadoJson = urllib.urlopen(requisicao).read()
    resposta = json.loads(resultadoJson)
    return resposta


def montaMatrizDeDistancias(resposta):
    matrizDeDistancias = []
    for linha in resposta['rows']:
        listaLinha = [linha['elements'][j]['distance']['value'] for j in range(len(linha['elements']))]
        matrizDeDistancias.append(listaLinha)
    return matrizDeDistancias


# FUNCOES UTILIZADAS NA SOLUCAO DO PROBLEMA DO CAIXEIRO VIAJANTE
def criaModeloDeDados(matrizDeDistancias):
    """Armazena os dados para o problema."""
    dados = {}
    dados['matrizDeDistancias'] = matrizDeDistancias
    dados['numVeiculos'] = 10
    dados['pontoDePartida'] = 0
    return dados


def imprimeSolucao(dados, gerenciador, roteamento, solucao):
    """Imprime a Solucao no arquivo/console."""
    f = open("solucaoSAT.txt", "a+")
    f.write("\n\n")
    distanciaMaxPercorrida = 0
    for idVeiculo in range(dados['numVeiculos']):
        indice = roteamento.Start(idVeiculo)
        planejamento = 'Rota para o veiculo {}:\n'.format(idVeiculo)
        distanciaRota = 0
        while not roteamento.IsEnd(indice):
            planejamento += ' {} -> '.format(gerenciador.IndexToNode(indice))
            indiceAnterior = indice
            indice = solucao.Value(roteamento.NextVar(indice))
            distanciaRota += roteamento.GetArcCostForVehicle(
                indiceAnterior, indice, idVeiculo)
        planejamento += '{}\n'.format(gerenciador.IndexToNode(indice))
        planejamento += 'Distancia da rota: {}m\n\n'.format(distanciaRota)
        f.write(str(planejamento))
        distanciaMaxPercorrida = max(distanciaRota, distanciaMaxPercorrida)
    f.write('Maior distancia entre as rotas: {}m'.format(distanciaMaxPercorrida))
    f.write("\n")


def getMatrizDeDistancias(dia):
    if dia == 0:  # segunda
        return  [
                    [0, 311290, 14774, 51265, 114051, 232315, 225014, 142764, 169493, 222845],
                    [317396, 0, 305159, 266708, 292149, 448290, 440989, 358739, 385468, 438820],
                    [15009, 297738, 0, 37712, 100499, 218763, 211462, 129212, 155941, 209293],
                    [51599, 261420, 39362, 0, 64181, 192221, 184920, 102670, 129399, 182751],
                    [114566, 293447, 102330, 63878, 0, 153238, 238159, 95240, 182638, 142835],
                    [246799, 463613, 234562, 206717, 152075, 0, 135445, 88827, 78906, 11567],
                    [223688, 440502, 211452, 183606, 237479, 133809, 0, 155982, 120154, 129481],
                    [142767, 359581, 130530, 102685, 95438, 74009, 159411, 0, 33327, 64539],
                    [169106, 385920, 156870, 129024, 182897, 64886, 122640, 33297, 0, 55416],
                    [222903, 439716, 210666, 182820, 141975, 11017, 132005, 64930, 55009, 0]
                ]
    elif dia == 1:  # terca
        return  [
                    [0, 85131, 311290, 145644, 350064, 252339, 133689, 97585, 150313, 169394, 270955, 154095, 128862],
                    [85211, 0, 379908, 65693, 266546, 198870, 53738, 17634, 70362, 140826, 191004, 72829, 74405],
                    [317396, 379324, 0, 442148, 566039, 475143, 430193, 394088, 446817, 371334, 589384, 463379, 401488],
                    [143911, 64363, 442754, 0, 147753, 174510, 29721, 48099, 27543, 167358, 117440, 23689, 104882],
                    [342903, 261709, 565511, 154925, 0, 193534, 218944, 272557, 223615, 299946, 95144, 150212, 278173],
                    [252017, 198512, 475725, 174321, 186416, 0, 153613, 194364, 158284, 108110, 113113, 210413, 127937],
                    [132563, 53015, 431406, 34201, 212111, 154570, 0, 45282, 18165, 140074, 138807, 57890, 77598],
                    [95812, 16264, 394655, 48060, 277555, 211749, 58720, 0, 61645, 151428, 195987, 70968, 85007],
                    [146153, 66605, 444995, 27641, 216113, 158573, 14278, 61691, 0, 151420, 142810, 51330, 88944],
                    [169044, 139832, 371021, 171329, 291409, 107451, 138669, 152286, 155293, 0, 218105, 195018, 69257],
                    [269482, 189934, 589353, 116147, 87437, 113049, 138459, 182201, 143130, 219461, 0, 111434, 197688],
                    [154207, 73014, 464397, 23445, 142268, 210346, 53166, 71076, 50987, 190803, 111956, 0, 128326],
                    [131816, 74366, 404905, 109687, 270679, 128256, 77027, 86820, 93651, 70212, 197376, 133376, 0]
                ]
    elif dia == 2:  # quarta
        return [
                    [0, 145965, 174309, 193014, 67981, 404421, 51265, 108223, 217859, 103292, 97172, 116474, 176081, 131390, 239297, 230703, 159832, 225014],
                    [153328, 0, 28939, 301572, 139593, 470818, 102639, 216781, 220213, 77975, 51312, 115788, 178435, 133744, 347856, 282609, 211739, 276921],
                    [180079, 29100, 0, 328323, 166344, 495596, 129391, 243532, 246964, 104726, 78063, 142540, 221209, 160496, 374607, 309360, 238490, 303672],
                    [192713, 300477, 328821, 0, 146875, 263074, 242776, 85587, 191492, 223375, 288684, 183614, 171884, 163132, 75526, 388410, 319906, 382722],
                    [67784, 138495, 166840, 146329, 0, 357736, 117847, 63330, 157280, 61393, 141363, 54686, 115502, 69602, 192613, 263481, 194977, 257793],
                    [403571, 490547, 513882, 262557, 357734, 0, 453634, 296445, 259641, 434233, 499542, 366668, 306465, 346186, 197114, 599269, 530764, 593580],
                    [51599, 96095, 124439, 243410, 118378, 454818, 0, 158619, 215668, 74681, 47303, 111243, 173890, 129199, 289694, 190609, 119738, 184920],
                    [108259, 216022, 244367, 85547, 64513, 296954, 158322, 0, 131300, 138920, 204229, 101251, 89522, 80769, 131831, 303956, 235451, 298268],
                    [237527, 219376, 247720, 191400, 157712, 260230, 215681, 131574, 0, 142274, 222243, 107493, 47291, 87012, 125957, 419282, 348412, 413593],
                    [122899, 77102, 105447, 223597, 61618, 435004, 75071, 138806, 142238, 0, 79970, 37813, 100460, 55770, 269881, 278671, 207801, 272983],
                    [103918, 50565, 78909, 295730, 141422, 507137, 53230, 210939, 222042, 79804, 0, 117617, 180264, 135573, 342014, 233199, 162329, 227511],
                    [125110, 114421, 142765, 183691, 63829, 367082, 110726, 100692, 107319, 37318, 117288, 0, 65541, 20850, 229975, 314327, 243456, 308638],
                    [195235, 177084, 205428, 172281, 115420, 307036, 173390, 89282, 47273, 99982, 179952, 65202, 0, 44720, 172764, 376990, 306120, 371302],
                    [141397, 133700, 162044, 163268, 75406, 346659, 130005, 80269, 86896, 56598, 136567, 21817, 45117, 0, 209551, 333606, 262735, 327917],
                    [239216, 346980, 375324, 75801, 193378, 197744, 289279, 132090, 126167, 269878, 335187, 233194, 172991, 212712, 0, 434913, 366409, 429225],
                    [232159, 283647, 311991, 373455, 248423, 584862, 192076, 288664, 421787, 280800, 234855, 317362, 380009, 335318, 419739, 0, 76027, 22460],
                    [162268, 213757, 242101, 322323, 197290, 533730, 122186, 237532, 351897, 210910, 164965, 247472, 310119, 265428, 368607, 74970, 0, 69282],
                    [223688, 275177, 303521, 380923, 255890, 592330, 183606, 296132, 413317, 272330, 226384, 308892, 371539, 326848, 427207, 19008, 67556, 0]
                ]
    elif dia == 3:  # quinta
        return  [
                    [0, 311290, 14774, 51265, 114051, 232315, 225014, 142764, 169493, 222845],
                    [317396, 0, 305159, 266708, 292149, 448290, 440989, 358739, 385468, 438820],
                    [15009, 297738, 0, 37712, 100499, 218763, 211462, 129212, 155941, 209293],
                    [51599, 261420, 39362, 0, 64181, 192221, 184920, 102670, 129399, 182751],
                    [114566, 293447, 102330, 63878, 0, 153238, 238159, 95240, 182638, 142835],
                    [246799, 463613, 234562, 206717, 152075, 0, 135445, 88827, 78906, 11567],
                    [223688, 440502, 211452, 183606, 237479, 133809, 0, 155982, 120154, 129481],
                    [142767, 359581, 130530, 102685, 95438, 74009, 159411, 0, 33327, 64539],
                    [169106, 385920, 156870, 129024, 182897, 64886, 122640, 33297, 0, 55416],
                    [222903, 439716, 210666, 182820, 141975, 11017, 132005, 64930, 55009, 0]
                ]
    elif dia == 4:  # sexta
        return [
                    [0, 85131, 311290, 108223, 145644, 350064, 252339, 133689, 97585, 150313, 169394, 270955, 154095, 225014, 128862],
                    [85211, 0, 379908, 116175, 65693, 266546, 198870, 53738, 17634, 70362, 140826, 191004, 72829, 184455, 74405],
                    [317396, 379324, 0, 311954, 442148, 566039, 475143, 430193, 394088, 446817, 371334, 589384, 463379, 440989, 401488],
                    [108259, 116304, 312328, 0, 176818, 347288, 163331, 164863, 128758, 181487, 59522, 273984, 185269, 298268, 85413],
                    [143911, 64363, 442754, 174875, 0, 147753, 174510, 29721, 48099, 27543, 167358, 117440, 23689, 164958, 104882],
                    [342903, 261709, 565511, 355782, 154925, 0, 193534, 218944, 272557, 223615, 299946, 95144, 150212, 156063, 278173],
                    [252017, 198512, 475725, 163946, 174321, 186416, 0, 153613, 194364, 158284, 108110, 113113, 210413, 278885, 127937],
                    [132563, 53015, 431406, 163527, 34201, 212111, 154570, 0, 45282, 18165, 140074, 138807, 57890, 199160, 77598],
                    [95812, 16264, 394655, 126777, 48060, 277555, 211749, 58720, 0, 61645, 151428, 195987, 70968, 196837, 85007],
                    [146153, 66605, 444995, 177117, 27641, 216113, 158573, 14278, 61691, 0, 151420, 142810, 51330, 192600, 88944],
                    [169044, 139832, 371021, 59242, 171329, 291409, 107451, 138669, 152286, 155293, 0, 218105, 195018, 383878, 69257],
                    [269482, 189934, 589353, 275297, 116147, 87437, 113049, 138459, 182201, 143130, 219461, 0, 111434, 179906, 197688],
                    [154207, 73014, 464397, 185172, 23445, 142268, 210346, 53166, 71076, 50987, 190803, 111956, 0, 141530, 128326],
                    [223688, 183974, 440502, 296132, 163803, 155695, 277430, 193525, 194822, 191346, 320783, 179040, 140337, 0, 254362],
                    [131816, 74366, 404905, 88375, 109687, 270679, 128256, 77027, 86820, 93651, 70212, 197376, 133376, 256329, 0]
                ]
    elif dia == 5:  # sabado
        return [
                    [0, 145965, 174309, 193014, 67981, 404421, 51265, 108223, 217859, 103292, 97172, 116474, 176081, 131390, 239297, 230703, 159832, 225014],
                    [153328, 0, 28939, 301572, 139593, 470818, 102639, 216781, 220213, 77975, 51312, 115788, 178435, 133744, 347856, 282609, 211739, 276921],
                    [180079, 29100, 0, 328323, 166344, 495596, 129391, 243532, 246964, 104726, 78063, 142540, 221209, 160496, 374607, 309360, 238490, 303672],
                    [192713, 300477, 328821, 0, 146875, 263074, 242776, 85587, 191492, 223375, 288684, 183614, 171884, 163132, 75526, 388410, 319906, 382722],
                    [67784, 138495, 166840, 146329, 0, 357736, 117847, 63330, 157280, 61393, 141363, 54686, 115502, 69602, 192613, 263481, 194977, 257793],
                    [403571, 490547, 513882, 262557, 357734, 0, 453634, 296445, 259641, 434233, 499542, 366668, 306465, 346186, 197114, 599269, 530764, 593580],
                    [51599, 96095, 124439, 243410, 118378, 454818, 0, 158619, 215668, 74681, 47303, 111243, 173890, 129199, 289694, 190609, 119738, 184920],
                    [108259, 216022, 244367, 85547, 64513, 296954, 158322, 0, 131300, 138920, 204229, 101251, 89522, 80769, 131831, 303956, 235451, 298268],
                    [237527, 219376, 247720, 191400, 157712, 260230, 215681, 131574, 0, 142274, 222243, 107493, 47291, 87012, 125957, 419282, 348412, 413593],
                    [122899, 77102, 105447, 223597, 61618, 435004, 75071, 138806, 142238, 0, 79970, 37813, 100460, 55770, 269881, 278671, 207801, 272983],
                    [103918, 50565, 78909, 295730, 141422, 507137, 53230, 210939, 222042, 79804, 0, 117617, 180264, 135573, 342014, 233199, 162329, 227511],
                    [125110, 114421, 142765, 183691, 63829, 367082, 110726, 100692, 107319, 37318, 117288, 0, 65541, 20850, 229975, 314327, 243456, 308638],
                    [195235, 177084, 205428, 172281, 115420, 307036, 173390, 89282, 47273, 99982, 179952, 65202, 0, 44720, 172764, 376990, 306120, 371302],
                    [141397, 133700, 162044, 163268, 75406, 346659, 130005, 80269, 86896, 56598, 136567, 21817, 45117, 0, 209551, 333606, 262735, 327917],
                    [239216, 346980, 375324, 75801, 193378, 197744, 289279, 132090, 126167, 269878, 335187, 233194, 172991, 212712, 0, 434913, 366409, 429225],
                    [232159, 283647, 311991, 373455, 248423, 584862, 192076, 288664, 421787, 280800, 234855, 317362, 380009, 335318, 419739, 0, 76027, 22460],
                    [162268, 213757, 242101, 322323, 197290, 533730, 122186, 237532, 351897, 210910, 164965, 247472, 310119, 265428, 368607, 74970, 0, 69282],
                    [223688, 275177, 303521, 380923, 255890, 592330, 183606, 296132, 413317, 272330, 226384, 308892, 371539, 326848, 427207, 19008, 67556, 0]
                ]
    else:
        return 0

def resolverdorSat():
    gmaps = False
    f = open("solucaoSAT.txt", "a+")
    # FUNCOES PARA MONTAGEM DA MATRIZ DE DISTANCIAS
    for x in range(0, 6):
        f.write("#################### Dia " + str(x) + " ####################\n")

        if gmaps:
            # Cria os dados.
            dados = getEnderecos(x)
            enderecos = dados['enderecos']
            chave_API = dados['chave_API']
            matrizDeDistancias = criaMatrizDeDistancias(dados)
            f.write("Matriz de distancias: \n" + str(matrizDeDistancias))
        else:
            matrizDeDistancias = getMatrizDeDistancias(x)

        # FUNCOES PARA RESOLUCAO DO PROBLEMA DO CAIXEIRO VIAJANTE
        """Resolucao do problema de roteamento."""
        # Instancia os dados do problema.
        dados = criaModeloDeDados(matrizDeDistancias)
        # Cria o gerenciador de indice do roteamento.
        gerenciador = pywrapcp.RoutingIndexManager(
            len(dados['matrizDeDistancias']), dados['numVeiculos'], dados['pontoDePartida'])
        # Cria o modelo do roteamento.
        roteamento = pywrapcp.RoutingModel(gerenciador)

        # Cria e registra callback de transito.
        def distance_callback(indiceOrigem, indiceDestino):
            """Retorna a distancia entre dois nos."""
            # Converte de um indice da variavel roteamento para um indice da matriz de distancias.
            noOrigem = gerenciador.IndexToNode(indiceOrigem)
            noDestino = gerenciador.IndexToNode(indiceDestino)
            return dados['matrizDeDistancias'][noOrigem][noDestino]

        transit_callback_index = roteamento.RegisterTransitCallback(distance_callback)

        # Define o custo para cada arco.
        roteamento.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        # Adiciona restricao de distancia.
        nomeDimensao = 'Distance'
        roteamento.AddDimension(
            transit_callback_index,
            0,  # sem folga
            400000000,  # maior distancia percorrida por um veiculo
            True,  # inicia acumulando do 0
            nomeDimensao)
        dimensaoDistancia = roteamento.GetDimensionOrDie(nomeDimensao)
        dimensaoDistancia.SetGlobalSpanCostCoefficient(100)

        # Configura a heuristica para "primeira solucao".
        parametrosDeBusca = pywrapcp.DefaultRoutingSearchParameters()
        parametrosDeBusca.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

        # Resolve com os parametros.
        solucao = roteamento.SolveWithParameters(parametrosDeBusca)

        if solucao:
            f.flush()
            imprimeSolucao(dados, gerenciador, roteamento, solucao)
            f.write("\n")
        else:
            f.flush()
            f.write("\nSolucao nao encontrada\n")
    f.close()

def resolverdorLinear():
    f = open("solucaoLinear.txt", "a+")
    # FUNCOES PARA MONTAGEM DA MATRIZ DE DISTANCIAS
    for x in range(0, 6):
        f.write("#################### Dia " + str(x) + " ####################\n")

        matrizDeDistancias = getMatrizDeDistancias(x)
        #f.write("Matriz de distancias: \n" + str(matrizDeDistancias))

        #Resolvedor Linear
        # Numero de clientes.
        n = len(matrizDeDistancias)
        # conjunto de clientes
        clientes = [x for x in range(1, n)]

        # nos do 'grafo'
        nos = [0] + clientes

        # Capacidade dos veiculos(distancia).
        Q = 15

        # O conjunto de clientes menos a empresa.
        N = [i for i in range(1, n + 1)]

        # O conjunto de clientes mais a empresa
        V = [0] + N

        # "rnd" gera numeros aleatorios.
        rnd = np.random
        rnd.seed(0)
        # Uma estrutura que armazena a demanda de cada no.
        q = {i: rnd.randint(1, 10) for i in clientes}

        ##### DESENHO INICIAL #####
        # Gera numero aleatorios entre(0 e 15)*200 para coordenada x
        coordx = rnd.rand(len(V)) * 200
        # Gera numero aleatorios entre(0 e 15)*100 para coordenada y
        coordy = rnd.rand(len(V)) * 100
        # Desenha os 'n' nos menos o no '0' e configura a cor azul para eles.
        plt.scatter(coordx[1:], coordy[1:], c='b')
        # Desenha o no '0' como um quadrado e colore ele de vermelho
        plt.plot(coordx[0], coordy[0], c='r', marker='s')
        plt.xlabel("Eixo X")
        plt.ylabel("Eixo Y")
        plt.title("Grafico de Nos | PRV")
        # Mostra a configuracao inicial.
        plt.show()
        ##############################

        # Inicializa um conjunto de arcos A.

        arcos = {(i, j) for i in nos for j in nos if i != j}
        #modelo cplex
        mdl = Model('PRV')
        # Inicializar a variavel binaria Xij
        x = mdl.binary_var_dict(arcos, name='x')

        # Inicializa a demanda cumulativa u
        u = mdl.continuous_var_dict(N, ub=Q, name='u')

        # Inicializa a funcao objetivo
        mdl.minimize(mdl.sum(matrizDeDistancias[i][j]*x[i,j] for i,j in arcos))
        # restricao 1
        mdl.add_constraints(mdl.sum(x[i, j] for j in nos if i != j) == 1 for i in clientes)
        # restricao 2
        mdl.add_constraints(mdl.sum(x[i, j] for i in nos if i != j) == 1 for j in clientes)
        # restricao 3
        mdl.add_indicator_constraints(mdl.indicator_constraint(x[i, j], u[i] + q[j] == u[j])for i, j in arcos if i != 0 and j != 0)
        # restricao 4
        mdl.add_constraints(u[i] >= q[i] for i in clientes)
        print("")

        #limitacao de tempo para achar a solucao
        mdl.parameters.timelimit = 120
        # Obtem a solucao
        solucao = mdl.solve(log_output=True)

        mdl.get_solve_status()
        solucao.display()
        # Imprime a solucao
        f.write(str(solucao))

        # Identifica os arcos escolhidos
        arcosEscolhidos = [a for a in arcos if x[a].solution_value > 0.9]
        plt.scatter(coordx[1:], coordy[1:], c='b')
        for i, j in arcosEscolhidos:
            # Colorindo as arestas ativas
            plt.plot([coordx[i], coordx[j]], [coordy[i], coordy[j]], c='g', alpha=0.3)
        plt.plot(coordx[0], coordy[0], c='r', marker='s')
        # Mostra a solucao
        plt.show()
    f.close()

########
# Main #
########
def main():
    print("Inicio resolvedor SAT\n")
    resolverdorSat()
    print("Fim Resolvedor SAT\n\n")

    print("Inicio resolvedor linear CPLEX\n")
    resolverdorLinear()
    print("Fim resolvedor linear CPLEX\n\n")


if __name__ == '__main__':
    main()
