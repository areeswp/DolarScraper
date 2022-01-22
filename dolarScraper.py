# import lib
# pip selenium, webdriver-manager

import datetime
from datetime import timedelta
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys
from webdriver_manager.chrome import ChromeDriverManager

# configurando selenium
# configuring selenium
driverOptions = webdriver.ChromeOptions()
driverOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(ChromeDriverManager().install(), options=driverOptions)
driver.get(
    "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/aplicacao#!/recursos/CotacaoDolarDia#eyJmb3JtdWxhcmlvIjp7IiRmb3JtYXQiOiJqc29uIiwiJHRvcCI6MTAwfX0="
)
driver.maximize_window()
time.sleep(1)
# id do campo de data de cotação do site
# website's quotation date id field
element = driver.find_element(By.ID, "param0")

# declaração das variáveis globais
# global variables
aimDate = datetime.date(2022, 1, 20)
userDate = datetime.date(2022, 1, 20)
# variável de 1 dia para alterar a variável data
# 1 day variable to change the date variable
day = timedelta(days=1)
# lista com os dias do final de semana
# list with weekend days
weekend = ["Saturday", "Sunday"]
# criação da variável aim, com a data fixada no dia 15 (ano e mês irrelevantes)
# variable aim, with date fixed in day 15 (year and month irrelevant)
aim = datetime.date(2021, 12, 15)
dolarCompra = "0"
dolarVenda = "0"
dataCompra = {}
dataVenda = {}
dataExata = "0"

print(
    "Essas são as minhas funções: \n" 
    "(1) = Valores do dólar para a data especificada (ou primeiro dia útil anterior à data)\n"
    "(2) = Valores do dólar no último dia útil na primeira quinzena do mês anterior à data especificada\n"
    )
dataExata = input("Por favor, selecione a função desejada: ")
while dataExata not in ("1","2"):
    print("Por favor, digite uma opção válida: (1 ou 2) ")
    dataExata = input("Por favor, selecione a função desejada: ")
# input da data pelo usuário
# user's date input
def inputDate():
    isValid = False
    global aimDate
    global userDate
    while not isValid:
        userDate = input(
            "Digite a data da movimentação (dd/mm/yyyy), ou 0 para sair do programa: "
        )
        time.sleep(1)
        if userDate == "0":
            print(
                "Lista das datas e respectivos preços de compra do dólar consultados:\n"
                + str(dataCompra)
            )
            print(
                "\nLista das datas e respectivos preços de venda do dólar consultados: \n"
                + str(dataVenda)
            )
            driver.close()
            sys.exit("\nFim do programa")
        try:  # conferência no formato de dd/mm/yyyy e armazenamento nas variáveis; checking format dd/mm/yyyy and store in variables
            aimDate = datetime.datetime.strptime(userDate, "%d/%m/%Y")
            # altera variável userDate em formato de data
            # changes userDate variable into a date format
            userDate = datetime.datetime.strptime(userDate, "%d/%m/%Y")
            isValid = True
        except:  # se o input tiver formato diferente, tente novamente; if different format, try again
            print("Verifique a data e tente novamente!")


inputDate()

# função com while para chegar ao mês anterior ao inputado
# this while function gets us to the month before the input
def adjustDate():
    global aimDate
    global userDate
    while aimDate.strftime("%m") == userDate.strftime("%m"):
        aimDate = aimDate - day
    # loop para chegar ao último dia da primeira quinzena do mês anterior da operação
    # loop to get to the last weekday of the first 15-days (fortnight) of the month before the input
    while aimDate.strftime("%d") > aim.strftime("%d"):
        aimDate = aimDate - day

# verifica o input do usuário na variável dataExata, e utiliza a função adjustDate se necessário
# verifies user input in dataExata variable and uses function adjustDate, if needed.

if dataExata == "2":
    adjustDate()
# função com loop para chegar em um dia útil, se necessário
# loop function to get to a weekday, if needed
def conferirData():
    global aimDate
    isValid = False
    while not isValid:
        if aimDate.strftime("%A") in weekend:
            aimDate = aimDate - day
        else:
            isValid = True


conferirData()
# função site com todos passos após abertura do bcb
# site function with all steps after site opening
def site():
    # apaga dados no campo
    # clears field data
    element.clear()
    # input da data no campo representado pela variável element
    # date input in the field represented by the element variable
    element.send_keys(aimDate.strftime("%m/%d/%Y")
    # encontra as checkboxes e as pressiona se não estiverem pressionadas
    # find the checkboxes and presses them, if not already pressed
    select1 = driver.find_element(By.XPATH, "//tr[1]/td[1]/input")
    if select1.is_selected() == False:
        select1.click()
    select2 = driver.find_element(By.XPATH, "//tr[2]/td[1]/input")
    if select2.is_selected() == False:
        select2.click()
    # pressione executar
    # press execute
    select3 = driver.find_element(By.XPATH, "//div[9]/div/div/button").click()
    time.sleep(2)


# loop para evitar erros. Se o programa não retornar valores, diminui um dia da data até encontrar resultados ou encerra o código se chegar a 7 repetições
# loop to avoid errors. If the program doesn't return values it decreases day by day until finding a result or shuts down the code if it gets to 7 repetitions
def tryanderror():
    contador = 0
    global dolarCompra
    global dolarVenda
    global aimDate
    while dolarCompra == "0":
        site()
        time.sleep(1)
        try:
            dolarCompra = driver.find_element(
                By.XPATH,
                "/html/body/div[3]/div/div/ng-view/olinda-ptax/div[3]/div[3]/div/div/div/div[2]/div[2]/div/div/div/div[1]/div",
            )
            dolarVenda = driver.find_element(
                By.XPATH,
                "/html/body/div[3]/div/div/ng-view/olinda-ptax/div[3]/div[3]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div",
            )
            # armazena apenas os valores de saída do BCB, ignorando a estrutura html
            # stores only the output value from BCB, ignoring html structure
            dolarCompra = dolarCompra.get_attribute("innerHTML")
            dolarVenda = dolarVenda.get_attribute("innerHTML")
        except:
            aimDate = aimDate - day
            conferirData()
            contador += 1
            if contador >= 7:
                print(
                    "Não foi possível encontrar uma data válida para o período especificado."
                )
                driver.close()
                print(
                    "Lista das datas e respectivos preços de compra do dólar consultados:\n"
                    + str(dataCompra)
                )
                print(
                    "\nLista das datas e respectivos preços de venda do dólar consultados: \n"
                    + str(dataVenda)
                )
                sys.exit("\nFim do programa")


tryanderror()
# output do programa
# program output
def output():
    global aimDate
    global dolarCompra
    global dolarVenda
    print(
        "\nA data utilizada foi "
        + str(aimDate.strftime("%d/%m/%Y"))
        + " e caiu em: "
        + str(aimDate.strftime("%A"))
    )
    dataCompra[aimDate.strftime("%d/%m/%Y")] = dolarCompra
    dataVenda[aimDate.strftime("%d/%m/%Y")] = dolarVenda
    print("\nO preço de compra do dólar no dia era de: R$" + str(dolarCompra))
    print("\nO preço de venda do dólar no dia era de: R$" + str(dolarVenda) + "\n")


output()
# repetição para inserir mais datas
# loop to get more dates
while userDate != "0":
    inputDate()
    if dataExata == "2":
        adjustDate()
    conferirData()
    dolarCompra = "0"
    tryanderror()
    output()
