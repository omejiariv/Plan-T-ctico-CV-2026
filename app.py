import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os

# 1. CONFIGURACIÓN PREMIUM DE LA PÁGINA
st.set_page_config(
    page_title="Plan de Seguridad Hídrica | CuencaVerde",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. INYECCIÓN AVANZADA DE CSS (Control Forzado de Contenedores stImage y Simetría)
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
        padding-top: 2rem !important;
        padding-bottom: 1rem !important;
    }
    
    .header-bloque {
        text-align: center;
        padding-top: 10px;
        margin-bottom: 15px;
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
        margin-top: 10px;
        letter-spacing: 0.3px;
    }
    
    .card-glass {
        background: rgba(15, 23, 42, 0.70);
        border: 1px solid rgba(56, 189, 248, 0.20);
        padding: 22px;
        border-radius: 16px;
        backdrop-filter: blur(12px);
        margin-bottom: 20px;
    }
    
    /* 💥 SOLUCIÓN AL PUNTO 3: Forzar el control del layout del div contenedor stImage para reducir el embalse a la mitad */
    [data-testid="stImage"] img {
        max-height: 220px !important;
        object-fit: cover !important;
        width: 100% !important;
        border-radius: 12px;
    }
    
    /* 💥 SOLUCIÓN AL PUNTO 2: Fijación estricta de simetría para la pestaña III (Fichas y ODS) */
    .contenedor-fichas-fijas [data-testid="stImage"] img {
        max-height: 250px !important;
        object-fit: contain !important;
        width: auto !important;
        margin: 0 auto !important;
    }
    
    .contenedor-crisis-carrusel [data-testid="stImage"] img {
        max-height: 340px !important;
        object-fit: cover !important;
        width: 100% !important;
        border-radius: 12px;
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
    st.markdown("<div style='display: flex; align-items: center; justify-content: center; height: 100%; padding-top: 10px;'>", unsafe_allow_html=True)
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

# 5. CONTROLADOR INTERNO DE SESIÓN (💥 SOLUCIÓN AL PUNTO 1: Blindaje total contra la duplicación)
if "menu_activo" not in st.session_state:
    st.session_state.menu_activo = "0. Seguridad Hídrica Integral"

# Navegación premium integrada mediante botones horizontales limpios antes de renderizar contenidos
col_n0, col_n1, col_n2, col_n3 = st.columns(4)
with col_n0: 
    if st.button("0. Seguridad Hídrica Integral", use_container_width=True): st.session_state.menu_activo = "0. Seguridad Hídrica Integral"
with col_n1: 
    if st.button("Ⅰ. El Origen y El Reto", use_container_width=True): st.session_state.menu_activo = "Ⅰ. El Origen y El Reto"
with col_n2: 
    if st.button("Ⅱ. La Ruta Táctica", use_container_width=True): st.session_state.menu_activo = "Ⅱ. La Ruta Táctica"
with col_n3: 
    if st.button("Ⅲ. El Retorno del Agua", use_container_width=True): st.session_state.menu_activo = "Ⅲ. El Retorno del Agua"

st.markdown("---")

# ==========================================
# PESTAÑA 0: SEGURIDAD HÍDRICA INTEGRAL
# ==========================================
if st.session_state.menu_activo == "0. Seguridad Hídrica Integral":
    st.markdown("### 🌍 Definición Operativa y Dimensiones Críticas de la Seguridad Hídrica Integral")
    
    # 💥 SOLUCIÓN AL PUNTO 2: Incorporación de los pilares técnicos de la imagen de Seguridad Hídrica Integral
    col_dim1, col_dim2, col_dim3, col_dim4, col_dim5, col_dim6  = st.columns(6)

    with col_dim1:
        st.markdown('<div class="card-glass" style="border-top: 3px solid #38BDF8; height: 100%; text-align:center;"><strong>1. Integridad ecosistémica</strong><p style="font-size:13.5px !important; margin-top:5px;">Capacidad para automantenerse y autorregularse, conservando su composición de especies, estructura física y sus funciones naturales.</p></div>', unsafe_allow_html=True)
    with col_dim2:
        st.markdown('<div class="card-glass" style="border-top: 3px solid #38BDF8; height: 100%; text-align:center;"><strong>2. Disponibilidad Confiable</strong><p style="font-size:13.5px !important; margin-top:5px;">Garantizar la oferta del recurso en cantidad para el metabolismo urbano de la Región Central.</p></div>', unsafe_allow_html=True)
    with col_dim3:
        st.markdown('<div class="card-glass" style="border-top: 3px solid #10B981; height: 100%; text-align:center;"><strong>3. Calidad Segura</strong><p style="font-size:13.5px !important; margin-top:5px;">Mitigar la sedimentación y cargas contaminantes en las microcuencas abastecedoras.</p></div>', unsafe_allow_html=True)
    with col_dim4:
        st.markdown('<div class="card-glass" style="border-top: 3px solid #EF4444; height: 100%; text-align:center;"><strong>4. Riesgos Gestionados</strong><p style="font-size:13.5px !important; margin-top:5px;">Identificar, evaluar y priorizar los peligros asociados a eventos extremos que amenazan la disponibilidad, calidad y acceso al agua para la población, los ecosistemas y la economía.</p></div>', unsafe_allow_html=True)
    with col_dim5:
        st.markdown('<div class="card-glass" style="border-top: 3px solid #F59E0B; height: 100%; text-align:center;"><strong>5. Resiliencia Colectiva Integral</strong><p style="font-size:13.5px !important; margin-top:5px;">Ruta metodológica clara hacia la seguridad hídrica y Climática con criterios socio-ecológicos.</p></div>', unsafe_allow_html=True)
    with col_dim6:
        st.markdown('<div class="card-glass" style="border-top: 3px solid #38BDF8; height: 100%; text-align:center;"><strong>6. Gobernanza adaptativa</strong><p style="font-size:13.5px !important; margin-top:5px;">Un Modelo flexible, multinivel y colaborativo, diseñado para articular actores, gestionar entornos de alta complejidad socioecologica y Alto riesgo global.</p></div>', unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    col_c1, col_c2 = st.columns([10, 10])
    
    with col_c1:
        st.markdown("#### **Mosaico Situacional de la Vulnerabilidad**")
        st.write("""
        Los escenarios de cambio climático intensifican de forma alarmante el ciclo hidrológico en las vertientes marginales de Antioquia. 
        La alternancia extrema entre sequías prolongadas, aguaceros torrenciales urbanos y la degradación forestal de rondas hídricas exige un esquema unificado de orquestación territorial.
        """)
        
    with col_c2:
        st.markdown("#### **🎥 Visor Secuencial de Evidencia Hidroclimática**")
        
        # 💥 SOLUCIÓN AL PUNTO 4: Mecanismo de control interactivo para auditar la carpeta data/CrisisAguaClima/
        dir_crisis = "data/CrisisAguaClima"
        imagenes_crisis = []
        if os.path.exists(dir_crisis):
            imagenes_crisis = [os.path.join(dir_crisis, f) for f in os.listdir(dir_crisis) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            imagenes_crisis.sort()
            
        if imagenes_crisis:
            if "indice_carrusel" not in st.session_state:
                st.session_state.indice_carrusel = 0
                
            st.markdown('<div class="contenedor-crisis-fijo">', unsafe_allow_html=True)
            st.image(imagenes_crisis[st.session_state.indice_carrusel], use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Botones de control secuencial para navegar la crisis en la Junta Directiva
            col_btn_a, col_btn_info, col_btn_s = st.columns([3, 6, 3])
            with col_btn_a:
                if st.button("◀ Anterior"):
                    st.session_state.indice_carrusel = (st.session_state.indice_carrusel - 1) % len(imagenes_crisis)
                    st.rerun()
            with col_btn_info:
                st.markdown(f"<p style='text-align:center; font-size:14px !important; color:#38BDF8; margin-top:8px;'>Evidencia {st.session_state.indice_carrusel + 1} de {len(imagenes_crisis)} en Repositorio</p>", unsafe_allow_html=True)
            with col_btn_s:
                if st.button("Siguiente ▶"):
                    st.session_state.indice_carrusel = (st.session_state.indice_carrusel + 1) % len(imagenes_crisis)
                    st.rerun()
        else:
            try:
                st.image("data/CrisisAguaClima/image_c9d060.jpg", use_container_width=True)
            except:
                st.info("Cargando matriz gráfica secuencial de la subcarpeta data/CrisisAguaClima/...")

# ==========================================
# PESTAÑA I: EL ORIGEN Y EL RETO
# ==========================================
elif st.session_state.menu_activo == "Ⅰ. El Origen y El Reto":
    # 💥 SOLUCIÓN AL PUNTO 0: Extensión corregida a .png para el Embalse
    try:
        st.image("data/EmbalseRG.png", use_container_width=True)
    except:
        try: st.image("data/EmbalseRG.jpg", use_container_width=True)
        except: pass
    st.caption("Ecosistema Estratégico Abastecedor - Región Central Funcional de Antioquia")

    st.markdown("<br>", unsafe_allow_html=True)
    col_text_origen, col_video_origen = st.columns([10, 10])
    with col_text_origen:
        st.markdown("### 🌊 Diagnóstico y Dependencia Socio-Ecológica")
        st.write("""
        El metabolismo urbano de Medellín depende críticamente de cuencas e infraestructuras ecológicas externas localizadas en el Norte y Oriente de Antioquia. 
        Los sistemas reguladores de **Río Grande II y La Fe** sostienen la vida de la ciudad.
        """)
        st.markdown("""
            <div class="card-glass" style="border-left: 4px solid #10B981;">
                <span style="color:#10B981; font-weight:600; text-transform:uppercase; font-size:12px; letter-spacing:0.5px;">Pilar 1: Soluciones Basadas en la Naturaleza (SbN)</span>
                <p style="margin-top:5px; margin-bottom:0; font-size:15px; color:#E2E8F0;">
                    Restauración dirigida de coberturas y mantenimiento de la conectividad ecohidrológica en la Estructura Ecológica Principal de las cuencas aportantes.
                </p>
            </div>
        """, unsafe_allow_html=True)
    with col_video_origen:
        st.markdown("#### **🎥 Materialización de la Visión Táctica**")
        try: st.video("data/SegHid.mp4")
        except: st.warning("Cargando archivo de video 'SegHid.mp4'...")

# ==========================================
# PESTAÑA II: LA RUTA TÁCTICA
# ==========================================
elif st.session_state.menu_activo == "Ⅱ. La Ruta Táctica":
    st.markdown("### 📋 Cuadro de Mando Interactivo del Plan Táctico")
    
    col_t1, col_t2 = st.columns([6, 6])
    with col_t1:
        tipo_vista = st.radio("Seleccione el formato de visualización estratégica:", ["📊 Diagrama de Flujo (Sankey)", "📋 Matriz de Datos Tradicional"], horizontal=True, key="vista_radio_s")
    with col_t2:
        programa_focus = st.selectbox(
            "Enfoque Estratégico Dinámico (Foco Sankey):", 
            ["2.1 Gran Pacto (Semana del Clima) 🌍", "3.2 Programa 2 (Infraestructura Verde y SbN) 🌱", "3.3 Escuela-Taller del Agua (ETAB) 💻"],
            key="focus_select_s"
        )

    # Base de datos unificada de la matriz técnica oficial
    @st.cache_data
    def obtener_matriz_tecnica_limpia():
        try:
            df = pd.read_csv("data/PlanTacticoSH_CV.xls - Hoja1.csv")
            df.columns = [c.strip() for c in df.columns]
            return df
        except:
            return pd.DataFrame({"Línea Estratégica": ["Línea 1"], "Acción Estratégica": ["1.1 Acuerdo"], "Meta Táctica (Años 1-2)": ["Meta"]})

    df_matriz = obtener_matriz_tecnica_limpia()
    
    if tipo_vista == "📊 Diagrama de Flujo (Sankey)":
        st.markdown("<br>", unsafe_allow_html=True)
        
        nodos = [
            "Línea 1: Inteligencia", "Línea 2: Gobernanza", "Línea 3: Intervenciones",  
            "1.1 Pacto Info", "1.2 SIHT", "1.3 Dashboard 🌐",  
            "2.1 Gran Pacto 🌍", "2.2 Consejo SH",  
            "3.1 Corredor Vivo", "3.2 SbN / AbE (Prog 2) 🌱", "3.3 Escuela-Taller (ETAB) 💻",  
            "Fase I (Comprender)", "Fase II (Acordar)", "Fase III (Hacer)"  
        ]
        
        sources = [0,0,0, 1,1, 2,2,2, 3, 4, 5, 6, 7, 8, 9, 10]
        targets = [3,4,5, 6,7, 8,9,10, 11, 11, 11, 12, 12, 13, 13,  13]
        values  = [1,1,1, 1,1, 1,1,1,   1,  1,  1,  1,  1,  1,  1,   1]
        
        x_manual = [0.05, 0.05, 0.05,  0.5, 0.5, 0.5,  0.5, 0.5,  0.5, 0.5, 0.5,  0.95, 0.95, 0.95]
        y_manual = [0.1,  0.45, 0.8,   0.05, 0.15, 0.25, 0.42, 0.52, 0.72, 0.82, 0.92, 0.2, 0.5, 0.8]
        
        colores_nodos = ["#0284C7", "#F59E0B", "#10B981", "#38BDF8", "#38BDF8", "#60A5FA", "#FBBF24", "#F59E0B", "#34D399", "#10B981", "#059669", "#6366F1", "#A5B4FC", "#4338CA"]
        
        if "2.1 Gran Pacto" in programa_focus: colores_nodos[6] = "#38BDF8"
        elif "3.2" in programa_focus: colores_nodos[9] = "#EC4899"
        elif "3.3" in programa_focus: colores_nodos[10] = "#A5B4FC"
            
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
              color = "rgba(56, 189, 248, 0.15)"
          ))])
        
        fig_sankey.update_layout(
            title_text="Mapeo Logístico Temporal: Conexión de Acciones con sus Fases de Destino",
            font_size=13,
            font_family="Montserrat",
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font_color="#E2E8F0"
        )
        st.plotly_chart(fig_sankey, use_container_width=True)

        if "2.1 Gran Pacto" in programa_focus:
            st.markdown("### 🌍 Agenda Global: Gran Pacto por la Seguridad Hídrica")
            col_pacto_txt, col_pacto_img = st.columns([8, 4])
            with col_pacto_txt:
                st.markdown('<div class="card-glass" style="border-left: 4px solid #38BDF8; padding:20px;"><strong>La Semana del Clima de Medellín</strong> es la ventana para convertir la seguridad hídrica en una agenda de ciudad.</div>', unsafe_allow_html=True)
            with col_pacto_img:
                try: st.image("data/Climate_Week_Medellin.png", use_container_width=True)
                except: st.image("data/aliados.png", use_container_width=True)

        elif "3.2" in programa_focus:
            st.markdown("### 🌱 Programa 2: Recuperación Ecohidrológica Multifuncional")
            col_v1, col_v2 = st.columns(2)
            with col_v1:
                st.markdown("#### **⚠️ Escenario A: Vulnerabilidad Estructural**")
                try: st.video("data/Prog2_Vulnerabilidad.mp4")
                except: st.info("Simulación de erosión de laderas marginales.")
            with col_v2:
                st.markdown("#### **🌱 Escenario B: Resiliencia Territorial con SbN**")
                try: st.video("data/Prog2_Resiliencia.mp4")
                except: st.success("Simulación de funcionalidad recuperada.")

        elif "3.3" in programa_focus:
            st.markdown("### 💻 Componente 3.3: Programa Escuela-Taller del Agua (ETAB)")
            col_et1, col_et2 = st.columns([9, 11])
            with col_et1:
                st.write("Formación avanzada y fortalecimiento de capacidades comunitarias en entornos rurales para promover la cultura del agua.")
            with col_et2:
                try: st.video("data/Escuelas_Taller.mp4")
                except: st.info("Cargando video institucional de soporte para las ETABs...")

    else:
        st.dataframe(df_matriz, use_container_width=True, hide_index=True)

