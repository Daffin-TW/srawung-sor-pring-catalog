# Streamlit imports
from streamlit import session_state as ss
from streamlit import secrets as sc
import streamlit as st
import random

# Custom package imports
from modules import (
    init_configuration, init_sidebar, init_style, init_navigation
)


# Initial
current_page = '🏠︎ Beranda'

init_configuration()
init_sidebar()
init_style()
init_navigation(current_page)

# ===== Dummy Data UMKM =====
umkm_data = [
    {"nama": "Warung Mbak Sri", "deskripsi": "Nasi pecel dan aneka gorengan"},
    {"nama": "Kopi Pring", "deskripsi": "Kopi seduh bambu khas lokal"},
    {"nama": "Wedang Sinom", "deskripsi": "Minuman herbal tradisional"},
    {"nama": "Jajanan Pak Dhe", "deskripsi": "Cilok, batagor, dan jajanan anak"},
    {"nama": "Kerajinan Bambu", "deskripsi": "Keranjang, vas, dan souvenir bambu"}
]

umkm_terpilih = random.sample(umkm_data, 3)

# ===== Tampilan Utama =====

# Judul
st.markdown("<h1 style='text-align: center;'>🌿 Srawung Sor Pring</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Platform digital untuk menjelajahi UMKM lokal di Taman Harmoni</p>", unsafe_allow_html=True)
st.divider()

# Denah (placeholder)
st.markdown("### 🗺️ Denah Lokasi")
st.markdown("""
<div style='width: 100%; height: 200px; background-color: #e8e8e8; border-radius: 10px; display: flex; align-items: center; justify-content: center;'>
    <p style='color: #555;'>[Placeholder Denah Lokasi]</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# Penjelasan tentang Srawung Sor Pring + ilustrasi di samping
st.markdown("### 🤝 Apa itu Srawung Sor Pring?")
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    <p style='font-size: 16px; text-align: justify;'>
    <b>Srawung Sor Pring</b> adalah kumpulan UMKM yang tumbuh di bawah rindangnya taman bambu di Taman Harmoni. 
    Melalui website ini, pengunjung dapat dengan mudah melihat daftar menu, lokasi, serta informasi terkini dari UMKM yang tersedia.
    </p>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style='width: 100%; height: 150px; background-color: #d4d4d4; border-radius: 10px; display: flex; align-items: center; justify-content: center;'>
        <p style='color: #555;'>[Ilustrasi Srawung]</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# UMKM Pilihan Hari Ini
st.markdown("### 🌟 UMKM Pilihan Hari Ini")

cols = st.columns(3)
for i, umkm in enumerate(umkm_terpilih):
    with cols[i]:
        st.markdown(f"""
        <div style='background-color: #f2f2f2; padding: 12px; border-radius: 10px; min-height: 120px;'>
            <h4 style='margin-bottom: 5px;'>{umkm['nama']}</h4>
            <p style='font-size: 14px; color: #555;'>{umkm['deskripsi']}</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# ====================
# Petunjuk Belanja
# ====================

st.markdown("### 📌 Petunjuk Belanja")
st.markdown("""
<ol style='font-size: 16px; padding-left: 20px; color: #444;'>
  <li>Pengunjung yang akan belanja wajib menggunakan <b>koin Srawung Sor Pring</b> yang dapat ditukar di loket informasi.</li>
  <li>Uang koin yang disediakan terdiri dari pecahan <b>2K, 3K, 5K, 10K, dan 20K</b>.</li>
  <li>Pengunjung yang membeli makanan untuk dibawa pulang diharapkan membawa <b>tas belanja sendiri</b>.</li>
  <li>Jika masih memiliki sisa koin, dapat ditukar kembali di loket informasi.</li>
  <li>Jaga kebersihan area <b>Srawung Sor Pring</b> dengan membuang sampah pada tempat yang disediakan.</li>
</ol>
""", unsafe_allow_html=True)

st.divider()

# Footer
st.markdown("""
<div style='text-align: center; font-size: 14px; color: #aaa; padding: 20px 0;'>
    © 2025 Srawung Sor Pring • KKN Kelompok 139 Arundiswara
</div>
""", unsafe_allow_html=True)
