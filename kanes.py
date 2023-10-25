def TO_KEY(chave,valor):

    nova_chave = {}
    contador = 0

    if(type(chave) == list and chave != []):
        for item in chave:
          nova_chave.update({item:valor[contador]})
          contador += 1
        return nova_chave
    else:
      print('Lista vazio ou argumento não e do tipo lista')