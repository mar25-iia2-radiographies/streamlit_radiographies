import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Exploration des données",
    page_icon="📊",
    layout="wide"
)

# ================= CSS =================
st.markdown("""
<style>

/* Réduire l'espace en haut de la page */
.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
}

.main-title{
    font-size:36px;
    font-weight:700;
    margin-bottom:20px;
}

.section-title{
    font-size:20px;
    font-weight:600;
    margin-top:20px;
    margin-bottom:15px;
}

.info-box{
    background-color:#f6f8fc;
    padding:20px;
    border-radius:15px;
    margin-top:15px;
    margin-bottom:30px;
    font-size:16px;
    line-height:2;
}

.comment-box{
    background-color:#f6f8fc;
    padding:12px;
    border-radius:10px;
    margin-top:15px;
    margin-bottom:25px;
    font-size:15px;
}

</style>
""", unsafe_allow_html=True)

# ================= TITLE =================
st.markdown(
    """
    <div class="main-title">
    📊 Exploration des données
    </div>
    """,
    unsafe_allow_html=True
)

# ================= GENERAL INFORMATION =================
st.markdown(
    """
    <div class="info-box">

    • <b>Nombre total d'images :</b> 21 165<br>

    • <b>Taille des images :</b> 299 × 299 pixels<br>

    • <b>Taille des masques :</b> 299 × 299 pixels<br>

    • <b>99,3 % des images</b> sont en niveaux de gris (Grayscale).<br>

    • <b>0,7 % des images</b> (140 images de la classe Viral Pneumonia)
    sont au format RGB.

    </div>
    """,
    unsafe_allow_html=True
)

# ================= CLASS DISTRIBUTION =================
st.markdown(
    """
    <div class="section-title">
    📈 Répartition des images par catégorie
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 3, 1])

with col2:
    st.image(
        "images/class_distribution_enhanced.png",
        width=600
    )

st.markdown(
    """
    <div class="comment-box">
    La classe <b>Normal</b> est la plus représentée (48,2 %),
    tandis que la classe <b>Viral Pneumonia</b> est la moins représentée (6,4 %).
    </div>
    """,
    unsafe_allow_html=True
)

# ================= HISTOGRAMS =================
st.markdown(
    """
    <div class="section-title">
    📉 Analyse des histogrammes de niveaux de gris
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    st.image(
        "images/gray_histogram.png",
        width=750
    )

st.markdown(
    """
    <div class="comment-box">
    Les distributions des niveaux de gris diffèrent légèrement entre les catégories,
    indiquant la présence de caractéristiques visuelles discriminantes. Cependant,
    ces différences restent insuffisantes pour une séparation directe des classes.
    </div>
    """,
    unsafe_allow_html=True
)