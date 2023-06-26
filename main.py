import streamlit as st
from painel_os import painel_os
from painel_os2 import painel_os2
from painel_ti import painel_ti


def main():
    # Configura o layout para modo wide
    st.set_page_config(layout="wide")
    st.sidebar.write("Selecione uma opção")
    menu = st.sidebar.selectbox('Selecione',['📊 PAINEIS DE CHAMADOS DA TI 🚀'])
    if menu == '📊 PAINEIS DE CHAMADOS DA TI 🚀':
        painel_ti()
if __name__ == "__main__":
    main()
