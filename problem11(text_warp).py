import textwrap

def warp(string, max_width):
  result= ""

  for i in range(0, len(string), max_width):
    result += string[i:i + max_width] + "\n"
  return result
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = warp(string, max_width)
    print(result)