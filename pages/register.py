# Streamlit imports
from streamlit import session_state as ss
import streamlit as st

# Custom package imports
from modules import page_init, umkm_registration, fetch_data


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
    email = st.text_input("Email", max_chars=100)
    username = st.text_input("Username", max_chars=15).lower()
    username = username.replace(' ', '')
    st.write('*username tanpa spasi dan menggunakan huruf kecil')
    password = st.text_input("Password", type="password", max_chars=100)

    st.subheader("🏪 Informasi UMKM")
    nama_umkm = st.text_input("Nama UMKM", max_chars=50)
    logo_umkm = st.file_uploader("Logo UMKM (opsional)", type=["png", "jpg", "jpeg"])
    tipe_umkm = st.selectbox("Tipe UMKM", ["Makanan", "Minuman", "Pakaian", "Kerajinan", "Lainnya"])
    deskripsi = st.text_area("Deskripsi Singkat UMKM", max_chars=512)

    st.subheader("📞 Kontak UMKM")
    nama_pemilik = st.text_input("Nama Pemilik", max_chars=100)
    instagram = st.text_input("Instagram (opsional)", max_chars=50)
    no_telepon = st.text_input("Nomor Telepon", max_chars=15)

    submit = st.form_submit_button("Daftar Sekarang")

    logo_umkm = ''  # Image upload incompatibility

    data = (
        username, email, password, nama_umkm, logo_umkm, tipe_umkm,
        deskripsi, nama_pemilik, instagram, no_telepon
    )

    condition = all([
        email, username, password, nama_umkm, tipe_umkm,
        deskripsi, nama_pemilik, no_telepon
    ])

    if submit:
        umkm_cred = fetch_data('umkm_credentials')

        if username in umkm_cred.index or email in umkm_cred.email:
            msg = 'Registrasi gagal, email/username telah digunakan!'
            st.error(msg)
            st.toast(msg, icon='⚠️')

        elif condition:
            result = umkm_registration(data)
            print(result)
            
            if result:
                msg = 'Registrasi berhasil! Silakan tunggu verifikasi admin'
                st.success(msg)
                st.toast(msg,  icon='✅')
                st.switch_page('pages/registered.py')
            
            else:
                msg = 'Registrasi gagal, mohon persingkat beberapa form!'
                st.error(msg)
                st.toast(msg, icon='⚠️')

        else:
            msg = 'Registrasi gagal, tolong isi form yang masih kosong!'
            st.error(msg)
            st.toast(msg, icon='⚠️')
    