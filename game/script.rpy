# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Victor = Character("Victor", color="#D63614", image = "victor")
define Thales = Character("Thales", color="#EFD636", image = "thales")
define Natasha = Character("Natasha", color="#AF4BDD", image = "natasha")
define Maia = Character("Maia", color="#2FD5CA", image = "maia")
default affection = 0

# The game starts here.

label start:

    label home:
        scene bg login

        menu:
            "login": 
                jump game
            "creditos": 
                jump creditos


    label creditos:
        scene bg credits
        menu:
            "voltar": 
                jump home
    
label game:
    #$ countGood = 0
    #$ countBad = 0
    scene bg indigo
    with fade
    play sound "audio/SFX/sfx_app_open.mp3"
    "Terca-feira. 19 horas."
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    play sound "audio/SFX/sfx_notification-002.ogg"
    Victor profile "Achei na mesa da cozinha, quem foi?"
    
    menu:
        " Não fui eu.": 
            play sound "audio/SFX/sfx_keyboard-001.ogg"
            Maia profile " Não fui eu."
            $ affection -= 1

        " Não sei...": 
            play sound "audio/SFX/sfx_keyboard-001.ogg"
            Maia profile"Não sei, estava na sala o tempo todo vendo o jogo."
            $ affection += 1

    play sound "audio/SFX/sfx_notification-002.ogg"
    Thales profile "Como você pode se preocupar com isso?? Nosso time perdeu!!"
    menu:
        "Realmente o jogo é mais importante..": 
            play sound "audio/SFX/sfx_keyboard-002.ogg"
            Maia "Realmente como você pode se preocupar com isso agora?"
            $ affection -= 1
            jump choices2b

        "Calma, não é por aí Thales..": 
            play sound "audio/SFX/sfx_keyboard-002.ogg"
            Maia "Caramba, Thales, você não gostaria se fosse contigo."
            $ affection += 1
            jump choices2b



label choices2a:
    play sound "audio/SFX/sfx_notification-002.ogg"
    Victor "Você tá de sacanagem, né? Vocês ferraram meu boné favorito."
    jump choices2_Com

label choices2b:
    play sound "audio/SFX/sfx_notification-002.ogg"
    Thales "('-.-)"
    jump choices2_Com


label choices2_Com:
    play sound "audio/SFX/sfx_notification-002.ogg"
    Victor "E a senhora draminha? Também não sabe nada?"

    play sound "audio/SFX/sfx_notification-002.ogg"
    Natasha profile "Gente, tá todo mundo de mal humor hoje, por que não falamos disso outro dia?"

    menu:
        " O boné era do pai dele!":
            "audio/SFX/sfx_keyboard-001.ogg"
            Maia "Gente, acho que o Victor está relmente chateado, esse boné era do pai dele."
            $ affection += 1
            jump choices3a
        " É, melhor falar depois":
            "audio/SFX/sfx_keyboard-001.ogg"
            Maia "Boa ideia, acho que poderíamos deixar essa discussão para depois."
            $ affection -= 1
            jump choices3b

label choices3a:
    "audio/SFX/sfx_notification-002.ogg"
    Victor "Pelo menos alguém se preocupa. "
    "audio/SFX/sfx_notification-002.ogg"
    Victor "Acho que não foi você então."
    jump choices3_Com

label choices3b:
    "audio/SFX/sfx_notification-002.ogg"
    Victor "PRA DEPOIS???? "
    "audio/SFX/sfx_notification-002.ogg"
    Victor "Quem nem o livro que você não devolveu já faz seis meses??"
    jump choices3_Com

label choices3_Com:
    "audio/SFX/sfx_notification-002.ogg"
    Thales "Podemos falar sobre isso. Contaot que não seja sobre o jogo."
    "audio/SFX/sfx_notification-002.ogg"
    Victor "Então... Por que você fez isso com meu boné?"
    "audio/SFX/sfx_notification-002.ogg"
    Thales "Agora eu sou o culpado? Apontar o dedo pra mim é mais fácil do que desembaraçar teu cabelo, não é?"
    "audio/SFX/sfx_notification-002.ogg"
    Natasha "Thales, vc sabe que ñ gosto qnd vc fala desse jeito?"
    "audio/SFX/sfx_notification-002.ogg"
    Natasha "Nada vai sair dessa conversa se a gente não dialogar. Vamos nos acalmar.."
    "audio/SFX/sfx_notification-002.ogg"
    Natasha  "Maia, me ajuda aqui..."

    menu:
        "Victor, me explica mais sobre a mancha.":
            play sound "audio/SFX/sfx_keyboard-002.ogg"
            $ affection += 1
            Maia "Victor, esse boné tá manchado de que?"
            jump choices4a
        "Vamo logo achar o culpado disso.":
            play sound "audio/SFX/sfx_keyboard-002.ogg"
            $ affection -= 1
            Maia "Acho que é melhor o responsável se entregar para resolvermos isso."
             
            jump choices4b

