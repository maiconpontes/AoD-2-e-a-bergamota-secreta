define mc = Character("[user]")
define z = Character("???", color="2F8FE4")
define h = Character("Hyoga", color="2F8FE4")
define p = Character("Professora", color="EF0B04")
define m = Character("Marcelo", color="#8D3A1C")
define w = Character("Waldir", color="#9351E7")
define g = Character("Gon", color="#8D881C")
define c = Character("Chaba", color="#DC925B")
define s = Character("Staraptor", color="#725BDC")
define l = Character("LeoShakur", color="#5BDCCE")
define a = Character("Ade")
define n = Character("Nunes", color="B6FF68")
define mira = Character("Mira")

transform halfleft:
    xalign 0.25 yalign 0.25

transform halfright:
    xalign 0.75 yalign 0.25

label start:
    pause (1.0)
    scene bg black
    play music dizzy
    "{color=#249afc}{i}...{/color} {/i}"
    "{color=#249afc}{i}......{/color} {/i}"
    "{color=#249afc}{i}........................{/color} {/i}"
    "{color=#249afc}{i}Onde estou?{/color} {/i}"
    "{color=#249afc}{i}O que aconteceu comigo?{/color} {/i}"
    "{color=#249afc}{i}Não me lembro de nada...{/color} {/i}"
    "{color=#249afc}{i}Que dor de cabeça!{/color} {/i}"
    "{color=#249afc}{i}Aaaaaach ooo queeee voooou desmaaaaaiaar...{/color} {/i}"
    stop music
    scene bg school with Fade(2.0, 1, 2.0)
    play music days

    "{color=#249afc}{i}Finalmente chegou o primeiro dia de aula na escola da esperança!{/color} {/i}"
    "{color=#249afc}{i}Essa escola é a melhor do mundo.{/color} {/i}"
    "{color=#249afc}{i}Apenas alunos extraordinários conseguem entrar nela.{/color} {/i}"
    "{color=#249afc}{i}Eu não tenho nenhum talento especial.{/color} {/i}"
    "{color=#249afc}{i}O único motivo que consegui entrar nessa escola foi...{/color} {/i}"
    "{color=#249afc}{i}Nepotismo.{/color} {/i}"
    "{color=#249afc}{i}Meus pais são amigos do diretor...{/color} {/i}"
    "{color=#249afc}{i}...{/color} {/i}"
    "{color=#249afc}{i}Há uma pessoa na entrada do portão me encarando.{/color} {/i}"
    "{color=#249afc}{i}Ela está vindo em minha direção!{/color} {/i}"
    show hyoga_idle at truecenter with dissolve

    z "Oi, quem é você?"
    z "Pera, não me diga, eu sei quem é você!"
    z "Seu nome é..."
    python:
        import os
        user2 = os.getlogin()
    z "[user2]!"
    z "Acertei?"
    menu:
        "Mas... como?":
            $ user = user2
            z "Finalmente eu te conheci, [user]!"
            z "Não via a hora disso acontecer..."
            h "Meu nome é Hyoga, muito prazer!"
            "{color=#249afc}{i}Esse cara me dá cala frios!{/color}{/i}"
            h "Estamos na mesma classe, por que não vamos pra sala de aula juntos?"
            mc "Acho que prefiro ir sozinho..."
            stop music
            play sound schoolbell
            ""
            h "Bora pra aula que estamos atrasados!"
            mc "Ei! Para de me puxar!"
            jump nafrentedaescola

        "Errou!":
            "Qual é seu nome então?"
            $ user = renpy.input("Digite o seu nome")
            z "Então, você é o [user]!"
            z "Finalmente eu te conheci, [user]!"
            z "Não via a hora disso acontecer..."
            h "Meu nome é Hyoga, muito prazer!"
            "{color=#249afc}{i}Esse cara me dá cala frios!{/color} {/i}"
            h "Estamos na mesma classe, por que não vamos pra sala de aula juntos?"
            mc "Acho que prefiro ir sozinho..."
            play sound schoolbell
            h "Bora pra aula que estamos atrasados!"
            mc "Ei! Para de me puxar!"
            jump nafrentedaescola

label nafrentedaescola:
    scene bg classroom
    play music days
    show prof
    p "Ei, vocês estão atrasados!"
    p "Vão ficar de castigo após a aula!"
    p "Assim que acabar a aula quero que vocês me encontrem na sala dos professores!"
    "{color=#249afc}{i}Puts!{/color} {/i}"
    "{color=#249afc}{i}Só me faltava essa!{/color} {/i}"
    stop music
    scene bg black with Fade(1, 1, 1)
    play sound schoolbell
    "Uma aula depois..."
    scene bg classroom2
    show hyoga_idle at truecenter
    play music days
    h "Ei, [user]! Antes de irmos à detenção, por que não conhecemos nossos colegas de classe?"
    "{color=#249afc}{i}Parece uma boa ideia mesmo... Mesmo esse cara sendo um pouco assustador ele tem boas ideias!{/color} {/i}"
    mc "Ok :)"
    jump classe_social

