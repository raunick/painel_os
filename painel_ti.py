import streamlit as st
import pandas as pd
import plotly.express as px


def painel_ti():
    df = pd.read_csv("ordens_de_servico.csv")
    df["OS"] = 1
    total_os = sum(df["OS"])
    # Título do aplicativo
    st.title("📊 PAINEIS DE CHAMADOS DA TI 🚀")
    st.write(f'# Total OS abertas: {total_os}')
    # Contagem de Ordens de Serviço por Setor
    sector_counts = df["Setor"].value_counts().reset_index()
    sector_counts.columns = ["Setor", "OS"]

    # Cálculo da porcentagem
    total_os = sector_counts["OS"].sum()
    sector_counts["Porcentagem"] = (sector_counts["OS"] / total_os) * 100

    # Setor com mais Ordens de Serviço abertas
    setor_mais_os = sector_counts.iloc[0]["Setor"]
    total_mais_os = sector_counts.iloc[0]["OS"]
    # Encontrar a menor data
    min_date = df["Data"].min()
    max_date = df["Data"].max()

    # Filtrar o DataFrame original com base na menor data
    minfiltered_df = df[df["Data"] == min_date]
    maxfiltered_df = df[df["Data"] == max_date]

    # Armazenar a ordem de serviço mais antiga
    min_os = minfiltered_df.iloc[0]
    max_os = maxfiltered_df.iloc[0]
    
    col1, col2, col3 = st.columns(3)
    col1.metric(f"Setor que mais abriu OS:", f"{setor_mais_os} com {total_mais_os} %")
    col2.metric("OS mais antiga:", f"{min_os[0]}")
    col3.metric("OS mais nova:", f"{max_os[0]}")
    # Container para alinhar os gráficos horizontalmente
    col1, col2, col3 = st.columns(3)

    # Gráfico de barras - Status das Ordens de Serviço
    with col1:
        st.header("📈 Status x Ordens de Serviço")
        status_counts = df["Status"].value_counts().reset_index()
        status_counts.columns = ["Status", "OS"]
        fig1 = px.bar(
            status_counts,
            x="OS",
            y="Status",
            orientation="h",
        )
        st.plotly_chart(fig1, use_container_width=True)

    # Gráfico de barras - Prioridades das Ordens de Serviço
    with col2:
        st.header("🚀 Prioridades x Ordens de Serviço")
        priority_counts = df["Prioridade"].value_counts().reset_index()
        priority_counts.columns = ["Prioridade", "OS"]
        fig2 = px.bar(priority_counts, x="OS", y="Prioridade", orientation="h")
        st.plotly_chart(fig2, use_container_width=True)

    # Gráfico de barras - Número de Ordens de Serviço por Setor
    with col3:
        st.header("📊 Ordens de Serviço x Setor")
        sector_counts = df["Setor"].value_counts().reset_index()
        sector_counts.columns = ["Setor", "OS"]
        fig3 = px.bar(sector_counts, x="OS", y="Setor", orientation="h")
        st.plotly_chart(fig3, use_container_width=True)
    # Título do aplicativo
    st.title("Gráfico de Linha - OS x mês")

    # Cria o gráfico de linha utilizando o Plotly Express
    fig_line = px.line(df, x="Data", y="OS", title="Status das Ordens de Serviço ao longo do tempo")
    # Converte a coluna "Data" para o tipo de dados de data
    df["Data"] = pd.to_datetime(df["Data"])

    # Agrupa os dados por mês e soma os OSes
    df_grouped = df.groupby(pd.Grouper(key="Data", freq="D")).sum().reset_index()

    # Cria o gráfico de linha utilizando o Plotly Express
    fig_line = px.line(df_grouped, x="Data", y="OS", title="Ordens de Serviço Abertas por Mês")

    # Renderiza o gráfico no Streamlit
    st.plotly_chart(fig_line,use_container_width=True)

    coluna1, coluna2 = st.columns([4, 2])

    with coluna1:
        # Tabela com os dados das Ordens de Serviço
        st.header("📋 Dados das Ordens de Serviço")
        st.dataframe(df,use_container_width=True)

    with coluna2:
        # Exemplo de visualização de dados individuais (multiselect)
        selected_os = st.multiselect(
            "⚙️ Selecione uma ou mais Ordens de Serviço", 
            df["Número OS"],
            default=[df["Número OS"].iloc[-1]]
        )
        if selected_os == []:
            st.info("Selecione uma OS")
        else:
            st.subheader("Detalhes das Ordens de Serviço selecionadas")
            st.write(df[df["Número OS"].isin(selected_os)])


# Executa o aplicativo Streamlit
if __name__ == "__painel_ti__":
    painel_ti()
