import streamlit as st
import pandas as pd
import openpyxl
import os

st.set_page_config(page_title="Cadastro de Clientes", page_icon="💻", layout="wide", initial_sidebar_state="expanded")


with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Funções auxiliares
#def read_data():
    #return pd.read_excel('database.xlsx')

def load_data(file_path):
    if os.path.exists(file_path):
        data = pd.read_excel(file_path)
    else:
        data = pd.DataFrame(columns=['ID', 'Cidade', 'Nome Completo', 'Telefone', 'CPF', 'RG', 'Endereço da obra', 'Endereço Residencial', 'Observação'])
    return data

file_path = 'database.xlsx'
df = load_data(file_path)
def write_data(df):
    df.to_excel('database.xlsx', index=False)


# Leitura dos dados
#df = read_data()

st.markdown('# 💻 Cadastro de Clientes' )

with st.container():
    st.success('### ⏬ Escolha Uma Operação ⏬')
    option = st.selectbox('', ["Ler os Dados", "Criar Dados", "Atualizar Registro", "Deletar Registro"])

if option == "Ler os Dados":
    st.info("###	📖 Leitura dos registros")
    with st.container():
        # Exibir a tabela com estilo CSS inline
        df_reset = df.reset_index(drop=True)
        st.table(df_reset)
        st.table(df)

elif option == "Criar Dados":
    st.info("### 🆕Adicionar novo registro")
    with st.container():
        cidade = st.selectbox("Cidade", ('Condeúba','Pres. Jânio Quadros','Maetinga', 'Cordeiros', 'Piripá', 'Mortugaba'))
        nome = st.text_input("Nome Completo")
        telefone = st.text_input("Telefone")
        cpf = st.text_input("CPF")
        rg = st.text_input("RG")
        endereco_obra = st.text_input("Endereço da obra", placeholder="Digite o endereço completo")
        endereco_residencial = st.text_input("Endereço Residencial", placeholder="Digite o endereço completo")
        obs = st.text_input("Observação")

    if st.button("Adicionar Registro", key='my_button'):
        new_id = df['ID'].max() + 1 if not df.empty else 1
        new_row = pd.DataFrame({
            'ID': [new_id],
            'Cidade': [cidade],
            'Nome Completo': [nome],
            'Telefone': [telefone],
            'CPF': [cpf],
            'RG': [rg],
            'Endereço da obra': [endereco_obra],
            'Endereço Residencial': [endereco_residencial],
            'Observação': [obs]
        })
        df = pd.concat([df, new_row], ignore_index=True)
        write_data(df)

        st.success("Registro adicionado com sucesso!")

elif option == "Atualizar Registro":

    st.info("### ♻️Atualizar um registro")
    with st.container():
        record_id = st.number_input("ID do registro a ser atualizado", min_value=0, step=1)
        if record_id in df['ID'].values:
            cidade = st.text_input("Cidade", value=df[df['ID'] == record_id]['Cidade'].values[0])
            nome = st.text_input("Nome", value=df[df['ID'] == record_id]['Nome'].values[0])
            telefone = st.text_input("Telefone", value=df[df['ID'] == record_id]['Telefone'].values[0])
            cpf = st.text_input("CPF", value=df[df['ID'] == record_id]['CPF'].values[0])
            rg = st.text_input("RG", value=df[df['ID'] == record_id]['RG'].values[0])
            endereco_obra = st.text_input("Endereço da obra", value=df[df['ID'] == record_id]['Endereço da obra'].values[0])
            endereco_residencial = st.text_input("Endereço Residencial", value=df[df['ID'] == record_id]['Endereço Residencial'].values[0])
            obs = st.text_area("Observação", value=df[df['ID'] == record_id]['Observação'].values[0])

            if st.button("Atualizar"):
                df.loc[df['ID'] == record_id, 'Cidade'] = cidade
                df.loc[df['ID'] == record_id, 'Nome'] = nome
                df.loc[df['ID'] == record_id, 'Telefone'] = telefone
                df.loc[df['ID'] == record_id, 'CPF'] = cpf
                df.loc[df['ID'] == record_id, 'RG'] = rg
                df.loc[df['ID'] == record_id, 'Endereço da obra'] = endereco_obra
                df.loc[df['ID'] == record_id, 'Endereço Residencial'] = endereco_residencial
                df.loc[df['ID'] == record_id, 'Observação'] = obs
                write_data(df)
                st.success("Registro atualizado com sucesso!")
        else:
            st.error("ID não encontrado!")
            with st.expander("Visualizar Registros"):
                df_reset = df.reset_index(drop=True)
                st.table(df_reset)

elif option == "Deletar Registro":
    st.info("### 🗑️Excluir um registro")
    with st.container():
        record_id = st.number_input("ID do registro a ser excluído", min_value=0, step=1)
        if record_id in df['ID'].values:

            if st.button("Excluir"):
                df = df[df['ID'] != record_id]
                write_data(df)
                st.success("Registro excluído com sucesso!")
                st.experimental_rerun()
            nome = st.text_input("Nome", value=df[df['ID'] == record_id]['Nome'].values[0])

        else:
            st.error("ID não encontrado!")
            with st.expander("Visualizar Registros"):
                df_reset = df.reset_index(drop=True)
                st.table(df_reset)
