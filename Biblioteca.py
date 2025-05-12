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

Livro = {
"codigo":"codigo",
"Título":"Titulo",
"Autor":"Autor",
"AnoPubli":"AnoPubli",
"Preço":"Preco",
"Exemplares":"Exemplares"
}

#3

Biblioteca = [[1, "historia para noobs", "Moysa", 1997],[6, "geografia para noobs", "emmanuelle", 2345]]

#4 código, título, autor, ano de publicação, preço e quantidade

def receberlivr():
    while True:
        try:
            codigo = input("Digite o código do livro : ")
            codigo = int(codigo)    
            if any(avaliador[0] == codigo for avaliador in Biblioteca):
                print("Erro ao cadastrar código! Tente novamente.  protocolo #1 : Valor já existente!")
            else:
                break
        except ValueError:
            print("Erro ao cadastrar código! Tente novamente. protocolo #2 : Valor não númerico!")
    titulo = input("Digite o título : ")
    autor = input("Digite o nome do autor : ")
    while True:
        try:
            anopubli = input("Digite o código do livro : ")
            anopubli = int(anopubli)    
            break
        except ValueError:
            print("Erro ao cadastrar Ano da publicação! Tente novamente. protocolo #2 : Valor não númerico!")
    
receberlivr()
