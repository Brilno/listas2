livros = [
    {"id": 1, "titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899},
    {"id": 2, "titulo": "1984", "autor": "George Orwell", "ano": 1949}
]

for livro in livros:
    print(f'ID: {livro["id"]} | O livro "{livro["titulo"]}" foi escrito por {livro["autor"]} em {livro["ano"]}.')
