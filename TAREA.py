import streamlit as st
import pandas as pd
import altair as alt


st.set_page_config(page_title="Gráficas Altair", layout="wide")

# Título principal
st.title("Análisis de Felicidad Mundial 2016")
st.write("Gráficas realizadas con Altair usando el archivo 2016-1.csv.")

# Cargar el archivo CSV
df = pd.read_csv("2016-1.csv")

# Mostrar las primeras filas del archivo
st.subheader("Vista previa de los datos")
st.dataframe(df.head())

# Colores principales de la empresa Gandhi
color_principal = "#0080FF"
color_secundario = "#FF7F00"

st.header("Gráficas con Altair")


# GRÁFICA 1
st.subheader("Gráfica 1: Top 10 países con mayor Happiness Score")

top10 = df.sort_values("Happiness Score", ascending=False).head(10)

grafica1 = (
    alt.Chart(top10)
    .mark_bar(color=color_principal)
    .encode(
        x="Happiness Score",
        y="Country"
    )
)

st.altair_chart(grafica1)

st.write(
    "En esta gráfica se muestran los 10 países con mayor Happiness Score en el año 2016. "
    "Me sirve para identificar rápidamente cuáles países tuvieron los niveles más altos de felicidad dentro del dataset. "
    "Utilicé una gráfica de barras porque permite comparar de forma clara el puntaje de cada país. "
    "Además, usé un solo color principal para mantener la visualización simple y enfocada en la comparación."
)


# GRÁFICA 2
st.subheader("Gráfica 2: Promedio de felicidad por región")

region_avg = df.groupby("Region")["Happiness Score"].mean().reset_index()

grafica2 = (
    alt.Chart(region_avg)
    .mark_bar()
    .encode(
        x="Happiness Score",
        y="Region",
        color="Region"
    )
)

st.altair_chart(grafica2)

st.write(
    "Esta gráfica compara el promedio de felicidad por región. "
    "Para hacerla, agrupé los datos por la variable Region y calculé el promedio del Happiness Score. "
    "Esto permite observar qué regiones tienen, en general, un mayor nivel de felicidad. "
    "Usé barras porque ayudan a comparar categorías, y el color por región facilita distinguir cada grupo."
)


# GRÁFICA 3
st.subheader("Gráfica 3: PIB per cápita vs Happiness Score")

grafica3 = (
    alt.Chart(df)
    .mark_point()
    .encode(
        x="Economy (GDP per Capita)",
        y="Happiness Score",
        color="Region"
    )
)

st.altair_chart(grafica3)

st.write(
    "En esta gráfica se analiza la relación entre el PIB per cápita y el Happiness Score. "
    "La idea es observar si los países con mayor nivel económico también tienden a tener mayor felicidad. "
    "Utilicé una gráfica de dispersión porque estoy comparando dos variables numéricas. "
    "Cada punto representa un país y el color indica la región a la que pertenece."
)


# GRÁFICA 4
st.subheader("Gráfica 4: Salud vs Happiness Score")

grafica4 = (
    alt.Chart(df)
    .mark_point()
    .encode(
        x="Health (Life Expectancy)",
        y="Happiness Score",
        color="Region"
    )
)

st.altair_chart(grafica4)

st.write(
    "Esta gráfica muestra la relación entre la salud, medida como esperanza de vida, y el puntaje de felicidad. "
    "Sirve para ver si los países con mejores condiciones de salud también presentan mayores niveles de felicidad. "
    "Se utilizó una gráfica de puntos porque permite observar la relación entre dos variables numéricas. "
    "El color por región ayuda a identificar si ciertos grupos de países tienen comportamientos parecidos."
)


# GRÁFICA 5
st.subheader("Gráfica 5: Libertad vs Happiness Score")

grafica5 = (
    alt.Chart(df)
    .mark_point()
    .encode(
        x="Freedom",
        y="Happiness Score",
        color="Region"
    )
)

st.altair_chart(grafica5)

st.write(
    "Esta gráfica compara la variable Freedom con el Happiness Score. "
    "El objetivo es analizar si los países donde las personas perciben mayor libertad también tienen un mayor puntaje de felicidad. "
    "Usé una gráfica de dispersión porque permite ver la relación entre ambas variables. "
    "Los colores representan las regiones, lo cual ayuda a comparar si la relación cambia dependiendo de la zona geográfica."
)


# GRÁFICA 6
st.subheader("Gráfica 6: Distribución del Happiness Score")

grafica6 = (
    alt.Chart(df)
    .mark_bar(color=color_secundario)
    .encode(
        x=alt.X("Happiness Score", bin=True),
        y="count()"
    )
)

st.altair_chart(grafica6)

st.write(
    "Esta gráfica muestra la distribución del Happiness Score dentro del dataset. "
    "A diferencia de las gráficas anteriores, aquí no se comparan países específicos, sino que se observa en qué rangos se concentran los puntajes de felicidad. "
    "Utilicé un histograma porque es útil para analizar la frecuencia de una variable numérica. "
    "Esto permite identificar si la mayoría de los países tienen puntajes bajos, medios o altos."
)


# GRÁFICA 7
st.subheader("Gráfica 7: Generosidad vs Happiness Score")

