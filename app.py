import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(
    page_title="Plan Táctico de Seguridad Hídrica - CuencaVerde",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos personalizados para reflejar la identidad técnica y ambiental
st.markdown("""
    <style>
    .main-title { font-size: 32px; font-weight: bold; color: #1E3A8A; }
    .subtitle { font-size: 18px; color: #4B5563; margin-bottom: 20px; }
    .metric-box { background-color: #F3F4F6; padding: 15px; border-radius: 8px; border-left: 5px solid #3B82F6; }
    </style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL ---
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=200&q=80", caption="Cuencas Saludables, Ciudades Resilientes")
    st.title("CuencaVerde")
    st.markdown("**Orquestador Hidro-Territorial**")
    st.markdown("---")
    st.markdown("### Control de Gobernanza")
    st.info("Seguimiento Trimestral mediante Dashboards SIHT-CV para la Junta Directiva.")

# --- TÍTULO PRINCIPAL ---
st.markdown('<p class="main-title">Plan Táctico de Seguridad Hídrica Territorial</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Presentación Estratégica para la Junta Directiva de CuencaVerde</p>', unsafe_allow_html=True)

# --- PESTAÑAS PRINCIPALES ---
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Resumen Ejecutivo", 
    "🌱 Estructura Programática", 
    "📅 Cronograma de Ejecución", 
    "💰 Presupuesto y Recursos"
])

# PESTAÑA 1: RESUMEN EJECUTIVO
with tab1:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### Business Case de Inversión")
        st.write("""
        Este Plan Táctico materializa la visión del Plan Estratégico de Seguridad Hídrica CV 2026 mediante la operacionalización de soluciones tangibles y de alto impacto. 
        Adopta una visión sistémica de **'Cuencas Saludables, Ciudades Resilientes'**, reconociendo la dependencia socio-ecológica con la Región Central funcional (Norte y Oriente) que sostiene el metabolismo urbano del Distrito de Medellín.
        """)
        st.write("""
        A través del **apalancamiento financiero estratégico del Artículo 41 de la Ley 99 de 1993** (mínimo el 1% de los ingresos corrientes del Distrito), CuencaVerde actuará como el orquestador hidro-territorial más allá de las fronteras administrativas.
        """)
    with col2:
        st.markdown('<div class="metric-box"><h4>Inversión Estimada Total</h4><h2>$19.000M COP</h2><p>Periodo 2026-2027</p></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### Vulnerabilidad Estructural y Contexto Regional")
    st.warning("Dependencia crítica de agua, energía y alimentos provenientes de ecosistemas abastecedores externos, como los embalses La Fe, Río Grande y las microcuencas rurales que los proveen.")

# PESTAÑA 2: ESTRUCTURA PROGRAMÁTICA
with tab2:
    st.markdown("### Líneas Estratégicas y Acciones de Prioridad Alta")
    
    linea = st.selectbox("Seleccione la Línea Estratégica a consultar:", [
        "Línea 1: Gestión del conocimiento e inteligencia Socio-ecológica",
        "Línea 2: Articulación multisectorial para la gobernanza multinivel",
        "Línea 3: Intervenciones con propósito y retorno"
    ])
    
    if "Línea 1" in linea:
        st.markdown("**Objetivo:** Consolidar una plataforma tecnológica multinivel que orqueste información biofísica, climática y sociodemográfica en tiempo real, generando modelación socioecológica predictiva regional.")
        data_l1 = {
            "Acción Principal": ["Pacto de transferencia de información", "Puesta en marcha del SIHT", "Desarrollo dashboard SIHT", "Inventario recursos financieros", "Banco de datos SH", "Observatorio de Inteligencia"],
            "Meta": ["1 Pacto implementado", "100% de desarrollo modelo conceptual v1", "100% de desarrollo del dashboard", "Consolidación avanzada del inventario", "Al menos 90% de implementación", "Al menos 90% de implementación"]
        }
        st.table(pd.DataFrame(data_l1))
        
    elif "Línea 2" in linea:
        st.markdown("**Objetivo:** Construir e implementar una arquitectura de gobernanza multinivel para la gestión corresponsable de la seguridad hídrica, articulando actores públicos, privados, comunitarios, académicos y territoriales.")
        data_l2 = {
            "Acción Principal": ["Gran Pacto por la Seguridad Hídrica", "Diseño y constitución del Consejo", "Formalización de acuerdos de gobernanza", "Constitución de Mesas Temáticas", "Constitución de nodos territoriales"],
            "Meta": ["100% de suscripción (Medellín)", "100% de conformación del consejo", "100% de formalización de compromisos", "100% de conformación de mesas priorizadas", "100% de conformación de nodos priorizados"]
        }
        st.table(pd.DataFrame(data_l2))
        
    elif "Línea 3" in linea:
        st.markdown("**Objetivo:** Diseñar e implementar mecanismos que reconozcan, incentiven y fortalezcan la participación multisectorial, promoviendo la conservación, restauración y la generación de beneficios compartidos.")
        st.markdown("#### Proyecto Sombrilla Destacado: Corredor Vivo Intercuencas Grande – Aburrá - Negro")
        st.info("Meta: 6 km de corredores riparios intervenidos de 10 m de ancho en la cuenca de Río Chico (vereda Zafra).")
        
        data_l3 = {
            "Acción Principal": ["Infraestructura verde y SbN", "Programa Escuela-Taller del Agua (ETAB)", "Campaña 'Conectados por el agua'", "Portafolio Certificación Neutralidad Hídrica", "Ranking de seguridad hídrica territorial"],
            "Meta": ["Plan Estratégico formulado y en marcha", "3 ETABs en marcha", "10 representantes / 25.000 interacciones digitales", "Certificar al menos 90% de organizaciones identificadas al 2028", "100% de entes municipales de AMVA, Norte y Oriente evaluados al 2027"]
        }
        st.table(pd.DataFrame(data_l3))

# PESTAÑA 3: CRONOGRAMA DE EJECUCIÓN
with tab3:
    st.markdown("### Secuencia Temporal de Acciones Priorizadas (2026–2027)")
    st.markdown("La hoja de ruta se organiza en tres fases de desarrollo progresivo:")
    
    col_f1, col_f2, col_f3 = st.columns(3)
    with col_f1:
        st.success("**Fase I: Comprender**\n(0-6 meses)")
    with col_f2:
        st.info("**Fase II: Acordar**\n(6-12 meses)")
    with col_f3:
        st.warning("**Fase III: Hacer**\n(12-18 meses)")
        
    st.markdown("### Visualización de Actividades")
    # Tabla resumen del cronograma basada en el docx
    cronograma_data = {
        "Línea": ["Línea 1", "Línea 1", "Línea 2", "Línea 2", "Línea 3", "Línea 3"],
        "Acción Estratégica": ["Pacto de Información", "Puesta en marcha SIHT", "Gran Pacto SH", "Consejo Territorial", "Corredor Vivo", "Infraestructura Verde y SbN"],
        "Fase I (Comprender)": ["✔", "✔", "✔", "✔", "✔", "✔"],
        "Fase II (Acordar)": ["✔", "✔", "", "", "✔", "✔"],
        "Fase III (Hacer)": ["✔", "✔", "", "", "✔", "✔"]
    }
    st.dataframe(pd.DataFrame(cronograma_data), use_container_width=True)

# PESTAÑA 4: PRESUPUESTO Y RECURSOS
with tab4:
    st.markdown("### Asignación Presupuestal y Requerimientos")
    
    st.markdown("""
    La implementación de este Plan Táctico requiere una inversión estimada de **$19.000 millones COP**, la cual optimizará la inversión distrital del Artículo 41 mediante sinergias interinstitucionales.
    """)
    
    st.markdown("#### Estructura de Personal Técnico a Cargar en Matriz de Recursos:")
    st.markdown("""
    El plan contempla el porcentaje de dedicación y tiempo (en meses) del siguiente equipo interdisciplinario asignado a las acciones tácticas (1.1 a 3.6):
    * Profesional SIG
    * Profesional Ambiental
    * Profesional Forestal
    * Profesional Social
    * Profesional Económico
    * Profesional Comunicaciones
    * Licencias de Software y Cómputo
    """)
    st.info("Nota: Las matrices de asignación analítica de tiempos y porcentajes se encuentran estructuradas en el backend del SIHT-CV para el seguimiento físico-financiero de la Junta Directiva.")
