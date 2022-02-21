# import libs
# pip selenium, webdriver-manager, pandas

import datetime
from datetime import timedelta
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# configurando selenium
# configuring selenium
driverOptions = webdriver.ChromeOptions()
driverOptions.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=driverOptions)
driver.get(
    "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/aplicacao#!/recursos/CotacaoDolarDia#eyJmb3JtdWxhcmlvIjp7IiRmb3JtYXQiOiJqc29uIiwiJHRvcCI6MTAwfX0="
)
driver.maximize_window()
time.sleep(1)
try: # busca o id do campo da data de cotação do site; tries to locate the website's quotation date id field
    element = driver.find_element(By.ID, "param0")
except: # mensagem de erro e finalização do programa caso não encontre o elemento necessário; error message and program end in case it doesn't find necessary element
    sys.exit(
        "Impossível de alcançar o site e localizar o elemento necessário; favor tente novamente mais tarde ou confira se houve alteração no HTML do site."
    )
# declaração das variáveis globais
# global variables
aimDate = datetime.date(2022, 1, 20) # data que o usuário busca, convertida em formato datetype; the date that the user aims, converted in datetype format
userDate = datetime.date(2022, 1, 20) # input do usuário, formato inicial em string e depois convertida para datetype; user input, string initial format, later converted to datetype
finalDate = datetime.date(2022, 1, 20) # em busca por período armazena a data final; in search by period it stores the final date
day = timedelta(days=1) # variável de 1 dia; 1 day variable
weekend = ["Saturday", "Sunday"] # lista com os dias do final de semana; list with weekend days
dolarCompra = "0"
dolarVenda = "0"
dataCompra = {}
dataVenda = {}
userOption = "0"

print(
    "Essas são as minhas funções: \n" 
    "(1) = Valores do dólar para a data especificada (ou primeiro dia útil anterior à data)\n"
    "(2) = Valores do dólar no último dia útil na primeira quinzena do mês anterior à data especificada\n"
    "(3) = Valores do dólar para o período especificado (entre duas datas)\n"
    )
userOption = input("Por favor, selecione a função desejada: ")
while userOption not in ("1","2","3"):
    print("Por favor, digite uma opção válida: (1, 2 ou 3) ")
    userOption = input("Por favor, selecione a função desejada: ")

# função para encerrar o programa
# exit program function
def endProgram():
    print(pd.DataFrame(list(dataCompra.items()),
                    columns=['Dia', 'Preço de Compra'])
    )
    print(pd.DataFrame(list(dataVenda.items()),
                    columns=['Dia', 'Preço de Venda'])
    )
    driver.close()
    sys.exit("\nFim do programa")

# função de input da data pelo usuário
# user's date input function
def inputDate():
    isValid = False
    global aimDate
    global userDate
    global finalDate
    while not isValid:
        if userOption in ("1","2"):
            userDate = input(
                "Digite a data da movimentação (dd/mm/yyyy), ou 0 para sair do programa: "
            )
            time.sleep(1)
            if userDate == "0": # confere o input para encerrar o programa; checks for the input to break the program
                endProgram()
            try:  # conferência no formato de dd/mm/yyyy e armazenamento nas variáveis; checking format dd/mm/yyyy and store in variables
                aimDate = datetime.datetime.strptime(userDate, "%d/%m/%Y")
                # altera variável userDate em formato de data
                # changes userDate variable into a date format
                userDate = datetime.datetime.strptime(userDate, "%d/%m/%Y")
                isValid = True
            except:  # se o input tiver formato diferente, tente novamente; if different format, try again
                print("Verifique a data e tente novamente!")
        if userOption == "3": # verifica a função de busca por período e pede pela data inicial e final; verifies the function and asks for initial and final dates
            userDate = input(
                "Digite a data inicial do período desejado (dd/mm/yyyy), ou 0 para sair do programa: "
            )
            if userDate == "0": # confere o input para encerrar o programa; checks for the input to break the program
                endProgram()
            finalDate = input(
                "Digite a data final do período desejado (dd/mm/yyyy), ou 0 para sair do programa: "
            )
            if finalDate == "0" : # confere o input para encerrar o programa; checks for the input to break the program
                endProgram()
            time.sleep(1)
            while userDate == finalDate: # evita erros por datas iguais; avoids errors by having the same date
                print ("Favor digitar datas diferentes ou utilizar uma das outras funções.")
                userDate = input(
                    "Digite a data inicial do período desejado (dd/mm/yyyy), ou 0 para sair do programa: "
                )
                if userDate == "0": # confere o input para encerrar o programa; checks for the input to break the program
                    endProgram()
                finalDate = input(
                "Digite a data final do período desejado (dd/mm/yyyy), ou 0 para sair do programa: "
                )
                if finalDate == "0" : # confere o input para encerrar o programa; checks for the input to break the program
                    endProgram()
            try:  # conferência no formato de dd/mm/yyyy e armazenamento nas variáveis; checking format dd/mm/yyyy and store in variables
                aimDate = datetime.datetime.strptime(userDate, "%d/%m/%Y")
                finalDate = datetime.datetime.strptime(finalDate, "%d/%m/%Y")
                userDate = datetime.datetime.strptime(userDate, "%d/%m/%Y")
                if finalDate < aimDate: # se data inicial for maior que a final inverte os valores; changes the values if initial date comes aftes final date
                    temp = finalDate
                    finalDate = aimDate
                    aimDate = temp
                    isValid = True
                else:
                    isValid = True
            except:  # se o input tiver formato diferente, tente novamente; if different format, try again
                print("Verifique a data e tente novamente!")
