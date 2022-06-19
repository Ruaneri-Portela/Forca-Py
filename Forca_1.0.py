from graphics import *
import random
def inicio():
    win=GraphWin("Iniciar",700,100)
    win.setBackground(color_rgb(181,90,48))
    ponto_central=Point(350,50)
    ponto_canto=Point(90,85)
    texto_canto=Text(ponto_canto,"F1(Ajuda) F2(Sobre)")
    texto_canto.draw(win)
    texto=Text(ponto_central,"Para iniciar aperte na janela!\nPara abrir os os menus aperte na janela com a tecla indicada!")
    texto.draw(win)
    win.getMouse()
    entrada_out_box=win.checkKey()
    if entrada_out_box=="F1":
        ajuda()
    if entrada_out_box=="F2":
        sobre()
    win.close()
def erro(entrada):
    win=GraphWin("Erro Fatal",700,100)
    win.setBackground(color_rgb(255,0,0))
    ponto_central=Point(350,25)
    string_de_saida="Ocorreu um erro fatal"
    texto=Text(ponto_central,string_de_saida)
    texto.draw(win)
    ponto_central=Point(350,50)
    string_de_saida=entrada
    texto=Text(ponto_central,string_de_saida)
    texto.draw(win)
    ponto_central=Point(350,75)
    string_de_saida="Execute novamente"
    texto=Text(ponto_central,string_de_saida)
    texto.draw(win)
    win.getMouse()
    win.close()
def sobre():
    win=GraphWin("Sobre",700,100)
    win.setBackground(color_rgb(181,90,48))
    ponto_central=Point(350,50)
    texto=Text(ponto_central,"Criado por Ruaneri Ferreira Portela \n FURG Nº 149369 \n 2021")
    texto.draw(win)
    win.getMouse()
    win.close()
def ajuda():
    win=GraphWin("Ajuda",700,200)
    win.setBackground(color_rgb(181,90,48))
    ponto_texto1=Point(350,50)
    ponto_texto2=Point(350,70)
    ponto_texto3=Point(350,100)
    ponto_texto4=Point(350,150)
    texto1=Text(ponto_texto1,"Para jogar insira a operaçao que você desconfie que esteja sendo usada na equação, ela pode ser:")
    texto1.draw(win)
    texto2=Text(ponto_texto2,"(+, -, * , /)")
    texto2.draw(win)
    texto3=Text(ponto_texto3,"Insira o que você acha no primeiro espaço da equerda para a direita e assim sucessivamente")
    texto3.draw(win)
    texto4=Text(ponto_texto4,"Para encerrar o jogo aperte (Esc), Para sair da tela de ajuda aperte na tela")
    texto4.draw(win)
    win.getMouse()
    win.close()
