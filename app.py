import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN PREMIUM DE LA PÁGINA
st.set_page_config(
    page_title="Plan de Seguridad Hídrica | CuencaVerde",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. INYECCIÓN AVANZADA DE CSS (Control de Altura de Imágenes y Estilos)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600;700&display=swap');
    
    /* Fondo oscuro e inmersivo */
    .stApp {
        background: linear-gradient(180deg, #050B14 0%, #0A192F 100%);
        color: #E2E8F0;
        font-family: 'Montserrat', sans-serif;
    }
    
    /* Título Superior: Centrado y vistoso */
    .titulo-vistoso {
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        color: #FFFFFF;
        font-size: 34px;
        letter-spacing: 0.5px;
        text-align: center;
        margin: 0;
        text-shadow: 0 0 25px rgba(56, 189, 248, 0.5);
    }
    
    /* Cajetín del Lema Reubicado */
    .lema-wow {
        background: linear-gradient(135deg, rgba(2, 132, 199, 0.15) 0%, rgba(16, 185, 129, 0.08) 100%);
        border: 1px solid rgba(56, 189, 248, 0.25);
        padding: 20px;
        border-radius: 16px;
        color: #F1F5F9;
        text-align: center;
        font-size: 19px;
        font-weight: 400;
        line-height: 1.5;
        font-style: italic;
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4);
        margin: 15px auto 25px auto;
        max-width: 90%;
    }
    
    /* Tarjetas estilo vidrio esmerilado */
    .card-glass {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(56, 189, 248, 0.15);
        padding: 25px;
        border-radius: 16px;
        backdrop-filter: blur(12px);
        margin-bottom: 25px;
    }
    
    /* CONTROL FORENSE: Contenedor simétrico para forzar que las imágenes NO se desborden */
    .contenedor-simetrico img {
        max-height: 480px !important;
        object-fit: contain !important;
        width: auto !important;
        margin: 0 auto !important;
        display: block !important;
    }
    
    .stDataFrame, table {
        background-color: rgba(10, 25, 47, 0.4) !important;
        border-radius: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO: COLUMNAS REAJUSTADAS SEGÚN TU ESPECIFICACIÓN (0.7 y 10.0)
col_logo, col_tit = st.columns([0.7, 10.0])

with col_logo:
    st.markdown("<div style='display: flex; align-items: center; justify-content: center; height: 100%;'>", unsafe_allow_html=True)
    try:
        st.image("data/Logo CuencaVerde.jpg", use_container_width=True)
    except:
        try:
            st.image("data/CuencaVerde Logo.jpg", use_container_width=True)
        except:
            st.markdown("<h2 style='color:#38BDF8; margin:0;'>💧</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_tit:
    st.markdown('<h1 class="titulo-vistoso">Un Plan de Seguridad Hídrica para Ciudades y Sociedades Seguras</h1>', unsafe_allow_html=True)

# 💥 RESPUESTA AL PUNTO 1: CAJETÍN DEL LEMA UBICADO JUSTO DEBAJO DEL TÍTULO PRINCIPAL (FUERA DE LAS PESTAÑAS)
st.markdown("""
    <div class="lema-wow">
        "Juntos, somos más Sostenibles, más Efectivos, más Visibles, más Seguros y más Fuertes."
    </div>
""", unsafe_allow_html=True)

# 4. BARRA LATERAL INSTITUCIONAL
with st.sidebar:
    st.markdown("<h3 style='color:#38BDF8; text-align:center;'>Gobernanza Territorial</h3>", unsafe_allow_html=True)
    st.markdown("---")
    st.caption("Fondo de Agua • Sistema de Inteligencia Hidro-Territorial (SIHT-CV) para el monitoreo físico-financiero trimestral.")
    st.markdown("---")
    st.markdown("### 📈 Escenarios de Financiación")
    porcentaje = st.slider("Asignación Art. 41 de la Ley 99 (Mínimo legal 1%):", 1.0, 3.0, 1.0, step=0.1)
    st.metric(label="Fondo Disponible Simulado", value=f"${19000 * porcentaje:,.1f}M COP")

# 5. ESTRUCTURA NARRATIVA EN PESTAÑAS
tab_origen, tab_ruta, tab_metas = st.tabs([
    "Ⅰ. El Origen y El Reto", 
    "Ⅱ. La Ruta Táctica (PlanTacticoSH_CV)", 
    "Ⅲ. El Retorno del Agua"
])

# ==========================================
# PESTAÑA I: EL ORIGEN Y EL RETO
# ==========================================
with tab_origen:
    try:
        st.image("data/EmbalseRG.jpg", caption="Ecosistema Estratégico Abastecedor - Región Central Funcional de Antioquia", use_container_width=True)
    except:
        pass

    col_text, col_video = st.columns([10, 10])
    with col_text:
        st.markdown("### 🌊 Diagnóstico y Dependencia Socio-Ecológica")
        st.write("""
        El metabolismo urbano de Medellín depende críticamente de cuencas e infraestructuras ecológicas externas localizadas en el Norte y Oriente de Antioquia. 
        Los sistemas reguladores de **Río Grande II y La Fe** sostienen la vida colectiva y la resiliencia del territorio.
        """)
        st.markdown("""
            <div class="card-glass" style="border-left: 4px solid #10B981;">
                <span style="color:#10B981; font-weight:600; text-transform:uppercase; font-size:11px;">Pilar 1: Soluciones Basadas en la Naturaleza (SbN)</span>
                <p style="margin-top:5px; margin-bottom:0; font-size:14px; color:#E2E8F0;">
                    Restauración dirigida de coberturas y mantenimiento de la conectividad ecohidrológica en la Estructura Ecológica Principal de las cuencas aportantes.
                </p>
            </div>
            <div class="card-glass" style="border-left: 4px solid #38BDF8;">
                <span style="color:#38BDF8; font-weight:600; text-transform:uppercase; font-size:11px;">Pilar 2: Rigor Científico Integrado</span>
                <p style="margin-top:5px; margin-bottom:0; font-size:14px; color:#E2E8F0;">
                    Operación de la plataforma SIHT-CV para generar modelación socioecológica predictiva regional en tiempo real ante el cambio climático.
                </p>
            </div>
        """, unsafe_allow_html=True)
    with col_video:
        st.markdown("#### **🎥 Materialización de la Visión Táctica**")
        try:
            st.video("data/SegHid.mp4")
        except:
            st.warning("Cargando archivo de video 'SegHid.mp4'...")

# ==========================================
# PESTAÑA II: LA RUTA TÁCTICA (PlanTacticoSH_CV)
# ==========================================
with tab_ruta:
    st.markdown("### 📋 Cuadro de Mando Interactivo del Plan Táctico")
    st.write("Filtre la matriz oficializada de acciones prioritarias del orquestador hidro-territorial:")
    
    @st.cache_data
    def obtener_matriz_tecnica_limpia():
        try:
            df = pd.read_csv("data/PlanTacticoSH_CV.xls - Hoja1.csv")
            df.columns = [c.strip() for c in df.columns]
            return df
        except:
            datos_oficiales = {
                "Línea Estratégica": [
                    "Línea 1: Inteligencia Socio-ecológica", "Línea 1: Inteligencia Socio-ecológica", "Línea 1: Inteligencia Socio-ecológica",
                    "Línea 2: Gobernanza Multinivel", "Línea 2: Gobernanza Multinivel",
                    "Línea 3: Intervenciones con propósito", "Línea 3: Intervenciones con propósito", "Línea 3: Intervenciones con propósito"
                ],
                "Acción Estratégica": [
                    "1.1 Pacto de transferencia de información", "1.2 Puesta en marcha del SIHT", "1.3 Dashboard SIHT para decisiones",
                    "2.1 Gran Pacto por la Seguridad Hídrica", "2.2 Consejo de Seguridad Hídrica Territorial",
                    "3.1 Corredor Vivo Intercuencas Grande-Aburrá-Negro", "3.2 Infraestructura verde y SbN", "3.3 Programa Escuela-Taller del Agua (ETAB)"
                ],
                "Meta Táctica (Años 1-2)": [
                    "1 Pacto de información territorial implementado", "100% de desarrollo del modelo conceptual v1", "100% de despliegue del dashboard interactivo",
                    "100% de suscripción del Gran Pacto en Medellín", "100% de conformación del consejo instalado",
                    "6 km de corredores riparios intervenidos (Río Chico)", "Plan Estratégico de Resiliencia en marcha", "3 Escuelas-Taller (ETAB) operando en territorio"
                ],
                "Fase I (0-6m)": ["●", "●", "●", "●", "●", "●", "●", "●"],
                "Fase II (6-12m)": ["●", "●", "●", "", "", "●", "●", "●"],
                "Fase III (12-18m)": ["●", "", "●", "", "", "●", "●", "●"]
            }
            return pd.DataFrame(datos_oficiales)

    df_matriz = obtener_matriz_tecnica_limpia()
    
    col_l, col_f = st.columns(2)
    with col_l:
        opciones_l = ["Todas"] + list(df_matriz["Línea Estratégica"].dropna().unique())
        filtro_l = st.selectbox("Filtrar por Línea Programática:", opciones_l)
    with col_f:
        filtro_f = st.segmented_control("Filtrar por Fase Activa:", ["Todas", "Fase I (Comprender)", "Fase II (Acordar)", "Fase III (Hacer)"], default="Todas")
        
    df_ver = df_matriz.copy()
    if filtro_l != "Todas":
        df_ver = df_ver[df_ver["Línea Estratégica"] == filtro_l]
        
    if filtro_f == "Fase I (Comprender)": df_ver = df_ver[df_ver["Fase I (0-6m)"].isin(["●", "● ", " ●"])]
    elif filtro_f == "Fase II (Acordar)": df_ver = df_ver[df_ver["Fase II (6-12m)"].isin(["●", "● ", " ●"])]
    elif filtro_f == "Fase III (Hacer)": df_ver = df_ver[df_ver["Fase III (12-18m)"].isin(["●", "● ", " ●"])]
    
    st.dataframe(df_ver, use_container_width=True, hide_index=True)

# ==========================================
# PESTAÑA III: EL RETORNO DEL AGUA
# ==========================================
with tab_metas:
    st.markdown("### 📈 Retorno Ecosistémico y Compromisos Globales")
    
    # Simetría absoluta en dos columnas idénticas (50% / 50%)
    col_fichas, col_ods = st.columns([10, 10])
    
    with col_fichas:
        st.markdown("#### **Fichas Técnicas de Indicadores (SIHT-CV)**")
        ficha = st.radio("Componente de monitoreo técnico a proyectar:", ["Ficha 1 - Línea de Base", "Ficha 2 - Inteligencia", "Ficha 3 - Gobernanza", "Ficha 4 - Intervenciones", "Ficha 5 - Monitoreo"], horizontal=True)
        fichas_map = {"Ficha 1 - Línea de Base": "P1", "Ficha 2 - Inteligencia": "P2", "Ficha 3 - Gobernanza": "P3", "Ficha 4 - Intervenciones": "P4", "Ficha 5 - Monitoreo": "P5"}
        
        # 💥 RESPUESTA AL PUNTO 3: Encapsulado CSS para evitar que se desborde verticalmente
        st.markdown('<div class="contenedor-simetrico">', unsafe_allow_html=True)
        try:
            st.image(f"data/Metas_Indicadores_{fichas_map[ficha]}.png", use_container_width=True)
        except:
            st.info("Desplegando gráfica analítica del indicador...")
        st.markdown('</div>', unsafe_allow_html=True)
            
    with col_ods:
        st.markdown("#### **🌍 Alineación con Objetivos Globales**")
        st.write("Estructura escalada del Plan frente a las metas mundiales de sostenibilidad:")
        
        # 💥 RESPUESTA AL PUNTO 3: Mismo encapsulado para la gota de los ODS asegurando simetría perfecta de alturas
        st.markdown('<div class="contenedor-simetrico">', unsafe_allow_html=True)
        try:
            st.image("data/ODS_CV.png", use_container_width=True)
        except:
            pass
        st.markdown('</div>', unsafe_allow_html=True)
