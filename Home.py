import streamlit as st
import pandas as pd

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

# Convert DataFrame to CSV
csv_file = df1.to_csv(index=False)
    
st.set_page_config(
    page_title="Home",
    layout="wide",
)

st.sidebar.markdown('# Fome Zero')

st.sidebar.download_button(label='Download Dataset',
        data=csv_file,
        file_name='data.csv',
        key='csv_download_button')

    
st.sidebar.markdown("""---""")

st.write("# Fome Zero Dashboard")

st.markdown(
    """
        Este dashboard foi construído como projeto do aluno no final do curso "Analisando dados com python" da plataforma Comunidade DS.
        
        Para saber mais detalhes sobre o projeto e suas etapas, escrevi o seguinte arquivo no Medium: [Análise Descritiva — Zomato Restaurants](https://medium.com/@luizfernandodelchello/an%C3%A1lise-descritiva-zomato-restaurants-938266b2bdd6). 
        
        Sinta-se a vontade para entrar em contato via LinkedIn através do perfil: [Luiz Fernando Delchello](https://www.linkedin.com/in/luiz-fernando-delchello/).
        """
)

st.markdown("""---""")

st.markdown(
    """
        ### Como funciona este dashboard?
        
        **Geral:**
        
            Visão geográfica utilizando agrupamento por localização, com todos os restaurantes cadastrados
            na base de dados.
            
        **Países:**
        
            Visão através de gráficos contendo informações referentes ao países, possui um filtro ao lado
            esquerdo em que se pode alterar os parâmetros de visualização.
            
        **Cidades:**
        
            Visão através de gráficos contendo informações referentes as cidades, possui um filtro ao lado
            esquerdo em que se pode alterar os parâmetros de visualização, além disso possui gráficos 
            interativos em que é possível clicar no nome do país para remover coluna referente a ele.

        
        **Culinárias:**
        
            Visão inicial através de dataframe com colunas específicas selecionadas, dois gráficos abaixo,
            contendo as culinárias com as melhores e piores notas respectivamente. Possui além dos filtros de 
            culinária e país, filtro de quantidade de restaurantes. Alterando assim a exibição do dashboard.
            
    """
)
