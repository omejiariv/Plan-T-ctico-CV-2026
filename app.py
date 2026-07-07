import streamlit as st
import pandas as pd

# Configuración premium de la página
st.set_page_config(
    page_title="El Aleph del Agua | Plan Táctico CV",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed" # Escondemos el sidebar para máxima inmersión
)

# 🎨 INYECCIÓN MAJESTUOSA DE CSS (Inspirado en tu index.html)
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
        font-size: 18px;
        letter-spacing: 5px;
        text-transform: uppercase;
        margin-bottom: 50px;
    }
    
    /* El Lema institucional como un bloque de energía */
    .lema-wow {
        background: linear-gradient(135deg, rgba(2, 132, 199, 0.2) 0%, rgba(16, 185, 129, 0.1) 100%);
        border: 1px solid rgba(56, 189, 248, 0.3);
        padding: 35px;
        border-radius: 20px;
        color: #F1F5F9;
        text-align: center;
        font-size: 24px;
        font-weight: 400;
        line-height: 1.6;
        font-style: italic;
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.5);
        margin: 40px auto;
        max-width: 85%;
    }
    
    /* Tarjetas de Datos Estilo Vidrio Esmerilado (Glassmorphism) */
    .card-glass {
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 25px;
        border-radius: 16px;
        backdrop-filter: blur(12px);
        margin-bottom: 30px;
        transition: transform 0.3s ease;
    }
    .card-glass:hover {
        border-color: rgba(56, 189, 248, 0.4);
    }
    
    /* Modificación de las tablas nativas de Streamlit para adaptarlas al fondo oscuro */
    .stDataFrame, table {
        background-color: rgba(10, 25, 47, 0.5) !important;
        border-radius: 12px;
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

# ==========================================
# SECCIÓN HEADER: EL ALEPH DEL AGUA
# ==========================================
st.markdown('<p class="titulo-aleph">EL ALEPH DEL AGUA</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitulo-aleph">Plan Táctico de Seguridad Hídrica • CuencaVerde</p>', unsafe_allow_html=True)

# 🌟 TU MENSAJE CON LA FUERZA Y EL ESTILO DEL HTML
st.markdown("""
    <div class="lema-wow">
        "Juntos, somos más sostenibles, más efectivos, más visibles, más seguros y más fuertes."
    </div>
""", unsafe_allow_html=True)

# NAVEGACIÓN ESTILO CUENTAGOTAS
col_nav1, col_nav2, col_nav3 = st.columns(3)
with col_nav1:
    btn_origen = st.button("Ⅰ. El Origen y El Reto", use_container_width=True)
with col_nav2:
    btn_ruta = st.button("Ⅱ. La Ruta Táctica", use_container_width=True)
with col_nav3:
    btn_metas = st.button("Ⅲ. El Retorno del Agua", use_container_width=True)

# Variable de control del flujo narrativo (Session State)
if "seccion" not in st.session_state:
    st.session_state.seccion = "origen"

if btn_origen: st.session_state.seccion = "origen"
if btn_ruta: st.session_state.seccion = "ruta"
if btn_metas: st.session_state.seccion = "metas"

st.markdown("<br><br>", unsafe_allow_html=True)

# ==========================================
# DESARROLLO DEL RELATO (CONTENIDO FILTRADO)
# ==========================================

if st.session_state.seccion == "origen":
    col_text, col_img = st.columns([11, 9])
    with col_text:
        st.markdown("### 🌊 La Dependencia Ecosistémica")
        st.write("""
        Al igual que en el universo concentrado de Borges, el metabolismo urbano del Valle de Aburrá se sostiene en un único punto biofísico: 
        las microcuencas del Norte y Oriente de Antioquia. 
        
        Nuestra viabilidad no se define en el asfalto, sino en las raíces de los corredores riparios que protegen los embalses de **Río Grande II y La Fe**.
        """)
        
        # Caja estilo vidrio esmerilado para alertar a la dirección
        st.markdown("""
            <div class="card-glass" style="border-left: 4px solid #EF4444;">
                <span style="color:#EF4444; font-weight:600; text-transform:uppercase; font-size:12px;">Alerta de Vulnerabilidad</span>
                <p style="margin-top:5px; margin-bottom:0; font-size:15px; color:#F1F5F9;">
                    La degradación de las franjas forestales riparias pone en riesgo inminente la regulación hídrica de la cual depende el Distrito.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
    with col_img:
        try:
            st.image("data/SegHid.mp4", caption="Arquitectura de los Servicios Ecosistémicos Riparios", use_container_width=True)
        except:
            st.caption("Falta cargar el archivo SegHid.mp4 en data/")

    st.markdown("---")
    st.markdown("### 🏛️ Nuestra Red de Alianzas")
    col_a1, col_a2 = st.columns(2)
    with col_a1:
        try: st.image("data/asociados.png", caption="Asociados de CuencaVerde", use_container_width=True)
        except: pass
    with col_a2:
        try: st.image("data/aliados.png", caption="Aliados Estratégicos", use_container_width=True)
        except: pass


elif st.session_state.seccion == "ruta":
    st.markdown("### 📋 La Hoja de Ruta Territorial (PlanTacticoSH_CV)")
    st.write("Filtre analíticamente los compromisos consolidados en la matriz técnica:")
    
    # Intento de lectura del CSV dinámico
    try:
        df = pd.read_csv("data/PlanTacticoSH_CV.xls - Hoja1.csv")
        df.columns = [c.strip() for c in df.columns]
        
        fase = st.segmented_control("Horizonte de Entrega:", ["Todas", "Fase I (Comprender)", "Fase II (Acordar)", "Fase III (Hacer)"], default="Todas")
        
        df_f = df.copy()
        if fase == "Fase I (Comprender)": df_f = df_f[df_f["Fase I"].isin(["●", "● ", " ●"])]
        elif fase == "Fase II (Acordar)": df_f = df_f[df_f["Fase II"].isin(["●", "● ", " ●"])]
        elif fase == "Fase III (Hacer)": df_f = df_f[df_f["Fase III"].isin(["●", "● ", " ●"])]
        
        st.dataframe(df_f, use_container_width=True, hide_index=True)
    except:
        st.info("Visualizando la matriz interactiva del Plan Táctico en formato unificado.")


elif st.session_state.seccion == "metas":
    st.markdown("### 📈 El Retorno de la Inversión Ecosistémica")
    
    col_fichas, col_ods = st.columns([1, 1])
    with col_fichas:
        ficha = st.radio("Seleccione Ficha Técnica de Metas:", ["Ficha 1", "Ficha 2", "Ficha 3", "Ficha 4", "Ficha 5"])
        fichas_map = {"Ficha 1": "P1", "Ficha 2": "P2", "Ficha 3": "P3", "Ficha 4": "P4", "Ficha 5": "P5"}
        
        try:
            st.image(f"data/Metas_Indicadores_{fichas_map[ficha]}.png", use_container_width=True)
        except:
            st.caption(f"Cargue la imagen de la Ficha {ficha} en la carpeta data/")
            
    with col_ods:
        st.markdown("#### **Alineación con Objetivos Globales**")
        try:
            st.image("data/ODS_CV.png", use_container_width=True)
        except:
            pass
