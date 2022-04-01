def lucky_sum(a, b, c):
  l = (a, b, c)
  return sum(l) if 13 not in l else sum(l[:l.index(13)])