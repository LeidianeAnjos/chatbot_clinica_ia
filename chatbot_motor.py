from chatbot_base import respostas_clinica, teclado_inicial, teclado_dias, teclado_horarios, teclado_info

def responder(texto_usuario):
    # Verifica em qual etapa o usuário está com base na mensagem
    if texto_usuario in respostas_clinica["inicial"]:
        return respostas_clinica["inicial"][texto_usuario], teclado_dias
    elif texto_usuario in respostas_clinica["dias_da_semana"]:
        return respostas_clinica["dias_da_semana"][texto_usuario], teclado_horarios
    elif texto_usuario in respostas_clinica["horarios"]:
        return respostas_clinica["horarios"][texto_usuario], teclado_info
    elif texto_usuario in respostas_clinica["informacoes"]:
        return respostas_clinica["informacoes"][texto_usuario], teclado_info
    else:
        return "Desculpe, não entendi. Por favor, selecione uma opção abaixo.", teclado_inicial
