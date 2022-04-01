def string_match(a, b):
  cnt = 0
  for i in range(min(len(b), len(a)) - 1):
    cnt += a[i:i+2] == b[i:i+2]
  return cnt