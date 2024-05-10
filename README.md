
# Utilização

Para executar os testes, rode com:

- python2 simulate.py

Ao fazer isso, ele vai pegar cada linha do arquivo entradas.txt e realizar a analize e plotar nos arquivos CSV no diretorio de Dados. Para modificar os testes, você pode mudar o aquivo simulate.py. 
Mude as requisiçõs do arquivo entradas.txt e coloque o range adequado em nas funções runFIFO e runSSTF, assim você pode gerar novos casos de testes e analizar outros tempos, note que você pode usar o função gerarRequisições para gerar requisições aleatórias.

Para vizualizar a parte grafica, pode tirar o comentario da ultima linha onde tem start('... e executar:

- python2 hdd.py -G

Note que não usamos a parte grafica e a implementação não é nossa, então acredito que não vai ser necessario.

# Requisitos

- Python 2
- Thinker
- pip

  Instale o Thinker atravéz de:

  pip install Thinker
