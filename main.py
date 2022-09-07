import math

class GRAFO():
    def __init__(self):
        self.grafo = {}

    def adiciona_vertice(self, nome_vertice):
        if nome_vertice in self.grafo:
            print(f"Vertice {nome_vertice} ja existe")
        else:
            self.grafo[nome_vertice] = []

    def adiciona_aresta(self, vertice1, vertice2, peso):
        if self.tem_aresta(vertice1, vertice2):
            print(f"Aresta entre {vertice1} -> {vertice2} ja existe")
        else:
            self.grafo[vertice1].append([vertice2, peso])

    def remove_aresta(self, vertice1, vertice2):
        nova_lista = []
        if self.tem_aresta(vertice1, vertice2):
            for i in self.grafo[vertice1]:
                if i[0] != vertice2:
                    nova_lista.append(i)
            self.grafo[vertice1] = nova_lista
        else:
            print(f"Aresta entre {vertice1} -> {vertice2} não existe")


    def remove_vertice(self, vertice):
        if vertice not in self.grafo:
            print(f"Vertice {vertice} não existe")
        else:
            del self.grafo[vertice]

    def tem_aresta(self, vertice1, vertice2):
        if vertice1 not in self.grafo or vertice1 not in self.grafo:
            return False
        for i in self.grafo[vertice1]:
            if i[0] == vertice2:
                return True
        return False

    def peso(self, vertice1, vertice2):
        if self.tem_aresta(vertice1, vertice2):
            for i in self.grafo[vertice1]:
                if i[0] == vertice2:
                    return i[1]
        return f"Aresta entre {vertice1} -> {vertice2} não existe"

    def grau(self, vertice):
        if vertice in self.grafo:
            return len(self.grafo[vertice])
        return f"Vertice {vertice} não existe"

    def imprime_lista_adjacencias(self):
        aresta = ""
        for key, value in self.grafo.items():
            for i in value:
                aresta += str(i) + " ->"
            print(f"{key} : {aresta}")
            aresta = ""

    def Dijkstra(self, start, end):
        dic_ = {key: math.inf for key in self.grafo if key != start}
        past_distance = 0
        dic_[start] = past_distance
        visited = [start]
        acc = 0
        while end not in visited:
            for key, value in self.grafo[visited[acc]]:
                if key in visited:
                    continue

                new_distance = value + dic_[visited[acc]]

                if dic_[key] > new_distance:
                    dic_[key] = new_distance

                visited.append(key)
            acc += 1
        return dic_[end]



def main():
    grafo1 = GRAFO()
    grafo1.adiciona_vertice("A")
    grafo1.adiciona_vertice("B")
    grafo1.adiciona_vertice("C")
    grafo1.adiciona_vertice("D")
    grafo1.adiciona_vertice("E")
    grafo1.adiciona_vertice("F")
    grafo1.adiciona_aresta("A", "B", 5)
    grafo1.adiciona_aresta("B", "C", 2)
    grafo1.adiciona_aresta("C", "A", 8)
    grafo1.adiciona_aresta("C", "D", 10)
    grafo1.adiciona_aresta("C", "E", 1)
    grafo1.adiciona_aresta("D", "E", 5)
    grafo1.adiciona_aresta("D", "A", 7)
    grafo1.adiciona_aresta("E", "B", 3)
    grafo1.adiciona_aresta("E", "A", 5)
    grafo1.adiciona_aresta("B", "D", 2)
    grafo1.adiciona_aresta("D", "F", 3)
    grafo1.imprime_lista_adjacencias()
    print(grafo1.Dijkstra("A","C"))




if __name__ == "__main__":
    main()
