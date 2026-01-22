import requests
import pandas as pd
import csv
import os

DATA_PATH = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "data", "datos.csv")
)
os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)

if not os.path.exists(DATA_PATH):
    # 1. Obtener lista de países y territorios del Banco Mundial
    resp = requests.get("https://api.worldbank.org/v2/country", params={"format": "json", "per_page": 400})
    data = resp.json()
    paises = data[1]
    
    # Crear tabla con datos básicos de cada país (DataFrame)
    df_countries = pd.DataFrame([
        {
            "name": p["name"],
            "iso3Code": p["id"],
            "region": p["region"]["value"],
            "adminregion": p["adminregion"]["value"]
        }
        for p in paises
    ])
    
    # Filtro para quitar agregados ( adminregion = "" )
    df_countries = df_countries[df_countries["region"] != "Aggregates"].reset_index(drop=True)
    
    # Usamos función para encapsular toda la lógica de descarga,
    # pero ahora descargamos TODOS los países a la vez para cada indicador
    # (muchísimo más rápido que hacerlo país por país)
    def logica_descarga(indicator_code, start_year=1980, end_year=2023):
    
        # URL para sacar TODA la serie del indicador para TODOS los países
        url = f"https://api.worldbank.org/v2/country/all/indicator/{indicator_code}"
    
        # Pedimos todo en una sola página (per_page alto)
        params = {
            "format": "json",
            "per_page": 20000,
            "date": f"{start_year}:{end_year}"
        }
    
        # Hacemos la petición a la API
        resp = requests.get(url, params=params)
    
        # Respuesta en JSON
        data = resp.json()
    
        # Convertimos la lista a diccionario (iso3, año) -> valor
        # para acceder muy rápido después
        series = {}
        for entry in data[1]:
            iso3 = entry["countryiso3code"]
            year = entry["date"]
            value = entry["value"]
            series[(iso3, year)] = value
    
        return series
    
    # Los códigos que necesitamos
    esperanza_vida = "SP.DYN.LE00.IN"
    pib = "NY.GDP.PCAP.CD"
    
    print("Descargando series de todos los países...")
    
    # >>> Aquí hacemos solo DOS peticiones: una por indicador
    esperanza_series = logica_descarga(esperanza_vida)
    pib_series = logica_descarga(pib)
    
    print("Descarga completada.")
    
    # Creamos el CSV donde guardaremos la tabla completa
    with open(DATA_PATH, "w",) as f:
        writer = csv.writer(f)
        writer.writerow(["country", "iso3", "region", "year", "life_expectancy", "gdp_per_capita"])
    
        # Recorremos cada país de nuestro DataFrame original
        for i, row in df_countries.iterrows():
            iso3 = row["iso3Code"]
            name = row["name"]
            region = row["region"]
    
            print(f"Escribiendo datos de {name}")
    
            # Recorremos cada año y hacemos una fila por año
            for year in range(1980, 2023 + 1):
                y = str(year)
    
                # Obtenemos los valores ya guardados en los diccionarios
                life = esperanza_series.get((iso3, y))
                gdp = pib_series.get((iso3, y))
    
                writer.writerow([name, iso3, region, y, life, gdp])

else:
    print("EL ARCHIVO YA ESTA DESCARGADO")
