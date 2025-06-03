# chatbot_motor.py

from chatbot_base import perguntas_respostas, teclado_opcoes

def responder(texto_usuario):
    # Procura resposta no dicionário ou responde com mensagem padrão
    resposta = perguntas_respostas.get(
        texto_usuario,
        "Desculpe, não entendi. Por favor, selecione uma das opções no teclado."
    )
    return resposta, teclado_opcoes