# ==========================================
# PESTAÑA III: EL RETORNO DEL AGUA
# ==========================================
elif st.session_state.menu_activo == "Ⅲ. El Retorno del Agua":
    st.markdown("### 📈 Retorno Ecosistémico y Compromisos Globales")
    
    col_fichas, col_ods = st.columns([7, 3])
    
    with col_fichas:
        st.markdown("#### **Fichas Técnicas de Indicadores (SIHT-CV)**")
        ficha = st.radio("Componente de monitoreo técnico a proyectar:", ["Ficha 1 - Línea de Base", "Ficha 2 - Inteligencia", "Ficha 3 - Gobernanza", "Ficha 4 - Intervenciones", "Ficha 5 - Monitoreo"], horizontal=True, key="ficha_r_s")
        fichas_map = {"Ficha 1 - Línea de Base": "P1", "Ficha 2 - Inteligencia": "P2", "Ficha 3 - Gobernanza": "P3", "Ficha 4 - Intervenciones": "P4", "Ficha 5 - Monitoreo": "P5"}
        
        st.markdown('<div class="contenedor-fichas-fijas">', unsafe_allow_html=True)
        try: st.image(f"data/Metas_Indicadores_{fichas_map[ficha]}.png", use_container_width=True)
        except: st.info("Desplegando gráfica analítica...")
        st.markdown('</div>', unsafe_allow_html=True)
            
    with col_ods:
        st.markdown("#### **🌍 Alineación con Objetivos Globales**")
        st.write("Metas globales de sostenibilidad:")
        
        st.markdown('<div class="contenedor-ods-fijo">', unsafe_allow_html=True)
        try: st.image("data/ODS_CV.png", use_container_width=True)
        except: pass
        st.markdown('</div>', unsafe_allow_html=True)
