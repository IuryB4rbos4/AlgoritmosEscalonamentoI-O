# Simulador

O simulador é o arquivo `hdd.py`, no entento você vai rodar o `simulate.py`. Basicamente, ao rodar esse arquivo o código vai simular uma série de requisições já pre estabelidas no arquivo `entradas.txt`. Nesse arquivo, cada linha é uma requisição que vamos simular com setores aleatorios. 
Após a simulação, você pode consultar os resultados no diretorio /Dados e os arquivos CSV dos resultados da FIFO e SSTF estarão disponiveis lá. Onde a primeira coluna (Entrada) é a quantidade de setores que vão ser lidos da 
requisição e a segunda coluna (Tempo) é a quantidade de tempo em milisegundos para atender essa requisição.
É possivel mudar as requisições que o código vai atender, é só modificar o arquivo `entradas.txt`, as requisições colocadas lá no formato num1, num2, num3. Exemplo: 12,58,60
Note que o intervalo de numeros que você pode usar é 0..106, colocar um setor fora desse intervalo gera erro. Caso você adicione mais requisiões, modifique o range do arquivo `simulate.py`, espeficicamente nas funções run.

# Utilização

Para executar os testes, rode com:

``` python2 simulate.py```

Para vizualizar a parte grafica, pode tirar o comentario da ultima linha onde tem start('... e executar:

``` python2 hdd.py -G```

Note que não usamos a parte grafica e a implementação não é nossa, já que o nosso simulador é uma adaptação de um outro simulador não modificamos a parte de gráficos já que não era relevante para a nossa analise.

# Requisitos

- Python 2
- Thinker
- pip
- Python-tk

Instale o Thinker atravéz de:

```pip install Thinker```

E o python-tk com:

```sudo apt install python-tk```
