# Streamlit imports
from streamlit import session_state as ss
from streamlit import secrets as sc
import streamlit as st

# Custom package imports
from modules import page_init

# Initial
current_page = '📌 Tentang Kami'

page_init.init_configuration()
page_init.init_sidebar()
page_init.init_style()
page_init.init_navigation(current_page)

# ==== HEADER ====
st.markdown("<div id='about-header'><h1>👥 Tentang Kami</h1></div>", unsafe_allow_html=True)
st.markdown("<p id='about-sub'>Website ini dikembangkan oleh Tim KKN Arundiswara 139 untuk mendukung UMKM Srawung Sor Pring di Taman Harmoni.</p>", unsafe_allow_html=True)

# ==== PENJELASAN WEBSITE ====
st.markdown("""
<div class="about-section">
    <h2>🌱 Apa itu Srawung Sor Pring?</h2>
    <p>
        Srawung Sor Pring adalah pasar UMKM yang berada di Taman Harmoni. Pasar ini menghadirkan berbagai produk lokal seperti makanan, minuman, dan kerajinan tangan yang dibuat oleh warga sekitar.
        Website ini bertujuan mempermudah pengunjung untuk melihat daftar menu tiap UMKM, serta mempercepat proses informasi dengan sistem katalog digital.
    </p>
</div>
""", unsafe_allow_html=True)

# ==== TIM KKN ====
st.markdown("""
<div class="about-section">
    <h2>🧑‍💻 Tim Pengembang</h2>
    <ul class="team-list">
        <li>Anggota 1 — Developer & UI/UX</li>
        <li>Anggota 2 — Dokumentasi & UMKM</li>
        <li>Anggota 3 — Koordinasi Lapangan</li>
        <li>Anggota 4 — Konten & Media</li>
        <li>Anggota 5 — Publikasi</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ==== FOOTER ====
st.markdown("""
<hr>
<div id="about-footer">
    <p>© 2025 Tim KKN Arundiswara 139</p>
</div>
""", unsafe_allow_html=True)
