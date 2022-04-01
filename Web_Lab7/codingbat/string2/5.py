def end_other(a, b):
  a = a.lower()
  b = b.lower()
  return a[-len(b):] == b or b[-len(a):] == a