inputDate()

# função com while para chegar ao mês anterior ao inputado
# while function to get to the month before the input
def adjustDate():
    # criação da variável aim, com a data fixada no dia 15 (ano e mês irrelevantes)
    # variable aim, with date fixed in day 15 (year and month irrelevant)
    aim = datetime.date(2021, 12, 15)
    global aimDate
    global userDate
    while aimDate.strftime("%m") == userDate.strftime("%m"):
        aimDate = aimDate - day
    # loop para chegar ao último dia da primeira quinzena do mês anterior da operação
    # loop to get to the last weekday of the first 15-days (fortnight) of the month before the input
    while aimDate.strftime("%d") > aim.strftime("%d"):
        aimDate = aimDate - day
# verifica o input do usuário na variável userOption, e utiliza a função adjustDate se necessário
# verifies user input in userOption variable and uses function adjustDate, if needed.
if userOption == "2":
    adjustDate()

# função com loop para chegar em um dia útil, se necessário
# loop function to get to a weekday, if needed
def conferirData():
    global aimDate
    isValid = False
    while not isValid:
        if aimDate.strftime("%A") in weekend:
            if userOption in ("1","2"):
                aimDate = aimDate - day
            if userOption == "3":
                aimDate = aimDate + day
        else:
            isValid = True
conferirData()

# função site com todos passos após abertura do bcb
# site function with all steps after site opening
def site():
    element.clear() # apaga dados no campo; clears field data
    # input da data no campo representado pela variável element
    # date input in the field represented by the element variable
    element.send_keys(aimDate.strftime("%m/%d/%Y"))
    # encontra as checkboxes e as pressiona se não estiverem pressionadas
    # find the checkboxes and presses them, if not already pressed
    select1 = driver.find_element(By.XPATH, "//tr[1]/td[1]/input")
    if select1.is_selected() == False:
        select1.click()
    select2 = driver.find_element(By.XPATH, "//tr[2]/td[1]/input")
    if select2.is_selected() == False:
        select2.click()
    select3 = driver.find_element(By.XPATH, "//div[9]/div/div/button").click() # pressione executar; press execute
    time.sleep(2)

# loop para evitar erros. Se o programa não retornar valores, diminui ou aumenta um dia da data até encontrar resultados ou encerra o código se chegar a 7 repetições
# loop to avoid errors. If the program doesn't return values it decreases or raises day by day until finding a result or shuts down the code if it gets to 7 repetitions
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
            if userOption in ("1", "2"):
                aimDate = aimDate - day
                conferirData()
                contador += 1
            if userOption == "3":
                aimDate = aimDate + day
                conferirData()
                contador += 1
            if contador >= 7:
                print(
                    "Não foi possível encontrar uma data válida para o período especificado."
                )
                endProgram()
tryanderror()

# função de output do programa
# program output function
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

# para a busca por período, faz um loop enquanto a primeira data for menor do que a data final
# in search by time period, loops whilst first date is earlier than final date
if userOption == "3":
    while aimDate < finalDate:
        aimDate = aimDate + day
        conferirData()
        dolarCompra = "0"
        tryanderror()
        output()

# repetição para inserir mais datas
# loop to get more dates
while userDate != "0":
    inputDate()
    if userOption == "2":
        adjustDate()
    conferirData()
    dolarCompra = "0"
    tryanderror()
    output()
