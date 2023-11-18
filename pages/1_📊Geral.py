#Importando bibliotecas necessárias
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
import streamlit as st
import pandas as pd
import math
import numpy as np
import folium


#Lendo dataframe
df = pd.read_csv('dataset/zomato.csv')
#Criando cópia para manter preservado o original
df1 = df.copy()

#Função para remover valores nan
def remove_nan(dataframe):
    df = dataframe.dropna()
    return df

#Função que recebe o dataframe e remove espaços das colunas object/texto/strings
def remove_spaces(dataframe):
    df.loc[:, 'Restaurant Name'] = df['Restaurant Name'].str.strip()
    df.loc[:, 'City'] = df['City'].str.strip()
    df.loc[:, 'Address'] = df['Address'].str.strip()
    df.loc[:, 'Locality'] = df['Locality'].str.strip()
    df.loc[:, 'Locality Verbose'] = df['Locality Verbose'].str.strip()
    df.loc[:, 'Cuisines'] = df['Cuisines'].str.strip()
    df.loc[:, 'Currency'] = df['Currency'].str.strip()
    df.loc[:, 'Cuisines'] = df['Cuisines'].str.strip()
    df.loc[:, 'Rating color'] = df['Rating color'].str.strip()
    df.loc[:, 'Rating text'] = df['Rating text'].str.strip()
    return df

#Lista com nomes dos países usando índice como parâmetro
COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}

#Função que captura o código do país e retorna o seu nome com base na lista "COUNTRIES"
def country_name(country_id):
    return COUNTRIES[country_id]

#Lista com nomes das cores usando índice hexadecimal como parâmetro
COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
}

def color_name(color_code):
    return COLORS[color_code]

def maps(df):
    columns = [
        'Restaurant Name',
        'Latitude',
        'Longitude'
        ]
    
    columns_groupby = ['Restaurant Name']

    data_plot = df.loc[:, columns].groupby( columns_groupby ).median().reset_index()
    
    m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=0)
    marker_cluster = MarkerCluster().add_to(m)
    
    for index, location_info in data_plot.iterrows():
        html = f"""
            <h4> {location_info[['Restaurant Name']].values}</h4><br>
            """
        folium.Marker( [location_info['Latitude'],
                        location_info['Longitude']],
                        popup=folium.Popup(html)).add_to(marker_cluster)
        
        
    folium_static( m, width=1024, height=600)


#Limpando dataframe
df1 = remove_spaces(df1)
df1 = remove_nan(df1)
df1 = df1.drop_duplicates(subset='Restaurant ID')
df1["Cuisines"] = df1.loc[:, "Cuisines"].apply(lambda x: x.split(",")[0])
df1['Country Code'] =  df1.loc[:, 'Country Code'].apply(country_name)
df1['Rating color'] =  df1.loc[:, 'Rating color'].apply(color_name)


# -------------------------STREAMLIT--------------------------------------#


#Nome da página na aba do navegador
st.set_page_config(
    page_title = '📊 Geral',
    layout="wide",
)

#Barra Lateral
st.sidebar.markdown('# Fome Zero')

#Linha
st.sidebar.markdown("""---""")

with st.container():
    st.title('Fome Zero!')
    st.markdown('O Melhor lugar para encontrar seu mais novo restaurante favorito!')
    st.markdown('**Temos as seguintes marcas dentro da nossa plataforma:**')

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5, gap='medium')
    with col1:
        restaurants = df1['Restaurant ID'].nunique()
        format = f'{restaurants:,}'.replace(',','.')
        col1.metric('**Restaurantes**', f'{format}')
    with col2:
        col2.metric('**Países**', df1['Country Code'].nunique())
    with col3:
        col3.metric('**Cidades**', df1['City'].nunique())
    with col4:
        votes = df1['Votes'].sum()
        format = f'{votes:,}'.replace(',','.')
        col4.metric('**Avaliações**', f'{format}')
    with col5:
        cuisines = df1['Cuisines'].nunique()
        format = f'{cuisines:,}'.replace(',','.')
        col5.metric('**Culinárias**', f'{format}')
        
#Linha
st.markdown("""---""")

with st.container():
    maps(df1)

































