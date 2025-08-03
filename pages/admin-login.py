# Streamlit imports
from streamlit import session_state as ss
from streamlit import secrets as sc
import streamlit as st

# Custom package imports
from modules import page_init, fetch_data, admin_state


# Initial
current_page = 'admin-login'

page_init.init_configuration(layout='centered')
page_init.init_style()

if admin_state.check_admin_state():
    st.switch_page('pages/admin.py')

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

# ==== Header Login ====
st.markdown("""
<div class="login-header">
    <h1>🔐 Login Akun Admin</h1>
    <p>Masuk untuk mengelola berkas UMKM di Srawung Sor Pring.</p>
</div>
""", unsafe_allow_html=True)

# Admin Credentials
df_cred = fetch_data('admin')

with st.form("login_form", clear_on_submit=True):
    username = st.text_input("Username").lower()
    password = st.text_input("Password", type="password")
    
    if st.form_submit_button("Login"):
        try:
            cred_pass = df_cred.loc[username].password
            
            if password == cred_pass:
                ss.admin_state = True
                st.switch_page('pages/admin.py')
        
            else:
                st.error('Username tidak ditemukan / Password tidak cocok')
        
        except KeyError as e:
            st.error('Username tidak ditemukan / Password tidak cocok')