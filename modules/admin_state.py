from streamlit import session_state as ss


def check_admin_state():
    if not ss.get('admin_state', ''):
        ss.admin_state = False
        return False
    
    else:
        return True