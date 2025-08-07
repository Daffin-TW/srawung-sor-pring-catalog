# Streamlit imports
from streamlit import session_state as ss
from streamlit import secrets as sc
import streamlit as st

# Custom package imports
from modules import page_init, fetch_data, fetch_data_filter
import pandas as pd


@st.dialog('👜 Katalog UMKM', width='large')
def umkm_catalog(username: str):
    df_category = fetch_data_filter('category', username)

    category_container = st.container(border=True)

    if not len(df_category):
        category_container.error('UMKM belum mendaftarkan produk')

    else:
        with category_container:
            for i, cat in df_category.iterrows():
                cat_name = cat['name']

                st.write(f'### Kategori {cat_name}')

                df_product = fetch_data_filter('product', i).reset_index()
                prod_values = df_product.values
                
                if not len(df_product):
                    st.error('UMKM belum mendaftarkan produk')
                
                else:
                    rows_total = (len(df_product) - 1) // 2 + 1
                    list_prod = [prod_values[i:i+2] for i in range(0, len(prod_values), 2)]

                    prod_container = st.container()

                    for i in range(rows_total):
                        inner_container = prod_container.container()
                        prod_cols = inner_container.columns(2, gap='medium', border=True)

                        for j, row in enumerate(list_prod[i]):
                            with prod_cols[j]:
                                if row[5] == 'Null':
                                    st.image(f'src/img/missing_product.png')
                                else:
                                    st.image(row.logo)

                                st.write(f'#### {row[2]}')
                                st.write(f'{row[3]}')
                                st.write(f'Rp{row[4]}')


# Initial
current_page = '🛒 Katalog'

page_init.init_configuration(layout='centered')
page_init.init_sidebar()
page_init.init_style()
page_init.init_navigation(current_page)


# Load data
umkm_df = pd.read_csv("src/data/umkm.csv", delimiter=';')

# === Header ===
st.markdown("""
<div class="katalog-header">
    <h1>📦 Katalog UMKM</h1>
    <p>Jelajahi berbagai produk menarik dari UMKM di Srawung Sor Pring!</p>
</div>
""", unsafe_allow_html=True)

df_umkm = fetch_data('umkm_status').reset_index()

for i, row in df_umkm.iterrows():
    umkm_container = st.container()

    with umkm_container:
        umkm_cols1 = st.columns([0.4, 2], vertical_alignment='center')

        with umkm_cols1[0]:
            if row[4] == 'Null':
                st.image(f'src/img/missing_product.png')
            else:
                st.image(row.logo)

        with umkm_cols1[1]:
            st.write(f'#### {row.umkm_name}')
            st.write(f'_UMKM Jenis {row.umkm_type}_')
            st.write(row.description)
        
        instagram = row.instagram

        if not instagram or instagram == 'Null':
            instagram = '...'
        else:
            instagram = instagram if instagram[0] == '@' else '@' + instagram

        umkm_cols2 = st.columns(3, vertical_alignment='center')

        umkm_cols2[0].write(f'🌐 **Instagram:** {instagram}')
        umkm_cols2[1].write(f'📞 {row.phone_number}')
        catalog_button = umkm_cols2[2].button(
            '🔎 Jelajahi katalog', key=f'umkm_{row.umkm_name}_but',
            use_container_width=True, type='tertiary'
        )

        if catalog_button:
            umkm_catalog(row.username)
    
    st.divider()