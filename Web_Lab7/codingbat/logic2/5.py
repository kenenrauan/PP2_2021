def round_sum(a, b, c):
  return sum(map(lambda x: x + 10 - x % 10 if x % 10 >= 5 else x - x % 10, (a, b, c)))