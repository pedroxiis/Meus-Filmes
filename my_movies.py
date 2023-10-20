def avaliar(filmes, titulo_filme, genero):
  nota_filme = float(input("Nota do filme de 0 a 5: "))
  while 0 > nota_filme or nota_filme > 6:
    nota_filme = float(input("Digite um valor válido\n"))
  genero_filme = int(input("Digite o número correspondente ao gênero do filme.\n \nDRAMA:1\nAÇÃO:2\nFICÇÃO CIENTÍFICA:3\nROMANCE:4\nSUSPENSE:5\nTERROR:6\nANIMAÇÃO:7\nCOMÉDIA:8\n"))
  while 1 > genero_filme or genero_filme > 8:
    genero_filme = int(input("Digite um valor válido\n"))
  genero.append(genero_filme)
  filmes[titulo_filme] = nota_filme
  return filmes
  return genero

def lista_desejos(lista, titulo_filme):
  while titulo_filme != "0":
    lista.append(titulo_filme)
    titulo_filme = input("Nome do filme ou (0) para sair: ")
  return lista

def recomendar(filmes, genero, generos,indicacoes):
  if len(filmes) == 0:
    perg = int(input("Não temos dados da sua preferencia de filmes.\nDigite (1) para escolher um genero.\nDigite (2) para sair.\n"))
    while perg != 1 and perg != 2:
      perg = int(input("Digite um valor válido.\n"))
    if perg == 1:
      escolher_gen(generos,indicacoes)
    elif perg == 2:
      return None
  else:
    from collections import Counter
    contador = Counter(genero)
    num_gen, quant = contador.most_common(1)[0]
    for gen, chave in generos.items():
      if num_gen == chave:
        pergunta_chave = input("De acordo com seus filmes assistidos iremos recomendar filmes de {}.\nDigite (1) se deseja receber recomendações de {}.\nDigite (2) se deseja escolher outro genero\n".format(gen,gen))
        while pergunta_chave != "1" and pergunta_chave != "2":
          pergunta_chave = input("Digite um valor válido\n")
        if pergunta_chave == "1":
          print(indicacoes[chave-1][0])
          print(indicacoes[chave-1][1])
        elif pergunta_chave == "2":
          escolher_gen(generos,indicacoes)
          
def escolher_gen(generos,indicacoes):
  genero_filme = int(input("Escolha o gênero.\n \nDRAMA:1\nAÇÃO:2\nFICÇÃO CIENTÍFICA:3\nROMANCE:4\nSUSPENSE:5\nTERROR:6\nANIMAÇÃO:7\nCOMÉDIA:8\n"))
  while genero_filme > 8 or genero_filme < 1:
    genero_filme = int(input("Digite um valor válido.\n"))
  for gen, chave in generos.items():
    if genero_filme == chave:
        print(indicacoes[chave-1][0])
        print(indicacoes[chave-1][1])
                
def pior_melhor(filmes):
  if len(filmes) == 0:
    print("Você não avaliou nenhum filme ainda")
  else:
    fil = list(filmes.keys())
    nota = list(filmes.values())
    maior = nota[0]
    menor = nota[0]
    indice_maior = 0
    indice_menor = 0
    for c in range(0,len(nota)):
      if nota[c] >= maior:
        maior = nota[c]
        indice_maior = c
      elif nota[c] <= menor:
        menor = nota[c]
        indice_menor = c
    m_filme = fil[indice_maior].upper()
    p_filme = fil[indice_menor].upper()
    print("Melhor filme: {}".format(m_filme))
    print(" Pior  filme: {}".format(p_filme))

def ver_lista(lista,genero,filmes):
  if len(lista) == 0:
    print("Lista de desejos vazia")
  else:
    film_remover = []
    for filme in lista:
      print(filme)
      print()
    pergunta_chave = input("DIGITE (1) PARA AVALIAR UM ITEM DA LISTA DE DESEJO\nDIGITE (2) PARA SAIR\n")
    while pergunta_chave != "1" and pergunta_chave != "2":
      pergunta_chave = input("Digite um valor válido.\n")
    if pergunta_chave == "1":
      for cont in range(0,len(lista)):
        print("Digite {} para avaliar {}".format(cont,lista[cont]))
      print("Digite (-1) para sair\n")
      pergunta_chave2 = int(input(""))
      while pergunta_chave2 != -1:
        if 0 <= pergunta_chave2 <= len(lista)-1:
          titulo_filme = lista[pergunta_chave2]
          avaliar(filmes, titulo_filme, genero)
          film_remover.append(titulo_filme)
        else:
          pergunta_chave2 = int(input("Digite um valor válido."))
    for c in film_remover:
      lista.remove(c)
    return lista