label classe_social:
    default met_gon = False
    default met_star = False
    default met_shakur = False
    default met_chaba = False
    default met_waldir = False
    default met_nunes = False
    default met_everyone = 0
    if met_everyone < 6:
        scene bg classroom
        play music bdays2
        call screen social1
        ""
        "{color=#249afc}{i}Com quem devo falar primeiro?{/color} {/i}"

        screen social1:
            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.2
                auto "waldir_%s.png"
                action Jump("waldir_social")

            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos 0.8
                ypos 0.2
                auto "shakur_%s.png"
                action Jump("shakur_social")

            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.2
                auto "gon_%s.png"
                action Jump("gon_social")

            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos 0.8
                ypos 0.7
                auto "chaba_%s.png"
                action Jump("chaba_social")

            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos 0.5
                ypos 0.7
                auto "star_%s.png"
                action Jump("star_social")

            imagebutton:
                xanchor 0.5
                yanchor 0.5
                xpos 0.2
                ypos 0.7
                auto "nunes_%s.png"
                action Jump("nunes_social")
    else:
        scene bg classroom
        show hyoga_idle at truecenter
        h "Acho que falamos com todo mundo, [user]!"
        mc "Sim, todo mundo mundo tem um super talento aqui?"
        h "Claro, nessa escola só entram pessoas super talentosas."
        h "Por falar nisso, não falei o meu talento ainda."
        h "Eu sou o super cultivador de bergamotas!"
        scene bg ci h
        stop music
        show hyoga_idle at truecenter
        with move
        play sound "<from 0 to 3>charintro.mp3"
        pause(3.0)
        play music bdays2
        scene bg classroom
        show hyoga_idle at truecenter
        h "É estimado que eu tenha cultivado cerca de 53 bilhões de bergamotas em toda minha vida!"
        stop music
        "Bergamota...?"
        "..."
        "..."
        scene bg aeroporto2
        with Fade(1,2,1)
        play music p3
        z "Obrigado por resgatar a bergamota filosofal!"
        z "Sei que foi uma jornada muito dura."
        z "Por que você não come ela?"
        mc "Mas é sua bergamota que eu resgatei, não seria educado eu comê-la."
        z "Por favor, eu ficaria muito feliz!"
        mc "Tudo bem, já que insiste!"
        "..."
        mc "Ela tem um gosto muito ruim!"
        mc "Achei que seria bem melhor para uma bergamota \"filosofal\"."
        z "Às vezes temos que fazer um sacrifício para conseguirmos o poder que queremos."
        mc "Do que você está falando?"
        z "A bergamota filosofal traz muitos poderes, mas tem alguns efeitos colaterais."
        mc "Essa bergamota que eu comi???"
        z "Você vai me agradecer em breve, [user]."
        mc "O que você fez comigo, seu maluco?"
        scene bg classroom
        with Fade(1,2,1)
        stop music
        "{color=#249afc}{i}O que foi isso?{/color} {/i}"
        "{color=#249afc}{i}Quem é aquele cara que eu vi?{/color} {/i}"
        show hyoga_idle at truecenter
        h "Ei, [user], você está bem?"
        h "Você ficou pálido de uma hora pra outra!"
        mc "Não foi nada... Estou bem."
        h "Aliás, você ainda não me falou qual o seu talento."
        h "Qual é seu talento?"
        mc "Meu talento...?"
        mc "Acho que não tenho nenhum... Ou não me lembro..."
        h "Que estranho! Isso não é algo que se esqueça facilmente..."
        h "Mas tudo bem, tenho certeza que você é especial do seu jeito haha"
        "{color=#249afc}{i}Isso foi um insulto?{/color} {/i}"
        h "Bom, devemos então ir à detenção, antes que a professora nos castigue novamente!"
        mc "Sim, claro."
        jump detencao

label waldir_social:
    show waldir_idle at halfleft
    show hyoga_idle at halfright
    if met_waldir == False:
        h "Esse é o Waldir"
        mc "Ei, eu conheço ele... ele é o do podcast cajuína!"
        h "Sim, ele é o proprietário do podcast mais famoso do mundo!"
        w "Eae pessoal, vai começar mais um episódio de cajuína sports!"
        hide hyoga_idle
        scene bg ci w
        stop music
        show waldir_idle at truecenter
        with move
        play sound "<from 0 to 3>charintro.mp3"
        pause(3.0)
        play music bdays2
        scene bg classroom
        show waldir_idle at truecenter
        w "Que tal eu entrevistar vocês?"
        h "É melhor entrevistar outros alunos hahaha"
        h "Somos muito insignificantes para participar do seu programa!"
        "{color=#249afc}{i}Ei! Fale por você mesmo...{/color} {/i}"
        $ met_everyone = met_everyone + 1
        $ met_waldir = True
        stop music
        play sound handbook
        "Nível de amizade com Waldir subiu!"
        jump classe_social
    else:
        hide hyoga_idle
        hide waldir_idle
        "{color=#249afc}{i}Já falei com ele, melhor conhecer os outros antes de ir à detenção!{/color} {/i}"
        jump classe_social

