data = list(range(1,11))
print(data)

def is_even(n):
    return n%2 == 0

evens = [n for n in data if is_even(n)]

print(evens)

evens = (n for n in data if is_even(n))
print(list(evens))
print(list(evens))


evens = filter(is_even, data)
print(evens)
print(list(evens))
print(list(evens))


evens = filter(lambda n: n%2 == 0, data)
print(evens)
print(list(evens))
print(list(evens))





