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

