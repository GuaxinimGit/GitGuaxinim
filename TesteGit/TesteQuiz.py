import random

# 1. Banco de dados de perguntas
perguntas = [
    {
        "pergunta": "Qual é a capital do Brasil?",
        "opcoes": ["A) Rio de Janeiro", "B) Brasília", "C) São Paulo", "D) Salvador"],
        "resposta": "B"
    },
    {
        "pergunta": "Quanto é 7 x 8?",
        "opcoes": ["A) 54", "B) 56", "C) 62", "D) 48"],
        "resposta": "B"
    },
    {
        "pergunta": "Qual elemento químico tem o símbolo 'O'?",
        "opcoes": ["A) Ouro", "B) Osmo", "C) Oxigênio", "D) Ozônio"],
        "resposta": "C"
    }
]

def executar_quiz(lista_perguntas):
    # Embaralha as perguntas para que apareçam em ordem aleatória
    perguntas_random = lista_perguntas.copy()
    random.shuffle(perguntas_random)

    pontuacao = 0

    print("=== BEM-VINDO AO QUIZ PYTHON! ===\n")

    for i, item in enumerate(perguntas_random, 1):
        print(f"Pergunta {i}: {item['pergunta']}")
        for opcao in item["opcoes"]:
            print(opcao)

        resposta_usuario = input("Sua resposta (A, B, C ou D): ").strip().upper()

        if resposta_usuario == item["resposta"]:
            print("✨ Resposta correta!\n")
            pontuacao += 1
        else:
            print(f"❌ Resposta errada! A correta era {item['resposta']}.\n")

    print(f"Quiz finalizado! Você acertou {pontuacao} de {len(perguntas_random)} perguntas.")

# Executar o programa
executar_quiz(perguntas)
