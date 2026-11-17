funcionarios = [
    [1, "Ana Silva", "Analista de Dados", 4500.00],
    [2, "Carlos Souza", "Desenvolvedor", 5200.00]
]


ID = 0
NOME = 1
SALARIO = 3

for indice, func in enumerate(funcionarios):
    if func[ID] == 2:
        funcionarios[indice][SALARIO] += 500
        
        nome = funcionarios[indice][NOME]
        novo_salario = funcionarios[indice][SALARIO]
        print(f"Aumento aplicado! O novo salário de {nome} é R$ {novo_salario:.2f}.")
        break
