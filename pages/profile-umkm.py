# Streamlit imports
from streamlit import session_state as ss
from streamlit import secrets as sc
import streamlit as st

# Custom package imports
from modules import (
    page_init, fetch_data_filter, fetch_data, check_umkm_state, umkm_update
)
import pandas as pd


@st.dialog('Rubah Informasi UMKM', width='large')
def profile_editing(data: pd.DataFrame):
    username = ss.umkm_state

    with st.form("register_form", clear_on_submit=False):
        st.subheader("🏪 Informasi UMKM")
        nama_umkm = st.text_input(
            "Nama UMKM", max_chars=50, value=data.umkm_name
        )
        logo_umkm = st.file_uploader("Logo UMKM (opsional)", type=["png", "jpg", "jpeg"])
        tipe = [
                "Makanan", "Minuman", "Pakaian", "Kerajinan", "Lainnya"
            ]
        tipe_umkm = st.selectbox(
            "Tipe UMKM",
            tipe,
            index=tipe.index(data.umkm_type)
        )
        deskripsi = st.text_area(
            "Deskripsi Singkat UMKM", max_chars=512, value=data.description
        )

        st.subheader("📞 Kontak UMKM")
        nama_pemilik = st.text_input(
            "Nama Pemilik", max_chars=100, value=data.owner_name
        )
        instagram = st.text_input(
            "Instagram (opsional)", max_chars=50, value=data.instagram
        )
        no_telepon = st.text_input(
            "Nomor Telepon", max_chars=15, value=data.phone_number
        )

        submit = st.form_submit_button("Simpan Perubahan")

        data = (
            nama_umkm, logo_umkm, tipe_umkm,
            deskripsi, nama_pemilik, instagram, no_telepon
        )

        condition = all([
            nama_umkm, tipe_umkm,
            deskripsi, nama_pemilik, no_telepon
        ])

        if submit:
            if condition:
                umkm_update('information', username, data)
                st.cache_data.clear()
                st.rerun()
            else:
                msg = 'Perubahan informasi gagal, tolong isi form yang masih kosong!'
                st.error(msg)
                st.toast(msg, icon='⚠️')

@st.dialog('Rubah Username UMKM', width='large')
def edit_username(data: pd.DataFrame):
    username = ss.umkm_state

    with st.form("register_form", clear_on_submit=False):
        st.subheader("📋 Email dan Username UMKM Saat Ini")
        st.write(f'### {data.email} | {username}')

        email = st.text_input("Email", max_chars=100, value=data.email)
        new_username = st.text_input(
            "Username Baru", max_chars=15, value=username
        ).lower()
        new_username = new_username.replace(' ', '')

        submit = st.form_submit_button("Rubah Informasi")

        data = (new_username, email)

        if submit:
            umkm_cred = fetch_data_filter('umkm_credentials', username)

            if username in umkm_cred.index or email in umkm_cred.email:
                msg = 'Perubahan informasi gagal, email/username telah digunakan!'
                st.error(msg)
                st.toast(msg, icon='⚠️')
            
            elif all(data):
                umkm_update('username', username, data)
                ss.umkm_state = new_username
                st.cache_data.clear()
                st.rerun()

            else:
                msg = 'Perubahan informasi gagal, tolong isi form yang masih kosong!'
                st.error(msg)
                st.toast(msg, icon='⚠️')

@st.dialog('Rubah Password UMKM', width='large')
def edit_password(data: pd.DataFrame):
    username = ss.umkm_state

    with st.form("register_form", clear_on_submit=False):

        password = st.text_input("Password", type="password", max_chars=100)
        verification = st.text_input("Ketik Ulang Password", type="password", max_chars=100)

        submit = st.form_submit_button("Rubah Password")

        data = (password, )

        if submit:
            if password != verification:
                msg = 'Password tidak sama, mohon isi ulang password!'
                st.error(msg)
                st.toast(msg, icon='⚠️')

            elif password == verification and all([password, verification]):
                umkm_update('password', username, data)

                st.cache_data.clear()
                st.rerun()

            else:
                msg = 'Perubahan informasi gagal, tolong isi form yang masih kosong!'
                st.error(msg)
                st.toast(msg, icon='⚠️')


# Initial
current_page = 'profile-umkm'

page_init.init_configuration(layout='wide')
page_init.init_style()

if not check_umkm_state():
    st.switch_page('pages/login.py')

with st.sidebar:
    st.title("Srawung Sor Pring")
    st.subheader('Katalog UMKM Taman Harmoni')

    _, img_col, _ = st.columns([.1, .5, .1])

    img_col.image(
        'src/img/srawung_sor_pring_logo.png', use_container_width=True,
    )
    
    st.divider()
    
    if st.button('Log Out', key="back_button", use_container_width=True):
        ss.umkm_state = False
        st.switch_page('main.py')

    st.divider()

    st.markdown(
        '<div class="sidebar-footer">© 2025 KKN 139 Arundiswara</div>',
        unsafe_allow_html=True
    )

st.markdown("""
    <div style='text-align: center; margin-top: 30px; margin-bottom: 20px;'>
        <h2>
            📋 Panel UMKM - Data Produk
        </h2>
    </div>
""", unsafe_allow_html=True)

username = ss.umkm_state

st.write('### 📒 Identitas UMKM')

df_umkm = fetch_data_filter('umkm', username).iloc[0]

identity_container = st.container(border=True)
id_cols = identity_container.columns([0.5, 0.7, 1, 0.7], gap='medium')

with id_cols[0]:
    st.write('#### Logo UMKM')

    if df_umkm.logo == 'Null':
        st.image(f'src/img/missing_logo.png')
    else:
        st.image(df_umkm.logo)

with id_cols[1]:
    st.write('#### Keterangan Akun')
    st.write(f'Username: {username}')
    st.write(f'Email: {df_umkm.email}')
    
with id_cols[2]:
    st.write('#### Deskripsi UMKM')
    st.write(f'Nama UMKM: {df_umkm.umkm_name}')
    st.write(f'Tipe UMKM: {df_umkm.umkm_type}')
    st.write(df_umkm.description)

with id_cols[3]:
    st.write('#### Keterangan Pemilik')
    st.write(f'Nama Pemilik: {df_umkm.owner_name}')
    st.write(f'Instagram: {df_umkm.instagram}')
    st.write(f'No. Telp: {df_umkm.phone_number}')

id_button_cols = identity_container.columns([2.5, 0.5, 0.5, 0.5])

if id_button_cols[1].button('Rubah Informasi'):
    profile_editing(df_umkm)

if id_button_cols[2].button('Rubah Username'):
    edit_username(df_umkm)

if id_button_cols[3].button('Rubah Password'):
    edit_password(df_umkm)