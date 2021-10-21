def confirm(num):
  answer = False
  while answer == False: 
    primary = True
    if num == 1 or num == 0:
      primary = False
      answer = True
    i = 2
    while i < num:
      if num/i == num//i and num != i:
        primary = False
        answer = True
      i += 1
    answer = True
  if primary:
    return True
  else:
    return False

def find(num1, num2):
  num = num1
  primaries = []
  while num <= num2:
    answer = False
    while answer == False: 
      primary = True
      if num == 1 or num == 0:
        primary = False
        answer = True
      i = 2
      while i < num:
        if num/i == num//i and num != i:
          primary = False
          answer = True
        i += 1
      answer = True
    if primary:
      primaries.append(num)
    num += 1
  return primaries
