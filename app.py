import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv(r'C:\Users\Jube\vehicles_env\Comparacion_vehiculos\vehicles_us.csv')

# Crear un encabezado
st.header('Comparador de vehículos')

# Crear un botón para construir un histograma
hist_button = st.button('Construir histograma')
# Al hacer clic en el botón
if hist_button:
    st.write('Crea un histograma para el conjunto de datos de venta de autos')
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para construir un diagrama de dispersión
scatter_button = st.button('Construir diagrama de dispersión')
# Al hacer clic en el botón
if scatter_button:
    st.write('Crea un diagrama de dispersión para el conjunto de datos de venta de autos')
    # Crear un diagrama de dispersión
    fig = px.scatter(car_data, x="odometer")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear una casilla de verificación para construir un histograma
build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('Construir un histograma para la columna odómetro')
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear una casilla de verificación para construir un diagrama de dispersión
build_scatter = st.checkbox('Construir un diagrama de dispersión')
if build_scatter:
    st.write('Construir un diagrama de dispersión para la columna odómetro')
    # Crear un diagrama de dispersión
    fig = px.scatter(car_data, x="odometer")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    