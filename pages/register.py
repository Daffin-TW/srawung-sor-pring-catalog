# Streamlit imports
from streamlit import session_state as ss
import streamlit as st

# Custom package imports
from modules import page_init


# Initial
current_page = 'register'

page_init.init_configuration(layout='centered')
page_init.init_style()

with st.sidebar:
    st.title("Srawung Sor Pring")
    st.subheader('Katalog UMKM Taman Harmoni')

    _, img_col, _ = st.columns([.1, .5, .1])

    img_col.image(
        'src/img/srawung_sor_pring_logo.png', use_container_width=True,
    )
    
    st.divider()
    
    if st.button('Kembali', key="back_button", use_container_width=True):
        st.switch_page('main.py')

    st.divider()

    st.markdown(
        '<div class="sidebar-footer">© 2025 KKN 139 Arundiswara</div>',
        unsafe_allow_html=True
    )

# ==== Header Register ====
st.markdown("""
<div class="register-header">
    <h1>📝 Daftar UMKM</h1>
    <p>Lengkapi data berikut untuk mendaftarkan UMKM Anda di katalog digital Srawung Sor Pring.</p>
</div>
""", unsafe_allow_html=True)

# ==== Form Registrasi ====
with st.form("register_form", clear_on_submit=False):
    st.subheader("📧 Informasi Akun")
    email = st.text_input("Email")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    st.subheader("🏪 Informasi UMKM")
    nama_umkm = st.text_input("Nama UMKM")
    logo_umkm = st.file_uploader("Logo UMKM (opsional)", type=["png", "jpg", "jpeg"])
    tipe_umkm = st.selectbox("Tipe UMKM", ["Makanan", "Minuman", "Pakaian", "Kerajinan", "Lainnya"])
    deskripsi = st.text_area("Deskripsi Singkat UMKM", max_chars=300)

    st.subheader("📞 Kontak UMKM")
    nama_pemilik = st.text_input("Nama Pemilik")
    instagram = st.text_input("Instagram (opsional)")
    no_telepon = st.text_input("Nomor Telepon")

    submit = st.form_submit_button("Daftar Sekarang")

    condition = all([
        email, username, password, nama_umkm, tipe_umkm,
        deskripsi, nama_pemilik, no_telepon
    ])

    if submit:
        if condition:
            msg = 'Registrasi berhasil! Silakan tunggu verifikasi admin'
            st.success(msg)
            st.toast(msg,  icon='✅')
            # Di sini bisa ditambahkan penyimpanan data ke database / file
        else:
            msg = 'Registrasi gagal, tolong isi form yang masih kosong!'
            st.error(msg)
            st.toast(msg,  icon='⚠️')
    