# Streamlit imports
from streamlit import session_state as ss
from streamlit import secrets as sc
import streamlit as st

# Custom package imports
from modules import page_init

# Initial
current_page = '🛒 Katalog'

page_init.init_configuration()
page_init.init_sidebar()
page_init.init_style()
page_init.init_navigation(current_page)

# ==== Header ====
st.markdown("<div id='katalog-header'><h1>📦 Katalog UMKM</h1></div>", unsafe_allow_html=True)
st.markdown("<p id='katalog-sub'>Temukan menu terbaik dari UMKM yang ada di Srawung Sor Pring.</p>", unsafe_allow_html=True)

# ==== Pilihan UMKM dan Tombol ====
st.markdown("<div id='katalog-controls'>", unsafe_allow_html=True)

umkm_list = ["Warung Mbah Darmo", "Es Dawet Bu Sri", "Nasi Bakar Kang Rudi", "Tahu Crispy Mbak Ita"]
selected_umkm = st.selectbox("Pilih UMKM", umkm_list, index=0)

col1, col2 = st.columns([3, 1])
with col1:
    search_term = st.text_input("Cari menu atau produk", placeholder="Contoh: es dawet, nasi bakar...")
with col2:
    search_clicked = st.button("🔍 Cari")

st.markdown("</div>", unsafe_allow_html=True)

# ==== Footer ====
st.markdown("""
<hr>
<div id='katalog-footer'>
    <p>© 2025 KKN Arundiswara 139 — Srawung Sor Pring</p>
</div>
""", unsafe_allow_html=True)
