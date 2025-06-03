from telegram import ReplyKeyboardMarkup

# Dicionário com perguntas e respostas
perguntas_respostas = {
    "Olá": "Olá! Bem-vindo à Clínica Hipermoderna! Como posso ajudar? Deseja marcar uma consulta?",
    "Quero marcar consulta": "Claro! Por favor, informe o nome completo e escolha um dia da semana para atendimento.",
    "Horário de atendimento": "Funcionamos de segunda a sábado, das 7h às 20h.",
    "Endereço": "Estamos localizados na Av. das Inovações, nº 456 – Centro Tecnológico, São Paulo.",
    "Convênios aceitos": "Aceitamos os seguintes convênios: Unimed, Amil, Bradesco Saúde, SulAmérica e Particular.",
    "Especialidades": "Oferecemos atendimento em: Clínica Geral, Cardiologia, Pediatria, Ginecologia, Dermatologia, Ortopedia e Psicologia.",
    "Exames disponíveis": "Realizamos exames como: Hemograma, Eletrocardiograma, Ultrassonografia, Raio-X, Teste Ergométrico e mais.",
    "Contato": "Você pode falar conosco pelo telefone (11) 4002-8922 ou pelo WhatsApp (11) 98888-0000.",
    "Obrigado": "De nada! Qualquer coisa, estou por aqui. 😊",
    "Tchau": "Até mais! A Clínica Hipermoderna agradece seu contato. 👋",
}

# Teclado principal com opções iniciais
teclado_principal = ReplyKeyboardMarkup(
    [
        ["Olá", "Quero marcar consulta"],
        ["Horário de atendimento", "Endereço"],
        ["Convênios aceitos", "Especialidades"],
        ["Exames disponíveis", "Contato"],
        ["Obrigado", "Tchau"]
    ],
    resize_keyboard=True
)

# Teclado com dias da semana para marcação
teclado_dias_semana = ReplyKeyboardMarkup(
    [
        ["Segunda-feira"],
        ["Terça-feira"],
        ["Quarta-feira"],
        ["Quinta-feira"],
        ["Sexta-feira"],
        ["Sábado"]
    ],
    resize_keyboard=True
)

# Função de resposta com teclado dinâmico
def responder(texto_usuario):
    resposta = perguntas_respostas.get(
        texto_usuario,
        "Desculpe, não entendi. Por favor, selecione uma das opções abaixo."
    )

    # Muda o teclado dependendo da pergunta
    if texto_usuario == "Quero marcar consulta":
        return resposta, teclado_dias_semana
    else:
        return resposta, teclado_principal
