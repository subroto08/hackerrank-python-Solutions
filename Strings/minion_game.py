def minion_game(string):
  kevin = 0
  stuart = 0

  strlen = len(string)

  for i in range(strlen):
    character = string[i]

    if character in "AEIOU":
      kevin = kevin + (strlen - i)
    else:
      stuart = stuart + (strlen - i)

  if kevin > stuart:
    print(f"kevin {kevin}")

  elif stuart > kevin:
    print(f"stuart {stuart}")

  else:
    print("Draw")


n = input()
minion_game(n)
