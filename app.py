import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. CONFIGURACIÓN PREMIUM DE LA PÁGINA
st.set_page_config(
    page_title="Plan de Seguridad Hídrica | CuencaVerde",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. INYECCIÓN AVANZADA DE CSS (Control Estricto de Redimensionamiento y Simetría)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap');
    
    /* Fondo oscuro e inmersivo */
    .stApp {
        background: linear-gradient(180deg, #050B14 0%, #0A192F 100%);
        color: #E2E8F0;
        font-family: 'Montserrat', sans-serif;
    }
    
    /* Textos generales */
    p, li, span, label {
        font-size: 16.5px !important;
        line-height: 1.6 !important;
        font-weight: 400;
        color: #E2E8F0;
    }
    
    .block-container {
        padding-top: 2.5rem !important;
        padding-bottom: 1rem !important;
    }
    
    .header-bloque {
        text-align: center;
        padding-top: 15px;
        margin-bottom: 20px;
    }
    
    .titulo-vistoso {
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        color: #FFFFFF;
        font-size: 32px;
        letter-spacing: -0.5px;
        margin: 0;
        text-shadow: 0 0 25px rgba(56, 189, 248, 0.4);
    }
    
    .subtitulo-lema {
        font-family: 'Montserrat', sans-serif;
        font-weight: 400;
        color: #38BDF8;
        font-size: 18.5px;
        font-style: italic;
        margin-top: 12px;
        letter-spacing: 0.3px;
    }
    
    .card-glass {
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(56, 189, 248, 0.15);
        padding: 25px;
        border-radius: 16px;
        backdrop-filter: blur(12px);
        margin-bottom: 25px;
    }
    
    /* 💥 RESPUESTA AL PUNTO 1: Blindaje CSS para que todas las fichas midan EXACTAMENTE lo mismo sin deformar el layout */
    .contenedor-ficha-fija img {
        height: 380px !important;
        width: 100% !important;
        object-fit: fill !important;
        border-radius: 12px;
        display: block !important;
        margin: 0 auto !important;
    }
    
    /* Contenedor simétrico para la gota de los ODS */
    .contenedor-ods-fijo img {
        height: 380px !important;
        object-fit: contain !important;
        width: auto !important;
        margin: 0 auto !important;
        display: block !important;
    }
    
    .stDataFrame, table {
        background-color: rgba(10, 25, 47, 0.4) !important;
        border-radius: 12px;
    }
    
    .link-sihclim {
        color: #38BDF8;
        font-weight: 600;
        text-decoration: none;
    }
    </style>
""", unsafe_allow_html=True)

# 3. ENCABEZADO INTEGRADO: LOGO (0.7) Y TÍTULO + LEMA EN BLOQUE UNIFICADO (10.0)
col_logo, col_tit = st.columns([0.7, 10.0])

with col_logo:
    st.markdown("<div style='display: flex; align-items: center; justify-content: center; height: 100%; padding-top: 15px;'>", unsafe_allow_html=True)
    try:
        st.image("data/Logo CuencaVerde.jpg", use_container_width=True)
    except:
        try:
            st.image("data/CuencaVerde Logo.jpg", use_container_width=True)
        except:
            st.markdown("<h2 style='color:#38BDF8; margin:0;'>💧</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col_tit:
    st.markdown("""
        <div class="header-bloque">
            <div class="titulo-vistoso">Un Plan de Seguridad Hídrica para Ciudades y Sociedades Seguras</div>
            <div class="subtitulo-lema">"Juntos, somos más Sostenibles, más Efectivos, más Visibles, más Seguros y más Fuertes."</div>
        </div>
    """, unsafe_allow_html=True)

# 4. BARRA LATERAL INSTITUCIONAL
with st.sidebar:
    st.markdown("<h3 style='color:#38BDF8; text-align:center;'>Gobernanza Territorial</h3>", unsafe_allow_html=True)
    st.markdown("---")
    st.caption("Fondo de Agua • Sistema de Inteligencia Hidro-Territorial (SIHT-CV) para el monitoreo físico-financiero.")
    st.markdown("---")
    st.markdown("### 📈 Escenarios de Financiación")
    porcentaje = st.slider("Asignación Art. 41 de la Ley 99 (Mínimo de ley: 1%):", 1.0, 3.0, 1.0, step=0.1)
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
                <span style="color:#10B981; font-weight:600; text-transform:uppercase; font-size:12px; letter-spacing:0.5px;">Pilar 1: Soluciones Basadas en la Naturaleza (SbN)</span>
                <p style="margin-top:5px; margin-bottom:0; font-size:15px; color:#E2E8F0;">
                    Restauración dirigida de coberturas y mantenimiento de la conectividad ecohidrológica en la Estructura Ecológica Principal de las cuencas aportantes.
                </p>
            </div>
            <div class="card-glass" style="border-left: 4px solid #38BDF8;">
                <span style="color:#38BDF8; font-weight:600; text-transform:uppercase; font-size:12px; letter-spacing:0.5px;">Pilar 2: Rigor Científico Integrado</span>
                <p style="margin-top:5px; margin-bottom:0; font-size:15px; color:#E2E8F0;">
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
    
    col_t1, col_t2 = st.columns([6, 6])
    with col_t1:
        tipo_vista = st.radio("Seleccione el formato de visualización estratégica:", ["📊 Diagrama de Flujo (Sankey)", "📋 Matriz de Datos Tradicional"], horizontal=True)
    with col_t2:
        # 💥 RESPUESTA AL PUNTO 2: Interruptor dinámico para activar la simulación del Programa 2
        programa_focus = st.selectbox("Enfoque de Programa Técnico (Sankey):", ["Todos los Programas", "Programa 2: Intervención en Quebradas y SbN"])

    # Base de datos unificada
    @st.cache_data
    def obtener_matriz_tecnica_limpia():
        try:
            df = pd.read_csv("data/PlanTacticoSH_CV.xls - Hoja1.csv")
            df.columns = [c.strip() for c in df.columns]
            return df
        except:
            datos_oficiales = {
                "Línea Estratégica": [
                    "Línea 1. Gestión del conocimiento e inteligencia socioecológica", "Línea 1. Gestión del conocimiento e inteligencia socioecológica", "Línea 1. Gestión del conocimiento e inteligencia socioecológica",
                    "Línea 2. Articulación Multisectorial para la Gobernanza Multinivel", "Línea 2. Articulación Multisectorial para la Gobernanza Multinivel",
                    "Línea 3. Intervenciones con propósito y retorno", "Línea 3. Intervenciones con propósito y retorno", "Línea 3. Intervenciones con propósito y retorno"
                ],
                "Acción Estratégica": [
                    "1.1 Pacto de transferencia de información por la SH", "1.2 Puesta en marcha del Sistema de Inteligencia Hidro-Territorial -SIHT-", "1.3 Desarrollo e implementación del Dashboard SIHT para la toma de decisiones",
                    "2.1 Gran Pacto por la seguridad Hídrica", "2.2 Conformación Consejo de Seguridad Hídrica Territorial",
                    "3.1 Corredor Vivo Intercuencas Grande – Aburrá - Negro", "3.2 Infraestructura verde y Soluciones Basadas en la naturaleza para la SH", "3.3 Programa Escuela-Taller del agua y la Biodiversidad (ETAB)"
                ],
                "Meta Táctica (Años 1-2)": [
                    "1 Pacto de información territorial implementado", "100% de desarrollo del modelo conceptual y primera versión del SIHT-CV", "100% de desarrollo del dashboard SIHT-CV",
                    "100% de suscripción del Gran Pacto por la Seguridad Hídrica de Medellín", "100% de conformación del consejo de seguridad hídrica territorial",
                    "6 km de corredores intervenidos de 10 m de ancho en la cuenca de Río Chico", "Plan Estratégico de Seguridad Hídrica y Resiliencia Territorial formulado y puesto en marcha", "3 ETABs en marcha"
                ],
                "Fase I": ["●", "●", "●", "●", "●", "●", "●", "●"],
                "Fase II": ["●", "●", "●", "", "", "●", "●", "●"],
                "Fase III": ["●", "●", "●", "", "", "●", "●", "●"]
            }
            return pd.DataFrame(datos_oficiales)

    df_matriz = obtener_matriz_tecnica_limpia()
    
    if tipo_vista == "📊 Diagrama de Flujo (Sankey)":
        st.markdown("<br>", unsafe_allow_html=True)
        
        nodos = [
            "Línea 1: Inteligencia", "Línea 2: Gobernanza", "Línea 3: Intervenciones",  
            "1.1 Pacto Info", "1.2 SIHT", "1.3 Dashboard (Clic abajo para abrir SIHCLI-POTER) 🌐",  
            "2.1 Gran Pacto", "2.2 Consejo SH",  
            "3.1 Corredor Vivo", "3.2 SbN / AbE (Programa 2) 🌟", "3.3 Escuela-Taller",  
            "Fase I (Comprender)", "Fase II (Acordar)", "Fase III (Hacer)"  
        ]
        
        sources = [0,0,0, 1,1, 2,2,2, 3,3, 4,4, 5,5,5, 6, 7, 8,8,8, 9,9,9, 10,10,10]
        targets = [3,4,5, 6,7, 8,9,10, 11,12, 11,12, 11,12,13, 11, 11, 11,12,13, 11,12,13, 11,12,13]
        values  = [1,1,1, 1,1, 1,1,1,  1,1,  1,1,  1,1,1,   1,  1,  1,1,1,  1,1,1,  1,1,1]
        
        x_manual = [0.05, 0.05, 0.05,  0.5, 0.5, 0.5,  0.5, 0.5,  0.5, 0.5, 0.5,  0.95, 0.95, 0.95]
        y_manual = [0.1,  0.45, 0.8,   0.05, 0.15, 0.25, 0.42, 0.52, 0.72, 0.82, 0.92, 0.2, 0.5, 0.8]
        
        # Resaltar la Línea 3 si el Programa 2 está seleccionado
        colores_nodos = ["#0284C7", "#F59E0B", "#10B981", "#38BDF8", "#38BDF8", "#60A5FA", "#FBBF24", "#F59E0B", "#34D399", "#10B981", "#059669", "#6366F1", "#A5B4FC", "#4338CA"]
        if "Programa 2" in programa_focus:
            colores_nodos[9] = "#EC4899" # Color rosa fucsia de alto impacto para el nodo 3.2
            
        fig_sankey = go.Figure(data=[go.Sankey(
            arrangement = "fixed",
            textfont = dict(size = 15, family = "Montserrat", color = "#FFFFFF"),
            node = dict(
              pad = 18,
              thickness = 22,
              line = dict(color = "#38BDF8", width = 0.5),
              label = nodos,
              x = x_manual,
              y = y_manual,
              color = colores_nodos
            ),
            link = dict(
              source = sources,
              target = targets,
              value = values,
              color = "rgba(236, 72, 153, 0.4)" if "Programa 2" in programa_focus else "rgba(56, 189, 248, 0.15)"
          ))])
        
        fig_sankey.update_layout(
            title_text="Mapeo de Flujo Estructurado: Sinergia de Programas hacia Fases de Ejecución",
            font_size=13,
            font_family="Montserrat",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color="#E2E8F0"
        )
        st.plotly_chart(fig_sankey, use_container_width=True)

        # 💥 RESPUESTA AL PUNTO 2: Despliegue sincrónico de las dos animaciones en paralelo para el Programa 2
        if "Programa 2" in programa_focus:
            st.markdown("### 🌿 Programa 2: Recuperación Ecohidrológica Multifuncional")
            st.write("""
            Intervención de quebradas rurales y periurbanas de Medellín y la Región Central mediante **Soluciones basadas en la Naturaleza (SbN)**. 
            El objetivo es mitigar riesgos de escorrentía, erosión y crecientes, transformándolas en ejes de infraestructura ecológica de estándar internacional.
            """)
            
            col_v1, col_v2 = st.columns(2)
            with col_v1:
                st.markdown("#### **⚠️ Escenario A: Vulnerabilidad Estructural (Erosión / Escorrentía)**")
                try:
                    st.video("data/Prog2_Vulnerabilidad.mp4") # Reemplazar con el nombre exacto de tus archivos de video cargados
                except:
                    st.info("Simulación del estado de degradación crítica actual de la ronda riparia.")
            with col_v2:
                st.markdown("#### **🌱 Escenario B: Resiliencia Territorial mediante Infraestructura Verde**")
                try:
                    st.video("data/Prog2_Resiliencia.mp4")
                except:
                    st.success("Simulación de la funcionalidad ecohidrológica recuperada con SbN.")
            st.markdown("---")
        
        st.markdown("""
            <div class="card-glass" style="border-left: 4px solid #60A5FA; margin-top: 10px; text-align: center;">
                <p style="margin: 0; font-size: 16px;">
                    🌐 <strong>Acceso Directo al Sistema de Información:</strong> El componente 1.3 orquesta los datos regionales en vivo. 
                    Puedes interactuar con el entorno de simulación entrando aquí: 
                    <a class="link-sihclim" href="https://sihclim-v1-6n3jcavvxqxpxrnqikzfpt.streamlit.app/" target="_blank">Abrir Plataforma SIHCLIM / SIHCLI-POTER</a>
                </p>
            </div>
        """, unsafe_allow_html=True)

    else:
        col_l, col_f = st.columns(2)
        with col_l:
            opciones_l = ["Todas"] + list(df_matriz["Línea Estratégica"].dropna().unique())
            filtro_l = st.selectbox("Filtrar por Línea Programática:", opciones_l)
        with col_f:
            filtro_f = st.segmented_control("Filtrar por Fase Activa:", ["Todas", "Fase I (Comprender)", "Fase II (Acordar)", "Fase III (Hacer)"], default="Todas")
            
        df_ver = df_matriz.copy()
        if filtro_l != "Todas":
            df_ver = df_ver[df_ver["Línea Estratégica"] == filtro_l]
            
        if filtro_f == "Fase I (Comprender)": df_ver = df_ver[df_ver["Fase I"].isin(["●", "● ", " ●"])]
        elif filtro_f == "Fase II (Acordar)": df_ver = df_ver[df_ver["Fase II"].isin(["●", "● ", " ●"])]
        elif filtro_f == "Fase III (Hacer)": df_ver = df_ver[df_ver["Fase III"].isin(["●", "● ", " ●"])]
        
        st.dataframe(df_ver, use_container_width=True, hide_index=True)

# ==========================================
# PESTAÑA III: EL RETORNO DEL AGUA
# ==========================================
with tab_metas:
    st.markdown("### 📈 Retorno Ecosistémico y Compromisos Globales")
    
    col_fichas, col_ods = st.columns([10, 10])
    
    with col_fichas:
        st.markdown("#### **Fichas Técnicas de Indicadores (SIHT-CV)**")
        ficha = st.radio("Componente de monitoreo técnico a proyectar:", ["Ficha 1 - Línea de Base", "Ficha 2 - Inteligencia", "Ficha 3 - Gobernanza", "Ficha 4 - Intervenciones", "Ficha 5 - Monitoreo"], horizontal=True)
        fichas_map = {"Ficha 1 - Línea de Base": "P1", "Ficha 2 - Inteligencia": "P2", "Ficha 3 - Gobernanza": "P3", "Ficha 4 - Intervenciones": "P4", "Ficha 5 - Monitoreo": "P5"}
        
        # 💥 RESPUESTA AL PUNTO 1: Caja de redimensionamiento estricto 'contenedor-ficha-fija' para congelar el tamaño
        st.markdown('<div class="contenedor-ficha-fija">', unsafe_allow_html=True)
        try:
            st.image(f"data/Metas_Indicadores_{fichas_map[ficha]}.png", use_container_width=True)
        except:
            st.info("Desplegando gráfica analítica del indicador...")
        st.markdown('</div>', unsafe_allow_html=True)
            
    with col_ods:
        st.markdown("#### **🌍 Alineación con Objetivos Globales**")
        st.write("Estructura escalada del Plan frente a las metas mundiales de sostenibilidad:")
        
        # Caja de redimensionamiento estricto para mantener la proporción de la gota ODS
        st.markdown('<div class="contenedor-ods-fijo">', unsafe_allow_html=True)
        try:
            st.image("data/ODS_CV.png", use_container_width=True)
        except:
            pass
        st.markdown('</div>', unsafe_allow_html=True)
