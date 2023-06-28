import streamlit as st

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="random",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'about': "# This is a header. This is an *extremely* cool app!"
    },
)
# Recupera os parâmetros da URL
url = st.experimental_get_query_params()
cd_setor = url.get('CD_SETOR', [''])[0]
pagina = url.get('pagina', ['Principal'])[0]

# Definir a função para a página principal
def home():
    st.title("Página Principal")
    # Adicione elementos e funcionalidades específicas da página principal aqui

# Definir a função para a página de configurações
def settings():
    st.title("Página de Configurações")
    # Adicione elementos e funcionalidades específicas da página de configurações aqui

# Criar um seletor de páginas no sidebar
page = st.sidebar.selectbox("Selecione uma página", ("Principal", "Configurações"))

# Criar um seletor de setor no sidebar
setor = st.sidebar.selectbox("Selecione uma página", ('PA','TI','CTI','FAT'))
# Atualizar os parâmetros da URL ao selecionar uma página
if page == "Principal":
    st.experimental_set_query_params(CD_SETOR=setor, pagina="Principal")
    home()
elif page == "Configurações":
    st.experimental_set_query_params(CD_SETOR=setor, pagina="Configurações")
    settings()


