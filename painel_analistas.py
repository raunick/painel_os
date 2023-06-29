import streamlit as st
import pandas as pd
import plotly.express as px
import datetime


def painel_analistas(csv):
    df = csv
    df["OS"] = 1
    total_os = sum(df["OS"])
    # Título do aplicativo
    st.title("💻 PAINEIS DOS ANALISTAS DA TI 🔍")
    st.write(f'# ✨ Barra de Conquistas ✨')
    # Contagem de Ordens de Serviço por Solicitante
    sector_counts = df["Solicitante"].value_counts().reset_index()
    sector_counts.columns = ["Solicitante", "OS"]
    meta_cliente = 95
    st.progress(70,text='Barra de Conclusão de OS 👍')
    st.progress(40,text='Barra de Tempo de Resolução 👋')
    st.progress(meta_cliente,text='Barra de Satisfação do Cliente 👏')
    
    if meta_cliente >= 98:
        st.balloons()
    # Cálculo do total de OS pendentes, fechadas e abertas
    total_pendentes = df[df["Status"] == "Aberto"].shape[0]
    total_fechadas = df[df["Status"] == "Encerrada"].shape[0]
    total_abertas = df[df["Status"] == "Em Processo"].shape[0]

    col1, col2, col3 = st.columns(3)

    col1.metric("Total de OS pendentes:", total_pendentes,delta=10)
    col2.metric("Total de OS fechadas:", total_fechadas,delta=10)
    col3.metric("Total de OS abertas:", total_abertas,delta=-20)
    # Gráfico de barras - Executante das Ordens de Serviço
    with col1:
        st.header("👑 TOP 5 Executantes 🎉")
        Executante_counts = df["Executante"].value_counts().reset_index()
        Executante_counts.columns = ["Executante", "OS"]
        fig1 = px.bar(
            Executante_counts,
            x="OS",
            y="Executante",
            orientation="h",
        )
        st.plotly_chart(fig1, use_container_width=True)

    # Gráfico de barras - Executante x Status
    with col2:
        # Gráfico de barras - Executante x Status
        st.header("🚀 Executante x Status")
        priority_counts = df.groupby(["Executante", "Status"]).size().reset_index(name="Count")
        fig2 = px.bar(priority_counts, x="Executante", y="Count", color="Status", barmode="stack")
        st.plotly_chart(fig2, use_container_width=True)

    # Gráfico de barras - Número de Solicitante por Ordens de Serviço
    with col3:
        st.header("👑 TOP 5 Solicitante 🎉")
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
    
    # Container para alinhar os gráficos horizontalmente
    col1, col2, col3 = st.columns(3)



    st.header("📋 Dados das Ordens de Serviço")
    tab = df.drop('OS', axis=1)   
    st.subheader("Detalhes das Ordens de Serviço selecionadas")
    Executante_os = st.sidebar.multiselect(
        "Filtro por Executante:", 
        df["Executante"].unique(),
        default=[tab["Executante"].iloc[-1]]
    )
    if Executante_os == []:
        st.sidebar.info("Selecione um Executante")
        st.dataframe(df,use_container_width=True)
    else:
        filtro_os = df[df["Executante"].isin(Executante_os)]
        st.dataframe(filtro_os,use_container_width=True)
    st.sidebar.write('🚧EM DESENVOLVIMENTO🚧')
    start_date = st.sidebar.date_input("Selecione a data inicial")
    end_date = st.sidebar.date_input("Selecione a data final")
    st.sidebar.write('Você selecionou um período de', start_date.strftime("%d/%m/%Y"), 'a', end_date.strftime("%d/%m/%Y"))
    valor = st.sidebar.select_slider(
        'Selecione um valor dentro da faixa de 1 a 100',
        options=list(range(1, 101)),
        value=(1, 100)
    )
    st.sidebar.write('Você selecionou o intervalo de valores entre', valor[0], 'e', valor[1])
    status = st.sidebar.radio(
        "Qual é o status da ordem de serviço?",
        ('Aberto', 'Em Processo', 'Encerrada'))

    if status == 'Aberto':
        st.sidebar.write('Você selecionou ordens de serviço abertas.')
    elif status == 'Em Processo':
        st.sidebar.write("Você selecionou ordens de serviço em processo.")
    else:
        st.sidebar.write("Você selecionou ordens de serviço encerradas.")
if __name__ == '__painel_analistas__':
    painel_analistas()