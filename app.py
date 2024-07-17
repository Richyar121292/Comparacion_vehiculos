import pandas as pd
import plotly.express as px
import streamlit as st

# Descripción de la aplicación
st.title('Comparador de Vehículos')
st.markdown("""
Esta aplicación permite comparar vehículos anunciados en los Estados Unidos. Puedes filtrar los vehículos por marca, tipo, condición , precio, año del modelo y tipo de combustible. 
Además, puedes visualizar distribuciones y relaciones entre variables mediante histogramas y diagramas de dispersión.
""")

# Cargar los datos
car_data = pd.read_csv(r'C:\Users\Jube\vehicles_env\Comparacion_vehiculos\vehicles_us')
# Rellenar la columna 'odometer' con 'new' donde el valor es 0
car_data.loc[car_data['odometer'] == 0, 'odometer'] = 'new'

# Eliminar las filas con celdas vacías
car_data.dropna(inplace=True)

# Crear un encabezado
st.header('Comparador de vehículos')

# Mostrar el DataFrame
st.write(car_data)

# Inicializar el contador de likes en session_state
if 'likes' not in st.session_state:
    st.session_state.likes = 0

# Botón de like
if st.button('👍 Like'):
    st.session_state.likes += 1

# Selector de marca en orden alfabético
brands = sorted(car_data['model'].unique())
selected_brand = st.selectbox('Selecciona una marca', brands)

# Filtrar datos por la marca seleccionada
filtered_data_by_brand = car_data[car_data['model'] == selected_brand]

# Selector de tipo de auto en orden alfabético
types = sorted(car_data['type'].unique())
selected_type = st.selectbox('Selecciona un tipo de auto', types)

# Selector de estado del vehículo
conditions = filtered_data_by_brand['condition'].unique()
selected_condition = st.selectbox('Selecciona un estado del vehículo', conditions)

# Filtrar datos por el estado seleccionado
filtered_data_by_brand_and_condition = filtered_data_by_brand[filtered_data_by_brand['condition'] == selected_condition]

# Filtro de rango de precios
min_price, max_price = int(filtered_data_by_brand_and_condition['price'].min()), int(filtered_data_by_brand_and_condition['price'].max())
selected_price_range = st.slider('Selecciona el rango de precios', min_price, max_price, (min_price, max_price))

# Filtrar datos por el rango de precios seleccionado
filtered_data = filtered_data_by_brand_and_condition[
    (filtered_data_by_brand_and_condition['price'] >= selected_price_range[0]) & 
    (filtered_data_by_brand_and_condition['price'] <= selected_price_range[1])
]

# Mostrar los datos filtrados
st.write(f'Datos filtrados por la marca {selected_brand}, estado {selected_condition} y rango de precios {selected_price_range}', filtered_data)

# Selector de columna para gráficos
column_to_plot = st.selectbox('Selecciona una columna para graficar', car_data.columns)

# Crear un botón para construir un histograma
if st.button('Construir histograma'):
    st.write(f'Crea un histograma para la columna {column_to_plot}')
    fig = px.histogram(filtered_data, x=column_to_plot)
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para construir un diagrama de dispersión
if st.button('Construir diagrama de dispersión'):
    st.write(f'Crea un diagrama de dispersión para la columna {column_to_plot}')
    fig = px.scatter(filtered_data, x=column_to_plot, y='price')  # Ejemplo: diagrama de dispersión con precio
    st.plotly_chart(fig, use_container_width=True)

# Crear filtros dinámicos
model_year = st.slider('Año del modelo', int(car_data['model_year'].min()), int(car_data['model_year'].max()), (int(car_data['model_year'].min()), int(car_data['model_year'].max())))
fuel_type = st.multiselect('Tipo de combustible', car_data['fuel'].unique(), car_data['fuel'].unique())

filtered_data = filtered_data[
    (filtered_data['model_year'] >= model_year[0]) & (filtered_data['model_year'] <= model_year[1]) &
    (filtered_data['fuel'].isin(fuel_type))
]

st.write('Datos filtrados por marca, estado del vehículo, rango de precios y otros criterios', filtered_data)

# Descripción estadística
if st.checkbox('Mostrar descripción estadística'):
    st.write(filtered_data.describe())

