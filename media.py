def mediaAluno(n1, n2):
    media = 0.4 * n1 + 0.6 * n2
    return media

# Solicita ao usuário que insira a primeira nota e converte a entrada para um número de ponto flutuante.
n1 = float(input("Insira n1: "))  

# Solicita ao usuário que insira a segunda nota e converte a entrada para um número de ponto flutuante.
n2 = float(input("Insira n2: "))  

# Chama a função 'mediaAluno' com as notas fornecidas e armazena o resultado na variável 'media'.
media = mediaAluno(n1, n2)  

# Verifica se a média é maior ou igual a 5.
if media >= 5:  
    # Se a média for maior ou igual a 5, imprime "Aprovado" seguido pela média calculada.
    print("Aprovado. Média:", media)  
else:
    # Se a média for menor que 5, imprime "Reprovado" seguido pela média calculada.
    print("Reprovado. Média:", media)  