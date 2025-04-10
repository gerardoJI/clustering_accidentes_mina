import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import folium
from folium.plugins import MarkerCluster
from streamlit.components.v1 import html
from io import BytesIO
from fpdf import FPDF

# Cargar y preparar los datos
np.random.seed(42)

n_incidents = 1000
latitudes = np.random.uniform(-18.5, -8.2, n_incidents)
longitudes = np.random.uniform(22.2, 33.5, n_incidents)
incident_types = np.random.choice(['Deslizamiento', 'Explosión', 'Derrumbe', 'Incendio', 'Inundación','Enfermedad'], n_incidents)
severity = np.random.choice(['Leve', 'Moderado', 'Grave'], n_incidents)

data = pd.DataFrame({
    'latitud': latitudes,
    'longitud': longitudes,
    'tipo_accidente': incident_types,
    'gravedad': severity
})

# Preprocesar los datos
data_encoded = pd.get_dummies(data[['tipo_accidente', 'gravedad']], drop_first=True)
X = pd.concat([data[['latitud', 'longitud']], data_encoded], axis=1)

# Escalar las características
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Aplicar KMeans
kmeans = KMeans(n_clusters=5, random_state=42)
data['Cluster_KMeans'] = kmeans.fit_predict(X_scaled)

# Aplicar DBSCAN
dbscan = DBSCAN(eps=1.2, min_samples=5)
data['Cluster_DBSCAN'] = dbscan.fit_predict(X_scaled)

# Evaluar el Silhouette Score para ambos modelos
silhouette_kmeans = silhouette_score(X_scaled, data['Cluster_KMeans'])
silhouette_dbscan = silhouette_score(X_scaled, data['Cluster_DBSCAN'][data['Cluster_DBSCAN'] != -1])

# Configuración de Streamlit
st.title("Análisis de Accidentes Mineros - Clustering")
st.markdown("Por Gerardo Jiménez Islas.")
st.markdown("Abril 2025.")
# Mostrar la imagen desde la URL
st.image(
    "https://images.kennametal.com/is/image/Kennametal/Underground%20Mining%202",
    caption="Imagen de minería subterránea (Fuente: Kennametal)"
)

st.subheader("'Si no se mide, no se controla': La clave para la mejora de la seguridad en minería.")
st.markdown('''La recopilación masiva de datos puede ser una herramienta poderosa para la mejora de
            la seguridad en el sector minero. Sin embargo, no basta con recolectar información: es 
            clave analizarla con profundidad y precisión, y es aquí donde la inteligencia artificial (IA)
             y el machine learning (ML) marcan la diferencia. Estas tecnologías permiten detectar patrones 
            ocultos en grandes volúmenes de datos, predecir eventos de riesgo antes de que ocurran, 
            y optimizar los recursos destinados a la prevención.''')

st.markdown("")
st.markdown("Convencido de lo anterior, en esta breve publicación se pretende identificar patrones y agrupaciones de incidentes mineros según su ubicación geográfica y características. Para ello, se utilizan algoritmos de clustering como KMeans y DBSCAN, que permiten agrupar los incidentes en función de su latitud, longitud y tipo de accidente. El objetivo es proporcionar una visión clara y concisa de la distribución de los incidentes, facilitando así la identificación de áreas críticas y la toma de decisiones informadas para mejorar la seguridad en el sector minero.")
st.markdown("")
st.markdown("IMPORTANTE: Este análisis es generado a partir de datos sintéticos, y no representa datos reales. Los resultados tienen fines de demostrativos.")

st.subheader("Datos aleatorios de accidentes mineros")
st.markdown("Descarga los datos utilizados para este análisis:")

# Función para descargar los datos en formato CSV
csv = data.to_csv(index=False)
st.download_button(
    label="Descargar datos como CSV",
    data=csv,
    file_name='accidentes_mineros.csv',
    mime='text/csv'
)

# Función para descargar los datos en formato PDF
from fpdf import FPDF
from io import BytesIO

