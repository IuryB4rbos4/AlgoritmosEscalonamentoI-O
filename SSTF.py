import random
import matplotlib.pyplot as plt

def sstf(current_position, requests):
    total_seek_time = 0
    current_track = current_position
    sorted_requests = sorted(requests, key=lambda x: abs(x - current_track))
    track_sequence = [current_position]
    
    while sorted_requests:
        next_request = sorted_requests.pop(0)
        total_seek_time += abs(next_request - current_track)
        current_track = next_request
        track_sequence.append(current_track)
    
    return total_seek_time, track_sequence

def fifo(current_position, requests):
    total_seek_time = 0
    current_track = current_position
    track_sequence = [current_position]
    
    for request in requests:
        total_seek_time += abs(request - current_track)
        current_track = request
        track_sequence.append(current_track)
    
    return total_seek_time, track_sequence

def sptf(current_position, requests):
    total_seek_time = 0
    current_track = current_position
    sorted_requests = sorted(requests)
    track_sequence = [current_position]
    
    while sorted_requests:
        next_request = sorted_requests.pop(0)
        total_seek_time += abs(next_request - current_track)
        current_track = next_request
        track_sequence.append(current_track)
    
    return total_seek_time, track_sequence

# Gerar solicitações de E/S aleatórias
# requests = [random.randint(0, 199) for _ in range(20)]
requests = [10, 11, 10, 12, 15, 13, 9, 7, 6, 14, 21, 20, 13, 22, 24, 23, 29, 52, 35, 32, 31, 18, 17, 19, 9, 8, 7, 6, 8, 4, 3, 5, 1]
# Posição inicial do cabeçote de leitura/gravação
#current_position = random.randint(0, 199)
current_position = 30

# Simulação SSTF
sstf_seek_time, sstf_track_sequence = sstf(current_position, requests)

# Simulação FIFO
fifo_seek_time, fifo_track_sequence = fifo(current_position, requests)

# Simulação SPTF
sptf_seek_time, sptf_track_sequence = sptf(current_position, requests)
print(requests)
# Plotagem do gráfico
plt.figure(figsize=(10, 6))
plt.plot(sstf_track_sequence, label='SSTF', marker='o')
plt.plot(fifo_track_sequence, label='FIFO', marker='x')
plt.plot(sptf_track_sequence, label='SPTF', marker='s')
plt.title('Simulação de Movimentação do Cabeçote de Leitura/Gravação')
plt.xlabel('Tempo de Serviço')
plt.ylabel('Posição do Cabeçote')
plt.xticks(range(len(requests) + 1), range(len(requests) + 1))
plt.legend()
plt.grid(True)
plt.show()

print("Tempo total de busca - SSTF:", sstf_seek_time)
print("Tempo total de busca - FIFO:", fifo_seek_time)
print("Tempo total de busca - SPTF:", sptf_seek_time)