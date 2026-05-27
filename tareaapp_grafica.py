from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Leer el archivo CSV
df = pd.read_csv("spotify.csv")

# Crear la aplicación
app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

# Build your components
mytitle = dcc.Markdown(children="# Dashboard de Spotify  \n### Integrantes: Patricio Espinosa y Jose Emiliano")
mygraph = dcc.Graph(figure={})

dropdown = dcc.Dropdown(
    options=[
        "Gráfica 1",
        "Gráfica 2",
        "Gráfica 3",
        "Gráfica 4",
        "Gráfica 5",
        "Gráfica 6",
        "Gráfica 7",
        "Gráfica 8",
        "Gráfica 9",
        "Gráfica 10"
    ],
    value="Gráfica 1",
    clearable=False
)

description = dcc.Markdown(children="")

# Layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([mytitle], width=8)
    ], justify="center"),

    dbc.Row([
        dbc.Col([dropdown], width=6)
    ], justify="center"),

    dbc.Row([
        dbc.Col([mygraph], width=12)
    ]),

    dbc.Row([
        dbc.Col([description], width=10)
    ], justify="center")
], fluid=True)

# Callback
@app.callback(
    Output(mygraph, "figure"),
    Output(description, "children"),
    Input(dropdown, "value")
)
def update(user_input):

    if user_input == "Gráfica 1":
        fig = px.histogram(df, x="popularity", nbins=30, marginal="rug", color_discrete_sequence=["#1DB954"], template="plotly_dark", title="Distribución de Popularidad de Canciones")
        descripcion = "# Gráfica 1 — Distribución de popularidad de canciones\n\nEn esta gráfica se muestra cómo se distribuye la popularidad de las canciones dentro del dataset. La variable analizada es popularity, y el histograma permite ver en qué rangos se concentran más canciones.\n\n# Conclusión\n\nSe puede observar que hay una gran cantidad de canciones con popularidad baja, especialmente cerca de 0. Después, la mayoría de las canciones se concentran entre valores aproximados de 20 a 60 de popularidad. También se nota que hay pocas canciones con popularidad muy alta, arriba de 80 o 90. En general, esta gráfica ayuda a ver que no todas las canciones del dataset son muy populares, sino que la mayoría tiene una popularidad media o baja."

    elif user_input == "Gráfica 2":
        datos = df.groupby("track_genre")["popularity"].mean().sort_values(ascending=False).head(15).reset_index()
        fig = px.bar(datos, x="popularity", y="track_genre", color="track_genre", orientation="h", title="Top 15 géneros con mayor popularidad promedio")
        descripcion = "# Gráfica 2 — Top 15 géneros con mayor popularidad promedio\n\nEn esta gráfica se muestran los 15 géneros que tienen mayor popularidad promedio en el dataset. Para hacerla, se agrupó la información por género musical y se calculó el promedio de popularidad de las canciones de cada uno.\n\n# Conclusión\n\nSe puede observar que los géneros con mayor popularidad promedio son pop-film, k-pop y chill. Esto quiere decir que, dentro del dataset, las canciones de estos géneros suelen tener mejores niveles de popularidad. También se nota que varios géneros tienen valores parecidos, por lo que la diferencia entre ellos no es tan grande. En general, esta gráfica ayuda a identificar qué géneros destacan más en Spotify según su popularidad promedio."

    elif user_input == "Gráfica 3":
        fig = px.scatter(df, x="energy", y="danceability", color="popularity", size="popularity", hover_data=["track_name"], color_continuous_scale="Viridis", template="plotly_dark", title="Relación entre Energía y Danceability")
        descripcion = "# Gráfica 3 — Relación entre energía y danceability\n\nEn esta gráfica se analiza la relación entre la energía de las canciones y su nivel de danceability, es decir, qué tan adecuadas son para bailar. Cada punto representa una canción del dataset, y el color indica su nivel de popularidad.\n\n# Conclusión\n\nSe puede observar que muchas canciones se concentran en niveles medios y altos de energía, y también en valores medios y altos de danceability. Esto quiere decir que varias canciones del dataset suelen ser energéticas y bailables al mismo tiempo. Sin embargo, no se ve una relación perfecta, porque también hay canciones con mucha energía pero baja danceability, o canciones bailables con menor energía. En general, esta gráfica ayuda a comparar cómo se comportan estas dos características musicales y cómo se relacionan con la popularidad."

    elif user_input == "Gráfica 4":
        datos = df["explicit"].value_counts()
        fig = px.pie(values=datos.values, names=["No Explicit", "Explicit"], color_discrete_sequence=["#1DB954", "#FF4ECD"], template="plotly_dark", title="Contenido Explícito")
        descripcion = "# Gráfica 4 — Contenido explícito\n\nEn esta gráfica se muestra la proporción de canciones explícitas y no explícitas dentro del dataset. La gráfica de pastel permite comparar de forma rápida qué porcentaje de canciones tiene contenido explícito y qué porcentaje no.\n\n# Conclusión\n\nSe puede observar que la mayoría de las canciones del dataset no tienen contenido explícito, ya que representan aproximadamente el 91.5%. En cambio, las canciones explícitas son una parte mucho menor, con alrededor del 8.55%. Esto quiere decir que, dentro de este dataset, predominan las canciones sin contenido explícito."

    elif user_input == "Gráfica 5":
        datos = df.groupby("explicit")["popularity"].mean().reset_index()
        fig = px.bar(datos, x="explicit", y="popularity", color="explicit", color_discrete_sequence=["#1CD3BF", "#30D31C"], template="plotly_dark", title="Popularidad promedio según contenido explícito")
        descripcion = "# Gráfica 5 — Popularidad promedio según contenido explícito\n\nEsta gráfica compara la popularidad promedio de las canciones explícitas y no explícitas. Se utilizó la columna explicit para separar las canciones en dos grupos.\n\n# Conclusión\n\nLa gráfica permite ver si las canciones con contenido explícito tienen una popularidad promedio mayor o menor que las canciones sin contenido explícito. Esto ayuda a comparar de forma sencilla si el tipo de contenido puede estar relacionado con la popularidad."

    elif user_input == "Gráfica 6":
        datos = df.groupby("track_genre")["danceability"].mean().sort_values(ascending=False).head(10).reset_index()
        fig = px.bar(datos, x="danceability", y="track_genre", orientation="h", color="danceability", color_continuous_scale=["#1C67D3", "#1CD363", "#D31C1E"], template="plotly_dark", title="Top 10 géneros con mayor danceability promedio")
        descripcion = "# Gráfica 6 — Top 10 géneros con mayor danceability promedio\n\nEsta gráfica muestra los 10 géneros musicales con mayor promedio de danceability, es decir, los géneros cuyas canciones tienden a ser más bailables dentro del dataset. Se utilizó una gráfica de barras horizontales para comparar más fácilmente el nivel promedio de danceability entre cada género.\n\n# Conclusión\n\nSe puede observar que géneros como kids, chicago-house, reggaeton, latino y reggae tienen los valores más altos de danceability promedio. Esto significa que, dentro del dataset, estos géneros suelen tener canciones con mayor ritmo o características más adecuadas para bailar. También se nota que los valores son bastante parecidos entre los primeros lugares, por lo que no hay una diferencia muy grande entre ellos."

    elif user_input == "Gráfica 7":
        datos = df.groupby("track_genre")["valence"].mean().sort_values(ascending=False).head(10).reset_index()
        fig = px.bar(datos, x="valence", y="track_genre", orientation="h", color="valence", color_continuous_scale=["#1CD363", "#D3631C"], template="plotly_dark", title="Top 10 géneros con mayor valence promedio")
        descripcion = "# Gráfica 7 — Top 10 géneros con mayor valence promedio\n\nEsta gráfica muestra los 10 géneros musicales con mayor promedio de valence. Esta variable se puede entender como qué tan positiva, alegre o animada suena una canción dentro del análisis de Spotify.\n\n# Conclusión\n\nSe puede observar que salsa es el género con mayor valence promedio, seguido por forro y rockabilly. Esto quiere decir que, dentro del dataset, estos géneros tienden a tener canciones con un sonido más positivo o alegre. También se nota que varios géneros tienen valores cercanos entre sí, por lo que todos los géneros mostrados presentan un nivel alto de valence en comparación con el resto."

    elif user_input == "Gráfica 8":
        datos = df.groupby("track_genre")["instrumentalness"].mean().sort_values(ascending=False).head(10).reset_index()
        fig = px.bar(datos, x="instrumentalness", y="track_genre", orientation="h", color="instrumentalness", color_continuous_scale=["#1C67D3", "#1CD363", "#D31C1E"], template="plotly_dark", title="Top 10 géneros con mayor instrumentalness promedio")
        descripcion = "# Gráfica 8 — Top 10 géneros con mayor instrumentalness promedio\n\nEsta gráfica muestra los 10 géneros musicales con mayor promedio de instrumentalness. Esta variable indica qué tan probable es que una canción sea instrumental, es decir, que tenga poca o ninguna voz.\n\n# Conclusión\n\nSe puede observar que study, minimal-techno y sleep son los géneros con mayor instrumentalness promedio dentro del dataset. Esto tiene sentido porque son géneros que suelen enfocarse más en sonidos, ambientes o bases musicales, en lugar de letras o voces. En general, esta gráfica ayuda a identificar qué géneros tienen canciones más instrumentales en Spotify."

    elif user_input == "Gráfica 9":
        datos = df.groupby("track_genre")["loudness"].mean().sort_values(ascending=False).head(10).reset_index()
        fig = px.bar(datos, x="loudness", y="track_genre", orientation="h", color="loudness", color_continuous_scale=["#1CD363", "#1CD3BF", "#30D31C"], template="plotly_dark", title="Top 10 géneros con mayor loudness promedio")
        descripcion = "# Gráfica 9 — Top 10 géneros con mayor loudness promedio\n\nEsta gráfica muestra los 10 géneros musicales con mayor promedio de loudness. Esta variable representa qué tan fuerte o intenso suena el audio de una canción. En la gráfica, los valores aparecen en números negativos porque así se mide normalmente el loudness en el dataset.\n\n# Conclusión\n\nSe puede observar que géneros como latin, latino, forro, dubstep y reggaeton tienen los valores más altos de loudness promedio. Esto significa que, dentro del dataset, estos géneros tienden a sonar con mayor intensidad o volumen percibido. También se nota que los valores están bastante cerca entre sí, por lo que no hay una diferencia extrema entre los primeros géneros. En general, esta gráfica ayuda a identificar qué estilos musicales suelen tener un sonido más fuerte."

    elif user_input == "Gráfica 10":
        datos = df.groupby("track_genre")["popularity"].mean().sort_values(ascending=True).head(10).reset_index()
        fig = px.bar(datos, x="popularity", y="track_genre", orientation="h", color="popularity", color_continuous_scale=["#631CD3", "#1CD363", "#D3631C"], template="plotly_dark", title="Top 10 géneros con menor popularidad promedio")
        descripcion = "# Gráfica 10 — Top 10 géneros con menor popularidad promedio\n\nEsta gráfica muestra los 10 géneros musicales con menor popularidad promedio dentro del dataset de Spotify. Para hacerla, se agruparon las canciones por track_genre y después se calculó el promedio de la variable popularity para cada género. La gráfica de barras horizontales permite comparar de forma clara cuáles géneros tienen los valores más bajos.\n\n# Conclusión\n\nSe puede observar que los géneros con menor popularidad promedio son iranian, romance y latin, ya que presentan los valores más bajos dentro de la gráfica. También aparecen géneros como detroit-techno, chicago-house y classical, que aunque tienen un poco más de popularidad, siguen estando entre los menos populares del dataset. En general, esta gráfica ayuda a identificar qué géneros tienen menor presencia o menor nivel de aceptación en términos de popularidad promedio dentro de la base de datos."

    return fig, descripcion
if __name__ == "__main__":
    app.run(debug=True, port=8054)