def generate_pdf(data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Accidentes Mineros - Datos", ln=True, align="C")

    # Agregar los datos al PDF (solo algunas filas para evitar un PDF gigante)
    for i, row in data.head(30).iterrows():  # puedes ajustar el número de filas si quieres
        pdf.cell(200, 10, 
                 txt=f"Lat: {row['latitud']:.2f}, Lon: {row['longitud']:.2f}, Tipo: {row['tipo_accidente']}, Gravedad: {row['gravedad']}", 
                 ln=True)

    pdf_bytes = pdf.output(dest='S').encode('latin1')  # output como string y codificado
    return BytesIO(pdf_bytes)


# Botón para descargar los datos como PDF
pdf_data = generate_pdf(data)
st.download_button(
    label="Descargar datos como PDF",
    data=pdf_data,
    file_name="accidentes_mineros.pdf",
    mime="application/pdf"
)
st.markdown("---")


# Gráfico interactivo de barras con Plotly (Distribución de incidentes por tipo y gravedad)
st.subheader("Distribución de Incidentes por Tipo y Gravedad")
st.markdown("En esta gráfica se aprecian las caracteristicas de los accidentes mineros, resumiendo la distribución de los accidentes.")
fig_bar = px.bar(data_frame=data, 
                 x='tipo_accidente', 
                 color='gravedad', 
                 title='Distribución de incidentes por tipo y gravedad',
                 category_orders={'tipo_accidente': ['Deslizamiento', 'Explosión', 'Derrumbe', 'Incendio', 'Inundación', 'Enfermedad']},
                 template='plotly_dark'
                 )
st.plotly_chart(fig_bar)

# Gráfico de distribución de clusters con KMeans (scatter plot)
st.subheader("Comparativa de clusterización de datos - KMeans vs DBSCAN")
st.markdown("")
st.subheader("Distribución de Incidentes - KMeans")

fig_kmeans = px.scatter(data_frame=data, 
                        x='latitud', 
                        y='longitud', 
                        color='Cluster_KMeans', 
                        title='Distribución de Incidentes por Cluster (KMeans)', 
                        template='plotly_dark')
st.plotly_chart(fig_kmeans)

# Gráfico de distribución de clusters con DBSCAN (scatter plot)
st.subheader("Distribución de Incidentes - DBSCAN")
fig_dbscan = px.scatter(data_frame=data, 
                        x='latitud', 
                        y='longitud', 
                        color='Cluster_DBSCAN', 
                        title='Distribución de Incidentes por Cluster (DBSCAN)', 
                        template='plotly_dark')
st.plotly_chart(fig_dbscan)

# Mostrar los resultados del Silhouette Score
st.markdown("Para evaluar los resultados de los algoritmos de clustering, se ha utilizado el Silhouette Score, que mide la calidad de la agrupación. Un valor cercano a 1 indica una buena separación entre los clusters, mientras que un valor cercano a -1 indica que los puntos están mal agrupados.")
st.write(f"**Silhouette Score KMeans**: {silhouette_kmeans:.2f}")
st.write(f"**Silhouette Score DBSCAN**: {silhouette_dbscan:.2f}")

# Crear mapa interactivo con Folium
st.subheader("Mapa Interactivo de Incidentes")
st.markdown("Finalmente, se utiliza la libreria Folium para crear un mapa interactivo que muestra la distribución geográfica de los accidentes mineros del set de datos generado.")
m = folium.Map(location=[-15.0, 28.0], zoom_start=6, control_scale=True)

# Agrupar los incidentes por tipo
marker_cluster = MarkerCluster().add_to(m)

# Añadir los incidentes al mapa
for i, row in data.iterrows():
    folium.CircleMarker(
        location=[row['latitud'], row['longitud']],
        radius=5,
        color='blue' if row['Cluster_DBSCAN'] == -1 else 'green',
        fill=True,
        fill_color='blue' if row['Cluster_DBSCAN'] == -1 else 'green',
        fill_opacity=0.6,
        popup=f"Tipo: {row['tipo_accidente']}, Gravedad: {row['gravedad']}",
    ).add_to(marker_cluster)

# Mostrar el mapa utilizando streamlit.components.v1.html()
map_html = m._repr_html_()  # Convertir el mapa folium a HTML
html(map_html, height=400)  # Mostrarlo en Streamlit

st.subheader("En resumen:")
st.markdown('''El uso de algoritmos de clustering como KMeans y DBSCAN ha permitido explorar de manera 
            efectiva la distribución geográfica y las características de los incidentes mineros, revelando 
            patrones que pueden ser clave para una gestión preventiva más eficiente. Aunque los datos utilizados
             en este análisis son sintéticos, los resultados evidencian un nivel aceptable de agrupación que puede
             orientar futuras investigaciones con datos reales. Este enfoque demuestra el valor que tiene 
            la aplicación de técnicas de inteligencia artificial y machine learning en la minería, no solo
             como herramientas analíticas, sino como aliados estratégicos en la identificación de áreas críticas
             y en la toma de decisiones para fortalecer la seguridad operacional.''')


# Sección personalizada sobre ti
st.markdown("---")
st.subheader("👤 Sobre mí")

col1, col2 = st.columns([1, 4])

with col1:
    # Si tienes una imagen de perfil local o URL, la puedes poner aquí
    st.image("https://avatars.githubusercontent.com/u/187279782?v=4", width=100)  # <-- reemplaza si tienes un link a tu foto

with col2:
    st.markdown("""
**Gerardo Jiménez Islas**  
💼 Analista de Datos | 💡 Apasionado por la inteligencia artificial y los datos

📫 Conéctate conmigo:

- [![LinkedIn](https://img.shields.io/badge/LinkedIn-Gerardo--Jiménez--Islas-blue?logo=linkedin)](https://www.linkedin.com/in/gerardo-jimenez-islas/)
- [![GitHub](https://img.shields.io/badge/GitHub-gerardoJI-black?logo=github)](https://github.com/gerardoJI)
    """)

st.markdown("---")