label gon_social:
    show gon_idle at halfleft
    show hyoga_idle at halfright
    if met_gon == False:
        h "Esse é o Gon."
        h "Ele é conhecido por ser o melhor advogado do mundo!"
        g "Olá, meu nome é Gon, prazer em conhecê-lo!"
        hide hyoga_idle
        scene bg ci g
        stop music
        show gon_idle at truecenter
        with move
        play sound "<from 0 to 3>charintro.mp3"
        pause(3.0)
        play music bdays2
        scene bg classroom
        show gon_idle at truecenter
        g "Desde pequeno fui treinado para decorar a constituição do Brasil para me tornar o melhor defensor público que exista. Hoje sei todas as leis e códigos civis!"
        g "Você sabia que o artigo 1.284 do código civil diz que \"Os frutos caídos de árvore do terreno vizinho pertencem ao dono do solo onde caíram, se este for de propriedade particular?"
        "{color=#249afc}{i}Esse cara é bom mesmo!{/color} {/i}"
        "{color=#249afc}{i}Se eu precisar um dia de um advogado já sei quem chamar!{/color} {/i}"
        $ met_everyone = met_everyone + 1
        $ met_gon = True
        stop music
        play sound handbook
        "Nível de amizade com Gon subiu!"
        jump classe_social
    else:
        hide hyoga_idle
        hide gon_idle
        "{color=#249afc}{i}Já falei com ele, melhor conhecer os outros antes de ir à detenção!{/color} {/i}"
        jump classe_social

label star_social:
    show star_idle at halfleft
    show hyoga_idle at halfright
    if met_star == False:
        h "Esse é o Star."
        h "Apesar do jeito reservado dele, ele é gente boa."
        s "..."
        mc "..."
        s "..."
        mc "Oi..."
        s "Ah... Você estava falando comigo... Desculpe..."
        s "Não consegui te ouvir por causa desses fones."
        "{color=#249afc}{i}Mas ele não estava me vendo???{/color} {/i}"
        s "Meu nome é Staraptor, mas você pode me chamar de Star."
        hide hyoga_idle
        scene bg ci s
        stop music
        show star_idle at truecenter
        with move
        play sound "<from 0 to 3>charintro.mp3"
        pause(3.0)
        play music bdays2
        scene bg classroom
        show star_idle at truecenter
        s "De acordo com meus dados, sou o melhor estatístico do mundo!"
        s "Alías, você que sabia que a probabilidade de um dado de 6 lados cair em um número específico não é 1 em 6?"
        play sound textnoise
        "{color=#249afc}{i}É o que???{/color} {/i}"
        s "A chance é menor que 1 em 6, pois existe a chance do dado parar de lado resultando assim em um valor nulo."
        mc "Me pegou!"
        $ met_everyone = met_everyone + 1
        $ met_star = True
        stop music
        play sound handbook
        "Nível de amizade com Star subiu!"
        jump classe_social
    else:
        hide hyoga_idle
        hide star_idle
        "{color=#249afc}{i}Já falei com ele, melhor conhecer os outros antes de ir à detenção!{/color} {/i}"
        jump classe_social

label nunes_social:
    show nunes_idle at halfleft
    show hyoga_idle at halfright
    if met_nunes == False:
        h "Esse cara é o Nunes."
        h "Ele é conhecido por ser o químico mais habilidoso do Brasil!"
        h "Nos últimos 3 anos ele descobriu 72 novos elementos químicos!"
        play sound textnoise
        "{color=#249afc}{i}Que???{/color} {/i}"
        n "Olá."
        n "Me chamo Nunes. Não me peça para sintetizar substâncias ilícitas antes de nos conhecermos melhor, por favor."
        hide hyoga_idle
        scene bg ci n
        stop music
        show nunes_idle at truecenter
        with move
        play sound "<from 0 to 3>charintro.mp3"
        pause(3.0)
        play music bdays2
        scene bg classroom
        show nunes_idle at truecenter
        n "Ei, você. Que tal me ajudar com o nome dessa nova substância radiotiva?"
        play sound textnoise
        "{color=#249afc}{i}Isso não é perigoso?{/color} {/i}"
        mc "Que tal... aodônio?"
        n "Hum, gostei. Você é bom nisso!"
        $ met_everyone = met_everyone + 1
        $ met_nunes = True
        stop music
        play sound handbook
        "Nível de amizade com Nunes subiu!"
        jump classe_social
    else:
        hide hyoga_idle
        hide nunes_idle
        "{color=#249afc}{i}Já falei com ele, melhor conhecer os outros antes de ir à detenção!{/color}{/i}"
        jump classe_social


label chaba_social:
    show chaba_idle at halfleft
    show hyoga_idle at halfright
    if met_chaba == False:
        h "Aquele ali é o Chabarator. O mestre da programação!"
        c "print(Iai, Chaba aqui)"
        c "print(Prazer em conhecê-los!)"
        hide hyoga_idle
        scene bg ci c
        stop music
        show chaba_idle at truecenter
        with move
        play sound "<from 0 to 3>charintro.mp3"
        pause(3.0)
        play music bdays2
        scene bg classroom
        show chaba_idle at truecenter
        c "Meu sonho é programar um mundo virtual que tome conta do universo, aonde as pessoas poderão fazer o que quiserem!"
        mc "Que legal! Mas deve faltar muito pra isso ainda..."
        c "Sim."
        c "Tenho pronto apenas 98\% do programa..."
        play sound textnoise
        "{color=#249afc}{i}Como isso é possível?{/color}{/i}"
        $ met_everyone = met_everyone + 1
        $ met_chaba = True
        stop music
        play sound handbook
        "Nível de amizade com Chaba subiu!"
        jump classe_social
    else:
        hide hyoga_idle
        hide chaba_idle
        "{color=#249afc}{i}Já falei com ele, melhor conhecer os outros antes de ir à detenção!{/color}{/i}"
        jump classe_social


