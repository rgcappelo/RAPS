import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Configuración de estilo para gráficos
plt.style.use("ggplot")

# Generar fechas para los últimos 12 meses
fecha_fin = datetime.now()
fecha_inicio = fecha_fin - timedelta(days=365)
fechas = pd.date_range(start=fecha_inicio, end=fecha_fin, freq="M")
meses = [fecha.strftime("%b %Y") for fecha in fechas]

# Función para generar datos aleatorios con tendencia
def generar_datos_con_tendencia(min_val, max_val, n=12, tendencia=0):
    base = np.random.randint(min_val, max_val, n)
    trend = np.linspace(0, tendencia, n)
    result = base + trend
    return np.clip(result, min_val, max_val).astype(int)

# 1. Generar datos simulados
# 1.1 Sensing (Detección de cambios en el entorno digital)
reportes_tendencias = generar_datos_con_tendencia(2, 6, len(fechas), 1)
clientes_migrados = generar_datos_con_tendencia(50, 150, len(fechas), 40)
tiempo_respuesta = generar_datos_con_tendencia(30, 90, len(fechas), -20)

# 1.2 Seizing (Aprovechamiento de oportunidades digitales)
usuarios_activos = generar_datos_con_tendencia(800, 1500, len(fechas), 300)
pedidos_procesados = generar_datos_con_tendencia(500, 1200, len(fechas), 400)
tiempo_procesamiento = generar_datos_con_tendencia(5, 20, len(fechas), -5)

# 1.3 Configuring (Adaptación del modelo operativo a nuevas tecnologías)
gasto_ti_opex = generar_datos_con_tendencia(30, 70, len(fechas), 15)
alianzas_tecnologicas = generar_datos_con_tendencia(1, 4, len(fechas), 1)
tiempo_inactividad = generar_datos_con_tendencia(1, 5, len(fechas), -1)

# Crear DataFrame con todos los datos
#Aqui se puede cambiar los nombres de los titulos de los graficos, pero hay que cambiarlo mas abajo tambien
data = pd.DataFrame({
    "Fecha": fechas,
    "Mes": meses,
    "Reportes_Tendencias": reportes_tendencias,
    "Clientes_Migrados": clientes_migrados,
    "Tiempo_Respuesta": tiempo_respuesta,
    "Usuarios_Activos": usuarios_activos,
    "Pedidos_Procesados": pedidos_procesados,
    "Tiempo_Procesamiento": tiempo_procesamiento,
    "Gasto_TI_OpEx1": gasto_ti_opex,
    "Alianzas_Tecnologicas": alianzas_tecnologicas,
    "Tiempo_Inactividad": tiempo_inactividad
})

# --- INTERFAZ EN STREAMLIT ---

st.title("📊 Dashboard de Transformación Digital de RAPS")
st.write("Texto de prueba 

         otro texto ")
st.sidebar.header("Opciones de Visualización de los KPIs")

# Selección de métricas a visualizar
opcion = st.sidebar.selectbox(
    "Seleccione una métrica para visualizar:",
    [
        "Clientes Migrados al Modelo Digital",
        "Usuarios Activos en MyRAzept",
        "Evolución del Gasto en TI bajo Modelo OpEx",
        "Pedidos Digitales Procesados",
        "Tiempo de Respuesta a Cambios Regulatorios",
        "Número de Alianzas Tecnológicas"
    ]
)

# --- GENERACIÓN DE GRÁFICOS EN STREAMLIT ---

def graficar_metrica(metrica, color, ylabel):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data["Fecha"], data[metrica], marker="o", linestyle="-", color=color)
    ax.set_title(metrica)
    ax.set_xlabel("Fecha")
    ax.set_ylabel(ylabel)
    ax.grid(True)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Mostrar la métrica seleccionada
if opcion == "Clientes Migrados al Modelo Digital":
    graficar_metrica("Clientes_Migrados", "blue", "Número de Clientes")

elif opcion == "Usuarios Activos en MyRAzept":
    graficar_metrica("Usuarios_Activos", "green", "Usuarios Activos")

elif opcion == "Evolución del Gasto en TI bajo Modelo OpEx":
    graficar_metrica("Gasto_TI_OpEx1", "red", "Porcentaje de Gasto OpEx")

elif opcion == "Pedidos Digitales Procesados":
    graficar_metrica("Pedidos_Procesados", "purple", "Cantidad de Pedidos")

elif opcion == "Tiempo de Respuesta a Cambios Regulatorios":
    graficar_metrica("Tiempo_Respuesta", "orange", "Días de Respuesta")

elif opcion == "Número de Alianzas Tecnológicas":
    graficar_metrica("Alianzas_Tecnologicas", "brown", "Número de Alianzas")

# Mostrar DataFrame con los datos
st.write("📌 Datos Simulados:")
st.dataframe(data)
