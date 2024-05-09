import random
import hdd
import csv
import time

class Requisicoes:

    def __init__(self):
        self.cont = 1
        self.requisicoes = 100
    
    def lerPorLinhas(self, linha):
        with open('entradas.txt', 'r') as file:
            lines = file.readlines()
            return lines[linha]            

    def lengthReq(self, requisicao):
        lista = requisicao.split(',')
        return len(lista)

    def gravarRequisicoes(self):
        while (self.cont<self.requisicoes):
            with open('entradas.txt', 'a') as file:
                file.write(self.gerarRequisicoes(self.cont) + "\n")

            self.cont += 1

    def gerarRequisicoes(self, mult):
        result = ''
        for i in range(0,(10*mult)):
            if(i != (10*mult-1)): 
                result +=  str(random.randint(0,106)) + "," 
            else:
                result += str(random.randint(0,106))
        
        return result

class ArmazenaDados:
    
    def __init__(self):
        self.data = [[]]

    def armazenaDados(self,entrada, lista):
        novaLista = []
        novaLista.append(entrada)
        novaLista.append(lista)
        self.data.append(novaLista)

    def gravar(self):
        with open('Dados/FIFO.csv', mode='w') as file:
            write = csv.writer(file)
            write.writerows(self.data)

class Analize:

    def __init__(self,env, data):
        self.env = env
        self.data = data

    def runFIFO(self):
        inicio = time.time()
        for i in range(0,99):
            self.data.armazenaDados(self.env.lengthReq(self.env.lerPorLinhas(i)), hdd.start(self.env.lerPorLinhas(i)))
        self.data.gravar()
        fim = time.time()
        print(fim)




req = Requisicoes()
analize = ArmazenaDados()

run = Analize(req, analize)
run.runFIFO()


