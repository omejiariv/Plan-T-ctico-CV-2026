import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN PREMIUM DE LA PÁGINA
st.set_page_config(
    page_title="El Aleph del Agua | Plan Táctico CV",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded" # Cambiado a expandido para asegurar visibilidad del logo
)

# 2. INYECCIÓN AVANZADA DE CSS (Inspirado en TNC, WWF y tu index.html)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Montserrat:wght@300;400;600&display=swap');
    
    /* Configuración de fondo oscuro y tipografía global */
    .stApp {
        background: linear-gradient(180deg, #050B14 0%, #0A192F 100%);
        color: #E2E8F0;
        font-family: 'Montserrat', sans-serif;
    }
    
    /* Títulos poéticos estilo Cinzel */
    .titulo-aleph {
        font-family: 'Cinzel', serif;
        color: #F8FAFC;
        text-align: center;
        font-size: 42px;
        letter-spacing: 3px;
        margin-top: 20px;
        text-shadow: 0 0 20px rgba(56, 189, 248, 0.4);
    }
    
    .subtitulo-aleph {
        font-family: 'Montserrat', sans-serif;
        font-weight: 300;
        color: #38BDF8;
        text-align: center;
        font-size: 16px;
        letter-spacing: 5px;
        text-transform: uppercase;
        margin-bottom: 40px;
    }
    
    /* Bloque del Lema Institucional */
    .lema-wow {
        background: linear-gradient(135deg, rgba(2, 132, 199, 0.15) 0%, rgba(16, 185, 129, 0.08) 100%);
        border: 1px solid rgba(56, 189, 248, 0.25);
        padding: 30px;
        border-radius: 20px;
        color: #F1F5F9;
        text-align: center;
        font-size: 22px;
        font-weight: 400;
        line-height: 1.6;
        font-style: italic;
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.4);
        margin: 30px auto;
        max-width: 85%;
    }
    
    /* Tarjetas de Datos Estilo Vidrio Esmerilado (Glassmorphism) */
    .card-glass {
        background: rgba(15, 23, 42, 0.65);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 25px;
        border-radius: 16px;
        backdrop-filter: blur(12px);
        margin-bottom: 25px;
    }
    
    /* Customización de botones de navegación */
    div.stButton > button {
        background-color: transparent;
        color: #38BDF8;
        border: 1px solid #38BDF8;
        padding: 10px 24px;
        border-radius: 30px;
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        letter-spacing: 1px;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #38BDF8;
        color: #050B14;
        box-shadow: 0 0 15px rgba(56, 189, 248, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# 3. BARRA LATERAL (Para mantener el Logo de CuencaVerde SIEMPRE visible)
with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    try:
        # Forzamos el uso del archivo oficial solicitado
        st.image("data/Logo CuencaVerde.jpg", use_container_width=True)
    except:
        try:
            st.image("data/CuencaVerde Logo.jpg", use_container_width=True)
        except:
            st.markdown("<h2 style='color:#38BDF8; text-align:center;'>💧 CuencaVerde</h2>", unsafe_allow_html=True)
            
    st.markdown("<p style='text-align:center; font-size:12px; color:#64748B;'>Orquestador Hidro-Territorial</p>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 🏛️ Control de Sesión")
    st.info("Navegue utilizando las pestañas superiores principales de la pantalla.")

# 4. ENCABEZADO Y RELATO NARRATIVO
st.markdown('<p class="titulo-aleph">EL ALEPH DEL AGUA</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo-aleph">Plan Táctico de Seguridad Hídrica • CuencaVerde</p>', unsafe_allow_html=True)

# 🌟 TU LEMA INSTITUCIONAL REFORZADO
st.markdown("""
    <div class="lema-wow">
        "Juntos, somos más sostenibles, más efectivos, más visibles, más seguros y más fuertes. MC De la Ossa Posada"
    </div>
""", unsafe_allow_html=True)

# 5. PESTAÑAS PRINCIPALES DEL NARRATIVO
tab_origen, tab_ruta, tab_metas = st.tabs([
    "Ⅰ. El Origen y El Reto", 
    "Ⅱ. La Ruta Táctica (PlanTacticoSH_CV)", 
    "Ⅲ. El Retorno del Agua"
])

# ==========================================
# PESTAÑA I: EL ORIGEN Y EL RETO
# ==========================================
with tab_origen:
    # Mostramos el Embalse de manera visible en la cabecera de la sección
    try:
        st.image("data/EmbalseRG.jpg", caption="Ecosistema Estratégico Abastecedor - Región Central Funcional de Antioquia", use_container_width=True)
    except:
        try:
            st.image("data/EmbalseRG.png", caption="Ecosistema Estratégico Abastecedor - Región Central Funcional de Antioquia", use_container_width=True)
        except:
            pass

    col_text, col_video = st.columns([10, 10])
    
    with col_text:
        st.markdown("### 🌊 Dependencia Socio-Ecológica")
        st.write("""
        El metabolismo urbano del Distrito de Medellín depende críticamente de cuencas e infraestructuras ecológicas externas localizadas en el Norte y Oriente de Antioquia. 
        Los sistemas reguladores de **Río Grande II y La Fe** sostienen la vida de la ciudad.
        """)
        
        st.markdown("""
            <div class="card-glass" style="border-left: 4px solid #F59E0B;">
                <span style="color:#F59E0B; font-weight:600; text-transform:uppercase; font-size:11px;">Rigor Científico y Calidad (4C)</span>
                <p style="margin-top:5px; margin-bottom:0; font-size:14px; color:#E2E8F0;">
                    CuencaVerde opera bajo estándares globales como Fondo de Agua ágil, integrando la gobernanza multinivel para mitigar el riesgo ecosistémico.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with col_video:
        st.markdown("#### **🎥 Materialización de la Visión Táctica**")
        try:
            # Integración nativa del video solicitado reemplazando el esquema anterior
            st.video("data/SegHid.mp4")
        except:
            st.warning("Subiendo archivo de video 'SegHid.mp4' a la carpeta data/...")

# ==========================================
# PESTAÑA II: LA RUTA TÁCTICA
# ==========================================
with tab_ruta:
    st.markdown("### 📋 Cuadro de Mando Interactivo (PlanTacticoSH_CV)")
    st.write("Filtre y explore de forma interactiva las acciones de prioridad alta extraídas de la matriz técnica oficial:")
    
    # Lectura automatizada del archivo consolidado
    try:
        df_matriz = pd.read_csv("data/PlanTacticoSH_CV.xls - Hoja1.csv")
        df_matriz.columns = [c.strip() for c in df_matriz.columns]
        
        col_filtro1, col_filtro2 = st.columns(2)
        with col_filtro1:
            lineas = ["Todas"] + list(df_matriz["Línea Estratégica"].dropna().unique())
            sel_linea = st.selectbox("Seleccione la Línea Programática:", lineas)
        with col_filtro2:
            sel_fase = st.segmented_control("Horizonte Temporal de Entrega:", ["Todas", "Fase I (Comprender)", "Fase II (Acordar)", "Fase III (Hacer)"], default="Todas")
            
        # Filtrado lógico analítico
        df_f = df_matriz.copy()
        if sel_linea != "Todas":
            df_f = df_f[df_f["Línea Estratégica"] == sel_linea]
            
        if sel_fase == "Fase I (Comprender)": df_f = df_f[df_f["Fase I"].isin(["●", "● ", " ●"])]
        elif sel_fase == "Fase II (Acordar)": df_f = df_f[df_f["Fase II"].isin(["●", "● ", " ●"])]
        elif sel_fase == "Fase III (Hacer)": df_f = df_f[df_f["Fase III"].isin(["●", "● ", " ●"])]
        
        st.dataframe(df_f, use_container_width=True, hide_index=True)
        
    except:
        st.info("Estructurando la base de datos de la matriz del Plan Táctico en el servidor...")

# ==========================================
# PESTAÑA III: EL RETORNO DEL AGUA
# ==========================================
with tab_metas:
    st.markdown("### 📈 Indicadores de Impacto y Retorno Ecosistémico")
    
    col_fichas, col_ods = st.columns([1, 1])
    
    with col_fichas:
        st.markdown("#### **Fichas Técnicas del SIHT-CV**")
        ficha = st.radio("Seleccione el componente de monitoreo a proyectar:", ["Ficha 1", "Ficha 2", "Ficha 3", "Ficha 4", "Ficha 5"])
        fichas_map = {"Ficha 1": "P1", "Ficha 2": "P2", "Ficha 3": "P3", "Ficha 4": "P4", "Ficha 5": "P5"}
        
        try:
            st.image(f"data/Metas_Indicadores_{fichas_map[ficha]}.png", use_container_width=True)
        except:
            pass
            
    with col_ods:
        st.markdown("#### **🌍 Alineación con Objetivos Globales**")
        st.write("Mapeo metodológico de intervenciones en la Estructura Ecológica Principal frente a las metas globales de sostenibilidad:")
        
        # Reducción a la mitad utilizando control fino de columnas en Streamlit
        col_sub_dim, _ = st.columns([1, 1]) 
        with col_sub_dim:
            try:
                st.image("data/ODS_CV.png", caption="Metas e Indicadores ODS Asociados", use_container_width=True)
            except:
                pass
