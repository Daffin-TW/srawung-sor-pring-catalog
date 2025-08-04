import streamlit as st

# Tampilan halaman berhasil registrasi
st.markdown("""
<div style='text-align: center; padding-top: 50px;'>
    <h2 style='color: green;'>✅ Registrasi Berhasil!</h2>
    <p style='font-size: 16px; color: #333;'>
        Akun Anda berhasil dibuat. Silakan lanjut ke halaman utama untuk login atau menjelajahi katalog UMKM.
    </p>
</div>
""", unsafe_allow_html=True)

# Tombol ke halaman main.py
_, col, _ = st.columns([1, 3, 1])

if col.button('🏠 Kembali ke Halaman Utama', use_container_width=True):
    st.switch_page('main.py')