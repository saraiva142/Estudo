import streamlit as st;
from os import write;
from numpy.core.fromnumeric import size;
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente


# Configurando o tema padrão
st.set_page_config(
    page_title="João Saraiva",
    page_icon=":blossom:",
    layout="wide",  # ou "centered"
)

st.title('Estudos João Saraiva :sparkles:')

with st.form(key="include_cliente"):
    input_name = st.text_input(label="Insira o seu nome")
    input_age = st.number_input(label="Insira sua idade", format="%d", step=1)#inteiro, ste=1 adicionar de um em um no +
    input_occupation = st.selectbox("Selecione seu cargo", ["Estagiário", "Analista", "Desenvolvedor", "Comercial"])
    input_button_submit = st.form_submit_button(label="Enviar")
    

if input_button_submit:  #(Se o input_botton_submit for True = Apertado)
    cliente.nome = input_name
    cliente.idade = input_age
    cliente.cargo = input_occupation
    
    ClienteController.Incluir(cliente)
    st.success('Cadastrado com sucesso!', icon="✅")