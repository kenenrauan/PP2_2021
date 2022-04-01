def close_far(a, b, c):
  close = lambda x, y: abs(y - x) <= 1
  return close(b, a) and not (close(c, a) or close (c, b)) or close(c, a) and not (close(b, a) or close (c, b))