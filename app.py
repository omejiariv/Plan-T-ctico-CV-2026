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

# Estilos CSS Avanzados
st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; }
    h1, h2, h3 { color: #0F172A; font-family: 'Helvetica Neue', sans-serif; }
    .metric-card {
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        border-top: 4px solid #0284C7;
        text-align: center;
    }
    .metric-val { font-size: 36px; font-weight: 800; color: #0369A1; margin: 10px 0; }
    .vulnerabilidad-box {
        background-color: #FEF2F2;
        border-left: 5px solid #EF4444;
        padding: 15px;
        border-radius: 8px;
        color: #991B1B;
    }
    .lema-box {
        background-color: #F0FDF4;
        border: 1px solid #BBF7D0;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        color: #166534;
        font-weight: 600;
        font-size: 16px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# --- BARRA LATERAL ---
with st.sidebar:
    # 📸 Intenta cargar el logo corporativo desde tu nueva carpeta 'data'
    try:
        st.image("data/Logo CuencaVerde", use_container_width=True)
    except:
        # Imagen de respaldo en caso de que el nombre exacto difiera
        st.image("data/CuencaVerde_Logo.jpg", use_container_width=True)
        
    st.markdown("<h3 style='color:#0369A1; text-align:center;'>Gobernanza Hidro-Territorial</h3>", unsafe_allow_html=True)
    st.markdown("---")
    
    # 📊 CONTROL DE INTERACTIVIDAD DEL SIDEBAR
    modo_vista = st.radio(
        "Enfoque de Visualización:", 
        ["Completo", "Solo Metas Críticas", "Foco Financiero"]
    )
    
    st.markdown("---")
    # 🌟 INTEGRACIÓN DE TU MENSAJE INSTITUCIONAL "WOW"
    st.markdown(f"""
        <div class="lema-box">
            "Juntos, somos más sostenibles, más efectivos, más visibles, más seguros y más fuertes."
        </div>
    """, unsafe_allow_html=True)

# --- ENCABEZADO ---
st.markdown("<p style='color:#0284C7; font-weight:700; text-transform:uppercase; margin-bottom:0;'>Sistema de Inteligencia Hidro-Territorial (SIHT-CV)</p>", unsafe_allow_html=True)
st.markdown("<h1 style='margin-top:0;'>Plan Táctico de Seguridad Hídrica Territorial 2026–2027</h1>", unsafe_allow_html=True)
st.markdown(f"**Vista activa:** Enfoque {modo_vista}")
st.markdown("---")


# --- LÓGICA DE FILTRADO SEGÚN EL SIDEBAR ---

if modo_vista == "Completo":
    tab1, tab2, tab3, tab4 = st.tabs(["🎯 Business Case", "🌿 Líneas de Entrega", "🗺️ Conectividad Ecosistémica", "📈 Inversión y Simulador"])
    
    with tab1:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("### Dependencia Socio-Ecológica Regional")
            st.write("La viabilidad futura del Distrito de Medellín depende de la Región Central funcional (Norte y Oriente).")
            # Mostrar paisaje del norte de Antioquia desde tu carpeta data si está disponible
            try:
                st.image("data/EmbalseRG.jpg", caption="Paisaje de la Región de Influencia - Embalse Río Grande II", use_container_width=True)
            except:
                pass
        with col2:
            st.markdown('<div class="metric-card"><p>PRESUPUESTO TOTAL</p><div class="metric-val">$19.000M</div><p>COP (2026-2027)</p></div>', unsafe_allow_html=True)

    with tab2:
        st.markdown("### Estructura Programática Completa")
        # Aquí va la lógica de las 3 líneas que teníamos antes...
        st.info("Utiliza los componentes para revisar las 3 líneas del Plan Táctico.")

    with tab3:
        st.markdown("### Activos Hidrológicos Críticos")
        map_data = pd.DataFrame({'lat': [6.1130, 6.5160], 'lon': [-75.5030, -75.4670]})
        st.map(map_data, zoom=9)

    with tab4:
        st.markdown("### Optimización del Artículo 41 (Ley 99 de 1993)")
        porcentaje = st.slider("Porcentaje efectivo asignado:", 1.0, 3.0, 1.0, step=0.1)
        st.metric(label="Fondo Disponible Simulado", value=f"${19000 * porcentaje:,.1f}M COP")


elif modo_vista == "Solo Metas Críticas":
    st.markdown("## 🎯 Foco Ejecutivo: Metas Críticas de Entrega")
    st.markdown("Esta vista filtra únicamente las acciones de prioridad alta con impacto directo sobre el territorio:")
    
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.subheader("🌿 Línea 3: Corredor Vivo Intercuencas")
        st.warning("Meta de choque: 6 km de corredores riparios intervenidos (Vereda Zafra - Río Chico).")
        try:
            st.image("data/EmbalseRG1.jpg", caption="Monitoreo de Coberturas en Zonas de Intervención", use_container_width=True)
        except:
            pass
            
    with col_m2:
        st.subheader("💻 Línea 1: Plataforma SIHT-CV")
        st.info("Meta de choque: 100% de despliegue conceptual y primer tablero analítico para toma de decisiones.")

    st.markdown("---")
    st.markdown("#### Matriz de Indicadores Clave")
    data_critica = {
        "Acción Estratégica": ["Pacto de Transferencia de Información", "Gran Pacto por la Seguridad Hídrica", "Escuela-Taller del Agua (ETAB)"],
        "Meta Crítica": ["1 Pacto Interinstitucional implementado", "100% suscripción por actores del Distrito", "3 Escuelas-Taller operando en comunidades rurales"]
    }
    st.table(pd.DataFrame(data_critica))


elif modo_vista == "Foco Financiero":
    st.markdown("## 📈 Foco Analítico: Presupuesto y Apalancamiento")
    st.markdown("Optimización y simulación de la inversión del **Artículo 41 de la Ley 99 de 1993**:")
    
    # Colocar el simulador en un lugar de alta relevancia
    porcentaje_recaudo = st.slider(
        "Ajuste de asignación del Artículo 41 (Mínimo legal 1%):",
        min_value=1.0, max_value=3.0, value=1.2, step=0.1
    )
    
    base_estimada = 19000
    recaudo_simulado = base_estimada * porcentaje_recaudo
    
    c1, c2 = st.columns(2)
    with c1:
        st.metric(label="Presupuesto Base Plan Táctico", value="$19.000M COP")
    with c2:
        st.metric(label="Fondo Escenario Simulado", value=f"${recaudo_simulado:,.1f}M COP", delta=f"${recaudo_simulado - base_estimada:,.1f}M adicionales")
        
    st.markdown("---")
    st.markdown("### Asignación Analítica de Recursos Humanos")
    recursos = ["Profesional SIG", "Profesional Ambiental", "Profesional Forestal", "Profesional Social", "Profesional Económico", "Profesional Comunicaciones"]
    st.dataframe(pd.DataFrame({
        "Perfil Profesional Asignado": recursos, 
        "Rol en Plan Táctico (1.1 a 3.6)": ["Modelación en SIHT", "Estructuración SbN", "Monitoreo Corredores", "Apropiación ETAB", "ROI Financiero", "Estrategia Conectados"]
    }), use_container_width=True, hide_index=True)
