import random

# CORES NO TERMINAL (ANSI)
VERMELHO = "\033[91m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
MAGENTA = "\033[95m"
CIANO = "\033[96m"
RESET = "\033[0m"
NEGRITO = "\033[1m"


def esperar():
    input(CIANO + "\nPressione ENTER para continuar..." + RESET)


def mostrar_inicio():
    print(AMARELO + NEGRITO)
    print("+==============================================+")
    print("|                                              |")
    print("|                AVENTURA RPG                  |")
    print("|                                              |")
    print("+==============================================+")
    print(RESET)

    print(CIANO + "+----------------------------------------------+")
    print("|                  CRIADORES                   |")
    print("+----------------------------------------------+" + RESET)

    print(VERDE + "| Rafaell Ribeiro Marins                       |")
    print("| Guillerme Dalgobo Fagundes                   |")
    print("| Vitória Azevedo de Souza                     |")
    print("| David Lucas Fernandes Alves                  |")
    print("| Lucas Nunes da Costa                         |")
    print("| Loran Soares da Silva                        |")
    print("| Christian Costa Sanches                      |" + RESET)

    print(CIANO + "+----------------------------------------------+" + RESET)
    print()


def escolher_dificuldade():
    print(NEGRITO + MAGENTA + "Escolha a dificuldade:" + RESET)
    print(CIANO + "1. Fácil" + RESET)
    print(CIANO + "2. Normal" + RESET)
    print(CIANO + "3. Difícil" + RESET)

    escolha = input(AMARELO + "Digite o número da dificuldade: " + RESET)

    while escolha not in ["1", "2", "3"]:
        print(VERMELHO + "Opção inválida. Escolha 1, 2 ou 3." + RESET)
        escolha = input(AMARELO + "Digite o número da dificuldade: " + RESET)

    if escolha == "1":
        dificuldade = "Fácil"

    elif escolha == "2":
        dificuldade = "Normal"

    else:
        dificuldade = "Difícil"

    print()
    print(VERDE + f"Dificuldade escolhida: {dificuldade}" + RESET)
    print()

    return dificuldade


def escolher_personagem():
    print(AMARELO + "Bem-vindo ao RPG!" + RESET)
    print(NEGRITO + MAGENTA + "Escolha seu personagem:" + RESET)

    print(CIANO + "1. Guerreiro" + RESET)
    print(CIANO + "2. Mago" + RESET)
    print(CIANO + "3. Arqueiro" + RESET)
    print(CIANO + "4. Feiticeiro" + RESET)

    escolha = input(AMARELO + "Digite o número do seu personagem: " + RESET)

    while escolha not in ["1", "2", "3", "4"]:
        print(VERMELHO + "Opção inválida. Escolha um número entre 1 e 4." + RESET)
        escolha = input(AMARELO + "Digite o número do seu personagem: " + RESET)

    if escolha == "1":
        personagem = "Guerreiro"
        vida = 150
        ataque = 20
        defesa = 10

    elif escolha == "2":
        personagem = "Mago"
        vida = 100
        ataque = 30
        defesa = 5

    elif escolha == "3":
        personagem = "Arqueiro"
        vida = 120
        ataque = 25
        defesa = 8

    else:
        personagem = "Feiticeiro"
        vida = 80
        ataque = 35
        defesa = 3

    print()
    print(VERDE + f"Você escolheu: {personagem}" + RESET)
    print(VERDE + f"Vida: {vida}" + RESET)
    print(VERDE + f"Ataque: {ataque}" + RESET)
    print(VERDE + f"Defesa: {defesa}" + RESET)

    return personagem, vida, ataque, defesa


def criar_inimigo(fase, dificuldade):
    if fase == 1:
        nome_fase = "Floresta Encantada"
        inimigos = ["Goblin", "Slime", "Morcego"]
        vida = random.randrange(55, 80, 5)
        ataque = random.randint(7, 14)
        defesa = 5

    elif fase == 2:
        nome_fase = "Caverna Sombria"
        inimigos = ["Orc", "Esqueleto", "Lobo Sombrio"]
        vida = random.randrange(75, 105, 5)
        ataque = random.randint(9, 19)
        defesa = 7

    elif fase == 3:
        nome_fase = "Castelo Abandonado"
        inimigos = ["Troll", "Cavaleiro Sombrio", "Minotauro"]
        vida = random.randrange(95, 130, 5)
        ataque = random.randint(12, 23)
        defesa = 8

    else:
        nome_fase = "Covil do Dragão"
        inimigos = ["Dragão"]
        vida = 134
        ataque = 24
        defesa = 8

    if dificuldade == "Fácil":
        vida = vida - 5
        ataque = ataque - 2
        defesa = defesa - 1

    elif dificuldade == "Difícil":
        vida = vida + 12
        ataque = ataque + 1

    if vida < 20:
        vida = 20

    if ataque < 5:
        ataque = 5

    if defesa < 0:
        defesa = 0

    inimigo = random.choice(inimigos)

    return nome_fase, inimigo, vida, ataque, defesa


def mostrar_fase(fase, nome_fase, inimigo):
    print()
    print(AMARELO + "+==============================================+" + RESET)
    print(AMARELO + f"|                   FASE {fase}                   |" + RESET)
    print(AMARELO + "+==============================================+" + RESET)
    print(AMARELO + f"Local: {nome_fase}" + RESET)
    print(VERMELHO + f"Inimigo: {inimigo}" + RESET)
    print(AMARELO + "+==============================================+" + RESET)


