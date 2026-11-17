funcionarios = []

funcionarios.append([1, "Ana Silva", "Analista de Dados", 4500.00])
funcionarios.append([2, "Carlos Souza", "Desenvolvedor", 5200.00])

for id_func, nome, cargo, salario in funcionarios:
    print(f"ID: {id_func} | Nome: {nome} | Cargo: {cargo} | Salário: R$ {salario:.2f}")
