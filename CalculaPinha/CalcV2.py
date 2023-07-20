### CalculaPinha versão.2
### -Henrique Pinheiro

### Import de Bibliotecas (Adição da B. Turtle para implementar tela de "Loading")
from tkinter import *
from tkinter import ttk

# Definir função para somar dois números
def somar():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 + num2
    saida.delete(0, END)
    saida.insert(0, resultado)

# Definir função para subtrair dois números
def subtrair():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 - num2
    saida.delete(0, END)
    saida.insert(0, resultado)

# Definir função para multiplicar dois números
def multiplicar():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 * num2
    saida.delete(0, END)
    saida.insert(0, resultado)

# Definir função para dividir dois números
def dividir():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 / num2
    saida.delete(0, END)
    saida.insert(0, resultado)

# Módulo de dois números
def modulo():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 % num2
    saida.delete(0, END)
    saida.insert(0, resultado)

# Potência de dois números
def pot():
    num1 = float(entrada1.get())
    num2 = float(entrada2.get())
    resultado = num1 ** num2
    saida.delete(0, END)
    saida.insert(0, resultado)

# Criar janela
janela = Tk()
janela.title("CalculaPinha versão.2")
janela.geometry("205x290")

# Estilo para o botão
estilo = ttk.Style()
estilo.configure('TButton', font=('Times New Roman', 10, 'bold'), borderwidth='4')

# Rótulos e caixas de entrada
numero1 = ttk.Label(janela, text="Digite o primeiro número:", font=('Times New Roman', 10, 'bold'))
numero1.grid(row=0, column=0, padx=10, pady=5)
entrada1 = ttk.Entry(janela, width=30)
entrada1.grid(row=1, column=0, padx=10, pady=5)

numero2 = ttk.Label(janela, text="Digite o segundo número:", font=('Times New Roman', 10, 'bold'))
numero2.grid(row=2, column=0, padx=10, pady=5)
entrada2 = ttk.Entry(janela, width=30)
entrada2.grid(row=3, column=0, padx=10, pady=5)

# Frame para os botões
frame_botao = Frame(janela, width=200, height=200)
frame_botao.grid(row=6, column=0, padx=10, pady=5)

# Botões para executar operações
botao_somar = ttk.Button(frame_botao, text="Somar", command=somar, width=10, padding=10)
botao_somar.grid(row=6, column=0, padx=0, pady=0)

botao_subtrair = ttk.Button(frame_botao, text="Subtrair", command=subtrair, width=10, padding=10)
botao_subtrair.grid(row=6, column=1, padx=0, pady=0)

botao_multiplicar = ttk.Button(frame_botao, text="Multiplicar", command=multiplicar,
                               width=10, padding=10)
botao_multiplicar.grid(row=7, column=0, padx=0, pady=0)

botao_dividir = ttk.Button(frame_botao, text="Dividir", command=dividir, width=10, padding=10)
botao_dividir.grid(row=7, column=1, padx=0, pady=0)

botao_modulo = ttk.Button(frame_botao, text="Módulo", command=modulo, width=10, padding=10)
botao_modulo.grid(row=8, column=0, padx=0, pady=0)

botao_pot = ttk.Button(frame_botao, text="Potência", command=pot, width=10, padding=10)
botao_pot.grid(row=8, column=1, padx=0, pady=0)

# Área de saída para exibir resultados
saida = ttk.Entry(janela, width=30)
saida.grid(row=8, column=0, padx=10, pady=5)

janela.mainloop()