def remover(filmes,lista):
  pergunta_chave = int(input("Digite (1) para remover da lista de desejos\nDigite (2) para remover filmes avaliados\n"))
  while pergunta_chave != 1 and pergunta_chave!=2:
    pergunta_chave = int(input("Digite um valor válido.\n"))  
  
  if pergunta_chave == 1 and len(lista) == 0:
    print("Não ha filmes para remover")
  if pergunta_chave == 1 and len(lista) != 0:
    for ind in range(0,len(lista)):
      print("Digite ({}) para remover {}".format(ind,lista[ind]))
    indice = int(input(""))
    lista.pop(indice)
  if pergunta_chave == 2 and len(filmes) == 0:
    print("Não ha filmes para remover")
  if pergunta_chave == 2 and len(filmes) != 0:
    for filme, avaliacao in filmes.items():
      print("Digite ({}) para remover {}".format(
          list(filmes.keys()).index(filme), filme))
    indice = int(input("Digite o índice do filme a ser removido: "))
    chaves = list(filmes.keys())
    if 0 <= indice < len(chaves):
        filme_removido = chaves[indice]
        del filmes[filme_removido]
    else:
        print("Índice inválido.")
          
def main():
  filmes = {} # Dicionário para armazenar filmes avaliados (título: nota)
  genero = [] # Lista para armazenar gêneros dos filmes avaliados
  generos = {"Drama":1,"Ação":2,"Ficção Científica":3,"Romance":4,"Suspense":5,"Terror":6,"Animação":7,"Comédia":8} # Mapeamento de gêneros
  indicacoes = [["Parasita","Clube da Luta"],["O Senhor dos Anéis: O Retorno do Rei","Batman: O Cavaleiro das Trevas"],["Tudo em Todo o Lugar ao Mesmo Tempo","Interestelar"],["Brilho Eterno de uma Mente sem Lembranças","Um Dia Quente de Verão"],["Garota Exemplar","Corra!"],["Hereditário","O iluminado"],["Homem-Aranha no Aranhaverso","Monstros S.A"],["O Grande Hotel Budapeste","Barbie"]] #matriz com recomendações de filmes onde o numero da linha é correspondente ao numero do genero do filme.
  lista = [] # Lista de filmes na lista de desejos do usuário
  pergunta_chave = "1"
  while pergunta_chave != "0":
    pergunta_chave = (input("DIGITE (1) PARA AVALIAR FILME\nDIGITE (2) PARA ADICIONAR UM FILME A LISTA DE DESEJO\nDIGITE (3) PARA RECOMENDAÇÃO DE FILMES\nDIGITE (4) PARA VER A SUA PIOR E MELHOR AVALIAÇÃO\nDIGITE (5) PARA VER LISTA DE DESEJOS\nDIGITE (6) PARA REMOVER FILMES\nDIGITE (0) PARA ENCERRAR PROGRAMA\n"))
    if pergunta_chave == "1":
      titulo_filme = input("Nome do filme ou (0) para sair: ")
      while titulo_filme != "0":
        avaliar(filmes, titulo_filme,genero)
        titulo_filme = input("Nome do filme ou (0) para sair: ")
    elif pergunta_chave == "2":
      titulo_filme = input("Nome do filme ou (0) para sair: ")
      if titulo_filme != "0":
        lista_desejos(lista, titulo_filme)
    elif pergunta_chave == "3":
      recomendar(filmes,genero,generos,indicacoes)
    elif pergunta_chave == "4":
      pior_melhor(filmes)
    elif pergunta_chave == "5":
      ver_lista(lista, genero, filmes)
    elif pergunta_chave == "6":
      remover(filmes,lista)
main()





