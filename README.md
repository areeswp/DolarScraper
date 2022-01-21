# DolarScraper PT-BR
Código para coleta do preço de compra e venda do dólar, a partir do site oficial do Banco Central do Brasil.

Possui duas funções: 
  1. Retorna os valores do dólar (compra e venda) para a data específica recebida pelo usuário, ou o primeiro dia útil anterior a data.
  2. Retorna os valores do dólar (compra e venda) para o último dia útil da primeira quinzena do mês anterior à data informada.

Nota-se que o programa possibilita a coleta de mais de um preço, porém não é recomendado fazer uma lista muito grande, para evitar problemas ocasionais no site que possam crashar o código e resultar na perda dos valores antes da impressão final.

[Link para o código](dolarScraper.py)
## Pré Requisitos
É necessário instalar duas libs do python para o devido funcionamento do programa, essas são:
  1. selenium
     -(Utilizado para o funcionamento da raspagem dos dados)
  2. webdriver-manager
     -(Auxílio ao selenium)
     
Para ajuda nesse sentido, recomendo esse [link](https://computadorcomwindows.com/2018/01/19/tutorial-como-instalar-uma-biblioteca-python-no-computador/).
Se o usuário ainda não possuir o python, sugiro esse [vídeo](https://www.youtube.com/watch?v=-RuY-rM-B4M).
## Uso
Após a execução do código:
  1. Primeiramente se pede a opção do usuário, 1 para data exata e 2 para a data do mês anterior
  2. Próximo input é a data desejada pelo usuário
  3. O retorno já é apresentado no terminal, porém também é armazenado em dois dicionários, um para dólar compra e outro para dólar venda
  4. Escolha do usuário:
     -y leva o usuário a mais um input de data
     -n encerra o programa, apresentando os dicionários com os dados armazenados.

Novamente aqui se recomenda não fazer uma lista muito grande, para evitar possíveis erros no site que resultem na perda dos dados armazenados.
# DollarScraper EN-US
Code to get BRL (Brazilian Real) dollar exchange rate, from official Banco Central do Brasil (Brazilian Central Bank) site.

It has two functions:
  1. Returns dollar exchange rate to the specific date received from the user, or the first business day before it.
  2. Returns dollar exchange rate to the last business day in the first 15-days (fortnight) of the month before the specified date.

Please note that the program allows multiple price inputs, but it is not recommended to make a big list, in order to avoid ocasional problems in the site that might crash the code and result in the loss of values before final print.

[Link for the code](dolarScraper.py)
## Precondition
It is necessary to install two libraries for Python for proper functioning of the program, those are:
  1. selenium
     -(Used for web scraping)
  2. wedriver-manager
     -(Auxiliar for selenium)

If you need help in this sense, I recommend this [link](https://packaging.python.org/en/latest/tutorials/installing-packages/).
## Use
After executing the code:
  1. First user has to input option: 1 for exact date and 2 for date from the month before
  2. The next input is the user's date
  3. The return is already presented in the terminal, but it is also stored in two dictionaries.
  4. User choice:
     -y takes the user to a new date input
     -n kills the program and prints the dictionaries with their stored data.

Once again, it it recommended not to store too many dates, to avoid possible errors that result in the loss of stored data.
