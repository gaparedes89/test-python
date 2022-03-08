''' from test.objeto import Objeto '''
import sys

class Objeto(object):
    def __init__(self, nombre):
       print("Constructor")
       self.hola(nombre)
 
    def hola(self, nombre):
        print(f"hola {nombre}")

if __name__ == "__main__":
   print("inicio")
   '''  print(sys.argv[0], print(sys.argv[1]), print(sys.argv[2])) '''
  
   try:
       obj1 = Objeto(sys.argv[1])
   except Exception as e:
       print(f"hubo un error: {e}, asignando valor NN")
       obj1 = Objeto("NN")
  
obj2 = Objeto("daniel")
obj3 = Objeto("sergio")


