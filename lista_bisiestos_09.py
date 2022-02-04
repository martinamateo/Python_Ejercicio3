

#lista con años bisiestos

bisiestos=[a for a in range(1583,2051) if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)]


bisiestos_final_decada=[a for a in bisiestos if (a % 10==0)]


print("Años bisiestos desde 1583 hasta 2050: ",bisiestos)
print("Años bisiestos desde 1583 a 2050 que son fin de decada:", bisiestos_final_decada)
print("Los primeros 10 numero de la lista anterior son: ",bisiestos_final_decada[:10])