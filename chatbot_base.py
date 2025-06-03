# chatbot_base.py

from telegram import ReplyKeyboardMarkup

# Dicionário com perguntas e respostas
perguntas_respostas = {
    "Olá": "Olá! Como posso ajudar? Deseja marcar uma consulta?",
    "Quero marcar consulta": "Claro! Por favor, informe o nome completo e escolha o melhor dia para o atendimento.",
    "Horário de atendimento": "Atendemos de segunda a sexta, das 8h às 18h.",
    "Endereço": "Estamos localizados na Rua da Saúde, nº 123.",
    "Obrigado": "De nada! Estou à disposição.",
    "Segunda-feira": "Agendamento para segunda-feira confirmado!",
    "Terça-feira": "Agendamento para terça-feira confirmado!",
    "Quarta-feira": "Agendamento para quarta-feira confirmado!",
}

# Teclado inicial com botões um abaixo do outro
def teclado_inicial():
    return ReplyKeyboardMarkup(
        [["Olá"],
         ["Quero marcar consulta"],
         ["Horário de atendimento"],
         ["Endereço"],
         ["Obrigado"]],
        resize_keyboard=True
    )

# Teclado para marcar consulta (dias da semana)


# Teclado para marcar consulta (dias da semana)
def teclado_marcacao():
    return ReplyKeyboardMarkup(
        [["Segunda-feira"],
         ["Terça-feira"],
         ["Quarta-feira"],
         ["Quinta-feira"],
         ["Sexta-feira"],
         ["Sábado"]],
        resize_keyboard=True  # <-- vírgula corrigida antes deste argumento
    )

def responder(texto_usuario):
    texto_usuario = texto_usuario.strip()  # remover espaços em branco

    # Se o usuário quer marcar consulta, mostrar opções de dias
    if texto_usuario == "Quero marcar consulta":
        resposta = perguntas_respostas.get(texto_usuario)
        return resposta, teclado_marcacao()

    # Se o usuário selecionou um dia para consulta, confirmar e voltar para o teclado inicial
    if texto_usuario in ["Segunda-feira", "Terça-feira", "Quarta-feira"]:
        resposta = perguntas_respostas.get(texto_usuario, "Dia inválido.")
        return resposta, teclado_inicial()

    # Para outras mensagens, responder com o teclado inicial
    resposta = perguntas_respostas.get(
        texto_usuario,
        "Desculpe, não entendi. Por favor, selecione uma opção."
    )
    return resposta, teclado_inicial()
