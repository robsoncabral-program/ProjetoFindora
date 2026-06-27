def assistente_inteligente():
    # Base de conhecimento: Dicionário que armazena a relação Pergunta -> Resposta
    conhecimento = {
        "ola": "Olá! Como posso ajudar-te hoje?",
        "quem es": "Sou um protótipo de assistente virtual em Python.",
        "como funcionas": "Eu aprendo contigo! Se eu não souber algo, tu podes ensinar-me.",
        "tudo bem": "Tudo excelente por aqui, pronto para programar!"
    }
    
    print("--- Assistente Offline Ativo ---")
    print("Dica: Se eu não souber responder, tu podes ensinar-me uma nova resposta!")
    print("Escreve 'sair' para terminar a conversa.")
    
    while True:
        # Limpeza de texto: minusculas e remover espaços nas pontas
        pergunta = input("\nTu: ").lower().strip()
        
        if pergunta in ["sair", "adeus", "fim"]:
            print("Assistente: Até à próxima! Foi um prazer conversar.")
            break
            
        # Interpretação de intenção: verificar se existe no dicionário
        if pergunta in conhecimento:
            print(f"Assistente: {conhecimento[pergunta]}")
        else:
            # Caso não encontre, ele pede ajuda ao utilizador (inteligência colaborativa)
            print("Assistente: Ainda não sei essa... o que devo responder quando me perguntarem isso?")
            nova_resposta = input("Tu (ensina-me): ")
            conhecimento[pergunta] = nova_resposta
            print("Assistente: Aprendi! Guardei essa nova resposta.")

# Iniciar o ciclo de conversa
assistente_inteligente()