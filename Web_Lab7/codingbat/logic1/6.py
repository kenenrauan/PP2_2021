def alarm_clock(day, vacation):
  return '7:00' if 0 < day < 6 and not vacation else 'off' if day in (0, 6) and vacation else '10:00'