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

# 2. INYECCIÓN AVANZADA DE CSS (Control Estricto de Redimensionamiento, Fuentes y Layout)
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
    
    /* CONGELAMIENTO RIGUROSO DE FICHAS TÉCNICAS E IMÁGENES CRISIS */
    .contenedor-ficha-fija img {
        height: 320px !important;
        width: 100% !important;
        object-fit: fill !important;
        border-radius: 12px;
        display: block !important;
        margin: 0 auto !important;
    }
    
    .contenedor-ods-fijo img {
        height: 320px !important;
        object-fit: contain !important;
        width: auto !important;
        margin: 0 auto !important;
        display: block !important;
    }
    
    /* Ajuste de escala para el visor de la Pestaña 0 */
    .contenedor-crisis-fijo img {
        height: 360px !important;
        object-fit: cover !important;
        width: 100% !important;
        border-radius: 12px;
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

# 5. ESTRUCTURA GLOBAL EN PESTAÑAS (Declaradas una sola vez en la raíz para evitar fallas lógicas de navegación)
tab_contexto, tab_origen, tab_ruta, tab_metas = st.tabs([
    "0. Seguridad Hídrica Integral",
    "Ⅰ. El Origen y El Reto", 
    "Ⅱ. La Ruta Táctica (PlanTacticoSH_CV)", 
    "Ⅲ. El Retorno del Agua"
])

# ==========================================
# PESTAÑA 0: SEGURIDAD HÍDRICA INTEGRAL
# ==========================================
with tab_contexto:
    st.markdown("### 🌍 El Punto de Inflexión Climático y Territorial")
    st.write("""
    La seguridad hídrica ha dejado de ser un asunto estrictamente ambiental para transformarse en el **activo más crítico y vulnerable de la estabilidad social, ecosistémica y económica** de nuestra era[cite: 3]. 
    La intensificación de fenómenos hidroclimáticos extremos sitúa a la Región Central ante retos de gestión ineludibles[cite: 3].
    """)
    
    # Selector interactivo para navegar por los activos gráficos que subiste
    categoria_riesgo = st.radio(
        "Explore las Dimensiones del Riesgo Territorial Hidroclimático:",
        ["⚠️ Crisis Climática Regional", "🔥 Sequía y Desabastecimiento (El Niño)", "🌧️ Lluvias Torrenciales e Inundaciones (La Niña)", "🚜 Pérdida de Cobertura y Erosión"],
        horizontal=True
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    col_c1, col_c2 = st.columns([10, 10])
    
    with col_c1:
        if categoria_riesgo == "⚠️ Crisis Climática Regional":
            st.markdown("#### **Vulnerabilidad Estructural en Antioquia**")
            st.write("""
            Las proyecciones térmicas indican un incremento sostenido de la temperatura media andina, alterando de manera drástica la regularidad de los patrones de precipitación. 
            Esta inestabilidad somete a una presión constante a la infraestructura de almacenamiento y abastecimiento regional.
            """)
            st.markdown("""
                <div class="card-glass" style="border-left: 4px solid #EF4444;">
                    <span style="color:#EF4444; font-weight:600; text-transform:uppercase; font-size:11px;">Presión Sobre Embalses</span>
                    <p style="margin-top:5px; margin-bottom:0; font-size:14px; color:#E2E8F0;">
                        Los eventos extremos más frecuentes comprometen los niveles operativos de los sistemas abastecedores externos, requiriendo un enfoque de mitigación basado en la ciencia.
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
        elif categoria_riesgo == "🔥 Sequía y Desabastecimiento (El Niño)":
            st.markdown("#### **Estrés Hídrico Extremo**")
            st.write("""
            Durante la ocurrencia del fenómeno de El Niño, los caudales base disminuyen críticamente, desencadenando incendios de cobertura vegetal en zonas de recarga y forzando el racionamiento o desabastecimiento severo en comunidades rurales y periurbanas.
            """)
            st.markdown("""
                <div class="card-glass" style="border-left: 4px solid #F59E0B;">
                    <span style="color:#F59E0B; font-weight:600; text-transform:uppercase; font-size:11px;">Riesgo Financiero y de Consumo</span>
                    <p style="margin-top:5px; margin-bottom:0; font-size:14px; color:#E2E8F0;">
                        La pérdida de capacidad reguladora de los suelos expone el desabastecimiento crónico, obligando al uso de carrotanques y comprometiendo el ROI de la matriz agrícola.
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
        elif categoria_riesgo == "🌧️ Lluvias Torrenciales e Inundaciones (La Niña)":
            st.markdown("#### **Avenidas Torrenciales Urbanas y Rurales**")
            st.write("""
            El fenómeno de La Niña satura los suelos de las vertientes andinas de forma acelerada. Sin la amortiguación natural de los bosques de galería, las lluvias torrenciales saturan los drenajes urbanos y provocan crecientes súbitas e inundaciones devastadoras.
            """)
            st.markdown("""
                <div class="card-glass" style="border-left: 4px solid #3B82F6;">
                    <span style="color:#3B82F6; font-weight:600; text-transform:uppercase; font-size:11px;">Colapso de Estructuras</span>
                    <p style="margin-top:5px; margin-bottom:0; font-size:14px; color:#E2E8F0;">
                        Los picos de inundación arrastran sedimentos que saturan las plantas de tratamiento y erosionan las obras civiles y vías de acceso vitales.
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
        elif categoria_riesgo == "🚜 Pérdida de Cobertura y Erosión":
            st.markdown("#### **Degradación de la Infraestructura Natural**")
            st.write("""
            La deforestación histórica de las fajas riparias altera directamente la salud de las cuencas. El suelo desnudo pierde su capacidad de infiltración, acelerando los procesos de remoción en masa y la socavación de riberas.
            """)
            st.markdown("""
                <div class="card-glass" style="border-left: 4px solid #10B981;">
                    <span style="color:#10B981; font-weight:600; text-transform:uppercase; font-size:11px;">El Antídoto Técnico</span>
                    <p style="margin-top:5px; margin-bottom:0; font-size:14px; color:#E2E8F0;">
                        La restauración biológica mediante Soluciones Basadas en la Naturaleza frena la escorrentía rápida y estabiliza mecánicamente los taludes marginales.
                    </p>
                </div>
            """, unsafe_allow_html=True)

    with col_c2:
        # Renderizado dinámico y controlado de tus archivos cargados respetando la ruta de la nueva subcarpeta
        st.markdown('<div class="contenedor-crisis-fijo">', unsafe_allow_html=True)
        if categoria_riesgo == "⚠️ Crisis Climática Regional":
            try: st.image("data/CrisisAguaClima/image_c9d060.jpg", use_container_width=True)
            except: st.image("data/EmbalseRG.jpg", use_container_width=True)
            
        elif categoria_riesgo == "🔥 Sequía y Desabastecimiento (El Niño)":
            try: st.image("data/CrisisAguaClima/Sequia_Embalse_Guatapé.png", use_container_width=True)
            except:
                try: st.image("data/CrisisAguaClima/embalseseco.jpg", use_container_width=True)
                except: st.info("Desplegando evidencia de estrés hídrico extremo (Embalses secos / Incendios forestales)[cite: 3].")
                
        elif categoria_riesgo == "🌧️ Lluvias Torrenciales e Inundaciones (La Niña)":
            try: st.image("data/CrisisAguaClima/aguaceros_Medellin.jpg", use_container_width=True)
            except:
                try: st.image("data/CrisisAguaClima/inundaciones_Medellin.png", use_container_width=True)
                except: st.info("Desplegando evidencia de inundaciones y desbordamientos en infraestructura urbana.")
                
        elif categoria_riesgo == "🚜 Pérdida de Cobertura y Erosión":
            try: st.image("data/CrisisAguaClima/SocavacionRio.jpg", use_container_width=True)
            except: st.info("Desplegando evidencia de pérdida de cobertura boscosa riparia y socavación crítica de riberas.")
        st.markdown('</div>', unsafe_allow_html=True)

# ==========================================
# PESTAÑA I: EL ORIGEN Y EL RETO
# ==========================================
with tab_origen:
    try:
        st.image("data/EmbalseRG.png", caption="Ecosistema Estratégico Abastecedor - Región Central Funcional de Antioquia", use_container_width=True)
    except:
        pass

    col_text_origen, col_video_origen = st.columns([10, 10])
    with col_text_origen:
        st.markdown("### 🌊 Diagnóstico y Dependencia Socio-Ecológica")
        st.write("""
        El metabolismo urbano de Medellín depende críticamente de cuencas e infraestructuras ecológicas externas localizadas en el Norte y Oriente de Antioquia[cite: 1]. 
        Los sistemas reguladores de **Río Grande II y La Fe** sostienen la vida colectiva y la resiliencia del territorio[cite: 1].
        """)
        st.markdown("""
            <div class="card-glass" style="border-left: 4px solid #10B981;">
                <span style="color:#10B981; font-weight:600; text-transform:uppercase; font-size:12px; letter-spacing:0.5px;">Pilar 1: Soluciones Basadas en la Naturaleza (SbN)</span>
                <p style="margin-top:5px; margin-bottom:0; font-size:15px; color:#E2E8F0;">
                    Restauración dirigida de coberturas y mantenimiento de la conectividad ecohidrológica en la Estructura Ecológica Principal de las cuencas aportantes[cite: 3].
                </p>
            </div>
            <div class="card-glass" style="border-left: 4px solid #38BDF8;">
                <span style="color:#38BDF8; font-weight:600; text-transform:uppercase; font-size:12px; letter-spacing:0.5px;">Pilar 2: Rigor Científico Integrado</span>
                <p style="margin-top:5px; margin-bottom:0; font-size:15px; color:#E2E8F0;">
                    Operación de la plataforma SIHT-CV para generar modelación socioecológica predictiva regional en tiempo real ante el cambio climático[cite: 1, 3].
                </p>
            </div>
        """, unsafe_allow_html=True)
    with col_video_origen:
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
        # Lógica de filtrado interna y hermética para evitar mutaciones de pestañas
        programa_focus = st.selectbox(
            "Enfoque Estratégico Dinámico (Foco Sankey):", 
            ["2.1 Gran Pacto (Semana del Clima) 🌍", "3.2 Programa 2 (Infraestructura Verde y SbN) 🌱", "3.3 Escuela-Taller del Agua (ETAB) 💻"]
        )

    # Carga analítica de la base de datos
    @st.cache_data
    def obtener_matriz_tecnica_limpia():
        try:
            df = pd.read_csv("data/PlanTacticoSH_CV.xls")
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
                    "1 Pacto de información territorial implementado[cite: 1]", "100% de desarrollo del modelo conceptual y primera versión del SIHT-CV[cite: 1]", "100% de desarrollo del dashboard SIHT-CV[cite: 1]",
                    "100% de suscripción del Gran Pacto por la Seguridad Hídrica de Medellín[cite: 1]", "100% de conformación del consejo de seguridad hídrica territorial[cite: 1]",
                    "6 km de corredores intervenidos de 10 m de ancho en la cuenca de Río Chico[cite: 1]", "Plan Estratégico de Seguridad Hídrica y Resiliencia Territorial formulado y puesto en marcha[cite: 1]", "3 ETABs en marcha[cite: 1]"
                ]
            }
            return pd.DataFrame(datos_oficiales)

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

        # DESPLIEGUE MULTIMEDIA UBICADO ESTRICTAMENTE DEBAJO DEL SANKEY
        if "2.1 Gran Pacto" in programa_focus:
            st.markdown("### 🌍 Agenda Global: Gran Pacto por la Seguridad Hídrica")
            col_pacto_txt, col_pacto_img = st.columns([8, 4])
            with col_pacto_txt:
                st.markdown("""
                <div class="card-glass" style="border-left: 4px solid #38BDF8; font-size:16.5px; padding:20px;">
                    <strong>La Semana del Clima de Medellín</strong> es la ventana para convertir la seguridad hídrica en una agenda de ciudad: 
                    ciencia, innovación, inversión y acción territorial al servicio de la naturaleza y de las personas[cite: 1].
                </div>
                """, unsafe_allow_html=True)
            with col_pacto_img:
                try: st.image("data/Climate_Week_Medellin.png", caption="Semana del Clima de Medellín", use_container_width=True)
                except: st.image("data/aliados.png", use_container_width=True)

        elif "3.2" in programa_focus:
            st.markdown("### 🌱 Programa 2: Recuperación Ecohidrológica Multifuncional")
            st.write("Mantenimiento y mitigación de escorrentías en la infraestructura ecológica de la Región Central[cite: 1]:")
            col_v1, col_v2 = st.columns(2)
            with col_v1:
                st.markdown("#### **⚠️ Escenario A: Vulnerabilidad Estructural**")
                try: st.video("data/Prog2_Vulnerabilidad.mp4")
                except: st.info("Simulación de erosión crítica actual.")
            with col_v2:
                st.markdown("#### **🌱 Escenario B: Resiliencia Territorial con SbN**")
                try: st.video("data/Prog2_Resiliencia.mp4")
                except: st.success("Simulación de la funcionalidad ecohidrológica recuperada[cite: 1].")

        elif "3.3" in programa_focus:
            st.markdown("### 💻 Componente 3.3: Programa Escuela-Taller del Agua y la Biodiversidad (ETAB)")
            col_et1, col_et2 = st.columns([9, 11])
            with col_et1:
                st.markdown("""
                Formación avanzada y fortalecimiento de capacidades comunitarias en entornos rurales para promover la cultura del agua, la gobernanza hídrica y el intercambio de saberes tradicionales sobre los ciclos hidrológicos locales[cite: 1].
                """)
            with col_et2:
                try: st.video("data/Escuelas_Taller.mp4")
                except: st.warning("Subiendo archivo multimedia 'Escuelas_Taller.mp4'...")
        
        # Enlace permanente a SIHCLIM
        st.markdown("""
            <div class="card-glass" style="border-left: 4px solid #60A5FA; margin-top: 15px; text-align: center;">
                <p style="margin: 0; font-size: 16px;">
                    🌐 <strong>Acceso Directo al Sistema de Información:</strong> El componente 1.3 orquesta los datos regionales en vivo[cite: 1]. 
                    Puedes interactuar con el entorno de simulación entrando aquí: 
                    <a class="link-sihclim" href="https://sihclim-v1-6n3jcavvxqxpxrnqikzfpt.streamlit.app/" target="_blank">Abrir Plataforma SIHCLIM / SIHCLI-POTER</a>
                </p>
            </div>
        """, unsafe_allow_html=True)

    else:
        # Visualización tabular tradicional
        col_l, col_f = st.columns(2)
        with col_l:
            opciones_l = ["Todas"] + list(df_metriz["Línea Estratégica"].dropna().unique())
            filtro_l = st.selectbox("Filtrar por Línea Programática:", opciones_l)
        with col_f:
            filtro_f = st.segmented_control("Filtrar por Fase Activa:", ["Todas", "Fase I", "Fase II", "Fase III"], default="Todas")
            
        df_ver = df_matriz.copy()
        if filtro_l != "Todas":
            df_ver = df_ver[df_ver["Línea Estratégica"] == filtro_l]
        st.dataframe(df_ver, use_container_width=True, hide_index=True)

# ==========================================
# PESTAÑA III: EL RETORNO DEL AGUA
# ==========================================
with tab_metas:
    st.markdown("### 📈 Retorno Ecosistémico y Compromisos Globales")
    
    col_fichas, col_ods = st.columns([10, 10])
    
    with col_fichas:
        st.markdown("#### **Fichas Técnicas de Indicadores (SIHT-CV)**[cite: 1]")
        ficha = st.radio("Componente de monitoreo técnico a proyectar:", ["Ficha 1 - Línea de Base", "Ficha 2 - Inteligencia", "Ficha 3 - Gobernanza", "Ficha 4 - Intervenciones", "Ficha 5 - Monitoreo"], horizontal=True)
        fichas_map = {"Ficha 1 - Línea de Base": "P1", "Ficha 2 - Inteligencia": "P2", "Ficha 3 - Gobernanza": "P3", "Ficha 4 - Intervenciones": "P4", "Ficha 5 - Monitoreo": "P5"}
        
        st.markdown('<div class="contenedor-ficha-fija">', unsafe_allow_html=True)
        try: st.image(f"data/Metas_Indicadores_{fichas_map[ficha]}.png", use_container_width=True)
        except: st.info("Desplegando gráfica analítica del indicador...")
        st.markdown('</div>', unsafe_allow_html=True)
            
    with col_ods:
        st.markdown("#### **🌍 Alineación con Objetivos Globales**")
        st.write("Estructura de la gota escalada simétricamente frente a las metas mundiales de sostenibilidad[cite: 1]:")
        
        st.markdown('<div class="contenedor-ods-fijo">', unsafe_allow_html=True)
        try: st.image("data/ODS_CV.png", use_container_width=True)
        except: pass
        st.markdown('</div>', unsafe_allow_html=True)
