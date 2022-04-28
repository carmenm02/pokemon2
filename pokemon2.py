import pandas as pd

df = pd.read_csv("Pokemon.csv",",")
num_pokemon = len(df)

print("Total de pokemon:" + str(num_pokemon))

#voy a crear una función para calcular la media

def Media(caracteristica):
  n = caracteristica.count()
  Suma = 0
  mediaritmetica = 0

  if n > 0:
    for valor in caracteristica:
      Suma = Suma + valor
      mediaritmetica = Suma/n
  return Media

#creo otra para la mediana

def Mediana(caracteristica):
  mediana = 0
  caracteristica = caracteristica.sort_values()
  caracteristica = caracteristica.reset_index(drop = True)
  n = self.caracteristica.count()
  par = False;
  if (n%2 == 0):
    print("El numero de observaciones es par")
    par = True
    if par:
      rango = (n/2);
      rangoPython = rango - 1
      valor1 = caracteristica[rangoPython]
      valor2 = caracteristica[rangoPython + 1]
      mediana = valor1 + ((valor2-valor1)/2)
    else:
      rango = ((n + 1)/2)
      rangoPython = rango - 1
      mediana = caracteristica [rangoPython]
    return Mediana

#hago lo mismo con la moda

def Moda(caracteristica):
  moda = Counter(caracteristica)
  return moda