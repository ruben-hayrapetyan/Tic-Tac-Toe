x = 1
def frange(start, stop, step):
  i = start
  while i < stop:
    yield i
    i += step

for x in range(1, 7):
    answer = 3*x - 2
    print(answer)