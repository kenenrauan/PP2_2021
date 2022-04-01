def last2(str):
  cnt = 0
  for i in range(2, len(str)):
    cnt += str[i-2:i] == str[-2:]
  return cnt