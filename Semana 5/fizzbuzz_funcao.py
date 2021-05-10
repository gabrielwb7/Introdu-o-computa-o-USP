def fizzbuzz(n):
    fizz = n % 3
    buzz = n % 5
    if fizz == 0 and buzz != 0:
        return "Fizz"
    elif fizz != 0 and buzz == 0:
        return 'Buzz'
    elif fizz == 0 and buzz == 0:
        return 'FizzBuzz'
    else:
        return n