from streamlit import session_state as ss
from streamlit import secrets as sc
from warnings import filterwarnings
import mysql.connector
import streamlit as st
import pandas as pd


filterwarnings(
    "ignore",
    category=UserWarning,
    message='.*pandas only supports SQLAlchemy connectable.*'
)
pd.set_option('future.no_silent_downcasting', True)

st.cache_resource(show_spinner=False, ttl=300)
def connect_db():
    try:
        db_connection = mysql.connector.connect(
            host=sc.db_credentials.host,
            user=sc.db_credentials.username,
            password=sc.db_credentials.password,
            database=sc.db_credentials.database,
            port=sc.db_credentials.port,
            charset=sc.db_credentials.charset
        )

        return db_connection
    
    except:
        st.toast("""
            Mengalami kendala? Hubungi [Daffin_TW](https://wa.me/6282332232896)
            untuk bertanya atau perbaikan.
        """, icon='🚨')
        st.error('⛔ Database tidak bisa dihubungi.')
        st.stop()

@st.cache_data(show_spinner=False, ttl=300)
def sql_to_dataframe(sql: str):
    with st.spinner('Sedang memuat data, mohon ditunggu...'):
        db_conn = connect_db()
        df = pd.read_sql(sql, db_conn)
        db_conn.close()

    return df.set_index(df.columns[0])

def fetch_data(table: str):
    match table:
        case 'admin':
            sql = 'SELECT * FROM `admin`'

        case 'umkm':
            sql = 'SELECT * FROM umkm_identity'

        case 'umkm_credentials':
            sql = 'SELECT username, email, password FROM umkm_identity'

        case 'umkm_unverified':
            sql = 'SELECT * FROM umkm_identity WHERE verification=0'

        case 'umkm_verified':
            sql = 'SELECT * FROM umkm_identity WHERE verification=1'

        # case 'status_umkm_new':
        #     sql = """
        #         SELECT * FROM umkm_status WHERE modified IN (
        #         SELECT MAX(modified) FROM umkm_status GROUP BY umkm_username
        #     )
        #     """

        case _:
            raise KeyError(f'{table} tidak ditemukan di database')
    
    return sql_to_dataframe(sql + ';')

def execute_sql_query(sql: list):
    ss.db_is_loading = True

    try:
        db_conn = connect_db()
        cursor = db_conn.cursor()

        for query in sql:
            cursor.execute(query)
            db_conn.commit()

        cursor.close()
        db_conn.close()
        st.cache_data.clear()
        ss.db_is_loading = False

        return (True, 'Success')
    
    except Exception as e:
        cursor.close()
        db_conn.close()
        st.cache_data.clear()
        ss.db_is_loading = False

        return (False, e)
    
def umkm_registration(data: tuple):
    # Modify data
    mod_data = tuple(map(lambda x: 'Null' if not x else x, data))

    sql = f"""
        INSERT INTO umkm_identity (
            username, email, password, umkm_name, logo, umkm_type,
            description, owner_name, instagram, phone_number
        ) VALUES {mod_data};
    """

    return execute_sql_query([sql])

def umkm_verification(username: str, status: bool):
    if status:
        sql = f"""
            UPDATE umkm_identity SET verification=1, status="Aktif"
            WHERE username="{username}";
        """

    else:
        sql = f"""
            DELETE FROM umkm_identity WHERE username="{username}";
        """

    return execute_sql_query([sql])

def umkm_status_change(username: str, status: bool):
    if status:
        sql = f"""
            UPDATE umkm_identity SET status="Aktif"
            WHERE username="{username}"; 
        """
    
    else:
        sql = f"""
            UPDATE umkm_identity SET status="Tidak Aktif"
            WHERE username="{username}"; 
        """
    
    return execute_sql_query([sql])