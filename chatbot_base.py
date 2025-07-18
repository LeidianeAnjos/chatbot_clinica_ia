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
    "Quinta-feira": "Agendamento para quinta-feira confirmado!",
    "Sexta-feira": "Agendamento para sexta-feira confirmado!",
    "1- Clínica Geral": "Clínica Geral selecionada!!! Escolha uma forma de pagamento.",
    "2- Ginecologia e Obstetrícia": "Ginecologia ou Obstetrícia selecionada!!! Escolha uma forma de pagamento.",
    "3- Cardiologia": "Cardiologia selecionada!!! Escolha uma forma de pagamento.",
    "4- Dermatologia": "Dermatologia selecionada!!! Escolha uma forma de pagamento.",
    "5- Ortopedia": "Ortopedia selecionada!!! Escolha uma forma de pagamento.",
    "6- Endocrinologia": "Endocrinologia selecionada!!! Escolha uma forma de pagamento.",
    "7- Psicologia": "Psicologia selecionada!!! Escolha uma forma de pagamento.",
    "8- Nutrição": "Nutrição selecionada!!! Escolha uma forma de pagamento.",
    "1- Amil": "Convênio Amil",
    "2- Bradesco Saúde": " Convênio Bradesco Saúde",
    "3- SulAmérica": " Convênio SulAmérica",
    "4- Unimed": " Convênio Unimed",
    "5- Hapvida": " Convênio Hapvida",
    "6- Particular": "Particular",

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
def teclado_marcacao():
    return ReplyKeyboardMarkup(
        [["Segunda-feira"],
         ["Terça-feira"],
         ["Quarta-feira"],
         ["Quinta-feira"],
         ["Sexta-feira"]],
        resize_keyboard=True
    )

def teclado_especialidade():
    return ReplyKeyboardMarkup(
        [["1- Clínica Geral"],
         ["2- Ginecologia e Obstetrícia"],
         ["3- Cardiologia"],
         ["4- Dermatologia"],
         ["5- Ortopedia"],
         ["6- Endocrinologia"],
         ["7- Psicologia"],
         ["8- Nutrição"]],
        resize_keyboard=True
    )

def teclado_convenio():
    return ReplyKeyboardMarkup(
        [["1- Amil"],
         ["2- Bradesco Saúde"],
         ["3- SulAmérica"],
         ["4- Unimed"],
         ["5- Hapvida"],
         ["6- Particular"]],
        resize_keyboard=True
    )

def responder(texto_usuario):
    texto_usuario = texto_usuario.strip()  # remover espaços em branco

    # Se o usuário quer marcar consulta, mostrar especialidade
    if texto_usuario == "Quero marcar consulta":
        resposta = perguntas_respostas.get(texto_usuario)
        return resposta, teclado_especialidade()


    # Se o usuário selecionou um dia para consulta, confirmar e voltar para o teclado inicial
    if texto_usuario in ["1- Clínica Geral","2- Ginecologia e Obstetrícia","3- Cardiologia","4- Dermatologia",
         "5- Ortopedia","6- Endocrinologia","7- Psicologia","8- Nutrição"]:
        resposta = perguntas_respostas.get(texto_usuario, "Inválido.")
        return resposta, teclado_convenio()

    # Para outras mensagens, responder com o teclado inicial
    resposta = perguntas_respostas.get(
        texto_usuario,
        "Desculpe, não entendi. Por favor, selecione uma opção."
    )
    return resposta, teclado_inicial()
