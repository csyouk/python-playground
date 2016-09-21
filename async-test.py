def custom_range(end):
  i = 0
  while i < end:
    yield i
    i + 1

gen = custom_range(10)


print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
