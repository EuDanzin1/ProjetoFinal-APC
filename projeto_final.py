file = [
  ['o', 'n', 'e', 'd', 'j', 'n', 'f', 'o', 'f', 'i'],
  ['p', 'p', 'p', 'y', 't', 'h', 'o', 'n', 'd', 'n'],
  ['a', 'j', 'h', 'k', 'a', 'v', 'a', 'j', 'h', 't'],
  ['a', 's', 'm', 'a', 'o', 'v', 'a', 'o', 'v', 'j'],
  ['c', 'a', 'j', 'o', 't', 'v', 'b', 's', 'x', 'f'],
  ['n', 'd', 'a', 'g', 'a', 'a', 'a', 'v', 'c', 'o'],
  ['o', 'm', 'm', 'o', 'r', 'c', 'e', 'g', 'o', 'a'],
  ['s', 'd', 's', 'b', 'a', 'v', 'a', 'j', 'j', 'i'],
  ['j', 'g', 'o', 'l', 'a', 'v', 'a', 'c', 'l', 'v'],
  ['j', 'j', 'n', 'f', 'a', 'v', 'a', 's', 'o', 'a'],
]

# Verifica se a palavra está na horizontal
def checkWordHorizontally(matrix, word, reverse = False):
  if reverse:
    word = word[::-1]

  for i in range(len(matrix)):
    count = 0
    positions = []

    for j in range(len(matrix[i])):
      if matrix[i][j] != word[count]:
        count = 0
        positions = []
      
      if matrix[i][j] == word[count]:
        positions.append([i, j, word[count]])
        count += 1

      if count == len(word):
        return positions

# Verifica se a palavra está na vertical
def checkWordVertically(matrix, word, reverse = False):
  width, height = len(matrix[0]), len(matrix)

  if reverse:
    word = word[::-1]

  for i in range(width):
    count = 0
    positions = []

    for j in range(height):
      if matrix[j][i] != word[count]:
        count = 0
        positions = []
      
      if matrix[j][i] == word[count]:
        positions.append([j, i, word[count]])
        count += 1

      if count == len(word):
        return positions

# Verifica se a palavra está nas diagonais em direção à diagonal secundária
def checkWordDiagonallyTowardsTheSecondaryDiagonal(matrix, word, reverse = False):
  width, height = len(matrix[0]), len(matrix)

  if reverse:
    word = word[::-1]

  for i in range(width + height - 1):
    count = 0
    positions = []

    for j in range(width):
      row = i - j

      if 0 <= row < height:
        if matrix[row][j] != word[count]:
          count = 0
          positions = []
        
        if matrix[row][j] == word[count]:
          positions.append([row, j, word[count]])
          count += 1

        if count == len(word):
          return positions

# Verifica se a palavra está nas diagonais em direção à diagonal principal
def checkWordDiagonallyTowardsTheMainDiagonal(matrix, word, reverse = False):
  width, height = len(matrix[0]), len(matrix)

  if reverse:
    word = word[::-1]

  for i in range(width + height - 1):
    count = 0
    positions = []

    for j in range(width):
      row = width - i + j - 1

      if 0 <= row < height:
        if matrix[row][j] != word[count]:
          count = 0
          positions = []
        
        if matrix[row][j] == word[count]:
          positions.append([row, j, word[count]])
          count += 1

        if count == len(word):
          return positions

# Gera a matriz com as palavras encontradas
def generateFinalMatrix(matrix, words_coords): 
  width, height = len(matrix[0]), len(matrix)

  finalMatrix = [['.' for i in range(width)] for j in range(height)]

  for word_coords in words_coords:
    for letter_coords in word_coords:
      x, y, letter = letter_coords

      finalMatrix[x][y] = letter

  return finalMatrix

positions = [
  checkWordHorizontally(file, 'python'),
  checkWordHorizontally(file, 'morcego'),
  checkWordHorizontally(file, 'cavalo', reverse = True),
  checkWordHorizontally(file, 'java', reverse = True),
  checkWordHorizontally(file, 'if', reverse = True),
  checkWordVertically(file, 'opa'),
  checkWordVertically(file, 'int'),
  checkWordVertically(file, 'aviao', reverse = True),
  checkWordVertically(file, 'json', reverse = True),
  checkWordDiagonallyTowardsTheSecondaryDiagonal(file, 'brabo'),
  checkWordDiagonallyTowardsTheSecondaryDiagonal(file, 'ovo', reverse = True),
  checkWordDiagonallyTowardsTheMainDiagonal(file, 'ava'),
  checkWordDiagonallyTowardsTheMainDiagonal(file, 'odo', reverse = True),
]

board = generateFinalMatrix(file, positions)

for line in board:
  for column in line:
    print(column, end=" ")
  print()