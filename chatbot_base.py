from telegram import ReplyKeyboardMarkup

# Dicionário com respostas organizadas por tópicos
respostas_clinica = {
    "inicial": {
        "Olá": "Olá! Bem-vindo(a) à Clínica Hipermoderna. Deseja marcar uma consulta?",
        "Quero marcar consulta": "Claro! Escolha o dia da semana que prefere para o atendimento:"
    },
    "dias_da_semana": {
        "Segunda-feira": "Ótimo! Qual horário é melhor pra você?",
        "Terça-feira": "Ótimo! Qual horário é melhor pra você?",
        "Quarta-feira": "Ótimo! Qual horário é melhor pra você?",
        "Quinta-feira": "Ótimo! Qual horário é melhor pra você?",
        "Sexta-feira": "Ótimo! Qual horário é melhor pra você?",
        "Sábado": "Sábado temos horários limitados. Qual seria o melhor horário pra você?"
    },
    "horarios": {
        "08h": "Consulta marcada às 08h. Deseja saber o endereço ou mais informações?",
        "10h": "Consulta marcada às 10h. Deseja saber o endereço ou mais informações?",
        "14h": "Consulta marcada às 14h. Deseja saber o endereço ou mais informações?",
        "16h": "Consulta marcada às 16h. Deseja saber o endereço ou mais informações?"
    },
    "informacoes": {
        "Endereço": "Estamos na Rua Futuro, nº 456, Centro - Cidade Exemplo.",
        "Contato": "Você pode nos ligar ou mandar WhatsApp no (11) 99999-0000.",
        "Serviços": "Oferecemos consultas médicas, exames laboratoriais e atendimento especializado.",
        "Obrigado": "De nada! Estou sempre à disposição. 😊"
    }
}

# Teclados separados por contexto
teclado_inicial = ReplyKeyboardMarkup(
    [["Olá"], ["Quero marcar consulta"]],
    resize_keyboard=True, one_time_keyboard=False
)

teclado_dias = ReplyKeyboardMarkup(
    [["Segunda-feira"], ["Terça-feira"], ["Quarta-feira"],
     ["Quinta-feira"], ["Sexta-feira"], ["Sábado"]],
    resize_keyboard=True, one_time_keyboard=True
)

teclado_horarios = ReplyKeyboardMarkup(
    [["08h"], ["10h"], ["14h"], ["16h"]],
    resize_keyboard=True, one_time_keyboard=True
)

teclado_info = ReplyKeyboardMarkup(
    [["Endereço"], ["Contato"], ["Serviços"], ["Obrigado"]],
    resize_keyboard=True, one_time_keyboard=False
)
