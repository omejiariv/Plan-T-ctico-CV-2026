import streamlit as st
import pandas as pd
import numpy as np

# Configuración avanzada de la página
st.set_page_config(
    page_title="SIHT-CV | Plan Táctico CuencaVerde",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS Avanzados para emular un Dashboard de Inteligencia Hidro-Territorial
st.markdown("""
    <style>
    /* Cambiar fondo y tipografías */
    .stApp { background-color: #F8FAFC; }
    h1, h2, h3 { color: #0F172A; font-family: 'Helvetica Neue', sans-serif; }
    
    /* Contenedores destacados (Cards) */
    .metric-card {
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);
        border-top: 4px solid #0284C7;
        text-align: center;
    }
    .metric-val { font-size: 36px; font-weight: 800; color: #0369A1; margin: 10px 0; }
    
    /* Alertas customizadas */
    .vulnerabilidad-box {
        background-color: #FEF2F2;
        border-left: 5px solid #EF4444;
        padding: 15px;
        border-radius: 8px;
        color: #991B1B;
    }
    </style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL (Identidad Institucional) ---
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?auto=format&fit=crop&w=400&q=80", use_container_width=True)
    st.markdown("<h2 style='color:#0369A1; text-align:center;'>CuencaVerde</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-style:italic;'>Orquestador Hidro-Territorial</p>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("### 🏛️ Control de Gobernanza")
    st.caption("Seguimiento de Metas, ROI Ecosistémico y Distribución de Recursos del Art. 41 para la Junta Directiva.")
    
    # Selector de visualización global para la Junta
    modo_vista = st.radio("Enfoque de Visualización:", ["Completo", "Solo Metas Críticas", "Foco Financiero"])

# --- ENCABEZADO ---
st.markdown("<p style='color:#0284C7; font-weight:700; text-transform:uppercase; margin-bottom:0;'>Sistema de Inteligencia Hidro-Territorial (SIHT-CV)</p>", unsafe_allow_html=True)
st.markdown("<h1 style='margin-top:0;'>Plan Táctico de Seguridad Hídrica Territorial 2026–2027</h1>", unsafe_allow_html=True)
st.markdown("---")

# --- PESTAÑAS INTERACTIVAS ---
tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 Business Case", 
    "🌿 Líneas de Entrega Táctica", 
    "🗺️ Conectividad Ecosistémica", 
    "📈 Inversión y Simulador"
])

# PESTAÑA 1: BUSINESS CASE
with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### Dependencia Socio-Ecológica Regional")
        st.write("""
        La viabilidad futura del Distrito de Medellín no puede depender exclusivamente de las fronteras de su infraestructura urbana. 
        Este Plan Táctico reconoce formalmente la **dependencia funcional con las regiones del Norte y Oriente de Antioquia**, cuyos ecosistemas sostienen el metabolismo urbano regional.
        """)
        st.markdown("""
        > **Visión Sistémica:** *«Cuencas Saludables, Ciudades Resilientes»*, operando bajo un modelo ágil de Fondo de Agua que garantiza el rigor científico y la calidad (4C).
        """)
    
    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <p style="color:#64748B; font-weight:600; margin:0;">PRESUPUESTO TOTAL ESTIMADO</p>
                <div class="metric-val">$19.000M</div>
                <p style="color:#0284C7; font-weight:500; margin:0;">COP Asignados (2026-2027)</p>
            </div>
        """, unsafe_allow_html=True)
        
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        <div class="vulnerabilidad-box">
            <strong>⚠️ Alerta de Vulnerabilidad Estructural:</strong> Gestión prioritaria sobre el riesgo crítico en el suministro de los embalses reguladores <strong>La Fe</strong> y <strong>Río Grande II</strong>, junto a sus microcuencas abastecedoras rurales.
        </div>
    """, unsafe_allow_html=True)

# PESTAÑA 2: LÍNEAS DE ENTREGA TÁCTICA
with tab2:
    st.markdown("### Estructura Programática de Entrega")
    
    linea_opt = st.segmented_control(
        "Seleccione la Línea Estratégica a evaluar:",
        options=["Línea 1: Inteligencia", "Línea 2: Gobernanza", "Línea 3: Intervenciones"],
        default="Línea 1: Inteligencia"
    )
    
    if "Línea 1" in linea_opt:
        st.markdown("#### Línea 1: Gestión del conocimiento e inteligencia Socio-ecológica")
        st.caption("Objetivo: Plataforma tecnológica multinivel para modelación socioecológica en tiempo real.")
        
        l1_data = {
            "Acción Táctica Clave": ["Puesta en marcha del SIHT-CV", "Dashboard de Toma de Decisiones", "Observatorio de Inteligencia"],
            "Indicador": ["Nivel de desarrollo del SIHT-CV", "Nivel de desarrollo del Dashboard", "Nivel de implementación"],
            "Meta Táctica (Años 1-2)": ["100% modelo conceptual y v1", "100% de despliegue del tablero", "Al menos 90% de operatividad"]
        }
        st.table(pd.DataFrame(l1_data))
        
    elif "Línea 2" in linea_opt:
        st.markdown("#### Línea 2: Articulación multisectorial para la gobernanza multinivel")
        st.caption("Objetivo: Construcción de una arquitectura de gobernanza corresponsable y multiescala.")
        
        l2_data = {
            "Acción Táctica Clave": ["Gran Pacto por la Seguridad Hídrica", "Consejo de Seguridad Hídrica", "Mesas Temáticas Especializadas"],
            "Indicador": ["Nivel de suscripción", "Nivel de conformación", "Número de mesas constituidas"],
            "Meta Táctica (Años 1-2)": ["100% firmado por actores en Medellín", "100% de la instancia instalada", "100% de mesas priorizadas en marcha"]
        }
        st.table(pd.DataFrame(l2_data))
        
    elif "Línea 3" in linea_opt:
        st.markdown("#### Línea 3: Intervenciones con propósito y retorno")
        st.caption("Objetivo: Acciones en territorio con retornos ecosistémicos verificables.")
        
        col_c1, col_c2 = st.columns(2)
        with col_c1:
            st.metric(label="Proyecto Sombrilla: Corredor Vivo Intercuencas", value="6 Km lineales", delta="10m de ancho de ronda ripariana")
        with col_c2:
            st.metric(label="Programa Escuela-Taller del Agua", value="3 ETABs", delta="Comunidades rurales articuladas")
            
        l3_data = {
            "Acción Táctica Clave": ["Infraestructura verde (SbN / AbE)", "Certificación de Neutralidad Hídrica", "Ranking de Seguridad Hídrica"],
            "Meta Táctica (Años 1-2)": ["Plan Estratégico e intervenciones formuladas", "90% de empresas meta certificadas al 2028", "100% de municipios del Valle de Aburrá, Norte y Oriente evaluados al 2027"]
        }
        st.dataframe(pd.DataFrame(l3_data), use_container_width=True, hide_index=True)

# PESTAÑA 3: CONECTIVIDAD ECOSISTÉMICA (EL MAPA "WOW")
with tab3:
    st.markdown("### Mapa de Intervenciones y Activos Hidrológicos Críticos")
    st.write("Visualización espacial de los nodos estratégicos que sostienen la resiliencia de la Región Central:")
    
    # Coordenadas aproximadas de la zona de influencia para desplegar el mapa nativo
    map_data = pd.DataFrame({
        'lat': [6.1130, 6.5160, 6.4350], # La Fe, Río Grande II, Río Chico (Zafra)
        'lon': [-75.5030, -75.4670, -75.5840],
        'Ubicación': ['Embalse La Fe (Abastecimiento Oriente)', 'Embalse Río Grande II (Abastecimiento Norte)', 'Corredor Vivo Río Chico (Vereda Zafra - Intervención 6km)']
    })
    
    st.map(map_data, zoom=9, use_container_width=True)
    st.caption("Los puntos representan la infraestructura ecológica externa clave priorizada en la Fase I (Comprender).")

# PESTAÑA 4: INVERSIÓN Y SIMULADOR
with tab4:
    st.markdown("### Optimización del Artículo 41 (Ley 99 de 1993)")
    st.write("Use el simulador interactivo para evaluar escenarios de apalancamiento financiero según el recaudo distrital:")
    
    # Componente interactivo (Slider)
    porcentaje_recaudo = st.slider(
        "Porcentaje efectivo asignado de los Ingresos Corrientes del Distrito (Mínimo de ley: 1%):",
        min_value=1.0, max_value=3.0, value=1.0, step=0.1
    )
    
    # Cálculo dinámico hipotético para impresionar con datos adaptativos
    base_estimada = 19000  # millones
    recaudo_simulado = base_estimada * porcentaje_recaudo
    
    c_inv1, c_inv2 = st.columns(2)
    with c_inv1:
        st.metric(label="Inversión Base Plan Táctico", value="$19.000M COP")
    with c_inv2:
        st.metric(label="Fondo Disponible Simulado", value=f"${recaudo_simulado:,.1f}M COP", delta=f"${recaudo_simulado - base_estimada:,.1f}M adicionales")
        
    st.markdown("---")
    st.markdown("#### Matriz Interdisciplinaria de Recursos")
    st.write("Personal asignado para el monitoreo físico-financiero trimestral a través del SIHT-CV:")
    
    recursos = ["Profesional SIG", "Profesional Ambiental", "Profesional Forestal", "Profesional Social", "Profesional Económico", "Profesional Comunicaciones"]
    st.dataframe(pd.DataFrame({"Perfil Profesional": recursos, "Dedicación Asignada": ["100% en SIHT", "Acompañamiento SbN", "Monitoreo Corredores", "Apropiación ETAB", "Análisis Financiero", "Campaña Conectados por el Agua"]}), use_container_width=True, hide_index=True)