grafica7 = (
    alt.Chart(df)
    .mark_point()
    .encode(
        x="Generosity",
        y="Happiness Score",
        color="Region"
    )
)

st.altair_chart(grafica7)

st.write(
    "Esta gráfica muestra la relación entre Generosity y Happiness Score. "
    "El objetivo es observar si los países con mayor nivel de generosidad también presentan mayores niveles de felicidad. "
    "Cada punto representa un país y el color indica su región. "
    "Aunque la relación no necesariamente implica causalidad, la visualización ayuda a identificar posibles patrones entre ambas variables."
)


# GRÁFICA 8 INTERACTIVA
st.subheader("Gráfica 8: Gráfica interactiva por región")

seleccion = alt.selection_point(fields=["Region"], bind="legend")

grafica8 = (
    alt.Chart(df)
    .mark_point()
    .encode(
        x="Economy (GDP per Capita)",
        y="Happiness Score",
        color="Region",
        opacity=alt.condition(seleccion, alt.value(1), alt.value(0.2))
    )
    .add_params(seleccion)
)

st.altair_chart(grafica8)

st.write(
    "Esta gráfica es interactiva porque permite seleccionar una región desde la leyenda. "
    "Al seleccionar una región, los puntos de esa categoría se resaltan y los demás quedan con menor intensidad. "
    "Esto ayuda a analizar con más detalle el comportamiento de una región sin eliminar el contexto general de los demás países. "
    "La interacción es útil porque permite explorar los datos de manera más dinámica y comparar regiones dentro de la misma gráfica."
)

# UNIÓN DE GRÁFICOS
st.header("Unión de gráficos")

st.write(
    "En esta parte junté varias gráficas para que el análisis se vea más como un tablero. "
    "La idea es no ver cada gráfica totalmente separada, sino poder comparar varias visualizaciones "
    "en una misma sección."
)

# Unión 1
grafinal1 = grafica1 & grafica2

st.altair_chart(grafinal1)

st.write(
    "En esta primera unión puse la gráfica de los países con mayor Happiness Score junto con el promedio por región. "
    "Esto me ayuda a ver primero cuáles son los países con mejores resultados y después comparar si esos resultados "
    "también se reflejan a nivel regional."
)


# Unión 2
grafinal2 = grafica3 & grafica4

st.altair_chart(grafinal2)

st.write(
    "En esta segunda unión comparé el Happiness Score con dos variables importantes: economía y salud. "
    "La intención es observar si los países con mayor PIB per cápita o mejor esperanza de vida también tienden "
    "a tener un puntaje de felicidad más alto."
)


# Unión 3
grafinal3 = grafica5 & grafica6

st.altair_chart(grafinal3)

st.write(
    "En esta tercera unión coloqué la relación entre libertad y felicidad junto con la distribución general del Happiness Score. "
    "Esto sirve porque primero se analiza una posible relación entre dos variables y después se observa cómo están repartidos "
    "los puntajes de felicidad en todos los países."
)


# Unión 4
grafinal4 = grafica7 & grafica8

st.altair_chart(grafinal4)

st.write(
    "En esta última unión puse la relación entre generosidad y felicidad junto con la gráfica interactiva por región. "
    "Esto permite ver otra posible variable relacionada con la felicidad y, además, explorar los datos de forma más dinámica "
    "seleccionando regiones desde la leyenda."
)


# CONCLUSIONES
st.header("Conclusiones")

st.write(
    "Como conclusión general, esta actividad me ayudó a entender cómo se pueden transformar datos de un archivo CSV "
    "en gráficas más claras y visuales usando Streamlit y Altair. También pude practicar cómo elegir colores, crear diferentes "
    "tipos de gráficas y unirlas en un tablero para analizar mejor la información del World Happiness Report 2016."
)

st.subheader("¿Cuál es la importancia de una buena elección de color para la representación de datos?")

st.write(
    "Una buena elección de color es importante porque ayuda a que los datos se entiendan de forma más fácil y rápida. "
    "Cuando los colores están bien elegidos, se pueden distinguir mejor las categorías, comparar regiones y resaltar información importante. "
    "En esta actividad usé una paleta basada en la empresa Gandhi, tomando como color principal el azul #0080FF. "
    "Esto ayudó a que las gráficas tuvieran una identidad visual más ordenada y no se vieran como colores puestos al azar."
)

st.subheader("¿Altair es una buena librería para realizar gráficas? Ventajas y desventajas")

st.write(
    "Sí considero que Altair es una buena librería para hacer gráficas, porque su estructura es bastante clara: "
    "se eligen los datos, después el tipo de gráfica y luego las variables que van en los ejes o en el color. "
    "Una ventaja es que permite hacer gráficas limpias y también interactivas, como la gráfica donde se puede seleccionar una región desde la leyenda. "
    "Otra ventaja es que se puede integrar con Streamlit para crear un dashboard. "
    "Como desventaja, algunas partes pueden ser confusas al principio, por ejemplo bin=True, selection_point() o condition(), "
    "porque no son tan fáciles de entender la primera vez. Aun así, después de practicarlo, Altair resulta útil para visualizar datos de forma ordenada."
)