def marge_the_tool(string, k):

  for i in range(0, len(string), k):
    substring = string[i : i + k]
    result = ""

    for i in substring:
      if i not in result:
        result += i


    print(result)


string, k = input(), int(input())
marge_the_tool(string, k)