label choices4a:
    "audio/SFX/sfx_notification-002.ogg"
    Victor "Levando em conta o cheiro... água sanitária."
    jump choices4_Com

label choices4b:
    "audio/SFX/sfx_notification-002.ogg"
    Natasha "Não deveríamos tentar solucionar ao invés de encontrar um culpado?"
    "audio/SFX/sfx_notification-002.ogg"
    Thales "Talvez a solução seja você colocar ele na cabeça pra vê se clareia suas ideias."
    jump choices4_Com

label choices4_Com:
    "audio/SFX/sfx_notification-002.ogg"
    Victor "Ele está manchado de água sanitária. Com certeza tem um culpado. Não tem solução, já manchou."

    menu:
        "Tem certeza?":
            play sound "audio/SFX/sfx_keyboard-004.ogg"
            Maia "Tem certeza?"
            $ affection -= 1
            jump choiceContinue
        "Entendo a situação, mas será que foi de proposito?":
            play sound "audio/SFX/sfx_keyboard-004.ogg"
            Maia "Olha, Victor, eu entendo sua situação. Mas, não sabemos da intenção da pessoa, ela pode não ter feito de propósito. "
            $ affection += 1
            "~E a pessoa não vai querer falar com você desse jeito..."
            jump choiceContinue

label choiceContinue:

    Natasha " Estou vendo que isso não está indo a lugar algum, então sinto que preciso me expressar. Victor, hoje enquanto assistíamos ao jogo, eu fui ao banheiro e seu boné estava lá largado e surrado."
    Natasha "Como você estava meio desanimado com o jogo, pensei em te animar. Então, decidi limpar o boné pra você. Só que, mano, o resultado não foi nada do que eu esperava."
    Natasha "Fiquei arrasada quando vi como o boné ficou depois da limpeza. Nçao era essa minha intenção, de vdd."

    Natasha "Sinto muito mesmo, tá? Não quero que você jogue a culpa no Thales, porque a responsabilidade é toda minha."
    Natasha "Espero que você entenda que a gente consiga resolver isso. Estou aqui para oq precisar, de verdade."

    menu:
        "Ai também foi burrice né..você é idiota?":
            Maia "Natasha, você é idiota??"
            if  affection > 0:
                jump niceEnding
            else:
                jump badEnding
        "Tudo bem, acontece Nati.":
            Maia "Tudo bem, amiga, no final sua intenção era boa."
            if affection > 0:
                jump niceEnding
            else:
                jump badEnding
label badEnding:
    "audio/SFX/sfx_notification-002.ogg"
    Thales "Calma, Maia. Quem nunca jogou água sanitária no balde de roupa suja?"
    "audio/SFX/sfx_notification-002.ogg"
    Thales "Sem falar que ficou bem mais bonito assim."
    "audio/SFX/sfx_notification-002.ogg"
    Victor "Cala a boca, Thales!! Vocês são o casal sem noção!"
    "audio/SFX/sfx_notification-002.ogg"
    Natasha "E o que isso tem a ver com sermos um casal sem noção? Tu nunca errou?"
    "audio/SFX/sfx_notification-002.ogg"
    Victor "Claro que eu errei mas não fiquei me achando o certo depois né..."
    "audio/SFX/sfx_notification-002.ogg"
    Thales "Não fala assim com ela não Victor tá doido?"
    "audio/SFX/sfx_notification-002.ogg"
    Victor "Até parece que tu nem é meu amigo, me esqueceu totalmente depois da Natasha"
    "audio/SFX/sfx_notification-002.ogg"
    Natasha "Não é sobre isso.. que drama!!"
    "audio/SFX/sfx_notification-002.ogg"
    Victor "Cansei de vocês. Isso não é coisa de quem se importa como outro"

    "Victor saiu do grupo."

    Thales "Bebê chorão demais..."
    Maia "Gente não precisava ter sido assim, Não é só ele que ta errado"
    Natasha "Verdade, maia. Certo tava ele de não ficar aguentando gente falando besteira"
    Thales "Mds.."
    "Natasha saiu do grupo"
    "Thales saiu do grupo"
    "Você é o unico integrante, o grupo será automaticamente encerrado."
    jump end
    

label niceEnding:
    Thales "Ah, foi você quem fez isso, amor? Realmente, não foi a melhor ideia."
    Thales "Tive uma ideia genial! Vamos pintar o boné com hidrocor"
    Victor "Vocês são fogo...Sei que foi sem querer, então vou deixar passar."
    Natasha "Obrigada por entender, e desculpa denovo."
    Maia "feliz que nos entendemos :)"
    Victor "De fato foi importante o dialogo"
    Natasha "Eu até que amo vocês kllklk"
    Thales "Eu amo vocês e jogar lkkkl vejo vocês na quarta."
    
    "Quarta, às 18hrs."

    Natasha "Foi muito massa! vou mandar as fotos"
    show galera foto
    jump end

label end:
    "FIM"

