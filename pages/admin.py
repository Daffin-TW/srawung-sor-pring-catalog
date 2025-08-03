# Streamlit imports
from streamlit import session_state as ss
from streamlit import secrets as sc
import streamlit as st

# Custom package imports
from modules import page_init, admin_state, fetch_data, umkm_verification
import pandas as pd


@st.dialog('Apakah anda yakin?', width='large')
def ver_decision(username: str, verified: bool):
    if verified:
        st.write(f'Verifikasi berkas milik {username}?')

        col1, col2 = st.columns(2)

        if col1.button('Verifikasi', use_container_width=True):
            umkm_verification(username, status=True)
            st.cache_data.clear()
            st.rerun()

        if col2.button('Batalkan', use_container_width=True):
            st.rerun()

    else:
        st.write(f'Menghapus berkas milik {username}?')

        col1, col2 = st.columns(2)

        if col1.button('Hapus', use_container_width=True):
            umkm_verification(username, status=False)
            st.cache_data.clear()
            st.rerun()

        if col2.button('Batalkan', use_container_width=True):
            st.rerun()

# Initial
current_page = 'admin'

page_init.init_configuration(layout='wide')
page_init.init_style()

if not admin_state.check_admin_state():
    st.switch_page('pages/admin-login.py')

with st.sidebar:
    st.title("Srawung Sor Pring")
    st.subheader('Katalog UMKM Taman Harmoni')

    _, img_col, _ = st.columns([.1, .5, .1])

    img_col.image(
        'src/img/srawung_sor_pring_logo.png', use_container_width=True,
    )
    
    st.divider()
    
    if st.button('Log Out', key="back_button", use_container_width=True):
        ss.admin_state = False
        st.switch_page('main.py')

    st.divider()

    st.markdown(
        '<div class="sidebar-footer">© 2025 KKN 139 Arundiswara</div>',
        unsafe_allow_html=True
    )

st.markdown("""
    <div style='text-align: center; margin-top: 30px; margin-bottom: 20px;'>
        <h2>
            📋 Panel Admin - Data UMKM Terdaftar
        </h2>
    </div>
""", unsafe_allow_html=True)

st.write('### Daftar Verifikasi Data UMKM')

df_umkm = fetch_data('umkm_unverified')

if not len(df_umkm):
    st.success('Tidak ada permintaan verifikasi berkas!')

else:
    ver_container = st.container(border=True)

    for username, row in df_umkm.iterrows():
        inner_container = ver_container.container(border=False)
        ver_cols = inner_container.columns([0.7, 1, 1, 1, 0.7])

        with ver_cols[0]:
            st.write('#### Logo UMKM')

            if row.logo == 'Null':
                st.image(f'src/img/missing_logo.png')
            else:
                st.image(row.logo)

        with ver_cols[1]:
            st.write('#### Keterangan Akun')
            st.write(f'Username: {username}')
            st.write(f'Email: {row.email}')
        
        with ver_cols[2]:
            st.write('#### Deskripsi UMKM')
            st.write(f'Nama UMKM: {row.umkm_name}')
            st.write(f'Tipe UMKM: {row.umkm_type}')
            st.write(row.description)

        with ver_cols[3]:
            st.write('#### Keterangan Pemilik')
            st.write(f'Nama Pemilik: {row.owner_name}')
            st.write(f'Instagram: {row.instagram}')
            st.write(f'No. Telp: {row.phone_number}')

        with ver_cols[4]:
            st.write('#### Verifikasi Berkas')
            ver_but_col1,ver_but_col2 = st.columns(2)
            
            if ver_but_col1.button('✅', key='acc_button' + username):
                ver_decision(username, True)

            if ver_but_col2.button('❌', key='dec_button' + username):
                ver_decision(username, False)

        inner_container.divider()

