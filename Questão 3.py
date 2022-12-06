palavras = input("Insira uma palavra: ")

vogal = ('a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U')

for letra in palavras:
    if letra in vogal:
        print(letra, end=' ')