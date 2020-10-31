
text = 'dsadsadsadsadsad'
def textToMatrix(text):
  matrix_group = [] 
  matrix_counter = 0
  hex_text = (text.encode(encoding="utf-8")).hex()
  hex_start = 0
  hex_end = 0

  if len(text) > 128:
    raise Exception('Message range exceed the 128 char limit')

  while hex_end < len(hex_text):
    matrix = []
    hex_start = 32 * matrix_counter
    hex_end = 32 * (matrix_counter + 1)
    hex_piece = hex_text[hex_start:hex_end]
    
    for i in range(16):
      hex_char = hex_piece[2 * i: 2 * (i + 1)]
      matrix.append(hex_char or '00')

    matrix_counter += 1
    matrix_group.append(matrix)
    

  print (matrix_group)
textToMatrix(text)
