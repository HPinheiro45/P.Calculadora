import tkinter as tk

def on_click(numero):
    entrada_texto.insert(tk.END, numero)

def calcular():
    try:
        expressao = entrada_texto.get()
        resultado = eval(expressao)
        entrada_texto.delete(0, tk.END)
        entrada_texto.insert(tk.END, resultado)
    except Exception:
        entrada_texto.delete(0, tk.END)
        entrada_texto.insert(tk.END, "Erro")

def limpar():
    entrada_texto.delete(0, tk.END)

# Configuração da janela principal
janela = tk.Tk()
janela.title("P.Cal")
janela.geometry("300x400")

entrada_texto = tk.Entry(janela, font=("Arial", 20))
entrada_texto.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Matriz de botões
botoes = [
    ("+", 1, 2), ("-", 1, 3), #aqui foi criado um espaço para o btn "C".
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("**", 3, 3),
    ("7", 4, 0), ("8", 4, 1), ("9", 4, 2), ("/", 4, 3),
    ("0", 5, 0), (".", 5, 1)
]

# Posicionando os botões
for valor, linha, coluna in botoes:
    botao = tk.Button(janela, text=valor, font=("Arial", 20),
                      command=lambda v=valor: on_click(v))
    botao.grid(row=linha, column=coluna, padx=5, pady=5, sticky="nsew")

botao_limpar = tk.Button(janela, text="C", font=("Arial", 20),command=limpar)
botao_limpar.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

botao_limpar = tk.Button(janela, text="=", font=("Arial", 20), command=calcular)
botao_limpar.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

# Responsividade
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)
for i in range(5):
    janela.grid_rowconfigure(i, weight=1)

janela.mainloop()