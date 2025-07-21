from streamlit import session_state as ss
import streamlit as st


def init_configuration(sidebar: str = 'auto'):
    st.set_page_config(
        page_title='Katalog Srawung Sor Pring',
        page_icon='src/img/logo_arundiswara.png',
        initial_sidebar_state=sidebar,
        layout='wide',
    )

def init_style():
    with open( "style.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>', unsafe_allow_html=True)

def init_sidebar():
    with st.sidebar:
        st.title("Srawung Sor Pring")
        st.subheader('Katalog UMKM Taman Harmoni')

        _, img_col, _ = st.columns([.1, .5, .1])

        img_col.image(
            'src/img/srawung_sor_pring_logo.png', use_container_width=True,
        )
        
        st.divider()

        if not ss.get('navigation', ''):
            ss.navigation = '🏠︎ Beranda'

        ss.navigation = st.radio(
            'navigasi',
            [
                "🏠︎ Beranda", 
                "🛒 Katalog", 
                "📌 Tentang Kami"
            ],
            label_visibility='collapsed',
        )

        st.markdown(
            '<div class="sidebar-footer">© 2025 KKN 139 Arundiswara</div>',
            unsafe_allow_html=True
        )