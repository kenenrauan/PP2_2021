def make_chocolate(small, big, goal):
  goal -= min(goal // 5, big) * 5
  return goal if goal <= small else -1