label shakur_social:
    show shakur_idle at halfleft
    show hyoga_idle at halfright
    if met_shakur == False:
        play music bob
        "{color=#249afc}{i}Cof... Cof...{/color} {/i}"
        "{color=#249afc}{i}Que fumaça nesse lado da classe!{/color} {/i}"
        h "Esse que está tossindo é o Leo Shakur, o maior topógrafo de todos!"
        l "Eae meus chapas"
        l "Sou o LeoShakur, mas podem me chamar apenas de Shakur. Bora f1?"
        l "Mas só depois de medir a curvatura do planeta terra!"
        hide hyoga_idle
        scene bg ci l
        stop music
        show shakur_idle at truecenter
        with move
        play sound "<from 0 to 3>charintro.mp3"
        pause(3.0)
        play music bdays2
        scene bg classroom
        show shakur_idle at truecenter
        mc "Não, obrigado. Não fumo."
        l "Puts."
        h "Eu quero!"
        mc "Ei Hyoga!"
        $ met_everyone = met_everyone + 1
        $ met_shakur = True
        stop music
        play sound handbook
        "Nível de amizade com Shakur subiu!"
        jump classe_social
    else:
        hide hyoga_idle
        hide shakur_idle
        "{color=#249afc}{i}Já falei com ele, melhor conhecer os outros antes de ir à detenção!{/color}{/i}"
        jump classe_social

label detencao:
    scene bg clubroom
    show prof
    play music days
    p "Muito bem queridos, a tarefa de você é bem simples!"
    p "Vocês vão ler e decorar as regras da escola."
    p "Aqui está o livro com as principais regras da escola, prestem bastante atenção."
    show book at halfright
    p "Estudem as regras pois será de super importância para a estadia de vocês aqui na escola."
    p "Tudo que contém nesse livro é puramente verdade!"
    p "Assim que vocês terminarem podem ir ao dormitório de vocês."
    p "Vejo vocês amanhã."
    hide prof
    play sound footstep
    show hyoga_idle at truecenter
    h "Demos sorte até, parece moleza ler esse livro!"
    mc "Realmente, só tem algumas páginas."
    h "Leia em voz alta por favor, [mc]."
    mc "Ok."
    hide book
    mc "Primeira regra:"
    stop music
    play music omen
    mc "Os alunos devem manter a escola limpa."
    h "Justo."
    mc "Segunda regra:"
    mc "Todos os funcionários da escola devem sempre falar a verdade."
    h "Huh?"
    h "Que regra estranha."
    mc "Terceira regra:"
    mc "Se um corpo for encontrado morto na escola, será imediatamente conduzido uma investigação pelos alunos para descobrir pistas sobre o caso."
    mc "Após disso, os alunos deverão discutir e entrar em acordo sobre o culpado da morte em questão, realizando uma votação para decidir."
    mc "Caso a maioria dos votos seja corretamente para o culpado, o mesmo será punido."
    mc "Caso a maioria dos votos sejam para um inocente; todos os alunos, exceto o culpado, será morto imediatamente."
    play sound textnoise
    h "Essa é mais estranha ainda!"
    mc "Que palhaçada é essa?"
    h "Continue lendo, [user]."
    mc "Quarta regra:"
    mc "Durante horário de aula, a entrada e saída de qualquer pessoa da escola é proibida."
    mc "Quinta regra:"
    mc "Se alguém quebrar uma regra, será punido imediatamente."
    mc "Esse livro é alguma brincadeira de mau gosto, Hyoga! A professora está de sacanagem com a gente!"
    h "Mas se for mentira, não seria um paradoxo?"
    h "No livro diz que os funcionários não podem mentir!"
    mc "Huh..."
    h "Bom, nossa parte fizemos, que era ler o livro!"
    h "Acho melhor irmos para os nossos dormitórios, [user]!"
    mc "Realmente, estou esgotado..."
    h "Vamos nessa então! Até amanhã, [user]!"

label fimdodia:
    scene bg 101
    "{color=#249afc}{i}Bom, pelo visto esse é meu quarto, 101.{/color}{/i}"
    "{color=#249afc}{i}Os outros quartos são dos meus colegas de classe, mas não quero pertubar-los no momento.{/color}{/i}"
    play sound door
    pause(2.0)
    scene bg dormroom
    "{color=#249afc}{i}Até que é aconchegante aqui.{/color}{/i}"
    "{color=#249afc}{i}Estou morto de cansado. Vou me trocar e dormir.{/color}{/i}"
    scene bg dormroomnight
    play music night
    "{color=#249afc}{i}Que dia maluco...{/color}{/i}"
    "{color=#249afc}{i}Nunca pensei que um dia eu iria conseguir entrar nessa escola.{/color}{/i}"
    "{color=#249afc}{i}E meus colegas de classe parecem tão talentosos!{/color}{/i}"
    "{color=#249afc}{i}Aliás, apenas eu não tenho um talento especial...{/color}{/i}"
    "{color=#249afc}{i}O Hyoga me perguntou qual era meu talento como se eu fosse obrigado a ter um.{/color}{/i}"
    "{color=#249afc}{i}Mas realmente eu me sinto fora de lugar aqui, com essas pessoas especiais.{/color}{/i}"
    "{color=#249afc}{i}E aquele livro de regras maluco da escola?{/color}{/i}"
    "{color=#249afc}{i}Será que é pegadinha da professora?{/color}{/i}"
    "{color=#249afc}{i}Mas no livro diz que os funcionários nunca podem mentir!{/color}{/i}"
    "{color=#249afc}{i}E afinal, quem era aquele cara que eu vi numa visão?{/color}{/i}"
    "{color=#249afc}{i}Eu tenho a impressão que conheci ele em algum lugar, mas não consigo me lembrar...{/color}{/i}"
    "{color=#249afc}{i}Recentemente não estou me lembrando de nada!{/color}{/i}"
    "{color=#249afc}{i}Nem tenho certeza que lembro dos nomes de todo mundo!{/color}{/i}"
    "{color=#249afc}{i}Parece até que tenho amnesia!{/color}{/i}"
    "{color=#249afc}{i}Mas deve ser algo passageiro, não devo me preocupar com isso agora.{/color}{/i}"
    "{color=#249afc}{i}Vou dormir pra acordar cedo!{/color}{/i}"

