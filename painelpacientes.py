import streamlit as st
import pandas as pd

pasta = 'data/'
def map_alta_liberada(valor):
    if valor == "Sim":
        return "📝"
    else:
        return "🏥"


def map_risco_paciente(valor):
    if valor == "Alto":
        return "🤕"
    elif valor == "Médio":
        return "🤒"
    else:
        return "🙂"


def map_exame_pendente(valor):
    if valor == "Sim":
        return "🩻"
    elif valor == "Lab":
        return "🧪"
    else:
        return "🟢"


def map_IC_pendente(valor):
    if valor == "Sim":
        return "🩺"
    elif valor == "Resp":
        return "📝"
    elif valor == "+48":
        return "🟠"
    else:
        return "🟢"

# estiliza as células com valores iguais a 2

def valida_exame(exame):
    if exame == "Sim":
        return "🟠"
    else:
        return "🟢"

def valida_med(med):
    if med != '-':
        n_med = f'💊 {med}'
        return n_med
    return '🟢'

def load_data():
    df = pd.read_csv(f"paciente.csv")
    df['IC'] = df['IC'].apply(map_IC_pendente)
    df['US']= df['US'].apply(valida_exame)
    df['RM']= df['RM'].apply(valida_exame)
    df['RX']= df['RX'].apply(valida_exame)
    df['EDA']= df['EDA'].apply(valida_exame)
    df['CC']= df['CC'].apply(valida_exame)
    df['Reav. Dor']= df['Reav. Dor'].apply(valida_exame)
    df['Med. Agora']= df['Med. Agora'].apply(valida_exame)
    df['Farm. Cl']= df['Farm. Cl'].apply(valida_med)
    df['alta']= df['alta'].apply(map_alta_liberada)
    df["atendimento"] = df["atendimento"].astype(str)
    return df


def mostrar_paciente():
    # Cria um botão para atualizar a página
    if st.button("Atualizar"):
        st.experimental_rerun()
    df = load_data()
    st.title("4º Andar")
    st.write("## Lista de pacientes: ")
    st.dataframe(df)
    st.write("### Legendas: ")
    st.write("Pendente = 🟠 ")
    st.write(" **Alta Medica** = 📝 ")
    st.write("### Legendas: ")
    st.write("### Legendas: ")
def atualizar():
    if st.button("Atualizar"):
        st.experimental_rerun()


def painel_internacao():
    # opções do menu
    opcao = st.sidebar.selectbox(
        "Selecione uma opção:",
        ["Painel de pacientes", "Painel de Pendencias"],
    )

    # condições para cada opção do menu
    if opcao == "Painel de pacientes":
        mostrar_paciente()
    elif opcao == "Painel de Pendencias":
        st.write("# 🚧EM CRIAÇÃO🚧")
