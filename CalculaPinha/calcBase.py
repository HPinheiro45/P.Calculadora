### Implementação de matemática basica
### -Henrique Pinheiro

### Definir função para somar dois números
def somar(x, y):
    return x + y

### Definir função para subtrair dois números
def subtrair(x, y):
    return x - y

### Definir função para multiplicar dois números
def multiplicar(x, y):
    return x * y

### Definir função para dividir dois números
def dividir(x, y):
    return x / y

### Definir função para o módulo
def modulo(x, y):
    return x % y

### Definir função para potência
def pot(x, y):
    return x ** y

### Imprimir as opções de operação disponíveis
print("Selecione a operação.")
print("1.Somar")
print("2.Subtrair")
print("3.Multiplicar")
print("4.Dividir")
print("5.Módulo")
print("6.Potência")

### Obter entrada do usuário para selecionar uma opção
escolha = input("Digite sua opção (1/2/3/4/5/6): ")

### Obter entrada do usuário para os números a serem operados
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

### Executar a operação selecionada
if escolha == '1':
    print(num1, "+", num2, "=", somar(num1, num2))

elif escolha == '2':
    print(num1, "-", num2, "=", subtrair(num1, num2))

elif escolha == '3':
    print(num1, "*", num2, "=", multiplicar(num1, num2))

elif escolha == '4':
    print(num1, "/", num2, "=", dividir(num1, num2))

elif escolha == '5':
    print(num1, "%", num2, "=", modulo(num1, num2))

elif escolha == '6':
    print(num1, "**", num2, "=", pot(num1, num2))

else:
    print("Opção inválida")
