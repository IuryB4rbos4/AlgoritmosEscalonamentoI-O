import random
import hdd
import csv
import time
#from Algoritmos import SSTF
import SSTF

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
        self.data.append(['Entrada', 'Tempo'])

    def armazenaDados(self,entrada, lista):
        novaLista = []
        novaLista.append(entrada)
        novaLista.append(lista)
        self.data.append(novaLista)

    def gravar(self, algorithm):
        end = 'Dados/'+algorithm+'.csv'
        with open(end, mode='w') as file:
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
        self.data.gravar('FIFO')
        fim = time.time()
        print(fim)

    def runSSTF(self):
        for i in range(0,99):
            lista = list(map(int, self.env.lerPorLinhas(i).split(',')))
            self.data.armazenaDados(self.env.lengthReq(self.env.lerPorLinhas(i)), hdd.start(SSTF.run(18, lista)))
        self.data.gravar('SSTF')
        #for i in range(0,99):
            
           # self.data.armazenaDados(self.env.lengthReq(self.env.lerPorLinhas(i)), hdd.start(self.env.lerPorLinhas(i)))





req = Requisicoes()
analize1 = ArmazenaDados()
analize2 = ArmazenaDados()

run1 = Analize(req, analize1)
run2 = Analize(req, analize2)
run1.runFIFO()
run2.runSSTF()


