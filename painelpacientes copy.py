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


def map_interconsulta_pendente(valor):
    if valor == "Sim":
        return "🩺"
    elif valor == "Resp":
        return "👩‍⚕️"
    else:
        return "🟢"

# estiliza as células com valores iguais a 2

def color_by_age(age):
    if age > 70:
        return "🟠"
    else:
        return ""


def load_data():
    df = pd.read_csv(f"pacientes.csv")
    return df

    return df,
def load_data1():
    df = pd.read_csv(f"{pasta}pacientes.csv")
    df["Alta Liberada "] = df["Alta Liberada"].apply(map_alta_liberada)
    df = df.drop(columns=["Alta Liberada"])
    df["Risco Paciente "] = df["Risco Paciente"].apply(map_risco_paciente)
    df = df.drop(columns=["Risco Paciente"])
    df["Ex Pendente "] = df["Ex Pendente"].apply(map_exame_pendente)
    df = df.drop(columns=["Ex Pendente"])
    df["Interconsulta "] = df["Interconsulta"].apply(map_interconsulta_pendente)
    df = df.drop(columns=["Interconsulta"])
    # aplica a função color_by_age na coluna 'Idade'
    df["70+ "] = df["Idade"].apply(color_by_age)

    return df

def mostrar_paciente():
    # Cria um botão para atualizar a página
    if st.button("Atualizar"):
        st.experimental_rerun()
    df = load_data()
    st.title("4º Andar")
    st.write("Lista de pacientes")
    print(df)
    st.dataframe(df)
    # Pop-up com informações adicionais do paciente
    paciente_selecionado = st.selectbox("Selecione um paciente:", options=df["Nome"])
    if paciente_selecionado:
        df_nomes = pd.read_csv(f"{pasta}prontuarios.csv")
        pacientes = df_nomes.loc[df_nomes["Nome"] == paciente_selecionado]

        # Seleciona a primeira linha do DataFrame
        paciente = pacientes.iloc[0]

        # Divide a página em duas colunas
        col1, col2, col3 = st.columns(3)

        # Exibe os dados do paciente em um formulário
        with col1:
            # st.write(emoji.emojize(':bust_in_silhouette: Nome:'), paciente['Nome'])
            st.write(("🎂 Idade"), paciente["Idade"].astype(str))
            st.write(("🚻 Sexo:"), paciente["Sexo"])
            st.write(("📏 Altura (cm):"), paciente["Altura (cm)"].astype(str))
            st.write(("👣 Peso (kg):"), paciente["Peso (kg)"].astype(str))

        with col2:
            st.write(("💓 Pressão Arterial:"), paciente["Pressão Arterial"])
            st.write(
                ("🧪 Colesterol (mg/dL):"), paciente["Colesterol (mg/dL)"].astype(str)
            )
            st.write(("💉 Glicemia (mg/dL):"), paciente["Glicemia (mg/dL)"].astype(str))
            st.write(("🌡️ Temperatura (°C):"), paciente["Temperatura (°C)"].astype(str))

        with col3:
            st.write(("🤒 Sintomas:"), paciente["Sintomas"])
            st.write(("📑 Diagnóstico:"), paciente["Diagnóstico"])
            st.write(("💊 Medicação:"), paciente["Medicação"])
            st.write(("🔬 Exames Pendentes:"), paciente["Exames Pendentes"])


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
