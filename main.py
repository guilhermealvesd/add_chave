#Dicionário

pessoa = {
    'Nome': 'Guilherme Alves',
    'Idade': 30,
    'Profissão': 'Analista de Produtos'
}

#Para o usuário informar a nova chave e novo campo

nova_chave = input('Digite o nome do campo: ')
novo_valor = input('Informe o valor do novo campo: ')

#Inserindo a nova chave e valor ao dicionário

pessoa[nova_chave] = novo_valor

# Exibe os dicionário com todos os dados

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')