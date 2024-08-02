import sys
import time
from collections import deque

# Função para ler o labirinto de um arquivo.


def ler_labirinto(filename):
    labirinto = []
    with open(filename, 'r') as f:
        for line in f:
            labirinto.append(list(line.strip()))
    return labirinto

# Função para imprimir o labirinto em um arquivo .txt.


def imprimir_labirinto_com_caminho(labirinto, caminho, nome_arquivo):
    with open(nome_arquivo, 'w') as f:
        for i in range(len(labirinto)):
            for j in range(len(labirinto[0])):
                if (i, j) in caminho:
                    f.write('* ')
                else:
                    f.write(labirinto[i][j] + ' ')
            f.write('\n')

# Implementação da busca em largura (BFS).


def bfs(labirinto, inicio, fim):
    fila = deque([inicio])
    visitados = set()
    mapa_pai = {}
    encontrado = False

    while fila:
        atual = fila.popleft()
        if atual == fim:
            encontrado = True
            break
        x, y = atual
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(labirinto) and 0 <= ny < len(labirinto[0]) and (nx, ny) not in visitados and labirinto[nx][ny] != '#':
                fila.append((nx, ny))
                visitados.add((nx, ny))
                mapa_pai[(nx, ny)] = (x, y)

    if encontrado:
        caminho = []
        atual = fim
        while atual != inicio:
            caminho.append(atual)
            atual = mapa_pai[atual]
        caminho.append(inicio)
        caminho.reverse()
        return caminho
    else:
        return None

# Implementação da busca em profundidade (DFS).


def dfs(labirinto, inicio, fim):
    stack = [inicio]
    visitados = set()
    mapa_pai = {}
    encontrado = False

    while stack:
        atual = stack.pop()
        if atual == fim:
            encontrado = True
            break
        x, y = atual
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(labirinto) and 0 <= ny < len(labirinto[0]) and (nx, ny) not in visitados and labirinto[nx][ny] != '#':
                stack.append((nx, ny))
                visitados.add((nx, ny))
                mapa_pai[(nx, ny)] = (x, y)

    if encontrado:
        caminho = []
        atual = fim
        while atual != inicio:
            caminho.append(atual)
            atual = mapa_pai[atual]
        caminho.append(inicio)
        caminho.reverse()
        return caminho
    else:
        return None

# Função principal


def main():
    while True:
        filename = input("Informe o arquivo (0 para sair): ")
        print()
        if filename == '0':
            break

        try:
            labirinto = ler_labirinto(filename)
            inicio = None
            fim = None
            for i in range(len(labirinto)):
                for j in range(len(labirinto[0])):
                    if labirinto[i][j] == 'S':
                        inicio = (i, j)
                    elif labirinto[i][j] == 'E':
                        fim = (i, j)
            if not inicio or not fim:
                print("Labirinto mal formado: Falta ponto de inicio ou fim.")
                continue

            print("Processando...")
            print()

            # Executando BFS
            tempo_inicio = time.time()
            caminho_bfs = bfs(labirinto, inicio, fim)
            tempo_fim = time.time()
            tempo_bfs = tempo_fim - tempo_inicio

            # Executando DFS
            tempo_inicio = time.time()
            caminho_dfs = dfs(labirinto, inicio, fim)
            tempo_fim = time.time()
            tempo_dfs = tempo_fim - tempo_inicio

            if caminho_bfs is None:
                print("Não foi encontrado um caminho usando BFS.")
            else:
                print("Caminho encontrado usando BFS:")
                for node in caminho_bfs:
                    print(node, end=' ')
                print()
                print()
                print(f"Tempo (BFS): {tempo_bfs:.3f} s")
                print()

                # Salvando labirinto com caminho encontrado em um arquivo
                nome_saida_bfs = filename.replace('.txt', '_blocks_bfs.txt')
                print(f"Salvando labirinto em {
                      nome_saida_bfs} usando BFS...")
                imprimir_labirinto_com_caminho(
                    labirinto, caminho_bfs, nome_saida_bfs)
                print()

            if caminho_dfs is None:
                print("Não foi encontrado um caminho usando DFS.")
            else:
                print("Caminho encontrado usando DFS:")
                for node in caminho_dfs:
                    print(node, end=' ')
                print()
                print()
                print(f"Tempo (DFS): {tempo_dfs:.3f} s")
                print()

                # Salvando labirinto com caminho encontrado em um arquivo
                nome_saida_dfs = filename.replace('.txt', '_blocks_dfs.txt')
                print(f"Salvando labirinto em {
                      nome_saida_dfs} usando DFS...")
                imprimir_labirinto_com_caminho(
                    labirinto, caminho_dfs, nome_saida_dfs)
                print()

        except FileNotFoundError:
            print(
                "Arquivo não encontrado. Por favor, verifique o nome e o caminho do arquivo.")
            print()


if __name__ == "__main__":
    main()
