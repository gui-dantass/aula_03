# váriaveis
# valor informado manualmente
nome_completo = "  Guilherme   " # texto -> str
idade = 16 # inteiro ->
altura = 1.67 # decimal -> float
cidade = "São Paulo"# str
estado = "São Paulo"# str
bairro = "Peinha"# str
tem_cnh = "Fasle" # booleano -> bool
tem_maioridade = True # bool

# criar as seguintes váriaveis: estado, cidade e bairro...
# criar output de todas as váriaveis criadas...
print(nome_completo)
print(idade)
print(altura)
print(cidade)
print(estado)
print(bairro)
print(tem_cnh)
print(tem_maioridade)

## qual tipo é? idade
print(type(idade))
print(type(nome_completo))
print(type(altura))
print(type(cidade))
print(type(estado))
print(type(bairro))
print(type(tem_cnh))
print(type(tem_maioridade))

# criar uma variável e atribuir o valor usado input

nome_cachorro = input("qual o nome do seu cachorro? ")

print("o nome do seu cachorro é ", nome_cachorro) # dois paremetros no print
print("o nome do seu cachorro é " + nome_cachorro) # soma de str
print(f"O nome do seu cachorro {nome_cachorro}") # f-strings

# operadores ariméticos
numero_um = int(input("digite o primeiro número: "))
numero_dois = int(input ("digiite o segundo numero: "))
print(type(numero_um))
print(type(numero_dois))
# qual tipo está recebendo...

soma = numero_um + numero_dois
subtracao = numero_um - numero_dois
divisao = numero_um / numero_dois
multiplicacao = numero_um * numero_dois