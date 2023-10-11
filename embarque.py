import streamlit as st
import pandas as pd
import numpy as np

st.title('Embarque de pessoas na uber em Nova York')

COLUNA_DATE='date/time'
URL_DADOS=('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def carregar_dados(num_linhas):
    dados= pd.read_csv(URL_DADOS, nrows=num_linhas)
    letra_minuscula=lambda x: str(x).lower()
    dados.rename(letra_minuscula,axis='columns',inplace=True)
    dados.info()
    dados[COLUNA_DATE]=pd.to_datetime(dados[COLUNA_DATE])
    return dados

status_carregamento= st.text('Carregando os dados..')
dados = carregar_dados(10000)
status_carregamento.text("Carregado!")
dados

st.subheader('Dados crús')
st.write(dados)
st.dataframe(dados)

st.subheader('Número de embarques por hora..')
historico_horas= np.histogram(
    dados[COLUNA_DATE].dt.hour, bins=24, range=(0,24))[0]

st.bar_chart(historico_horas)

# st.subheader('Mapas dos embarques')
# st.map(dados)

#FILTRANDO POR HORA

hora=int(st.text_input('Defina uma hora'))
hora_filtro = dados[dados[COLUNA_DATE].dt.hour == hora]

st.subheader(f'Mapa de todas os embarques na hora {hora}:00')
st.map(hora_filtro)