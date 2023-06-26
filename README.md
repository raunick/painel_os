# 🖥️ Painel TI

Este aplicativo Streamlit, denominado "Painel TI", apresenta visualizações de dados e estatísticas relacionadas às Ordens de Serviço (OS) em um ambiente de Tecnologia da Informação (TI). O painel utiliza pandas, plotly.express e outras bibliotecas para manipulação e visualização dos dados.

## veja online: https://painelosti.streamlit.app/

## 📋 Pré-requisitos
Antes de executar o Painel TI, certifique-se de ter as seguintes bibliotecas instaladas:

- streamlit
- pandas
- plotly.express
Você também precisará do arquivo ordens_de_servico.csv para carregar os dados das Ordens de Serviço.

## 🚀 Execução
Para executar o Painel TI, siga as etapas abaixo:

Clone este repositório em sua máquina local:
```bash
git clone https://github.com/raunick/painel_os.git
```
Navegue até o diretório clonado:
```bash
cd painel_os
```
Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```
*Certifique-se de que o arquivo ordens_de_servico.csv esteja presente no diretório.*

## Inicie o aplicativo Streamlit:

```bash
streamlit run main.py
```
O Painel TI será aberto em seu navegador padrão. Explore as diferentes visualizações e estatísticas disponíveis.

# 🔎 O Painel TI oferece as seguintes funcionalidades e visualizações:

- Contagem total de Ordens de Serviço abertas.
- Setor que mais abriu Ordens de Serviço.
- Ordem de Serviço mais antiga e mais nova.
- Gráfico de barras: Status x Ordens de Serviço.
- Gráfico de barras: Prioridades x Ordens de Serviço.
- Gráfico de barras: Número de Ordens de Serviço por Setor.
- Gráfico de linha: Ordens de Serviço abertas por mês.
- Tabela com os dados das Ordens de Serviço.
- Detalhes das Ordens de Serviço selecionadas.


## 😎 Contribuição
Contribuições são bem-vindas! Se você deseja contribuir para este projeto, siga as etapas abaixo:

Faça um fork deste repositório.
Crie um branch para suas alterações:
```bash
git checkout -b minha-branch
```
Faça as alterações desejadas e commit:
```bash
git commit -m "Minha contribuição"
```
Envie as alterações para o seu repositório remoto:
```bash
git push origin minha-branch
```
*Abra um pull request neste repositório para que suas alterações possam ser revisadas e mescladas ao projeto principal.*
