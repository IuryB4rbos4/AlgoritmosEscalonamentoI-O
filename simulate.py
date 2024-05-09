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

class Simalate():
    req = Requisicoes()

    for i in range(5):
        d = Disk(addr='1,5,60,5', addrDesc=options.addrDesc, lateAddr=options.lateAddr, lateAddrDesc=options.lateAddrDesc,
        policy=options.policy, seekSpeed=float(options.seekSpeed), rotateSpeed=float(options.rotateSpeed),
        skew=options.skew, window=options.window, compute=True, graphics=options.graphics, zoning=options.zoning)

    

class Main():
    r = Requisicoes()
    print(r.lerPorLinhas(0))
    #r.gravarRequisicoes()

if __name__ == "__main__":
    main = Main()  # Crie uma instância da classe Main