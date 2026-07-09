import streamlit as st

st.title("Calculadora de Engranes")

# 1. Entrada dinámica del usuario
entrada = st.text_input("Ingresa tus engranes disponibles (separados por coma):", "20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60")

# Convertimos la entrada de texto a una lista de números
try:
    engranes = [int(x.strip()) for x in entrada.split(",")]
except:
    st.error("Por favor, ingresa solo números separados por comas.")
    st.stop()

# 2. Configuración de parámetros
objetivo = st.number_input("Relación objetivo:", value=0.345, format="%.4f")

if st.button("Calcular"):
    with st.spinner('Buscando combinaciones...'):
        resultados = []
        encontrados = 0
        
        # Bucle optimizado con el límite de 10
        for a in engranes:
            for b in engranes:
                for c in engranes:
                    for d in engranes:
                        # Restricción actualizada
                        if (c/2) + (d/2) > (b / 1.5):
                            val = (a/b) * (c/d)
                            if abs(val - objetivo) <= 0.001:
                                resultados.append(f"{a}/{b} * {c}/{d} = {val:.6f}")
                                encontrados += 1
                                if encontrados >= 10: break # Se detiene al llegar a 10
                    if encontrados >= 10: break
                if encontrados >= 10: break
            if encontrados >= 10: break
        
        # Mostrar resultados
        if resultados:
            st.success(f"Se encontraron {len(resultados)} combinaciones:")
            for r in resultados:
                st.write(r)
        else:
            st.warning("No se encontraron resultados con esos engranes y restricción.")