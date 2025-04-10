# Análisis de Clustering de Incidentes Mineros

🚀 **Explorando patrones ocultos en los datos de incidentes mineros con técnicas de Clustering**

Como **ingeniero de minas** y **analista de datos**, me apasiona combinar el conocimiento del terreno con el poder de la **data science** para mejorar la seguridad y eficiencia en las operaciones. 🛠️📊

Recientemente, apliqué **técnicas de clustering** para analizar incidentes mineros en una **región geográfica** de Zambia. El objetivo: **identificar agrupaciones** de accidentes según su **ubicación, tipo y gravedad**. Esto puede ayudar a detectar zonas de alto riesgo, mejorar la prevención de incidentes y optimizar la asignación de recursos.

## 🧭 **Metodología aplicada**:

1. **Generación de datos sintéticos**:
   - Simulación de incidentes mineros con variables como **latitud**, **longitud**, **tipo de accidente** y **gravedad** en diversas zonas geográficas de Zambia.
   
2. **Preprocesamiento de los datos**:
   - Codificación de variables categóricas como **tipo de accidente** (e.g., deslizamiento, explosión) y **gravedad** (leve, moderado, grave) utilizando **One-Hot Encoding**.
   - **Escalado de variables**: Normalización de coordenadas geográficas y características categóricas con **StandardScaler** para mejorar la precisión de los modelos de clustering.
   
3. **Técnicas de clusterización**:
   - **KMeans**: Segmentación de los incidentes en **5 clusters**. Esta técnica agrupó los incidentes en zonas de alto riesgo con patrones espaciales y operativos similares.
   - **DBSCAN**: Se utilizó **DBSCAN** para identificar **anomalías** o puntos de ruido en los datos, lo que permite detectar incidentes atípicos o fuera de lo común.
   
4. **Evaluación del modelo**:
   - **Silhouette Score**: Se empleó para evaluar la calidad de los clusters obtenidos y asegurar que las agrupaciones fueran apropiadas.

## 📈 **Resultados**:

- **Clusters bien definidos**: Identificación de **zonas geográficas** donde ciertos tipos de incidentes, como deslizamientos o explosiones, ocurren con mayor frecuencia. Esto puede ser útil para la asignación de recursos de manera más eficiente.
  
- **Detección de anomalías**: Gracias a **DBSCAN**, se encontraron incidentes que no se ajustan a los patrones generales, lo que indica posibles **errores de datos** o eventos inesperados que podrían requerir una investigación adicional.
  
- **Estrategia de prevención más eficiente**: Los resultados de clustering proporcionan una **segmentación precisa** que puede ser utilizada para desarrollar **estrategias de intervención** en las áreas con mayor riesgo, mejorando así la seguridad.

## 🔧 **Tecnologías y herramientas utilizadas**:

- **Python**: El lenguaje de programación utilizado para todo el flujo de trabajo.
  
- **Librerías**:
  - **pandas** y **numpy**: Para manipulación de datos y matrices.
  - **matplotlib** y **seaborn**: Para visualización de clusters y análisis exploratorio de los datos.
  - **plotly**: Para la creación de gráficos interactivos, como la distribución de incidentes por tipo y gravedad, y la visualización geográfica de los incidentes.
  - **folium**: Para crear un mapa interactivo donde se visualizan las ubicaciones geográficas de los incidentes.
  - **scikit-learn**: Para la implementación de los algoritmos **KMeans** y **DBSCAN**, así como para la evaluación del modelo con el **Silhouette Score**.

## 💻 **Aplicación interactiva con Streamlit**:

Además de los análisis, he desarrollado una aplicación interactiva utilizando **Streamlit**. A través de esta aplicación, puedes:

- Visualizar los **clusters** generados por **KMeans** y **DBSCAN** en mapas interactivos y gráficos de dispersión.
- Explorar cómo se distribuyen los incidentes según su tipo y gravedad en gráficos interactivos creados con **Plotly**.
- Acceder a **análisis visuales** en tiempo real con **folium** y **Streamlit**, donde se muestran las ubicaciones exactas de los incidentes.


