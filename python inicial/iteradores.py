
class Iterador:

    def __init__(self,datos):
        self.datos = datos
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.datos):
            raise StopIteration
        element = self.datos[self.index]
        self.index += 2
        return element


it = Iterador([])
for i in it:
    print(i)
it = Iterador([1])
for i in it:
    print(i)
it = Iterador([2,3])
for i in it:
    print(i)
it = Iterador([2,3, 4,5,6])
for i in it:
    print(i)
