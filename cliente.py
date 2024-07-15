import streamlit as st
import pandas as pd
import openpyxl

st.set_page_config(page_title="Cadastro de Clintes", page_icon="💻", layout="wide", initial_sidebar_state="expanded")

st.success("# Paulo Eiji Viana \n Engenheiro - CREABA 37645/D")

with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Funções auxiliares
def read_data():
    return pd.read_excel('database.xlsx')


def write_data(df):
    df.to_excel('database.xlsx', index=False)


# Leitura dos dados
df = read_data()
st.markdown('## 💻 Cadastro de Clientes' )

with st.container():

    st.info("🆕Preencha os campos abaixo")
    with st.container():
        with st.form('cadastro', clear_on_submit=True):
            cidade = st.selectbox("Cidade", ('Condeúba','Pres. Jânio Quadros','Maetinga', 'Cordeiros', 'Piripá', 'Mortugaba'))
            nome = st.text_input("Nome Completo")
            telefone = st.text_input("Telefone")
            cpf = st.text_input("CPF")
            rg = st.text_input("RG")
            endereco_obra = st.text_input("Endereço da obra (Completo)")
            endereco_residencial = st.text_input("Endereço Residencial (Completo)")
            obs = st.text_input("Observação")
            btn_enviar = st.form_submit_button("Enviar", type="primary")

        if btn_enviar:
            new_id = df['ID'].max() + 1 if not df.empty else 1
            new_row = pd.DataFrame({
                'ID': [new_id],
                'Cidade': [cidade],
                'Nome Completo': [nome],
                'Telefone': [telefone],
                'CPF': [cpf],
                'RG': [rg],
                'Endereço da obra (Completo)': [endereco_obra],
                'Endereço Residencial (Completo)': [endereco_residencial],
                'Observação': [obs]
            })
            df = pd.concat([df, new_row], ignore_index=True)
            write_data(df)

            st.success("Registro adicionado com sucesso!")
