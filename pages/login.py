# Streamlit imports
from streamlit import session_state as ss
import streamlit as st

# Custom package imports
from modules import page_init


# Initial
current_page = 'login'

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

# ==== Header Login ====
st.markdown("""
<div class="login-header">
    <h1>🔐 Login Akun UMKM</h1>
    <p>Masuk untuk mengelola menu UMKM Anda di Srawung Sor Pring.</p>
</div>
""", unsafe_allow_html=True)


with st.form("login_form", clear_on_submit=False):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

st.markdown("""
    <div style='margin-top: 20px; text-align: center;'>
        Belum punya akun? <a href="/register" target="_self">Daftar di sini</a>
    </div>
    """,
    unsafe_allow_html=True
)