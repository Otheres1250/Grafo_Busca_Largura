from classes.grafo import Grafo
from classes.leitor_arquivo import LeitorArquivo
from classes.vertice import Vertice

if __name__ == '__main__':
    leitor: LeitorArquivo = LeitorArquivo()
    grafo: Grafo = leitor.ler_arquivo_entrada()
    grafo.criar_matriz_adjacencias()
    vertices: list[Vertice] = grafo.buscar_vertices_adjacentes('b', printar=True)