label dia2:
    play sound galo
    pause(2.0)
    scene bg dormroom
    play music days fadeout 2.0
    "{color=#249afc}{i}Hora de ir pra aula!{/color}{/i}"
    "{color=#249afc}{i}Aliás, esqueci o horário que começa as aulas!{/color}{/i}"
    "{color=#249afc}{i}Mas devo estar no horário certo.{/color}{/i}"
    play sound door
    pause(1.5)
    scene bg school
    play sound schoolbell
    "{color=#249afc}{i}Cheguei na hora!{/color}{/i}"
    scene bg classroom
    show prof at truecenter
    "{color=#249afc}{i}Bom dia alunos!{/color}{/i}"
    "{color=#249afc}{i}Hoje a aula será sobre maneiras efetivas de matar uma pessoa sem ser descoberto!{/color}{/i}"
    stop music
    scene bg black with Fade(1, 1, 1)
    play sound schoolbell
    "Uma aula depois..."
    scene bg classroom2
    "{color=#249afc}{i}Tenho um tempo livre antes da próxima aula!{/color}{/i}"
    "{color=#249afc}{i}Com quem desejo passar o tempo?{/color}{/i}"
    "Tempo livre"
    "Escolha alguém para passar o tempo!"
    jump social_link

label social_link:
    scene bg classroom
    play music hey
    call screen social2
    screen social2:
        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.35
            ypos 0.2
            auto "waldir_%s.png"
            action Jump("waldir_confirm")

        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.6
            ypos 0.2
            auto "shakur_%s.png"
            action Jump("shakur_confirm")

        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.1
            ypos 0.2
            auto "gon_%s.png"
            action Jump("gon_confirm")

        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.85
            ypos 0.2
            auto "hyoga_%s.png"
            action Jump("hyoga_confirm")

        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.8
            ypos 0.7
            auto "chaba_%s.png"
            action Jump("chaba_confirm")

        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.5
            ypos 0.7
            auto "star_%s.png"
            action Jump("star_confirm")

        imagebutton:
            xanchor 0.5
            yanchor 0.5
            xpos 0.2
            ypos 0.7
            auto "nunes_%s.png"
            action Jump("nunes_confirm")

label waldir_confirm:
    scene bg classroom
    menu:
        "Passar tempo com Waldir?":
            jump waldir_social2
        "Escolher alguém diferente":
            jump social_link

label waldir_social2:
    scene bg clubroom
    play music social
    "{color=#249afc}{i}Ali está Waldir, na frente do espelho praticando sua dicção.{/color}{/i}"
    mc "Oi Waldir!"
    show waldir_idle at truecenter
    w "Iae [user], bem vindo a mais um episódio do cajuína cast!"
    mc "Oi?"
    w "Desculpe, força do hábito, haha."
    mc "Você sempre pratica sua fala na frente do espelho?"
    w "Sim, sempre que possível eu pratico minha comunicação."
    w "Eu acredito que a comunicação é a melhor coisa do mundo!"
    mc "Você realmente tem talento pra coisa, é realmente divertido te ouvir falar!"
    w "Não foi sempre assim..."
    stop music
    play music reverie
    w "Quando eu era mais novo, eu gagueja muito!"
    mc "Nossa, você gaguejava?"
    w "Sim. Eu sofria bullying todo dia pelos meus colegas de sala..."
    w "Sempre que queria falar algo para alguém, eu pensava duas vezes antes de falar, por medo de passar vergonha..."
    w "Quando a professora chamava meu nome, eu queria morrer!"
    w "Um certo dia, ao responder à uma pergunta em voz alta, uma colega de classe deu tanta risada da minha gagueira que acabou falecendo."
    mc "...!!!"
    w "A partir desse momento, decidi que esse problema não seria mais parte da minha vida e comecei a praticar minha diccção 24h por dia."
    stop music
    play music smile
    w "Hoje felizmente estou curado da minha gagueira, mas ainda penso nela todos os dias."
    mc "Que história de superação, Waldir!"
    w "[user], muito obrigado por ouvir minha história."
    w "Sinto que posso confiar em você."
    play sound handbook
    "Nível de amizade com Waldir subiu!"
    "Você recebeu uma foto íntima do Waldir!"
    jump fim_do_sl

label gon_confirm:
    scene bg classroom
    menu:
        "Passar tempo com Gon?":
            jump gon_social2
        "Escolher alguém diferente":
            jump social_link

