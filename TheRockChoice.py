# Link para sound effect de menu https://www.youtube.com/watch?v=X-aU6-cSRdA&ab_channel=LTSoundEffects


import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
import webbrowser
import random
from bs4 import BeautifulSoup


print("\nOlá seja bem vindo ao")

print("""  
           ▀▀█▀▀ █░░█ █▀▀   █▀▀█ █▀▀█ █▀▀ █░█   █▀▀█ █░░█ █▀▀█ ░▀░ █▀▀ █▀▀
           ░▒█░░ █▀▀█ █▀▀   █▄▄▀ █░░█ █░░ █▀▄   █░░░ █▀▀█ █░░█ ▀█▀ █░░ █▀▀
           ░▒█░░ ▀░░▀ ▀▀▀   █░▒█ ▀▀▀▀ ▀▀▀ ▀░▀   █▄▄█ ▀░░▀ ▀▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀""")

print("\nNão sabe qual filme do THE ROCK VER HOJE?\n")
print("\nSeus problemas acabaram, iremos escolher o filme perfeito para você de acordo com seus dados\n")
nome = input("\nPor favor digite seu nome:\n")
time.sleep(3)
idade = input("\nAgora preciso de sua idade:\n")
time.sleep(3)
color = input("\nMuito bem, agora sua cor favorita:\n")
time.sleep(3)
signo = input("\nQual o seu signo:\n")
time.sleep(2)
print("\nCarregando dados")
print("\n-", nome, "-", idade, "-", color, "-", signo,"-", signo, "-", color, "-", idade, "-", nome)
time.sleep(2)
print("\nAnalisando informações sanguineas")
time.sleep(2)
print("\nA pagina do filme ideal do The Rock escolhido irá abrir nos próximos segundos, aproveite o filme.💪")
time.sleep(1)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)


luck = random.randint(0, 36)


navegador = webdriver.Edge()

lista_The_Rock = ["https://www.justwatch.com/br/filme/velocidade-furiosa-8",
                  "https://www.justwatch.com/br/serie/ballers",
                  "https://www.justwatch.com/br/filme/jumanji-welcome-to-the-jungle",
                  "https://www.justwatch.com/br/filme/jumanji-o-nivel-seguinte",
                  "https://www.justwatch.com/br/filme/fast-five-extended",
                  "https://www.justwatch.com/br/filme/dc-league-of-super-pets",
                  "https://www.justwatch.com/br/filme/velozes-and-furiosos-hobbs-and-shaw",
                  "https://www.justwatch.com/br/filme/velozes-e-furiosos-7",
                  "https://www.justwatch.com/br/filme/terremoto-a-falha-de-san-andreas",
                  "https://www.justwatch.com/br/filme/moana",
                  "https://www.justwatch.com/br/filme/jungle-cruise",
                  "https://www.justwatch.com/br/filme/rampage-fora-de-controlo",
                  "https://www.justwatch.com/br/filme/red-notice",
                  "https://www.justwatch.com/br/filme/hercules",
                  "https://www.justwatch.com/br/serie/young-rock",
                  "https://www.justwatch.com/br/filme/os-outros-caras",
                  "https://www.justwatch.com/br/filme/uma-familia-no-ringue",
                  "https://www.justwatch.com/br/filme/race-to-witch-mountain",
                  "https://www.justwatch.com/br/filme/o-retorno-da-mumia",
                  "https://www.justwatch.com/br/filme/a-gangue-esta-em-campo",
                  "https://www.justwatch.com/br/filme/com-as-proprias-maos",
                  "https://www.justwatch.com/br/filme/baywatch-mares-vivas",
                  "https://www.justwatch.com/br/filme/central-intelligence",
                  "https://www.justwatch.com/br/filme/g-i-joe-retaliacao",
                  "https://www.justwatch.com/br/filme/o-rei-escorpiao",
                  "https://www.justwatch.com/br/filme/arranha-ceus-2018",
                  "https://www.justwatch.com/br/filme/sem-dor-sem-ganho",
                  "https://www.justwatch.com/br/filme/agente-86",
                  "https://www.justwatch.com/br/filme/o-fada-do-dente",
                  "https://www.justwatch.com/br/filme/rapida-vinganca",
                  "https://www.justwatch.com/br/filme/viagem-2",
                  "https://www.justwatch.com/br/filme/treinando-o-papai",
                  "https://www.justwatch.com/br/filme/empire-state-o-assalto",
                  "https://www.justwatch.com/br/filme/doom-a-porta-do-inferno",
                  "https://www.justwatch.com/br/filme/o-acordo",
                  "https://www.justwatch.com/br/filme/bem-vindos-a-selva"]


pum = lista_The_Rock[luck]

webbrowser.open_new_tab(pum)

print("Bye")
