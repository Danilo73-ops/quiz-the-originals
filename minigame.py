import random

# Contadores para as respostas
klaus = 0
elijah = 0
rebekah = 0
kol = 0
freya = 0

# Função para exibir a pergunta e registrar a resposta
def perguntar(pergunta, opcoes):
    global klaus, elijah, rebekah, kol, freya
    print(pergunta)
    random.shuffle(opcoes)  # Embaralha as opções
    for i, opcao in enumerate(opcoes, 1):
        print(f"{chr(64 + i)}. {opcao}")  # Usando letras A, B, C, D, E
    resposta = input("Escolha uma opção (A, B, C, D, E): ").upper()
    
    if resposta == 'A':
        klaus += 1
    elif resposta == 'B':
        elijah += 1
    elif resposta == 'C':
        rebekah += 1
    elif resposta == 'D':
        kol += 1
    elif resposta == 'E':
        freya += 1

# Perguntas do minigame
perguntar("1. Como você lidaria com um grande perigo para sua família?", 
          ["Enfrentaria com tudo, sem medo.", 
           "Tentaria resolver de forma estratégica.", 
           "Protegeria a todos a qualquer custo.", 
           "Usaria uma abordagem mais imprevisível.", 
           "Tentaria encontrar uma solução mágica."])

perguntar("2. Qual é a sua maior prioridade na vida?", 
          ["Poder e vingança.", 
           "Família e honra.", 
           "Amor e liberdade.", 
           "Diversão e caos.", 
           "Proteção e equilíbrio."])

perguntar("3. O que você faria se tivesse que escolher entre salvar um amigo e sua família?", 
          ["Salvaria a minha família, sem pensar.", 
           "Tentaria salvar os dois, mas priorizaria a família.", 
           "Tentaria salvar todos, custe o que custar.", 
           "Tomaria uma decisão impulsiva sem pensar muito.", 
           "Usaria magia para salvar os dois."])

perguntar("4. Como você se sentiria se alguém ameaçasse alguém que ama?", 
          ["Furia total.", 
           "Tentaria resolver com calma e racionalidade.", 
           "Defensiva, faria qualquer coisa para proteger.", 
           "Provocaria e desafiaria a pessoa.", 
           "Usaria seus poderes para impedir qualquer ameaça."])

perguntar("5. O que você acha do amor?", 
          ["O amor é uma fraqueza, mas não posso fugir dele.", 
           "O amor é uma força poderosa que deve ser respeitada.", 
           "O amor é tudo que importa, mesmo que eu tenha que sacrificar por ele.", 
           "O amor é divertido, mas não é prioridade.", 
           "O amor pode ser tanto uma benção quanto uma maldição, dependendo de como você o usa."])

# Determinando o personagem baseado nas respostas
resultados = {
    "Klaus": klaus,
    "Elijah": elijah,
    "Rebekah": rebekah,
    "Kol": kol,
    "Freya": freya
}

# Encontrar o personagem com o maior número de respostas
personagem = max(resultados, key=resultados.get)
print(f"\nVocê seria o personagem: {personagem}!")