label gon_social2:
    scene bg hall
    play music social
    "{color=#249afc}{i}Gon está nos ármarios, mexendo em seus livros de leis.{/color}{/i}"
    mc "Eae, Gon!"
    show gon_idle at truecenter
    g "Olá, [user]. Como vai?"
    mc "Tudo bem, espero não estar te atrapalhando."
    g "Não está não. Aliás, gostaria de fazer uma pergunta à você."
    mc "Pergunta?"
    g "O que acha do famoso juiz Sérgio Morre?"
    mc "Não sei bem opinar... Ele me parece, como posso dizer... desonesto?"
    g "Pois bem, a justiça deve sempre ser imparcial."
    g "Se você for imparcial, você é um lixo."
    g "O problema é que com toda nossa bagagem de vida, como seremos totalmente imparciais?"
    mc "Realmente, não sei..."
    stop music
    play music reverie
    g "Quando eu era criança, eu estava em um supermercado e presenciei uma criança pobre roubando comida."
    g "Eu não ia falar nada, mas o policial que estava por perto viu o ato e prendeu a pobre criança."
    g "Eu tentei argumentar com ele e até ofereci pra pagar a comida, mas ele não quis saber e levou ela à delegacia."
    g "Fiquei muito pensativo. Ela só queria comer, não é justo ela ser presa."
    g "Mais tarde, no noticiário, vi uma notícia que a criança que foi presa cometeu um atentado suicida contra a delegacia e todos os policiais foram mortos por um explosão."
    mc "...!!!"
    stop music
    play music smile
    g "Aquele momento me fez seguir lutando por uma sociedade mais justa para todos."
    g "Foi aonde me encontrei."
    mc "Uau, que bela história!"
    g "[user], obrigado por conversar comigo."
    g "Sinto que posso confiar em você."
    play sound handbook
    "Nível de amizade com Gon subiu!"
    "Você recebeu uma foto íntima do Gon!"
    jump fim_do_sl

label shakur_confirm:
    scene bg classroom
    menu:
        "Passar tempo com Shakur?":
            jump shakur_social2
        "Escolher alguém diferente":
            jump social_link

label shakur_social2:
    scene bg tenis
    play music social
    "{color=#249afc}{i}Ali está Shakur, o que ele está fazendo no meio da quadra de tênis?{/color}{/i}"
    "{color=#249afc}{i}De novo essa fumaça!{/color}{/i}"
    stop music
    play music bob
    show shakur_idle at truecenter
    l "Eae, [user]. Bora f1?"
    mc "Por que você está fumando aqui no meio da quadra de tênis? Cof... Cof..."
    l "De tanto eu fumar eu aprendi as artes de camuflagem."
    l "Aonde você espera que alguém iria fumar?"
    mc "Em algum lugar que não seja uma quadra de tênis..."
    l "Exato, [user]."
    l "Às vezes o melhor esconderijo é o mais fácil de achar."
    l "Além da quadra ser verde também, rs."
    mc "Mas por que você fuma tanto?"
    stop music
    play music reverie
    l "Quando eu era criança eu viva brincando com meu amigo Bob."
    l "Ele era muito mais descolado que eu."
    l "Um dia ele apareceu com um cigarro do demo pra gente experimentar."
    l "Eu tentei mas só tossi..."
    l "A princípio Bob pareceu ter conseguido fumar sem problemas."
    l "Porém, ao dar uma tragada o cigarro foi para suas vias aéreas e Bob começou a engasgar."
    l "Como o cigarro estava aceso, Bob começou a pegar fogo de dentro pra fora."
    l "As últimas palavras dele antes de morrer cremado foram: \"Shakur, não tenha medo de explorar o mundo e a mente.\""
    mc "Meu deus que tragédia!!!"
    stop music
    play music smile
    l "Por isso, em homenagem à ele eu fumo sempre e tenho como objetivo secundário explorar toda curvatura do planeta terra."
    mc "Entendo..."
    l "Obrigado por fumar um comigo, [user]."
    l "Sinto que posso confiar em você, meu chapa."
    play sound handbook
    "Nível de amizade com Shakur subiu!"
    "Você recebeu uma foto íntima do Shakur!"
    jump fim_do_sl

label hyoga_confirm:
    scene bg classroom
    menu:
        "Passar tempo com Hyoga?":
            jump hyoga_social2
        "Escolher alguém diferente":
            jump social_link

label hyoga_social2:
    scene bg teatro
    play music social
    "{color=#249afc}{i}Hyoga está no palco, segurando uma caveira e recitando Shakespeare.{/color}{/i}"
    "{color=#249afc}{i}Ele é realmente um cara interessante.{/color}{/i}"
    show hyoga_idle at truecenter
    h "Ser ou não ser, eis a questão."
    h "[user]!"
    h "Qual o sentido da vida pra você?"
    mc "Não tenho ideia..."
    h "Pra mim é bergamotas."
    mc "Por quê?"
    stop music
    play music reverie
    h "Quando eu era criança, eu era órfão e morava nas ruas."
    h "Passava frio, fome e não tinha amigos."
    h "Um certo dia, um homem me perguntou se eu queria uma bergamota."
    h "Eu faminto que estava, aceitei na hora."
    h "Como agradecimento, dei meu colar pra ele. Era o único objeto que eu tinha à disposição."
    h "O homem colocou o colar no pescoço, porém, algo terrível aconteceu."
    h "Ele foi enforcado pelo colar e morreu ali no local."
    h "Eu desesperado apenas consegui pegar o endereço daonde ele conseguiu a bergamota que me deu."
    h "Lá na fazenda, eu consegui um emprego para me sustentar."
    h "Não demorou muito para que meu talento florescesse."
    stop music
    play music smile
    h "Fui subindo de cargo na fazenda por causa de minhas habilidades cultivadoras e tomei a fazenda para mim."
    h "Por isso digo, que pra mim, bergamota é o sentido da minha vida."
    h "O que acha da minha história, [user]?"
    mc "Confesso que é difícil acreditar..."
    mc "Mas todos os alunos daqui são especiais, então sei bem que é possível."
    h "Você é legal, [user]."
    h "Sinto que posso confiar em você."
    play sound handbook
    "Nível de amizade com Hyoga subiu!"
    "Você recebeu uma foto íntima do Hyoga!"
    jump fim_do_sl

