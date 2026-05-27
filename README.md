# Dashboard de Spotify con Dash y Plotly

## Integrantes

- Patricio Espinosa — Matrícula: A01712476
- Jose Emiliano — Matrícula: A01711141

## Descripción del proyecto

Este proyecto utiliza un conjunto de datos de Spotify para realizar un análisis exploratorio y crear un dashboard básico utilizando Dash y Plotly.

El dashboard permite seleccionar diferentes gráficas mediante un componente Dropdown. Al seleccionar una opción, se actualiza la gráfica y se muestra debajo una descripción con su conclusión correspondiente.

## Archivos incluidos

- `spotify.csv`: base de datos utilizada.
- `Actividad_Dashboards_y_Plotly`: notebook con el análisis exploratorio y las 10 gráficas.
- `tareaapp_grafica.py`: archivo Python con el dashboard interactivo.
- `README.md`: archivo con la descripción del proyecto, nombres y nuestras matrículas.

## Gráficas incluidas

1. Distribución de popularidad de canciones.
2. Top 15 géneros con mayor popularidad promedio.
3. Relación entre energía y danceability.
4. Contenido explícito.
5. Popularidad promedio según contenido explícito.
6. Top 10 géneros con mayor danceability promedio.
7. Top 10 géneros con mayor valence promedio.
8. Top 10 géneros con mayor instrumentalness promedio.
9. Top 10 géneros con mayor loudness promedio.
10. Top 10 géneros con menor popularidad promedio.

## Librerías utilizadas

- pandas
- plotly
- dash
- dash-bootstrap-components

## Cómo ejecutar el dashboard

Primero se instalan las librerías necesarias:

```bash
pip install pandas plotly dash dash-bootstrap-components