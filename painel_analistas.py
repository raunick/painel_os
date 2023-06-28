import streamlit as st
import pandas as pd
import plotly.express as px

def painel_analistas(csv):
    df = csv
    df["OS"] = 1
    total_os = sum(df["OS"])
    # Título do aplicativo
    st.title("💻 PAINEIS DOS ANALISTAS DA TI 🔍")
    st.write(f'# Total OS abertas: {total_os}')
    # Contagem de Ordens de Serviço por Solicitante
    sector_counts = df["Solicitante"].value_counts().reset_index()
    sector_counts.columns = ["Solicitante", "OS"]

    # Cálculo da porcentagem
    total_os = sector_counts["OS"].sum()
    sector_counts["Porcentagem"] = (sector_counts["OS"] / total_os) * 100

    # Solicitante com mais Ordens de Serviço abertas
    setor_mais_os = sector_counts.iloc[0]["Solicitante"]
    total_mais_os = sector_counts.iloc[0]["OS"]
    # Encontrar a menor data
    min_date = df["Data"].min()
    max_date = df["Data"].max()

    # Filtrar o DataFrame original com base na menor data
    minfiltered_df = df[df["Data"] == min_date]
    maxfiltered_df = df[df["Data"] == max_date]
    min_os = minfiltered_df.iloc[0]
    max_os = maxfiltered_df.iloc[0]

    col1, col2, col3 = st.columns(3)
    col1.metric(f"Solicitante que mais abriu OS:", f"{setor_mais_os} com {total_mais_os} %")
    col2.metric("OS mais antiga:", f"{min_os[0]}")
    col3.metric("OS mais nova:", f"{max_os[0]}")
    # Container para alinhar os gráficos horizontalmente
    col1, col2, col3 = st.columns(3)

    # Gráfico de barras - Executante das Ordens de Serviço
    with col1:
        st.header("📈 Executante x Ordens de Serviço")
        Executante_counts = df["Executante"].value_counts().reset_index()
        Executante_counts.columns = ["Executante", "OS"]
        fig1 = px.bar(
            Executante_counts,
            x="OS",
            y="Executante",
            orientation="h",
        )
        st.plotly_chart(fig1, use_container_width=True)

    # Gráfico de barras - Executante das Ordens de Serviço
    with col2:
        # Gráfico de barras - Prioridades x Executante
        st.header("🚀 Executante x Prioridades")
        priority_counts = df.groupby(["Executante", "Prioridade"]).size().reset_index(name="Count")
        fig2 = px.bar(priority_counts, x="Executante", y="Count", color="Prioridade", barmode="stack")
        st.plotly_chart(fig2, use_container_width=True)

    # Gráfico de barras - Número de Solicitante por Ordens de Serviço
    with col3:
        st.header("📊 Solicitante x Ordens de Serviço")
        sector_counts = df["Solicitante"].value_counts().reset_index()
        sector_counts.columns = ["Solicitante", "OS"]
        fig3 = px.bar(sector_counts, x="OS", y="Solicitante", orientation="h")
        st.plotly_chart(fig3, use_container_width=True)
    # Converte a coluna "Data" para o tipo de dados de data
    df["Data"] = pd.to_datetime(df["Data"])

    # Filtra as ordens de serviço abertas
    df_abertas = df[df["Status"] == "Aberto"]

    # Agrupa os dados de ordens abertas por dia
    df_abertas_grouped = df_abertas.groupby(pd.Grouper(key="Data", freq="D")).size().reset_index(name="Abertas")

    # Filtra as ordens de serviço fechadas
    df_fechadas = df[df["Status"] == "Encerrada"]

    # Agrupa os dados de ordens fechadas por dia
    df_fechadas_grouped = df_fechadas.groupby(pd.Grouper(key="Data", freq="D")).size().reset_index(name="Fechadas")

    # Mescla os dataframes de ordens abertas e fechadas
    df_merged = df_abertas_grouped.merge(df_fechadas_grouped, on="Data", how="outer")

    # Preenche os valores nulos com zero
    df_merged.fillna(0, inplace=True)

    # Ordena os dados por data
    df_merged.sort_values("Data", inplace=True)

    # Cria o gráfico de linha com duas linhas para ordens abertas e fechadas
    fig_line = px.line(df_merged, x="Data", y=["Abertas", "Fechadas"], title="Ordens de Serviço Abertas e Fechadas por Dia")

    # Renderiza o gráfico no Streamlit
    st.plotly_chart(fig_line, use_container_width=True)
    coluna1, coluna2 = st.columns([4, 2])

    with coluna1:
        # Tabela com os dados das Ordens de Serviço
        st.header("📋 Dados das Ordens de Serviço")
        tab = df.drop('OS', axis=1)
        st.dataframe(tab,use_container_width=True)

    with coluna2:
        # Exemplo de visualização de dados individuais (multiselect)
        selected_os = st.multiselect(
            "⚙️ Selecione uma ou mais Ordens de Serviço", 
            df["Número OS"],
            default=[tab["Número OS"].iloc[-1]]
        )
        if selected_os == []:
            st.info("Selecione uma OS")
        else:
            st.subheader("Detalhes das Ordens de Serviço selecionadas")
            st.write(tab[df["Número OS"].isin(selected_os)])


if __name__ == '__painel_analistas__':
    painel_analistas()