label nunes_confirm:
    scene bg classroom
    menu:
        "Passar tempo com Nunes?":
            jump nunes_social2
        "Escolher alguém diferente":
            jump social_link

label nunes_social2:
    scene bg fundo
    play music social
    "{color=#249afc}{i}Ali está Nunes, mexendo com seu kit de química.{/color}{/i}"
    mc "Olá, Nunes!"
    show nunes_idle at truecenter
    n "Olá, [user]. Você chegou em uma boa hora."
    n "Esse é o aodônio, de antes, que você nomeou."
    mc "Não é perigoso, manipular ele assim?"
    n "Isso que quero testar, [user]."
    n "Por favor, quero que você engula essa solução de aodônio."
    play sound textnoise
    mc "Nem pensar!"
    n "Entendo... Você tem medo de morrer."
    mc "Desse jeito, sim!"
    n "Eu também tinha, [user]."
    n "Por isso estudo química."
    stop music
    play music reverie
    n "Quando eu era criança, eu e minha amiga Kelly fomos explorar uma fábrica abandonada perto de nossas casas."
    n "Essa fábrica quando ativa era usada pelo governo para fazer experimentos científicos."
    n "Porém acabamos ficando presos nela, pois não conseguíamos alcançar a janela que entramos."
    n "Então encontramos dois frascos com dois líquidos, um verde e outro vermelho."
    n "Decidimos que a melhor ação a fazer seria tomá-los, pois senão morreríamos ambos ali."
    n "Kelly tomou o líquido vermelho e eu o verde."
    n "Logo em seguida, Kelly começou a se derreter e seu corpo vaporizar."
    n "A reação causou uma explosão que abriu uma saída pra eu escapar dali."
    mc "Meu deus, que horror!"
    stop music
    play music smile
    n "Não sei o que era o líquido verde, mas gosto de pensar que me deu forças pra estudar química."
    n "Se eu soubesse o suficiente sobre o assunto, minha amiga estaria viva hoje."
    n "Ignorância é o maior dos defeitos, [user]."
    mc "Sinto muito..."
    n "Obrigado por me escutar, [user]."
    n "Sinto que posso confiar em você."
    play sound handbook
    "Nível de amizade com Nunes subiu!"
    "Você recebeu uma foto íntima do Nunes!"
    jump fim_do_sl

label star_confirm:
    scene bg classroom
    menu:
        "Passar tempo com Star?":
            jump star_social2
        "Escolher alguém diferente":
            jump social_link

label star_social2:
    scene bg gym
    play music social
    "{color=#249afc}{i}Ao chegar na quadra de esportes me deparo com Star praticando enterradas.{/color}{/i}"
    "{color=#249afc}{i}Mesmo não sendo tão alto, ele consegue chegar numa altura impressionante!{/color}{/i}"
    show star_idle at truecenter
    s "Olá, [user]! Veio jogar um basquete também?"
    mc "Olá, Star. Não, não... Não sou bom em esportes. Apenas gostaria de passar um tempo com você."
    s "Ótimo! Estou precisando mesmo de um companheiro para me ajudar analisar essas estatísticas do meu treino."
    "{color=#249afc}{i}Star me mostra folhas com diversas estatísticas relacionadas com o treino dele. Ele realmente leva bem a sério!{/color}{/i}"
    s "Por mais que consiga juntar e analisar estatísticas e dados sobre qualquer coisa, quando o assunto é pessoal, você não consegue fazer um bom trabalho."
    mc "Realmente, como diria o ditado popular \"santo de casa não faz milagres\"!"
    s "[user], deixe-me perguntar uma coisa:"
    s "Se estivesse em uma situação aonde você pudesse salvar apenas 1 pessoa, mas mataria outras 5. E vice-versa. Qual você escolheria?"
    mc "Certamente escolheria matar apenas 1!"
    s "Mas e se essa única pessoa fosse um(a) amigo(a) seu?"
    mc "Aí complica..."
    s "Por isso me dedico tanto à estatistica..."
    stop music
    play music reverie
    scene bg train
    play sound train
    s "Era uma manhã como outra qualquer."
    s "Estava atravessando a linha de trem abrir quando percebi que o guarda estava dormindo e não ativou o sistema de segurança pros pedrestres."
    s "Logo à frente estava vindo um trem de carga em alta velocidade."
    s "De um lado, 5 pedrestes atravessando a linha de trem."
    s "Do outro lado, minha amiga de infância, Ester."
    s "Nenhum deles percebeu o trem desgovernado e eu precisava fazer uma decisão naquele momento."
    s "Eu precisava puxar a alavanca para decidir aonde o trem iria."
    s "Se eu puxasse para um lado, 5 pessoas morreriam."
    s "Se eu puxasse para o outro, minha amiga morreria."
    s "Foi tudo tão rápido que nem me lembro exatamente como as coisas aconteceram."
    stop sound
    scene bg gym
    show star_idle at truecenter
    mc "Uau..."
    s "Ontem faz 3 anos que Ester morreu por minha culpa."
    mc "...!!!"
    s "Por isso, a partir daquele momento decidi me dedicar à estatística."
    stop music
    play music smile
    s "Tenho conforto com os números que fiz a decisão certa."
    s "Mesmo que nunca mais verei minha amiga novamente."
    s "No final das contas, somos todos números."
    s "Eu, você, essa escola."
    s "Apenas dados que não trazem nenhum tipo de emoção às pessoas."
    s "Por isso, quero seguir esse caminho para entender o mundo e a mim mesmo, de uma maneira melhor."
    mc "Pensando dessa maneira é um pouco triste, mas te entendo."
    s "Obrigado por passar o tempo comigo, [user]."
    s "Sinto em você um amigo que posso confiar."
    play sound handbook
    "Nível de amizade com Star subiu!"
    "Você recebeu uma foto íntima do Star!"
    jump fim_do_sl

