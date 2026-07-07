import streamlit as st
import pandas as pd

# Configuración premium de la página
st.set_page_config(
    page_title="SIHT-CV | Plan Táctico de Seguridad Hídrica",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS Avanzados: Identidad "Fondo de Agua" institucional y tipografías limpias
st.markdown("""
    <style>
    .stApp { background-color: #F8FAFC; }
    h1, h2, h3 { color: #0F172A; font-family: 'Helvetica Neue', sans-serif; }
    
    /* Contenedor del Lema Principal */
    .lema-wow {
        background: linear-gradient(135deg, #1E3A8A 0%, #0284C7 100%);
        padding: 30px;
        border-radius: 16px;
        color: #FFFFFF;
        text-align: center;
        font-size: 22px;
        font-weight: 700;
        line-height: 1.4;
        box-shadow: 0 10px 15px -3px rgba(2, 132, 199, 0.2);
        margin-bottom: 35px;
    }
    
    /* Tarjetas de Métricas */
    .card-metrica {
        background-color: #FFFFFF;
        padding: 24px;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
        border-top: 5px solid #10B981;
        text-align: center;
    }
    .val-metrica { font-size: 38px; font-weight: 800; color: #065F46; }
    
    /* Cajas de Alerta de Riesgo */
    .alerta-territorial {
        background-color: #FFFBEB;
        border-left: 5px solid #F59E0B;
        padding: 20px;
        border-radius: 8px;
        color: #92400E;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)


# --- BARRA LATERAL (Estructura de Gobernanza e Identidad) ---
with st.sidebar:
    try:
        st.image("data/Logo CuencaVerde.jpg", use_container_width=True)
    except:
        try:
            st.image("data/CuencaVerde Logo.jpg", use_container_width=True)
        except:
            st.markdown("<h2 style='color:#0284C7;'>CuencaVerde</h2>", unsafe_allow_html=True)
            
    st.markdown("### 🏛️ Control de Gobernanza")
    modo_vista = st.radio(
        "Filtrar enfoque de la sesión:",
        ["Nuestra Alianza y Retos", "Ruta de Navegación Táctica", "Metas e Indicadores de Impacto"]
    )
    st.markdown("---")
    st.caption("Fondo de Agua • Sistema de Inteligencia Hidro-Territorial")


# ==========================================
# ENFOQUE 1: NUESTRA ALIANZA Y RETOS
# ==========================================
if modo_vista == "Nuestra Alianza y Retos":
    
    # 🌟 EL LEMA PRINCIPAL EN GRAN FORMATO NARRATIVO
    st.markdown("""
        <div class="lema-wow">
            "Juntos, somos más sostenibles, más efectivos, más visibles, más seguros y más fuertes."
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<p style='color:#0284C7; font-weight:700; text-transform:uppercase; margin-bottom:0;'>Marco Estratégico-Táctico Consolidado</p>", unsafe_allow_html=True)
    st.markdown("<h1>El Valor de Nuestra Unión Territorial</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    # Bloque de Gobernanza: Asociados y Aliados
    st.markdown("### 👥 Estructura de Gobernanza del Fondo de Agua")
    col_asoc, col_alia = st.columns(2)
    
    with col_asoc:
        st.markdown("#### **Nuestros Asociados**")
        try:
            st.image("data/asociados.png", use_container_width=True)
        except:
            st.info("Cargando matriz de asociados institucionales...")
            
    with col_alia:
        st.markdown("#### **Nuestros Aliados Estratégicos**")
        try:
            st.image("data/aliados.png", use_container_width=True)
        except:
            st.info("Cargando red de aliados estratégicos...")
            
    st.markdown("---")
    
    # Bloque de Diagnóstico y Vulnerabilidad
    st.markdown("### 🗺️ El Reto Hidro-Territorial Colectivo")
    col_diag, col_img_se = st.columns([1, 1])
    
    with col_diag:
        st.markdown("""
        La viabilidad futura del Distrito de Medellín y el Valle de Aburrá no puede depender exclusivamente de sus fronteras administrativas. 
        Mantenemos una **dependencia socio-ecológica crítica** de la Región Central funcional (Norte y Oriente de Antioquia). 
        
        Nuestros grandes activos y fuentes reguladoras, como los embalses **La Fe y Río Grande II**, requieren esquemas urgentes de conservación basados en Soluciones basadas en la Naturaleza (SbN).
        """)
        
        st.markdown("""
        <div class="alerta-territorial">
            <strong>⚠️ Vulnerabilidad Estructural Detectada:</strong> Riesgo creciente en la provisión de servicios hídricos debido a la degradación de coberturas riparias en microcuencas rurales abastecedoras.
        </div>
    """, unsafe_allow_html=True)
        
    with col_img_se:
        try:
            st.image("data/SE Riparios 2.png", caption="Esquema Técnico de Beneficios y Servicios Ecosistémicos Riparios", use_container_width=True)
        except:
            st.warning("Subiendo esquema analítico de servicios riparios...")


# ==========================================
# ENFOQUE 2: RUTA DE NAVEGACIÓN TÁCTICA
# ==========================================
elif modo_vista == "Ruta de Navegación Táctica":
    st.markdown("<p style='color:#0284C7; font-weight:700; text-transform:uppercase; margin-bottom:0;'>Matriz Operativa Interactiva</p>", unsafe_allow_html=True)
    st.markdown("<h1>Plan Táctico de Seguridad Hídrica (PlanTacticoSH_CV)</h1>", unsafe_allow_html=True)
    st.markdown("Filtre la matriz oficial de forma dinámica para enfocar el debate de la Junta:")
    st.markdown("---")
    
    # Carga de la matriz técnica que subiste
    @st.cache_data
    def cargar_datos_matriz():
        try:
            df = pd.read_csv("data/PlanTacticoSH_CV.xls")
            # Limpieza básica de nombres de columnas
            df.columns = [c.strip() for c in df.columns]
            return df
        except:
            # Datos de respaldo estructurados por si cambia la ruta
            return pd.DataFrame({
                "Línea Estratégica": ["Línea 1", "Línea 2", "Línea 3"],
                "Acción Estratégica": ["1.1 Pacto de Información", "2.1 Gran Pacto SH", "3.1 Corredor Vivo"],
                "Descripción": ["Intercambio de información", "Gobernanza multiescala", "6km de intervenciones"],
                "Fase I": ["●", "●", "●"],
                "Fase II": ["●", "", "●"],
                "Fase III": ["", "", "●"]
            })

    df_matriz = cargar_datos_matriz()
    
    # 🎛️ CONTROLES DINÁMICOS PARA LA JUNTA (Filtros amigables)
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        lineas_disponibles = df_matriz["Línea Estratégica"].dropna().unique()
        linea_sel = st.selectbox("Seleccione la Línea de Trabajo:", ["Todas"] + list(lineas_disponibles))
    with col_f2:
        fase_sel = st.segmented_control("Filtrar por Horizonte Temporal de Ejecución:", ["Todas", "Fase I (Comprender)", "Fase II (Acordar)", "Fase III (Hacer)"], default="Todas")
        
    # Aplicación de filtros lógicos en cascada
    df_filtrado = df_matriz.copy()
    if linea_sel != "Todas":
        df_filtrado = df_filtrado[df_filtrado["Línea Estratégica"] == linea_sel]
        
    if fase_sel == "Fase I (Comprender)":
        df_filtrado = df_filtrado[df_filtrado["Fase I"].isin(["●", "● ", " ●"])]
    elif fase_sel == "Fase II (Acordar)":
        df_filtrado = df_filtrado[df_filtrado["Fase II"].isin(["●", "● ", " ●"])]
    elif fase_sel == "Fase III (Hacer)":
        df_filtrado = df_filtrado[df_filtrado["Fase III"].isin(["●", "● ", " ●"])]
        
    # Renderizado estético de la tabla oficial transformándola en interactiva
    st.markdown("### 📋 Acciones y Actividades Programadas")
    st.dataframe(
        df_filtrado,
        column_config={
            "Línea Estratégica": st.column_config.TextColumn("Línea", width="medium"),
            "Acción Estratégica": st.column_config.TextColumn("Acción Estratégica", width="large"),
            "Descripción": st.column_config.TextColumn("Descripción Detallada", width="large"),
            "Actividades": st.column_config.TextColumn("Actividades de Entrega", width="large"),
        },
        use_container_width=True,
        hide_index=True
    )


# ==========================================
# ENFOQUE 3: METAS E INDICADORES DE IMPACTO
# ==========================================
elif modo_vista == "Metas e Indicadores de Impacto":
    st.markdown("<p style='color:#10B981; font-weight:700; text-transform:uppercase; margin-bottom:0;'>Monitoreo Físico y Retorno Ecosistémico</p>", unsafe_allow_html=True)
    st.markdown("<h1>Compromisos Globales y Dashboard del SIHT-CV</h1>", unsafe_allow_html=True)
    st.markdown("---")
    
    col_ods, col_metas = st.columns([1, 1])
    
    with col_ods:
        st.markdown("### 🌍 Contribución Directa a los ODS")
        st.write("""
        Las metas e intervenciones definidas en el horizonte 2026-2027 no son esfuerzos aislados. 
        Están diseñadas metodológicamente para asegurar el cumplimiento transversal de las metas globales del agua, la acción climática y las alianzas territoriales.
        """)
        try:
            st.image("data/ODS_CV.png", caption="Alineación Estratégica de CuencaVerde con las Metas Globales", use_container_width=True)
        except:
            st.info("Cargando matriz ODS...")
            
    with col_metas:
        st.markdown("### 📊 Hojas de Ruta Analíticas de Indicadores")
        st.write("Seleccione una de las fichas de metas analizadas por el equipo técnico:")
        
        ficha_sel = st.radio(
            "Seleccionar Ficha de Entrega:",
            ["Ficha 1 - Línea de Base", "Ficha 2 - Inteligencia Hidro-Territorial", "Ficha 3 - Gobernanza Multinivel", "Ficha 4 - Intervenciones SbN", "Ficha 5 - Gestión del Monitoreo"]
        )
        
        # Diccionario para mapear de forma segura las imágenes que subiste
        fichas_img = {
            "Ficha 1 - Línea de Base": "data/Metas_Indicadores_P1.png",
            "Ficha 2 - Inteligencia Hidro-Territorial": "data/Metas_Indicadores_P2.png",
            "Ficha 3 - Gobernanza Multinivel": "data/Metas_Indicadores_P3.png",
            "Ficha 4 - Intervenciones SbN": "data/Metas_Indicadores_P4.png",
            "Ficha 5 - Gestión del Monitoreo": "data/Metas_Indicadores_P5.png"
        }
        
        try:
            st.image(fichas_img[ficha_sel], caption=f"Desglose Técnico: {ficha_sel}", use_container_width=True)
        except:
            st.warning(f"Asegúrate de que el archivo {fichas_img[ficha_sel]} se encuentre en la carpeta data/")
