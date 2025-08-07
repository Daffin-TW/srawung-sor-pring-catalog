# Streamlit imports
from streamlit import session_state as ss
from streamlit import secrets as sc
import streamlit as st

# Custom package imports
from modules import page_init
import pandas as pd
import random


# Initial
current_page = '🏠︎ Beranda'

page_init.init_configuration()
page_init.init_sidebar()
page_init.init_style()
page_init.init_navigation(current_page)

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

plan_col1, plan_col2 = st.columns([1, 2])

# Denah
with plan_col1:
    st.markdown("### 🗺️ Denah Lokasi")
    st.image('src/img/site_plan.png', use_container_width=10)

# Petunjuk Belanja
with plan_col2:
    st.markdown("### 📌 Petunjuk Belanja")
    st.markdown("""
    <ol style='font-size: 16px; padding-left: 20px; color: #444;'>
    <li>Pengunjung yang akan belanja wajib menggunakan <b>koin Srawung Sor Pring</b> yang dapat ditukar di loket informasi.</li>
    <li>Uang koin yang disediakan terdiri dari pecahan <b>2K, 3K, 5K, 10K, dan 20K</b>.</li>
    <li>Setiap pengunjung yang ingin membawa pulang makanan dan minuman <b>tersedia tas belanja berbayar</b>.</li>
    <li>Jika masih memiliki sisa koin, dapat ditukar kembali di loket informasi.</li>
    <li>Jaga kebersihan area <b>Srawung Sor Pring</b> dengan membuang sampah pada tempat yang disediakan.</li>
    </ol>
    """, unsafe_allow_html=True)

st.divider()

# Penjelasan tentang Srawung Sor Pring + ilustrasi di samping
st.markdown("### 🤝 Apa itu Srawung Sor Pring?")
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
        <p>
        <strong>Srawung Sor Pring</strong> adalah sebuah inisiatif yang menghadirkan beragam pelaku Usaha Mikro, Kecil, dan Menengah (UMKM) dalam satu ruang terbuka yang asri.
        </p>

        <p>
        Melalui website ini, pengunjung dapat dengan mudah:
        <ul>
            <li>Menjelajahi berbagai <strong>menu dan produk</strong> yang ditawarkan oleh UMKM,</li>
            <li>Menemukan informasi lengkap seperti <strong>lokasi, jadwal shift, dan jenis usaha</strong>,</li>
            <li>Serta melihat <strong>kabar dan aktivitas terbaru</strong> dari komunitas Srawung Sor Pring.</li>
        </ul>
        </p>

        <p>
        Selain berfungsi sebagai katalog digital, website ini juga menjadi jembatan antara UMKM dan pengunjung, 
        mempermudah transaksi, memperluas jangkauan promosi, dan menciptakan pengalaman berbelanja yang lebih terarah dan menyenangkan.
        </p>
    """, unsafe_allow_html=True)

with col2:
    st.image('src/img/taman_harmoni.jpg', use_container_width=10)

st.divider()

cat_cols = st.columns([2, 1])
cat_cols[0].markdown('### 🛒 Akses Katalog UMKM Srawung Sor Pring')
if cat_cols[1].button('**🏷️ Katalog UMKM**'):
    ss.navigation = '🛒 Katalog'
    st.rerun()

st.divider()

# Footer
st.markdown("""
<div style='text-align: center; font-size: 14px; color: #aaa; padding: 20px 0;'>
    © 2025 Srawung Sor Pring • KKN Kelompok 139 Arundiswara
</div>
""", unsafe_allow_html=True)
