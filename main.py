import streamlit as st
import pandas as pd
from painel_ti import painel_ti
from painel_analistas import painel_analistas


def main():
    st.set_page_config(
        page_title="PAINEL TI",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.sidebar.write("Selecione uma opção")
    menu = st.sidebar.selectbox('Selecione',
                                ['📊 PAINEIS DE CHAMADOS DA TI 🚀',
                                '💻 PAINEIS DOS ANALISTAS DA TI 🔍'
                                ]                                
                                )
    upload_file = st.sidebar.file_uploader("Upload de arquivo", type=["csv", "xlsx"],help='Insira seu arquivo em CSV ou em EXCEL')

    if upload_file is not None:
        if st.sidebar.checkbox("Atualizar arquivo existente"):
            with open("ordens_de_servico.csv", "wb") as f:
                f.write(upload_file.getbuffer())    
    dados = pd.read_csv("ordens_de_servico.csv")
    
    if menu == '📊 PAINEIS DE CHAMADOS DA TI 🚀':
        painel_ti()
    elif menu == '💻 PAINEIS DOS ANALISTAS DA TI 🔍':
        painel_analistas(dados)
if __name__ == "__main__":
    main()
