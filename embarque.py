import streamlit as st
import pandas as pd
import numpy as np

st.title('Embarque de pessoas na uber em Nova York')

DATE_COLUMN='date/time'
DATA_URL=('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def carregar_dados(num_linhas=1):
    dados= pd.read_csv(DATA_URL, nrows=num_linhas)
    letra_minuscula=lambda x: str(x).lower()
    dados.rename(letra_minuscula,axis='columns',inplace=True)
    dados.info()
    dados[DATE_COLUMN]=pd.to_datetime(dados[DATE_COLUMN])
    return dados

status_carregamento= st.text('Carregando os dados..')
dados = carregar_dados(10000)
status_carregamento.text("Done! (using st.cache_data)")
dados
    