def mostrar_status(vida, vida_maxima, inimigo, vida_inimigo, vida_inimigo_maxima):
    print()
    print(AZUL + "---------- STATUS ----------" + RESET)
    print(VERDE + f"Sua vida: {vida}/{vida_maxima}" + RESET)
    print(VERMELHO + f"Vida do {inimigo}: {vida_inimigo}/{vida_inimigo_maxima}" + RESET)
    print(AZUL + "----------------------------" + RESET)


def batalha(vida, vida_maxima, ataque, defesa, inimigo, vida_inimigo, ataque_inimigo, defesa_inimigo):
    vida_inimigo_maxima = vida_inimigo
    especial_usado = False

    while vida > 0 and vida_inimigo > 0:
        mostrar_status(vida, vida_maxima, inimigo, vida_inimigo, vida_inimigo_maxima)

        print()
        print(CIANO + "1. Atacar" + RESET)
        print(CIANO + "2. Defender" + RESET)
        print(CIANO + "3. Fugir" + RESET)
        print(CIANO + "4. Ataque especial" + RESET)

        acao = input(AMARELO + "Escolha sua ação: " + RESET)

        if acao == "1":
            dano = random.randint(5, ataque)
            defesa_sorteada = random.randint(0, defesa_inimigo)
            dano_final = dano - defesa_sorteada

            if dano_final < 1:
                dano_final = 1

            vida_inimigo = vida_inimigo - dano_final

            if vida_inimigo < 0:
                vida_inimigo = 0

            print(VERDE + f"Você atacou e causou {dano_final} de dano!" + RESET)

        elif acao == "2":
            print(AZUL + "Você se preparou para defender!" + RESET)

        elif acao == "3":
            chance_fuga = random.randint(1, 100)

            if chance_fuga <= 35:
                print(AMARELO + "Você conseguiu fugir!" + RESET)
                return vida, "fugiu"
            else:
                print(VERMELHO + "Você tentou fugir, mas não conseguiu!" + RESET)

        elif acao == "4":
            if especial_usado == False:
                dano = random.randint(ataque, ataque * 2)
                defesa_sorteada = random.randint(0, defesa_inimigo)
                dano_final = dano - defesa_sorteada

                if dano_final < 1:
                    dano_final = 1

                vida_inimigo = vida_inimigo - dano_final
                especial_usado = True

                if vida_inimigo < 0:
                    vida_inimigo = 0

                print(MAGENTA + f"Você usou o ataque especial e causou {dano_final} de dano!" + RESET)

            else:
                print(VERMELHO + "Você já usou o ataque especial nessa batalha." + RESET)
                continue

        else:
            print(VERMELHO + "Opção inválida. Escolha 1, 2, 3 ou 4." + RESET)
            continue

        if vida_inimigo <= 0:
            print(VERDE + f"Você derrotou o {inimigo}!" + RESET)
            return vida, "venceu"

        chance_esquiva = random.randint(1, 100)

        if chance_esquiva <= 15:
            print(CIANO + "Você desviou do ataque inimigo!" + RESET)
        else:
            dano_inimigo = random.randint(5, ataque_inimigo)
            defesa_heroi = random.randint(0, defesa)

            if acao == "2":
                defesa_heroi = defesa_heroi + random.randint(5, 15)

            dano_final_inimigo = dano_inimigo - defesa_heroi

            if dano_final_inimigo < 1:
                dano_final_inimigo = 1

            vida = vida - dano_final_inimigo

            if vida < 0:
                vida = 0

            print(VERMELHO + f"O {inimigo} causou {dano_final_inimigo} de dano!" + RESET)

    return vida, "perdeu"


def main():
    mostrar_inicio()
    esperar()

    dificuldade = escolher_dificuldade()
    personagem, vida, ataque, defesa = escolher_personagem()
    vida_maxima = vida
    resultado = ""
    esperar()

    for fase in range(1, 5):
        nome_fase, inimigo, vida_inimigo, ataque_inimigo, defesa_inimigo = criar_inimigo(fase, dificuldade)

        mostrar_fase(fase, nome_fase, inimigo)
        esperar()

        vida, resultado = batalha(
            vida,
            vida_maxima,
            ataque,
            defesa,
            inimigo,
            vida_inimigo,
            ataque_inimigo,
            defesa_inimigo
        )

        if resultado == "perdeu":
            print()
            print(VERMELHO + "Você foi derrotado..." + RESET)
            break

        elif resultado == "fugiu":
            print()
            print(AMARELO + "Você fugiu da batalha. A aventura terminou por enquanto." + RESET)
            break

        else:
            print()
            print(VERDE + "Você venceu a batalha e avançou!" + RESET)

            vida = vida + 25

            if vida > vida_maxima:
                vida = vida_maxima

            print(VERDE + f"Você recuperou um pouco de vida. Vida atual: {vida}/{vida_maxima}" + RESET)
            esperar()

    if vida > 0 and resultado == "venceu":
        print()
        print(VERDE + NEGRITO + "Parabéns! Você completou a aventura!" + RESET)


main()