label chaba_confirm:
    scene bg classroom
    menu:
        "Passar tempo com Chaba?":
            jump chaba_social2
        "Escolher alguém diferente":
            jump social_link

label chaba_social2:
    scene bg roof
    play music social
    "{color=#249afc}{i}Chaba está comendo lanche e conversando com alguém.{/color}{/i}"
    "{color=#249afc}{i}Mas quem é essa?{/color}{/i}"
    play sound textnoise
    "{color=#249afc}{i}Pera, é um robô???{/color}{/i}"
    show chaba_idle at halfright
    show robo at halfleft
    c "Olá, [user]!"
    z "Olá, [user]!"
    mc "Oi..."
    c "Essa é minha robô, Maira."
    c "Eu mesmo a programei para agir como se fosse um humano."
    mira "Eu gosto de doces e cachorros."
    play sound dulltext
    mc "Realmente parece um humano..."
    c "Me diga [user], qual sua opinião sobre inteligência artificial?"
    mc "Acho bem legal! Mas temos que tomar cuidado para não sermos exterminados por robôs!"
    c "Pra mim, Maira tem um papel muito importante."
    stop music
    play music reverie
    c "Eu tinha uma amiga de infância chamada Maria."
    c "Um dia, uma máquina agrícola estava passando perto daonde nós estávamos brincando."
    c "De repente, a máquina começou a apresentar defeitos e sair faíscas dela."
    c "O operador da máquina não conseguiu controlá-la e a máquina passou por cima e triturou Maria."
    c "Depois desse trauma, passei a vida toda aprendendo a programar para poder construir uma robô igual a Maria."
    c "Inclusive o nome Maira é uma referência a Maria."
    mc "Uau, que triste..."
    stop music
    play music smile
    c "Claro que não consegui substituir minha amiga por uma robô."
    c "Mas com meus conhecimentos vou procurar avanços na realidade virtual pelo mundo e ajudar pessoas com problemas similares."
    c "Obrigado por lanchar com a gente, [user]."
    c "Sinto que posso confiar em você."
    play sound handbook
    "Nível de amizade com Chaba subiu!"
    "Você recebeu uma foto íntima do Chaba!"
    jump fim_do_sl

label fim_do_sl:
    scene bg classroom
    play music omen
    "{color=#249afc}{i}Foi bem interessante passar meu tempo com essa pessoa!{/color}{/i}"
    "{color=#249afc}{i}Me sinto até cansado...{/color}{/i}"
    "{color=#249afc}{i}Agora de volta pra aula...{/color}{/i}"
    "{color=#249afc}{i}...{/color}{/i}"
    "{color=#249afc}{i}Cadê a professora?{/color}{/i}"
    show hyoga_idle at truecenter
    h "Ei [user], por que não vamos na sala da professora e checamos se está tudo bem?"
    "{color=#249afc}{i}Devemos fazer isso...?{/color}{/i}"
    "{color=#249afc}{i}Bom, não há nada demais irmos até la.{/color}{/i}"
    mc "Tudo bem Hyoga, vamos lá."
    scene bg black
    "{color=#249afc}{i}A cada passo que eu dava eu sinto meu coração bater mais rápido.{/color}{/i}"
    "{color=#249afc}{i}Como se uma descoberta fosse puxar nossas almas pra fora dos nossos corpos.{/color}{/i}"
    "{color=#249afc}{i}Ao entrar na sala da professora, soubemos do que isso se tratava.{/color}{/i}"
    "{color=#249afc}{i}A sensação de desespero total.{/color}{/i}"
    "{color=#249afc}{i}A sensação de falta de esperança.{/color}{/i}"
    stop music
    scene bg clubroom2 with Fade(2,1,1)
    play sound body1
    show prof2 at truecenter
    "{color=#249afc}{i}Ali estava o corpo sem vida da nossa professora.{/color}{/i}"
    play sound body
    pause(2.5)
    narrator "Um corpo foi encontrado dentro das dependências escolares."
    narrator "Após um período de investigação será iniciado um debate para resolução do caso."
    narrator "Porém, isso será apenas no AoD:3 Prisoneiro de Azkaban."
    narrator "Obrigado por jogar AoD:2 e a bergamota secreta!"
    "Feito por Maicon Kyle"
    return