def principal():
    win=GraphWin("Forca v1.0",400,400)
    win.setBackground(color_rgb(181,90,48))
    tela_interna=Rectangle(Point(25,25),Point(375,375))
    tela_interna.setFill(color_rgb(253, 172, 83))
    tela_interna.draw(win)
    valor1=random.randrange(0,10)
    valor2=random.randrange(0,10)
    valor3=random.randrange(0,10)
    valor4=random.randrange(0,10)
    sinais=["/","*","-","+"]
    gat=True
    while gat==True:
        try:
            simbolo1=random.choice(sinais)
            simbolo2=random.choice(sinais)
            simbolo3=random.choice(sinais)
            string_eval=str(valor1)+str(simbolo1)+str(valor2)+str(simbolo2)+str(valor3)+str(simbolo3)+str(valor4)
            resultado=eval(string_eval)
            gat=False
        except:
            pass
    resultado=float(resultado)
    resultado=('%.2f' % (resultado))
    string_de_saida=valor1,"------",valor2,"------",valor3,"-----",valor4,"=",resultado
    ponto_texto_equacao=Point(200,300)
    equacao_oculta=Text(ponto_texto_equacao,string_de_saida)
    equacao_oculta.draw(win)
    ponto_titulo=Point(200,50)
    titulo=Text(ponto_titulo,"Forca númerica\n Não deixe o triangulo 3D se formar")
    titulo.draw(win)
    #vetor do triangulo
    P1=Point(165,180)
    P2=Point(205,180)
    P3=Point(185,200)
    P4=Point(150,200)
    P5=Point(180,110)
    C1=Line(P1,P2)
    C2=Line(P2,P3)
    C3=Line(P1,P4)
    l4=Line(P3,P4)
    l5=Line(P3,P5)
    l6=Line(P4,P5)
    l7=Line(P1,P5)
    l8=Line(P2,P5)
    contador =0
    #----------------
    ponto_entrada_usr=Point(200,350)
    entra_usuario= Entry(ponto_entrada_usr,3)
    entra_usuario.draw(win)
    ponto_retorno=Point(200,250)
    retoro=Text(ponto_retorno,"")
    retoro.draw(win)
    inicio_logica=True
    l1=True
    l2=True
    l3=True
    gat1=3
    inicio()
    while inicio_logica==True:
        if contador==8:
              retoro.setText("Você perdeu!")
        entrada_out_box=win.checkKey()
        entra_usuario.setText("")
        while l1==True:
            retoro.setText("Aperte dentro da janela pra enviar!")
            win.getMouse()
            entrada_out_box=win.checkKey()
            entrada_in_box=entra_usuario.getText()
            if entrada_in_box==simbolo1:
                novoeq=(valor1,simbolo1,valor2,"------",valor3,"-----",valor4,"=",resultado)
                equacao_oculta.setText(novoeq)
                retoro.setText("Acertou(Aperte para descartar!)")
                win.getMouse()
                l1=False
                entra_usuario.setText("")
            if entrada_in_box!=simbolo1:
                contador=contador+1
                if contador == 1:
                     C1.draw(win)
                if contador == 2:
                     C2.draw(win)
                if contador == 3:
                     C3.draw(win)
                if contador == 4:
                     l4.draw(win)
                if contador == 5:
                     l5.draw(win)
                if contador == 6:
                     l6.draw(win)
                if contador == 7:
                     l7.draw(win)
                if contador ==8:
                     l1=False
                     l3=False
                     l2=False
                     l1=False
                     l8.draw(win)
                retoro.setText("Errou(Aperte para descartar!)")
                win.getMouse()
                entra_usuario.setText("")
        entra_usuario.setText("")
        while l2==True:
            retoro.setText("Aperte dentro da janela pra enviar!")
            win.getMouse()
            entrada_out_box=win.checkKey()
            entrada_in_box=entra_usuario.getText()
            if entrada_in_box==simbolo2:
                novoeq=(valor1,simbolo1,valor2,simbolo2,valor3,"-----",valor4,"=",resultado)
                equacao_oculta.setText(novoeq)
                retoro.setText("Acertou(Aperte para descartar!)")
                win.getMouse()
                l2=False
                entra_usuario.setText("")
                retoro.setText("")
            if entrada_in_box!=simbolo2:
                contador=contador+1
                if contador == 1:
                     C1.draw(win)
                if contador == 2:
                     C2.draw(win)
                if contador == 3:
                     C3.draw(win)
                if contador == 4:
                     l4.draw(win)
                if contador == 5:
                     l5.draw(win)
                if contador == 6:
                     l6.draw(win)
                if contador == 7:
                     l7.draw(win)
                if contador ==8:
                     l8.draw(win)
                     l3=False
                     l2=False
                     l1=False
                retoro.setText("Errou(Aperte para descartar!)")
                win.getMouse()
                retoro.setText("")
                entra_usuario.setText("")
        while l3==True:
            retoro.setText("Aperte dentro da janela pra enviar!")
            win.getMouse()
            entrada_out_box=win.checkKey()
            entrada_in_box=entra_usuario.getText()
            if entrada_in_box==simbolo3:
                novoeq=(valor1,simbolo1,valor2,simbolo2,valor3,simbolo3,valor4,"=",resultado)
                equacao_oculta.setText(novoeq)
                retoro.setText("Acertou(Aperte para descartar!)")
                win.getMouse()
                l3=False
                entra_usuario.setText("")
                retoro.setText("")
            if entrada_in_box!=simbolo3:
                contador=contador+1
                if contador == 1:
                     C1.draw(win)
                if contador == 2:
                     C2.draw(win)
                if contador == 3:
                     C3.draw(win)
                if contador == 4:
                     l4.draw(win)
                if contador == 5:
                     l5.draw(win)
                if contador == 6:
                     l6.draw(win)
                if contador == 7:
                     l7.draw(win)
                if contador ==8:
                     l8.draw(win)
                     l3=False
                     l2=False
                     l1=False
                retoro.setText("Errou(Aperte para descartar!)")
                win.getMouse()
                entra_usuario.setText("")
                retoro.setText("")
            entra_usuario.setText("")
            if contador<8:
                retoro.setText("Você ganhou!")
        if contador<8:
            retoro.setTextColor(color_rgb(0,255,10)) 
        if contador >=8:
             retoro.setTextColor(color_rgb(255,0,0)) 
        equacao_oculta.setText(string_eval+"="+resultado)    
    win.close()
principal()