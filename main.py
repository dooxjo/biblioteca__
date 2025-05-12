def calculo():
  numeros = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]
  soma=0.0
  p=0

  for i in numeros:
    soma= soma+i
  media=soma/15
  minimo=min(numeros)
  maximo=max(numeros)

  for i in numeros:
    if i%2==0:
      p=p+1
    else:
      continue

    
  print(media)
  print(minimo)
  print(maximo)
  print(f'{p} números pares')