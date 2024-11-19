import streamlit as st
import openai

# Configuração do Streamlit App
st.title("Resumo de Aulas com GPT")
st.write("Insira a chave de API do OpenAI e a transcrição da aula para gerar um resumo detalhado.")

# Entrada da chave API
api_key = st.text_input("Digite sua chave API do OpenAI:", type="password")

# Entrada do conteúdo (transcrição da aula)
conteudo = st.text_area("Insira o conteúdo da transcrição da aula aqui:")

# Instruções e pergunta padrão
instrucoes = """
algumas intruções: não chamar de vídeo, tutorial etc. sempre chamar de aula. não falar sobre instrutor ou apresentador também. 
segue um modelo de resumo: Geração de Anaglifos no QGIS e UIS. O tutorial explica como gerar anaglifos, que são imagens que criam um efeito 3D quando visualizadas com óculos 3D. 
Este processo envolve o uso do QGIS para a configuração inicial e processamento de imagens, seguido de ajustes finais no software UIS. 
As ferramentas necessárias incluem imagens de satélite, modelos digitais de elevação e o programa UIS para combinar essas imagens em uma imagem estereoscópica.
Conclusão: O tutorial conclui mostrando como criar imagens estereoscópicas 3D ou anaglifos usando software GIS. Após configurar as camadas necessárias no QGIS e realizar o processamento inicial, 
as imagens são importadas para o UIS para manipulação adicional. O resultado final é um par de imagens (visões esquerda e direita) que, quando visualizadas através de óculos 3D, fornecem uma perspectiva tridimensional.
Pontos Chave: Conceito de Anaglifo: Anaglifos são imagens que criam um efeito 3D quando visualizadas com óculos vermelho-ciano. Preparação no QGIS: O tutorial envolve a configuração de imagens de satélite e modelos digitais de elevação no QGIS. 
Uso do Software UIS: O UIS é um software mais antigo usado para combinar as imagens em um formato de anaglifo.
"""

pergunta = (
    "Abaixo, temos a descrição de uma aula em vídeo. "
    "Poderia resumar esta aula em 3 linhas? Além disso, citar 3 pontos chaves, 3 perguntas e respostas para quiz e um FAQ de 3 perguntas. "
    + conteudo
    + instrucoes
)

# Botão para gerar o resumo
if st.button("Gerar Resumo"):
    if api_key and conteudo:
        try:
            # Configurar a API Key
            openai.api_key = api_key
            
            # Solicitação à API do OpenAI
            response = openai.ChatCompletion.create(
                model="gpt-4",  # Modelo a ser usado
                messages=[
                    {"role": "system", "content": "Você é um assistente que gera resumos detalhados de aulas com base em transcrições."},
                    {"role": "user", "content": pergunta},
                ],
            )
            
            # Exibir a resposta
            resposta = response['choices'][0]['message']['content']
            st.subheader("Resumo Gerado:")
            st.write(resposta)
        except Exception as e:
            st.error(f"Erro ao acessar a API: {e}")
    else:
        st.warning("Por favor, insira tanto a chave API quanto o conteúdo da aula.")
