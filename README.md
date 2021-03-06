# DolarScraper PT-BR
Código para coleta do preço de compra e venda do dólar, a partir do site oficial do Banco Central do Brasil.

Possui duas funções: 
  1. Retorna os valores do dólar (compra e venda) para a data específica recebida pelo usuário, ou o primeiro dia útil anterior a data.
  2. Retorna os valores do dólar (compra e venda) para o último dia útil da primeira quinzena do mês anterior à data informada.
  3. Retorna os valores do dólar (compra e venda) dentro de um período especificado por data inicial e data final.

Nota-se que o programa possibilita a coleta de mais de um preço, porém não é recomendado fazer uma lista muito grande, para evitar problemas não recorrentes no site que possam crashar o código e resultar na perda dos valores antes da impressão final.

Também é recomendado realizar apenas as ações no terminal, e não interagir com o webdriver aberto.

[Link para o código](dolarScraper.py)
## Pré Requisitos
É necessário instalar as seguintes bibliotecas do python para o devido funcionamento do programa, essas são:
  - **selenium**
  - **webdriver-manager**
  - **pandas**
  - talvez seja necessária a **openpyxl** também
     
Para ajuda nesse sentido, recomendo esse [link](https://computadorcomwindows.com/2018/01/19/tutorial-como-instalar-uma-biblioteca-python-no-computador/).
Se o usuário ainda não possuir o python, sugiro esse [vídeo](https://www.youtube.com/watch?v=-RuY-rM-B4M).
## Uso
Após a execução do código:
  1. Primeiramente se pede a opção do usuário, 1 para data exata e 2 para a data do mês anterior
  2. Próximo input é a data desejada pelo usuário
  3. O retorno já é apresentado no terminal, porém também é armazenado em dois dicionários, um para dólar compra e outro para dólar venda
  4. Escolha do usuário:
     - pedir mais datas
     - Digitar "0" para encerrar o programa.
  5. Após o usuário digitar "0", se apresenta os resultados em dataframes do pandas (baseado nos dicionários preenchidos), para facilitar a visualização dos resultados.

Novamente aqui se recomenda não fazer uma lista muito grande, para evitar possíveis erros no site que resultem na perda dos dados armazenados.
# DollarScraper EN-US
Code to get BRL (Brazilian Real) dollar exchange rate, from official Banco Central do Brasil (Brazilian Central Bank) site.

It has two functions:
  1. Returns dollar exchange rate to the specific date received from the user, or the first business day before it.
  2. Returns dollar exchange rate to the last business day in the first 15-days (fortnight) of the month before the specified date.
  3. Returns dollar exchange rate for a time period specified by initial and final dates.

Please note that the program allows multiple price inputs, but it is not recommended to make a big list, in order to avoid ocasional problems in the site that might crash the code and result in the loss of values before final print.

[Link for the code](dolarScraper.py)
## Precondition
It is necessary to install the following libraries for Python for proper functioning of the program, those are:
  - **selenium**
  - **wedriver-manager**
  - **pandas**
  - **and perhaps you may need openpyxl as well**

If you need help in this sense, I recommend this [link](https://packaging.python.org/en/latest/tutorials/installing-packages/).
## Use
After executing the code:
  1. First user has to input option: 1 for exact date, 2 for date from the month before or 3 for search by time period
  2. The next input is the user's date
  3. The return is already presented in the terminal, but it is also stored in two dictionaries.
  4. User choice:
     - ask for a new date
     - type "0" to end the program
  5. After the user types "0", it is printed the dataframes from pandas (based on the stored dictionaries) for easier visualization of the results.

Once again, it it recommended not to store too many dates, to avoid non-recurring errors that may result in the loss of stored data.

It is also recommended to only realize actions in the terminal, and to not interact with the webdriver.
