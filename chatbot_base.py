from telegram import ReplyKeyboardMarkup

perguntas_respostas = {
    "Olá": "Olá! Como posso ajudar? Deseja marcar uma consulta?",
    "Quero marcar consulta": "Claro! Por favor, informe o nome completo e o melhor dia para o atendimento.",
    "Horário de atendimento": "Atendemos de segunda a sexta, das 8h às 18h.",
    "Endereço": "Estamos localizados na Rua da Saúde, nº 123.",
    "Obrigado": "De nada! Estou à disposição.",
}

# Teclado com botões
teclado_opcoes = ReplyKeyboardMarkup(
    [["Olá", "Quero marcar consulta"], ["Horário de atendimento", "Endereço"], ["Obrigado"]],
    resize_keyboard=True
)

def responder(texto_usuario):
    resposta = perguntas_respostas.get(texto_usuario, "Desculpe, não entendi. Por favor, selecione uma opção.")
    return resposta, teclado_opcoes
