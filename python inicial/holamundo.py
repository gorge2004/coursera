print("Hola mundo")

def fibonacci  (n):
    if(n <= 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print('fibonacci', fibonacci(35) )

s = 0

for n in range(1, 10):

    if n % 7 == 0:

        break;

    s += n

print(s)

s = 0

for n in range(1, 10):

    if n % 2 != 0:

      continue;

s += n

else:

    s += 5

print(s)