print ('Программа для шифрования или дешифрования текста')

v1 = input ('Хотите зашифровать или дешифровать текст? (Ш | Д)')
v2 = input ('Русский или английский текст? (ru | en)')
v3 = int (input ('Введите шаг сдвига (цифрами):'))
text = input ('Введите текст:')

ru_a = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ru_a2 = 'абвгдежзийклмнопрстуфхцчшщъыьэюяабвгдежзийклмнопрстуфхцчшщъыьэюя'
en_a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
en_a2 = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

def encryption ():
  total = ''
  for i in range (len (text)):
    if text [i].isupper() and text [i].isalpha():
      if v2.lower () == 'ru':
        x = ru_a.find (text [i])
        x2 = text [i].replace (text [i], ru_a [x + v3])
      elif v2.lower () == 'en':
        x = en_a.find (text [i])   
        x2 = text [i].replace (text [i], en_a [x + v3])
      total += x2
    elif text [i].islower() and text [i].isalpha():
      if v2.lower () == 'ru':
        y = ru_a2.find (text [i])
        y2 = text [i].replace (text [i], ru_a2 [y + v3])
      elif v2.lower () == 'en':
        y = en_a2.find (text [i])
        y2 = text [i].replace (text [i], en_a2 [y + v3])
      total += y2
    else:
      total += text [i]
  return total


def decryption ():
  total = ''
  for i in range (len (text)):
    if text [i].isupper () and text [i].isalpha ():
      if v2.lower () == 'ru':
        x = ru_a.rfind (text [i])
        x2 = text [i].replace (text [i], ru_a [x - v3])
      elif v2.lower () == 'en':
        x = en_a.rfind (text [i])
        x2 = text [i].replace (text [i], en_a [x - v3])
      total += x2
    elif text [i].islower () and text [i].isalpha ():
      if v2.lower () == 'ru':
        y = ru_a2.rfind (text [i])
        y2 = text [i].replace (text [i], ru_a2 [y - v3])
      elif v2.lower () == 'en':
        y = en_a2.rfind (text [i])
        y2 = text [i].replace (text [i], en_a2 [y - v3])
      total += y2
    else:
      total += text [i]
  return total

if v1.lower () == 'ш':
  print (encryption ())
elif v1.lower () == 'д':
  print (decryption ())
