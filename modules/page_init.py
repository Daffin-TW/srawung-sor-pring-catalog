from streamlit import session_state as ss
import streamlit as st


def init_configuration(sidebar: str = 'auto', layout: str = 'wide'):
    st.set_page_config(
        page_title='Katalog Srawung Sor Pring',
        page_icon='src/img/logo_arundiswara.png',
        initial_sidebar_state=sidebar,
        layout=layout,
    )

def init_style():
    with open("style.css") as css:
        st.markdown( f'<style>{css.read()}</style>', unsafe_allow_html=True)

def init_pages():
    return {
        '🏠︎ Beranda': 'main.py',
        '🛒 Katalog': 'pages/catalog.py',
        '📌 Tentang Kami': 'pages/about_us.py'
    }

def init_sidebar():
    with st.sidebar:
        st.title("Srawung Sor Pring")
        st.subheader('Katalog UMKM Taman Harmoni')

        _, img_col, _ = st.columns([.1, .5, .1])

        img_col.image(
            'src/img/srawung_sor_pring_logo.png', use_container_width=True,
        )
        
        st.divider()
        
        if st.button("Login", key="login_button", use_container_width=True):
            st.switch_page('pages/login.py')

        st.divider()

        pages = init_pages()
        pages_list = list(pages.keys())

        if not ss.get('navigation', ''):
            ss.navigation = pages_list[0]

        ss.navigation = st.radio(
            'navigasi', pages.keys(),
            index=pages_list.index(ss.navigation),
            label_visibility='collapsed',
        )

        st.markdown(
            '<div class="sidebar-footer">© 2025 KKN 139 Arundiswara</div>',
            unsafe_allow_html=True
        )

def init_navigation(current_page: str):
    pages = init_pages()

    if ss.get('navigation', '') != current_page:
        st.switch_page(pages[ss.navigation])