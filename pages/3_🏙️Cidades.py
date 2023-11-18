#Importando bibliotecas necessárias
import streamlit as st
import pandas as pd
import math
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

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

#Limpando dataframe
df1 = remove_spaces(df1)
df1 = remove_nan(df1)
df1 = df1.drop_duplicates(subset='Restaurant ID')
df1["Cuisines"] = df1.loc[:, "Cuisines"].apply(lambda x: x.split(",")[0])
df1['Country Code'] =  df1.loc[:, 'Country Code'].apply(country_name)
df1['Rating color'] =  df1.loc[:, 'Rating color'].apply(color_name)


def restaurants_countries(df1):
    df_aux = df1.loc[:, ['Restaurant ID', 'Country Code']].groupby('Country Code').count().sort_values(by='Restaurant ID', ascending=False).reset_index()
    
    fig = px.bar( df_aux, x='Country Code', y='Restaurant ID', text_auto='.2s')

    fig.update_traces(textfont_size=12, textangle=0, textfont_color = '#ffffff', textposition="inside", cliponaxis=False)

    return fig

def cities_country(df1):
    df_aux = df1.loc[:, ['Country Code', 'City']].groupby('Country Code').nunique().sort_values(by='City', ascending=False).reset_index()

    fig = px.bar(df_aux, x='Country Code', y='City', text_auto='.2s')

    fig.update_traces(textfont_size=12, textangle=0, textfont_color = '#ffffff', textposition="inside", cliponaxis=False)

    return fig

def mean_rating_country(df1):
    df_aux = df1.loc[:, ['Country Code', 'Votes']].groupby('Country Code').mean().sort_values(by = 'Votes', ascending= False).reset_index()
    df_aux['Votes'] = df_aux['Votes'].apply(lambda x: round(x, 2))

    fig = px.bar(df_aux, x='Country Code', y='Votes', text_auto='.5s')

    fig.update_traces(textfont_size=12, textangle=0, textfont_color = '#ffffff', textposition="outside", cliponaxis=False)

    return fig

def average_cost_for_two(df1):
    df_aux = df1.loc[:, ['Country Code', 'Average Cost for two']].groupby('Country Code').mean().sort_values(by = 'Average Cost for two', ascending = False).reset_index()
    df_aux['Average Cost for two'] = df_aux['Average Cost for two'].apply(lambda x: round(x,2))

    fig = px.bar(df_aux, x='Country Code', y='Average Cost for two', text_auto='.5s')

    fig.update_traces(textfont_size=12, textangle=0, textfont_color = '#ffffff', textposition="outside", cliponaxis=False)
    
    return fig

def more_restaurants(df1):
    df_aux = df1.loc[:, ['City','Country Code', 'Restaurant ID']].groupby(['City', 'Country Code']).count().sort_values(by = 'Restaurant ID', ascending = False).head(10).reset_index()

    # Criar um gráfico de barras agrupado por cidade e país
    fig = px.bar(df_aux, x='City', y='Restaurant ID', color='Country Code', text_auto='.2s')

    fig.update_traces(textfont_size=12, textangle=0, textfont_color = '#FFFFFF', textposition="inside", cliponaxis=False)
    
    return fig    

def top7_restaurants(df1):
    df_aux = df1.loc[df1.loc[:, 'Aggregate rating'] > 4, ['City', 'Country Code', 'Restaurant ID']].groupby(['Country Code', 'City']).count().sort_values(by = 'Restaurant ID', ascending = False).head(7).reset_index()

    # Criar um gráfico de barras agrupado por cidade e país
    fig = px.bar(df_aux, x='City', y='Restaurant ID', color='Country Code', text_auto='.2s')

    fig.update_traces(textfont_size=12, textangle=0, textfont_color = '#FFFFFF', textposition="inside", cliponaxis=False)
    
    return fig    

def top7_restaurants_2_5(df1):
    df_aux = df1.loc[df1.loc[:, 'Aggregate rating'] < 2.5, ['City', 'Country Code', 'Restaurant ID']].groupby(['Country Code', 'City']).count().sort_values(by = 'Restaurant ID', ascending = False).head(7).reset_index()

    # Criar um gráfico de barras agrupado por cidade e país
    fig = px.bar(df_aux, x='City', y='Restaurant ID', color='Country Code', text_auto='.2s')

    fig.update_traces(textfont_size=12, textangle=0, textfont_color = '#FFFFFF', textposition="inside", cliponaxis=False)
    
    return fig   

def top10_diferents_cuisines(df1):
    df_aux = df1.groupby(['Country Code', 'City'])['Cuisines'].nunique().sort_values(ascending = False).head(10).reset_index()

    # Criar um gráfico de barras agrupado por cidade e país
    fig = px.bar(df_aux, x='City', y='Cuisines', color='Country Code', text_auto='.2s')

    fig.update_traces(textfont_size=12, textangle=0, textfont_color = '#FFFFFF', textposition="inside", cliponaxis=False)
    
    return fig   

#-------------------------STREAMLIT--------------------------------------#

#Nome da página na aba do navegador
st.set_page_config(
    page_title = '🏙️ Cidades',
    layout="wide",
)

#Barra Lateral
st.sidebar.markdown('# Fome Zero')
st.sidebar.markdown('## Filtros')

countries = st.sidebar.multiselect(
    'Escolha os países que deseja visualizar as informações', #Título 
    ["India", "Australia", "Brazil", "Canada", "Indonesia", "New Zeland", "Philippines",
     "Qatar", "Singapure", "South Africa", "Sri Lanka", "Turkey", "United Arab Emirates",
     "England", "United States of America"], #Opções para serem selecionadas 
    ['Brazil', 'England', 'Qatar', 'South Africa', 'Canada', 'Australia']  #Opções padrão
)

#Filtro de trânsito
linhas = df1['Country Code'].isin(countries)
df1 = df1.loc[linhas, :]

#Linha
st.markdown("""---""")

with st.container():
    st.title('🏙️ Visão Cidades')

st.markdown("""---""")

with st.container():
    st.markdown('**Top 10 cidades com mais restaurantes**')
    fig = more_restaurants(df1)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("""---""")

with st.container():
    col1, col2 = st.columns(2, gap = 'Large')
    with col1:
        st.markdown('**Top-7 cidades com restaurantes com média acima de 4.0**')
        fig = top7_restaurants(df1)
        st.plotly_chart(fig, use_container_width = True)
    with col2:
        st.markdown('**Top-7 cidades com restaurantes com média abaixo de 2.5**')
        fig = top7_restaurants_2_5(df1)
        st.plotly_chart(fig, use_container_width = True)

with st.container():
    st.markdown('**Top 10 cidades com mais culinárias distintas**')
    fig = top10_diferents_cuisines(df1)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("""---""")













