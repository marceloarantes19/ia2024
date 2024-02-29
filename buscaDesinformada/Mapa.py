from Grafo import Grafo 
class Mapa(Grafo):
  def geraMapa(self):
    self.insereVerticeNome("Arad")
    self.insereVerticeNome("Bucharest")
    self.insereVerticeNome("Craiova")
    self.insereVerticeNome("Dobreta")
    self.insereVerticeNome("Eforie")
    self.insereVerticeNome("Fagaras")
    self.insereVerticeNome("Giurgiu")
    self.insereVerticeNome("Hirsova")
    self.insereVerticeNome("Iasi")
    self.insereVerticeNome("Lugoj")
    self.insereVerticeNome("Mehadia")
    self.insereVerticeNome("Neamt")
    self.insereVerticeNome("Oradea")
    self.insereVerticeNome("Pitesti")
    self.insereVerticeNome("Rimnicu Vilcea")
    self.insereVerticeNome("Sibiu")
    self.insereVerticeNome("Timisoara")
    self.insereVerticeNome("Vaslui")
    self.insereVerticeNome("Urziceni")
    self.insereVerticeNome("Zerind")

    self.insereArestaNome("Arad", "Sibiu")
    self.insereArestaNome("Arad", "Timisoara")
    self.insereArestaNome("Arad", "Zerind")

    self.insereArestaNome("Bucharest", "Fagaras")
    self.insereArestaNome("Bucharest", "Giurgiu")
    self.insereArestaNome("Bucharest", "Pitesti")
    self.insereArestaNome("Bucharest", "Urziceni")

    self.insereArestaNome("Craiova", "Dobreta")
    self.insereArestaNome("Craiova", "Pitesti")
    self.insereArestaNome("Craiova", "Rimnicu Vilcea")

    self.insereArestaNome("Dobreta", "Mehadia")
    self.insereArestaNome("Eforie", "Hirsova")
    self.insereArestaNome("Fagaras", "Sibiu")
    self.insereArestaNome("Hirsova", "Urziceni")
    self.insereArestaNome("Iasi", "Neamt")
    self.insereArestaNome("Iasi", "Vaslui")
    self.insereArestaNome("Lugoj", "Mehadia")
    self.insereArestaNome("Lugoj", "Timisoara")
    self.insereArestaNome("Oradea", "Sibiu")    
    self.insereArestaNome("Oradea", "Zerind")
    self.insereArestaNome("Pitesti", "Rimnicu Vilcea")
    self.insereArestaNome("Rimnicu Vilcea", "Sibiu")
    self.insereArestaNome("Vaslui", "Urziceni")





