def no_teen_sum(a, b, c):
  return sum(map(lambda x: 0 if x in (13, 14, 17, 18, 19) else x, (a, b, c)))