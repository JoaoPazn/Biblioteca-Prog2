# Problema: Gerenciamento de Livraria
# Você deve criar um sistema simples para gerenciar livros em uma livraria. O
# programa deve permitir:

# 1. Criar uma sequência que contém as categorias de livros da livraria. Esta
# sequência não pode ser alterada.

# 2. Cada livro será representado por uma estrutura que terá os seguintes
# atributos: código, título, autor, ano de publicação, preço e quantidade
# disponível.

# 3. Criar uma sequência que representará o banco de dados da livraria, onde
# cada livro será armazenado onde será possível, adicionar, remover e
# modificar cada livro..

# 4. Criar uma função que recebe os dados de um livro e que o adiciona ao banco
# de dados.

# 5. Criar uma função que receba o código de um livro e a quantidade comprada
# e que calcule o valor a ser pago por esse livro.

# 6. Criar uma função que diminui a quantidade de um livro disponível, sempre
# que um ou mais exemplares dele for(em) vendido(s).

# Exemplo: digamos que o livro “A máquina do caos” tenha 5 exemplares
# inicialmente. Após uma pessoa comprar 2 exemplares dele, a quantidade
# deste livro na lista deve ser atualizada para 3.

# 7. Criar uma função que simula um caixa e que fica perguntando o código do
# livro e a quantidade, até que o caixa encerre a compra. Ao final, deve
# retornar o valor devido pelo cliente e deve diminuir a quantidade de livros
# disponíveis que foram comprados.

# 8. Crie uma função que lista todos os livros cadastrados, com a seguinte
# estrutura:
# Código: xxxx
# Título: xxxxx
# Autor: xxx
# Preço: R$ xx,xx
# Exemplares : xxx

# 9. Crie uma função que buscar livros por autor.

# 10. Crie uma função que remove um livro pelo título

#1

categorias = ("Hístoria", "Ciências-Tecnologicas", "Literatura", "Artes", "Ciêncas-Naturais", "Ciêncas-Sociais", "Linguagem", "Filosofia", "Religiao")

#2 

livro = {
    "Código": 1,
    "Título": "Don Quixote",
    "Autor": "Sancho",
    "Ano de Publicação": 1899,
    "Preço": 10,
    "Quantidade": 1
}

#3

Biblioteca = []

#3.1 

Livroscomprados = []

#4 código, título, autor, ano de publicação, preço e quantidade



  
def receberlivr():

    while True:
        try:
            codigo = input("Digite o código do livro : ")
            codigo = int(codigo)    
            if any(avaliador[0] == codigo for avaliador in Biblioteca):
                print("Erro ao cadastrar código! Tente novamente.  protocolo #1 : Valor já existente!")
            elif any(avaliador[0] == 0 for avaliador in Biblioteca):
                print("Erro ao cadastrar Código! Tente novamente. protocolo #3 : Valor Invalido!")
            else:
                break
        except ValueError:
            print("Erro ao cadastrar código! Tente novamente. protocolo #2 : Valor não númerico!")
    titulo = input("Digite o título : ")
    autor = input("Digite o nome do autor : ")
    while True:
        try:
            anopubli = input("Digite o ano da publicação do livro : ")
            anopubli = int(anopubli)    
            if anopubli <= 1850 or anopubli > 2025:
                print("Erro ao cadastrar Ano da publicação! Tente novamente. protocolo #3 : Valor Invalido!")
            else:
                break
        except ValueError:
            print("Erro ao cadastrar Ano da publicação! Tente novamente. protocolo #2 : Valor não númerico!")
    while True:
        try:
            preco = input("Digite o preco do livro : ")
            preco = preco.replace(",",".")
            preco = float(preco)    
            if preco < 5:
                print("Erro ao cadastrar preco! Tente novamente. protocolo #4.1 : preço muito baixo!")
            elif preco > 100:
                print("Erro ao cadastrar preco! Tente novamente. protocolo #4.2 : preço muito alto!")
            else:
                break
        except ValueError:
            print("Erro ao cadastrar preco! Tente novamente. protocolo #2 : Valor não númerico!")
    while True:
        try:
            exemplares = input("Digite a quantidade de exemplares do livro : ")
            exemplares = int(exemplares)    
            break
        except ValueError:
            print("Erro ao cadastrar Exemplares! Tente novamente. protocolo #2 : Valor não númerico!")
    
    livro = {
        "Código": codigo,
        "Título": titulo,
        "Autor": autor,
        "Ano de Publicação": anopubli,
        "Preço": preco,
        "Quantidade": exemplares
    }

    Biblioteca.append(livro)

# 4.5 Protocolos

def showprotcol():
    print('''Protocolo #1 : Valores já existentes 
Protocolo #2 : Valor não númerico
Protocolo #3 : Valor invalido
Protocolo #4 : Relacionado a preços
''')

# 5. Criar uma função que receba o código de um livro e a quantidade comprada
# e que calcule o valor a ser pago por esse livro.

def compraritens():
    if not Biblioteca:
        print("A biblioteca está vazia.")
        return
    
    print("\n--- Livros disponíveis ---")
    for i, livro in enumerate(Biblioteca, start=1):
        print(f"{i}. Código : {livro['Código']} | "
            f"Título : {livro['Título']} | "
            f"Autor : {livro['Autor']} | "
            f"Ano : {livro['Ano de Publicação']} | "
            f"Preço : R${livro['Preço']:.2f} | "
            f"Quantidade : {livro['Quantidade']}")
        while True:
            compliv = input("Gostaia de comprar algum/outro livro? 1 - Sim / 0 - Não : ")
            if compliv == 1:
                seleclivro = int(input("Insira o Código do livro que você vai comprar : "))
                if any


receberlivr()
compraritens()
