from streamlit import session_state as ss


def check_umkm_state():
    if not ss.get('umkm_state', ''):
        ss.umkm_state = False
        return False
    
    else:
        return True