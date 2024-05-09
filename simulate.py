import random
import hdd
class Requisicoes:

    def __init__(self):
        self.cont = 1
        self.requisicoes = 100
    
    def lerPorLinhas(self, linha):
        with open('entradas.txt', 'r') as file:
            lines = file.readlines()
            return lines[linha]            

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

#hdd.d.Go()

req = Requisicoes()
hdd.start(req.lerPorLinhas(4))
