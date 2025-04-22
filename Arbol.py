class Node:
    def __init__(self,data):
        self.data = data
        self.sons = []
        
    def addSon(self,SNode):
        self.sons.append(SNode)
        
class Arbol:
    def __init__(self,root):
        self.root = root
    
    def ImprimirNivel(self, nodo, nivel=0):
        print(' '*6*nivel+str(nodo.data))
        for son in nodo.sons:
                self.ImprimirNivel(son,nivel+1)
                
    def Imprimir(self):
        self.ImprimirNivel(self.root)
        
    def Contador(self,nodo):
        contador = 1
        if not nodo.sons:
            return contador
        else:
            for son in nodo.sons:
                contador += self.Contador(son)
            return contador
    
    def peso(self):
        return self.Contador(self.root)
    
    def CalcularAltura(self,nodo):
        if not nodo.sons:
            return 0
        else:
            return 1 + max(self.CalcularAltura(h) for h in nodo.sons)
        
    def Altura(self):
       return self.CalcularAltura(self.root)
    
    def calcularOrden(self,nodo):
        orden = len(nodo.sons)
        for son in nodo.sons:
            orden = max(orden,self.calcularOrden(son))
        return orden
    
    def orden(self):
        return self.calcularOrden(self.root)
    
    def find(self, data, nodo=None):
        if nodo is None:
            nodo = self.root
        if nodo.data == data:
            return nodo
        for hijo in nodo.sons:
            res = self.find(data, hijo)
            if res:
                return res
        return None

    def insert(self, parent_data, new_data):
        padre = self.find(parent_data)
        if not padre:
            print(f"Nodo '{parent_data}' no encontrado.")
            return False
        nuevo = Node(new_data)
        padre.addSon(nuevo)
        return True
        

root = Node("A")
node_b = Node("B")
node_c = Node("C")
node_d = Node("D")
node_e = Node("E")
node_f = Node("f")
node_g = Node("G")
node_h = Node("H")

root.addSon(node_b)
root.addSon(node_c)
root.addSon(node_d)
node_b.addSon(node_e)
node_b.addSon(node_f)
node_c.addSon(node_g)
node_e.addSon(node_h)

arbol = Arbol(root)
arbol.Imprimir()
print("peso:",arbol.peso())
print("Altura:",arbol.Altura())
print("Orden:",arbol.orden())