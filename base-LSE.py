# ===========================================
# By: Nury Farelo - Estructuras Datos
#And Luis Felipe Rueda García 2240021
# Name: Lista Simplemente Enlazada 
# ===========================================

# Clase Nodo
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def __del__(self):
		print("Destructor called", self.data)
		return True

# CLase Listas enlazada simple
class SimpleLinkdList:
	def __init__(self):
		self.head = None
  
  	# Lista Vacia Return String
	def isEmptyString(self):
		if self.isEmpty():
			print("Está vacia")
		else:
			print("Lista no vacia")

	#Lista Vacia Return Boolean

	def isEmpty(self):
		if self.head == None:
			return True
		else:
			return False

	# Agregar al inicio
	def insertHead(self, data):
		newNode = Node(data)
		if self.head is None:
			self.head = newNode
			return
		else:
			newNode.next = self.head
			self.head = newNode
	
	#Insertar Al final
	def insertAtEnd(self, data):
		temporalNode = None
		escape = False
		if self.isEmpty():
			self.insertHead(data)
		else:
			temporalNode=self.head
			while escape !=True:
				if temporalNode.next!=None:
					temporalNode = temporalNode.next
				else:
					newNode = Node(data)
					temporalNode.next=newNode
					escape = True

	#Insertar antes de un elemento X
	def insertBefore(self,data,x):
		#if (self.isValueOnList(x)):
		currentTemporalNode = None
		pastTemporalNode = None
		escape = False
		if self.isEmpty():
			return False
		else:

			if self.head.data == x:
				self.insertHead(data)
				return True
			else:
				currentTemporalNode=self.head

				while escape !=True:

					if currentTemporalNode.data == x:
						
						newNode = Node(data)
						newNode.next=currentTemporalNode
						pastTemporalNode.next=newNode
						return True
					else:
						if currentTemporalNode.next!=None:
							pastTemporalNode=currentTemporalNode
							currentTemporalNode = currentTemporalNode.next
						else:
							escape = True
		return False

	
	#Insertar después de un elemento X
	def insertAfter(self,data,x):
		#if (self.isValueOnList(x)):
		temporalNode = None
		escape = False
		if self.isEmpty():
			return False
		else:
			temporalNode=self.head
			while escape !=True:

				if temporalNode.data == x:
					newNode = Node(data)
					newNode.next=temporalNode.next
					temporalNode.next=newNode
					return True
				else:
					if temporalNode.next!=None:
						temporalNode = temporalNode.next
					else:
						escape = True
		return False

	#Eliminiar primero
	def deleteFirst(self):
		if self.isEmpty():
			return False
		else:
			if self.head.next==None:
				self.head==None

			else:
				self.head=self.head.next

			return True


	#Eliminar último
	def deleteLast(self):
		if self.isEmpty():
			return False
		else:
			if self.head.next==None:
				self.head==None

			else:
				escape=False
				currentTemporalNode=self.head
				pastTemporalNode=None
				while escape !=True:
					if currentTemporalNode.next!=None:
						pastTemporalNode=currentTemporalNode
						currentTemporalNode = currentTemporalNode.next
					else:
						pastTemporalNode.next=None
						escape = True

			return True

	#Buscar un elememto por su valor (devuelve True or False)
	def isValueOnList(self,x):
		temporalNode = None
		escape = False
		if self.isEmpty():
			return False
		else:
			temporalNode=self.head
			while escape !=True:

				if temporalNode.data == x:
					return True
				else:
					if temporalNode.next!=None:
						temporalNode = temporalNode.next
					else:
						escape = True

		return False
	
	#Buscar un elememto por su valor (devuelve la posicion)
	def findValuePosition(self,x):
		temporalNode = None
		escape = False
		if self.isEmpty():
			return -1
		else:
			temporalNode=self.head
			i=0
			while escape !=True:

				if temporalNode.data == x:
					return i
				else:
					i+=1
					if temporalNode.next!=None:
						temporalNode = temporalNode.next
					else:
						escape = True

		return -1

	#Contar cuántos elementos tiene la lista
	def length(self):
		count = 0
		temporalNode = None
		escape = False
		if self.isEmpty():
			return count
		else:
			temporalNode=self.head
			while escape !=True:
				if temporalNode.next!=None:
					count+=1
					temporalNode = temporalNode.next
				else:
					escape = True
					
		return count
	
	#print content
	def printContent(self):
		temporalNode = None
		escape = False
		if self.isEmpty():
			return False
		else:
			temporalNode=self.head
			print(temporalNode.data)
			while escape !=True:
				if temporalNode.next!=None:
					temporalNode = temporalNode.next
					print(temporalNode.data)
				else:
					escape = True

mylist = SimpleLinkdList()
print("esta vacia la lista?",mylist.isEmpty())
for i in range (1,12):
	mylist.insertAtEnd(i*3)
print("esta vacia la lista?",mylist.isEmpty())
print("la cabeza  contiene el Nodo con el dato",mylist.head.data)
print("la lista tiene",mylist.length())
print("esta 15 en la lista : ",mylist.isValueOnList(15))
print("esta 11 en la lista : ",mylist.isValueOnList(11))
print("el valor 15 en la lista en la posición: ",mylist.findValuePosition(15))

mylist.printContent()
mylist.insertAfter(77,15)
mylist.printContent()
mylist.insertBefore(44,6)
mylist.printContent()
mylist.deleteFirst()
mylist.printContent()
mylist.deleteLast()
mylist.printContent()
mylist.deleteFirst()
mylist.printContent()
mylist.deleteLast()
mylist.printContent()