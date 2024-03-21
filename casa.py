import turtle
import random
def main():
    r = turtle.Screen()
    r.setup(width=500, height=500)
    r.bgcolor("#6D6EC4")
    s = turtle.Turtle()
    s.shape("turtle")
    s.speed(90)

    chao(s)
    estrela(s)
    ladrilho(s)
    corpo(s)
    teto(s)
    porta(s)
    janela(s)
    tronco(s)
    arvore(s)
    arvore2(s)
    arvore3(s)
    
    
    turtle.done()
    
def chao(s):
    s.penup()
    s.goto(-250, -250)
    s.pendown()
    s.fillcolor("#9BDEAC")
    s.begin_fill()
    s.forward(500)
    s.left(90)
    s.forward (250)
    s.left(90)
    s.forward (500)
    s.left(90)
    s.forward (250)
    s.left(90)
    s.end_fill()
    

def corpo(s):
    s.penup()
    s.goto(0, -100)
    s.pendown()
    s.fillcolor("#FAF9A5")
    s.begin_fill()
    s.forward(200)
    s.left(90)
    s.forward (200)
    s.left(90)
    s.forward (200)
    s.left(90)
    s.forward (200)
    s.left(90)
    s.end_fill()


def teto(s):
    s.penup()
    s.goto(0, 100)
    s.pendown()
    s.fillcolor("#FA2723")
    s.begin_fill()
    s.goto(200, 100)
    s.goto(100, 150)
    s.goto(0, 100)
    s.end_fill()
    

def porta(s):
    s.penup()
    s.goto(25, -100)
    s.pendown()
    s.fillcolor("#EAE1C2")
    s.begin_fill()
    s.forward(50)
    s.left(90)
    s.forward (100)
    s.left(90)
    s.forward (50)
    s.left(90)
    s.forward (100)
    s.left(90)
    s.end_fill()
    

def janela(s):
    s.penup()
    s.goto(100, -35)
    s.pendown()
    s.fillcolor("#C8C0A6")
    s.begin_fill()
    s.forward(75)
    s.left(90)
    s.forward (75)
    s.left(90)
    s.forward (75)
    s.left(90)
    s.forward (75)
    s.left(90)
    s.end_fill()
    
    s.penup()
    s.goto(100, 2.5)
    s.pendown()
    s.forward (75)
    
    s.penup()
    s.goto(137.5, 40)
    s.pendown()
    s.right(90)
    s.forward (75)
    
def arvore(s):
    s.penup() 
    s.goto(-5, 150) 
    s.pendown() 
    s.fillcolor("#FFBED9")
    s.begin_fill()
    s.forward(185)
    s.left(90)
    s.forward (185)
    s.left(90)
    s.forward (185)
    s.left(90)
    s.forward (185)
    s.left(90)
    s.end_fill()

def arvore2(s):
    s.penup() 
    s.goto(-40, 120) 
    s.pendown() 
    s.fillcolor("#F299B3")
    s.begin_fill()
    s.forward(180)
    s.left(90)
    s.forward (180)
    s.left(90)
    s.forward (180)
    s.left(90)
    s.forward (180)
    s.left(90)
    s.end_fill()
    
def arvore3(s):
    s.penup() 
    s.goto(-60, 80) 
    s.pendown() 
    s.fillcolor("#CA758F")
    s.begin_fill()
    s.forward(190)
    s.left(90)
    s.forward (190)
    s.left(90)
    s.forward (190)
    s.left(90)
    s.forward (190)
    s.left(90)
    s.end_fill()
    
def tronco(s):
    s.right(90)
    s.fillcolor("#724C27")
    s.begin_fill()
    s.penup()
    s.goto(-35, 90)
    s.pendown()
    s.forward(30)
    s.left(90)
    s.forward(250)
    s.left(90)
    s.forward(30)
    s.left(90)
    s.forward(250)
    s.left(90)
    s.end_fill()

    s.begin_fill()
    s.penup()
    s.goto(-90, 60)
    s.pendown()
    s.forward(30)
    s.left(90)
    s.forward(250)
    s.left(90)
    s.forward(30)
    s.left(90)
    s.forward(250)
    s.left(90)
    s.end_fill()
    
    
    s.begin_fill()
    s.penup()
    s.goto(-150, 40)
    s.pendown()
    s.forward(30)
    s.left(90)
    s.forward(250)
    s.left(90)
    s.forward(30)
    s.left(90)
    s.forward(250)
    s.left(90)
    s.end_fill()
    
def ladrilho(s):
    s.color("black")
    s.penup()
    s.goto(25, -100)
    s.pendown()
    s.fillcolor("#7E304C")
    s.begin_fill()
    s.goto(175, -100)
    s.goto(125, -250)
    s.goto(-50, -250)
    s.goto(25, -100)
    s.end_fill()
    
def estrela(s):
    for _  in range(50):  # Você pode ajustar o número de estrelas conforme desejar
        x = random.randint(-250, 250)  # Posição aleatória no eixo x
        y = random.randint(0, 250)  # Posição aleatória no eixo y
        tamanho = random.randint(1, 4)  # Tamanho aleatório da estrela
        s.penup()
        s.goto(x, y)
        s.pendown()
        s.color("#FFFADE")  # Define a cor da estrela
        estrela2(s, tamanho)
        
def estrela2(s, tamanho):
    for _  in range(5):
        s.forward(tamanho)
        s.right(144)
main()
