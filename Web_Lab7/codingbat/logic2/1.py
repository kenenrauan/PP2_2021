def make_bricks(small, big, goal):
  goal -= min(goal // 5, big) * 5
  return goal <= small