def caught_speeding(speed, is_birthday):
  return 0 if speed <= 60 + 5*is_birthday else 1 if speed <= 80 + 5*is_birthday else 2