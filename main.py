# Streamlit imports
from streamlit import session_state as ss
from streamlit import secrets as sc
import streamlit as st

# Custom package imports
from modules import init_configuration, init_sidebar, init_style


init_configuration()
init_sidebar()
init_style()

print(ss.get('navigation', ''))