# - 8 Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três instâncias de Carro e Moto
# com diferentes marcas, modelos, quantidade de portas e tipos.
# - 9 Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.
from Exercicios2.Classes.Carro import Carro
from Exercicios2.Classes.moto import Moto

carro1 = Carro("HB20", "Hyundai", 4)
carro2 = Carro("Civic", "Honda", 4)
carro3 = Carro("Onix", "Chevrolet", 4)

moto1 = Moto("Yamaha", "MT-07", "esportiva")
moto2 = Moto("Honda", "Biz", "casual")
moto3 = Moto("Kawasaki", "Ninja 400", "esportiva")

print(moto1)
print(moto2)
print(moto3)
print(carro1)
print(carro2)
print(carro3)
