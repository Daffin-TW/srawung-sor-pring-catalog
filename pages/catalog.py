# Streamlit imports
from streamlit import session_state as ss
from streamlit import secrets as sc
import streamlit as st

# Custom package imports
from modules import page_init
import pandas as pd

# Initial
current_page = '🛒 Katalog'

page_init.init_configuration(layout='centered')
page_init.init_sidebar()
page_init.init_style()
page_init.init_navigation(current_page)


# Load data
umkm_df = pd.read_csv("src/data/umkm.csv", delimiter=';')

# === Header ===
st.markdown("""
<div class="katalog-header">
    <h1>📦 Katalog UMKM</h1>
    <p>Jelajahi berbagai produk menarik dari UMKM di Srawung Sor Pring!</p>
</div>
""", unsafe_allow_html=True)

# === Filter Search ===
search = st.text_input("🔍 Cari UMKM atau produk...")

# === Tampilkan UMKM ===
for _, row in umkm_df.iterrows():
    umkm_nama = row['nama_umkm']
    
    # Filter jika tidak sesuai search
    if search and search.lower() not in umkm_nama.lower():
        continue

    st.markdown(f"""
    <div class="umkm-card">
        <div class="umkm-info">
            <iframe src="{row['logo']}" class="umkm-logo" allow="autoplay"></iframe>
            <div>
                <h3>{row['nama_umkm']}</h3>
                <p><i>{row['jenis_umkm']}</i> · Shift {row['shift']}</p>
                <p>{row['deskripsi_umkm']}</p>
                <p><b>Kontak:</b> {row['notelp']} · IG: @{row['instagram']}</p>
                <a href="#{umkm_nama.replace(' ', '-')}" class="lihat-produk-btn">🔎 Lihat Produk</a>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
