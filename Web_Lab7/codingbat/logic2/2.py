def lone_sum(a, b, c):
  l = (a, b, c)
  return sum(x * (l.count(x) == 1) for x in l)