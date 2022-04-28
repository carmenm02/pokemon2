import pandas as pd
from math import *
import matplotlib.pyplot as plt

df = pd.read_csv("Pokemon.csv",",")
num_pokemon = len(df)

print("Total de pokemon:" + str(num_pokemon))

class Estadisticas:
  def __init__(self,caracteristica):
    self.caracteristica = caracteristica
#voy a crear una función para calcular la media

  def Media(self):
    n = self.caracteristica.count()
    Suma = 0
    mediaritmetica = 0

    if n > 0:
      for valor in self.caracteristica:
        Suma = Suma + valor
        mediaritmetica = Suma/n
    return Media

#creo otra para la mediana

  def Mediana(self):
    mediana = 0
    caracteristica = self.caracteristica.sort_values()
    caracteristica = self.caracteristica.reset_index(drop = True)
    n = self.caracteristica.count()
    par = False;
    if (n%2 == 0):
      print("El numero de observaciones es par")
      par = True
      if par:
        rango = (n/2);
        rangoPython = rango - 1
        valor1 = self.caracteristica[rangoPython]
        valor2 = self.caracteristica[rangoPython + 1]
        mediana = valor1 + ((valor2-valor1)/2)
      else:
        rango = ((n + 1)/2)
        rangoPython = rango - 1
        mediana = self.caracteristica [rangoPython]
      return Mediana

#hago lo mismo con la moda

  def Moda(self):
    moda = Counter(self.caracteristica)
    return moda

#repito con la desviacion tipica y la varianza

  def Varianza(self):
    n = self.caracteristica.count()
    Media = self.caracteristica.mean()
    varianza = 0
    c3 = 0
    for valor in self.caracteristica:
      x = valor
      moy = Media
      c1 = valor - Media
      c2 = c1 * c1
      c3 = c3 + c2
    varianza = c3 / (n-1)
    desviaciontipica = sqrt(varianza)
    return ([varianza,desviaciontipica])