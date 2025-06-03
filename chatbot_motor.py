def responder(texto_usuario):
    if texto_usuario == "Quero marcar consulta":
        resposta = perguntas_respostas.get(texto_usuario)
        return resposta, teclado_marcacao()

    # Teclado padrão para outras interações
    resposta = perguntas_respostas.get(
        texto_usuario,
        "Desculpe, não entendi. Por favor, selecione uma opção."
    )
    return resposta, teclado_inicial()
