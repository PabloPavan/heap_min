# Algoritmo para testar se uma palavra é palindroma ou
# se alterando uma letra somente ela é poderia ser palindroma
# exemplos:
# abccba retorna True
# abccbb retorna True pq pode se trocar a letra 'b' por 'a'
# abcbbc retorna False pq precisaria trocar duas letras

import textwrap

string = "abcxz"

def diferenca(seq1, seq2):
  count = 0
  for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
      count += 1
  return count

def quasepalidromo(palavra):
  if (palavra == palavra[::-1]):
    return True;
  else:
    if ((len(palavra) % 2) == 1):
      meio = palavra[int(len(palavra)/2)]
      parte1, parte2 = textwrap.wrap(palavra, (int(len(palavra)/2)+1))
      palavra = parte1 + meio + parte2
  parte1, parte2 = textwrap.wrap(palavra, (int(len(palavra)/2)))
  if (diferenca(parte1,parte2[::-1]) == 1):
    return True
  else:
    return False

print(quasepalidromo(string))