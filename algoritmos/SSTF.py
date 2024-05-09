# Calcula a diferença entre a cabeça e o possível proximo setor da fila.
def calculateDifference(queue, head, diff):
    for i in range(len(diff)):
        diff[i][0] = abs(queue[i] - head)

# Encontrar o próximo com a menor diferença
def findMin(diff):
    min_diff = float('inf')
    index = -1
    for i in range(len(diff)):
        if not diff[i][1] and diff[i][0] < min_diff:
            min_diff = diff[i][0]
            index = i
    return index
     
def shortestSeekTimeFirst(requisicoes, head):          
        if (len(requisicoes) == 0): 
            return
         
        length_req = len(requisicoes)

        diff = [[0, 0] for _ in range(length_req)] 
         
        seek_sequence = [0] * (length_req + 1) 
         
        for i in range(length_req): 
            seek_sequence[i] = head 
            calculateDifference(requisicoes, head, diff) 
            index = findMin(diff) 
             
            diff[index][1] = True

            head = requisicoes[index] 
     
        seek_sequence[len(seek_sequence) - 1] = head 

        return seek_sequence

if __name__ =="__main__":
     
    # request array 
    proc = [104,80,14,44,79,75,91,29,46,85]
    print(shortestSeekTimeFirst(proc, 50))