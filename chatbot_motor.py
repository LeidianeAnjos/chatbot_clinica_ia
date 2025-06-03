from chatbot_base import perguntas_respostas

def responder(pergunta_usuario):
    pergunta_usuario = pergunta_usuario.lower()
    for pergunta in perguntas_respostas:
        if pergunta in pergunta_usuario:
            return perguntas_respostas[pergunta]
    return "Desculpe, ainda não sei responder essa pergunta."
