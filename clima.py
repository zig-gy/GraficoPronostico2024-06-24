"""_summary_
    Descargar datos de sobre el pronostico climatico y crear un grafico con estos.
    Se imprimen los datos por consola y se muestra un popup con el grafico.
    
    2024-06-24
    Benjamin Chadwick
"""

import pandas
import matplotlib.pyplot as plt
import requests

# Conseguir informacion de la API
url = "http://api.meteored.cl/index.php?api_lang=cl&localidad=18578&affiliate_id=59lbfhamrp71&v=3.0"
clima_raw = requests.get(url).json()
clima_dataframe = pandas.DataFrame.from_dict(clima_raw)
print(clima_dataframe)

# Procesa los dias y selecciona solo los datos que se necesitan
dias = []
for dia in clima_dataframe["day"]:
    # Consigue la fecha, lo convierte en una lista y agrega "-" en
    # los lugares necesarios para hacerla leible Y vuelve a concatenarla en una string
    date = list(dia["date"])
    date[6:6] = "-"
    date[4:4] = "-"
    date = "".join(date)
    
    nombre = dia["name"]
    temperatura_minima = int(dia["tempmin"])
    temperatura_maxima = int(dia["tempmax"])
       
    informacion = [date, nombre, temperatura_minima, temperatura_maxima]
    dias.append(informacion)
       
# Los datos se aplican a un dataframe para utlizarlos mejor 
df_temperaturas = pandas.DataFrame(
    data = dias,
    columns = ["Fecha","Dia","Temperatura minima","Temperatura maxima"],
)
print(df_temperaturas)

# Graficando con el DataFrame
# Especificar ancho de las barras
ancho = 0.65

# La barra de la temperatura minima
plt.bar(
    df_temperaturas["Dia"],
    df_temperaturas["Temperatura minima"],
    width=ancho,
    label='Temp. Mínima',
    color="RoyalBlue"
)

# La barra de la temperatura maxima, pero restada con la minima y puesta encima
plt.bar(
    df_temperaturas["Dia"],
    df_temperaturas["Temperatura maxima"] - df_temperaturas["Temperatura minima"],
    width=ancho,
    bottom=df_temperaturas["Temperatura minima"],
    label='Temp. Máxima',
    color='Crimson'
)

# Agregar labels y titulos
plt.xlabel('Día')
plt.ylabel('Temperatura (C°)')
plt.title(f'Comparacion temperaturas proyectadas semana de {df_temperaturas["Fecha"][0]}')
plt.legend()

# Mostrar el plot
plt.show()