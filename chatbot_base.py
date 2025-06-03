from telegram import ReplyKeyboardMarkup

# Dicionário com perguntas e respostas
perguntas_respostas = {
    "Olá": "Olá! Como posso ajudar? Deseja marcar uma consulta?",
    "Quero marcar consulta": "Claro! Por favor, informe o nome completo e o melhor dia para o atendimento.",
    "Horário de atendimento": "Atendemos de segunda a sexta, das 8h às 18h.",
    "Endereço": "Estamos localizados na Rua da Saúde, nº 123.",
    "Obrigado": "De nada! Estou à disposição.",
}

# Teclado com botões, para facilitar a interação e evitar erros de digitação
teclado_opcoes = ReplyKeyboardMarkup(
    [["Olá", "Quero marcar consulta"], ["Horário de atendimento", "Endereço"], ["Obrigado"]],
    resize_keyboard=True
)

def responder(texto_usuario):
    # Busca a resposta no dicionário, se não encontrar, responde padrão
    resposta = perguntas_respostas.get(
        texto_usuario,
        "Desculpe, não entendi. Por favor, selecione uma opção."
    )
    # Retorna a resposta e o teclado para mostrar sempre as opções
    return resposta, teclado_opcoes
