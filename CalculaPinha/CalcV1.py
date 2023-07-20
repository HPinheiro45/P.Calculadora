### MVP CaculaPinha
### -Henrique Pinheiro

### Import de Biblioteca
from tkinter import *

### Somar dois números
def somar():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 + num2
    saida.delete(0, END)
    saida.insert(0, resultado)

### Subtrair dois números
def subtrair():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 - num2
    saida.delete(0, END)
    saida.insert(0, resultado)

### Multiplicar dois números
def multiplicar():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 * num2
    saida.delete(0, END)
    saida.insert(0, resultado)

### Dividir dois números
def dividir():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 / num2
    saida.delete(0, END)
    saida.insert(0, resultado)

### Módulo de dois números
def modulo():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 % num2
    saida.delete(0, END)
    saida.insert(0, resultado)

### Potência de dois números
def pot():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 ** num2
    saida.delete(0, END)
    saida.insert(0, resultado)

### Criar janela
janela = Tk()
janela.title("CALCULAPINHA P.1")

### Labels e caixas de entrada
rotulo1 = Label(janela, text="Digite o primeiro número:")
rotulo1.pack()
entrada1 = Entry(janela)
entrada1.pack()

rotulo2 = Label(janela, text="Digite o segundo número:")
rotulo2.pack()
entrada2 = Entry(janela)
entrada2.pack()

### Botões para executar operações
botao_somar = Button(janela, text="Somar", command=somar)
botao_somar.pack()

botao_subtrair = Button(janela, text="Subtrair", command=subtrair)
botao_subtrair.pack()

botao_multiplicar = Button(janela, text="Multiplicar", command=multiplicar)
botao_multiplicar.pack()

botao_dividir = Button(janela, text="Dividir", command=dividir)
botao_dividir.pack()

botao_modulo = Button(janela, text="Módulo", command=modulo)
botao_modulo.pack()

botao_pot = Button(janela, text="Potência", command=pot)
botao_pot.pack()

### Área para exibir resultados
saida = Entry(janela)
saida.pack()


janela.mainloop()
