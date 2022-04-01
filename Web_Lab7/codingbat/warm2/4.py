def string_splosion(str):
  result = ''
  for i in range(1, len(str) + 1):
    result += str[:i]
  return result