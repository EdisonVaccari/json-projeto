

import streamlit as st
import json

# Configuração da página
st.set_page_config(page_title="Análise de Inicial e Contestação com JSON", layout="wide")

# Inicializar o estado da sessão se não estiver presente
if "dados_inicial_input" not in st.session_state:
    st.session_state["dados_inicial_input"] = ""
if "dados_contestacao_input" not in st.session_state:
    st.session_state["dados_contestacao_input"] = ""

# Função para limpar os campos
def limpar_campos():
    st.session_state["dados_inicial_input"] = ""
    st.session_state["dados_contestacao_input"] = ""

# Campos para colar os dados JSON
st.subheader("Cole os dados JSON para INICIAL")
dados_inicial_input = st.text_area(
    "Dados JSON da Inicial", 
    value=st.session_state["dados_inicial_input"], 
    height=150, 
    placeholder='Cole aqui o JSON da Inicial...'
)

st.subheader("Cole os dados JSON para CONTESTAÇÃO")
dados_contestacao_input = st.text_area(
    "Dados JSON da Contestação", 
    value=st.session_state["dados_contestacao_input"], 
    height=150, 
    placeholder='Cole aqui o JSON da Contestação...'
)

# Botão para processar os dados
if st.button("Processar Dados JSON"):
    try:
        # Converter os dados JSON colados em dicionários Python
        st.session_state["dados_inicial_input"] = dados_inicial_input
        st.session_state["dados_contestacao_input"] = dados_contestacao_input
        
        dados_inicial = json.loads(dados_inicial_input)
        dados_contestacao = json.loads(dados_contestacao_input)

        # Layout em duas colunas para exibir os dados
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Títulos da Inicial")
            titulos_inicial = dados_inicial.get("titulos", [])
            titulos_inicial_texto = "\n".join(titulos_inicial)
            st.text_area("Todos os Títulos da Inicial", value=titulos_inicial_texto, height=150, key="todos_titulos_inicial")
            if st.button("Copiar Títulos da Inicial"):
                st.write("Títulos da Inicial copiados para a área de transferência!")

            st.subheader("Resumos da Inicial")
            resumos_inicial = dados_inicial.get("resumos", [])
            for i in range(min(10, len(titulos_inicial), len(resumos_inicial))):
                if resumos_inicial[i].strip():  # Verifica se o resumo não está vazio
                    st.text_area(f"Resumo {i+1} - Inicial", value=resumos_inicial[i], height=150, key=f"resumo_inicial_{i}")
                    if st.button(f"Copiar Resumo {i+1} - Inicial", key=f"btn_resumo_inicial_{i}"):
                        st.write(f"Resumo {i+1} copiado para a área de transferência!")

        with col2:
            st.subheader("Títulos da Contestação")
            titulos_contestacao = dados_contestacao.get("titulos", [])
            titulos_contestacao_texto = "\n".join(titulos_contestacao)
            st.text_area("Todos os Títulos da Contestação", value=titulos_contestacao_texto, height=150, key="todos_titulos_contestacao")
            if st.button("Copiar Títulos da Contestação"):
                st.write("Títulos da Contestação copiados para a área de transferência!")

            st.subheader("Resumos da Contestação")
            resumos_contestacao = dados_contestacao.get("resumos", [])
            for i in range(min(10, len(titulos_contestacao), len(resumos_contestacao))):
                if resumos_contestacao[i].strip():  # Verifica se o resumo não está vazio
                    st.text_area(f"Resumo {i+1} - Contestação", value=resumos_contestacao[i], height=150, key=f"resumo_contestacao_{i}")
                    if st.button(f"Copiar Resumo {i+1} - Contestação", key=f"btn_resumo_contestacao_{i}"):
                        st.write(f"Resumo {i+1} copiado para a área de transferência!")

    except json.JSONDecodeError:
        st.error("Erro ao processar os dados JSON. Verifique a formatação e tente novamente.")

# Botão para limpar os campos
if st.button("Limpar Tudo"):
    limpar_campos()
