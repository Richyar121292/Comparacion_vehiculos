import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv(r'C:\Users\Jube\vehicles_env\Comparacion_vehiculos\vehicles_us.csv')

# Crear un encabezado
st.header('Comparador de vehículos')

# Crear un botón para construir un histograma
if st.button('Construir histograma'):
    st.write('Crea un histograma para el conjunto de datos de venta de autos')
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para construir un diagrama de dispersión
if st.button('Construir diagrama de dispersión'):
    st.write('Crea un diagrama de dispersión para el conjunto de datos de venta de autos')
    # Crear un diagrama de dispersión
    fig = px.scatter(car_data, x="odometer")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear una casilla de verificación para construir un histograma
if st.checkbox('Construir un histograma'):
    st.write('Construir un histograma para la columna odómetro')
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear una casilla de verificación para construir un diagrama de dispersión
if st.checkbox('Construir un diagrama de dispersión'):
    st.write('Construir un diagrama de dispersión para la columna odómetro')
    # Crear un diagrama de dispersión
    fig = px.scatter(car_data, x="odometer")
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    