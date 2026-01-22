# Proyecto ETL + Análisis Exploratorio de Datos 1.0

Este proyecto combina un proceso **ETL (Extract, Transform, Load)** implementado en Python con un **análisis exploratorio de datos (EDA)** realizado en un *Jupyter Notebook*. Su objetivo principal es cargar datos desde un archivo CSV, transformarlos y prepararlos para su análisis posterior, sacando ideas claras y fáciles de entender sobre los datos.

---

📁 Estructura del Proyecto

```
Proyecto/
│
├── data/
│   ├── datos.csv               # Datos de origen
│   └── Readme data.txt         # Documentación de los datos
├── src/
│   └── etl.py                  # Script principal del proceso ETL
│
├── notebook.ipynb              # Notebook con análisis exploratorio
│
└── README
    
```

---

## 🔧 Tecnologías Utilizadas

- Python 3.13
- Pandas
- Jupyter Notebook
- NumPy 
- Matplotlib
- Seaborn
- Os
- Requests
- Csv

---

##  Instalación

### 1 Clonar el repositorio

```
git clone https://github.com/JuanR88/proyecto_ETL.git
cd proyecto
```

### 3️⃣ Instalar dependencias

```
!pip install pandas
!pip install numpy
!pip install csv
!pip install matplotlib
!pip install requests
!pip install seaborn
```

---

##  Ejecución del Proceso ETL

Ejecuta el script principal desde cosola:

```
python src/etl.py
```

---

##  Análisis de Datos

Para abrir el notebook:

```
jupyter notebook notebook.ipynb
```

El notebook incluye analisis:

- Visualización de datos procesados
- Estadísticas descriptivas
- Gráficos y correlaciones

---

El notebook incluye preguntas :

- ¿Cuáles son los países con mayor y menor PIB per cápita (último año disponible)?
- ¿Cuáles son los países con mayor y menor esperanza de vida?
- ¿Coinciden los países más ricos con los de mayor esperanza de vida?
- ¿Cómo ha evolucionado el PIB per cápita medio mundial desde el año 2000?
- ¿Cómo se distribuye el PIB per cápita medio por regiones del mundo?
- ¿Cómo se distribuye la esperanza de vida media por regiones?
- ¿Qué países se comportan de forma atípica respecto a la relación riqueza–bienestar?
- ¿Cómo ha evolucionado conjuntamente el PIB per cápita medio y la esperanza de vida media desde el año 2000?

---

##  Datos Utilizados

La carpeta `data/` incluye:

- **datos.csv**: archivo de datos original
- **Readme data.txt**: notas sobre los datos

---


