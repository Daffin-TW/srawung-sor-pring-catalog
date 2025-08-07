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

        case 'umkm_status':
            sql = "SELECT * FROM umkm_identity WHERE status='Aktif'"

        case _:
            raise KeyError(f'{table} tidak ditemukan di database')
    
    return sql_to_dataframe(sql + ';')

def fetch_data_filter(table: str, filter_: str):
    match table:
        case 'umkm':
            sql = f"SELECT * FROM umkm_identity WHERE username='{filter_}'"
        
        case 'umkm_credentials':
            sql = f"SELECT * FROM umkm_identity WHERE NOT username='{filter_}'"

        case 'category':
            sql = f"SELECT * FROM product_category WHERE umkm_username='{filter_}'"

        case 'product':
            sql = f"SELECT * FROM product WHERE category_id='{filter_}'"

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
            UPDATE umkm_identity SET verification=1, status='Aktif'
            WHERE username='{username}';
        """

    else:
        sql = f"""
            DELETE FROM umkm_identity WHERE username='{username}';
        """

    return execute_sql_query([sql])

def umkm_status_change(username: str, status: bool):
    if status:
        sql = f"""
            UPDATE umkm_identity SET status='Aktif'
            WHERE username='{username}';
        """
    
    else:
        sql = f"""
            UPDATE umkm_identity SET status='Tidak Aktif'
            WHERE username='{username}';
        """
    
    return execute_sql_query([sql])

def umkm_update(table: str, username: str, data: tuple):
    mod_data = tuple(map(lambda x: 'Null' if not x else x, data))
    sql = []

    match table:
        case 'information':
            sql.append(f"""
                UPDATE umkm_identity SET
                    umkm_name='{mod_data[0]}',
                    logo='{mod_data[1]}',
                    umkm_type='{mod_data[2]}',
                    description='{mod_data[3]}',
                    owner_name='{mod_data[4]}',
                    instagram='{mod_data[5]}',
                    phone_number='{mod_data[6]}'
                WHERE username='{username}'; 
            """)

        case 'username':
            sql.append(f"""
                UPDATE umkm_identity SET
                    username='{mod_data[0]}',
                    email='{mod_data[1]}'
                WHERE username="{username}";
            """)

        case 'password':
            sql.append(f"""
                UPDATE umkm_identity SET
                    password='{mod_data[0]}'
                WHERE username='{username}';
            """)

        case _:
            raise KeyError(f'{table} tidak ditemukan di database')

    return execute_sql_query(sql)

def insert_category(username: str, category: str):
    sql = f"""
        INSERT INTO product_category (umkm_username, name) VALUES
        ('{username}', '{category}');
    """
    
    return execute_sql_query([sql])

def delete_category(category_id: int):
    sql = []

    sql.append(f"""
        DELETE FROM product WHERE category_id='{category_id}';
    """)

    sql.append(f"""
        DELETE FROM product_category WHERE id='{category_id}';
    """)

    return execute_sql_query(sql)

def insert_product(data: tuple):
    mod_data = tuple(map(lambda x: 'Null' if not x else x, data))

    sql = f"""
        INSERT INTO product (
            category_id, `name`, `description`, price, image
        ) VALUES {mod_data};
    """
    
    return execute_sql_query([sql])

def delete_product(product_id: int):
    sql = f"""
        DELETE FROM product WHERE id='{product_id}';
    """
    
    return execute_sql_query([sql])