def is_prime():
    for n in range(1,101):
        status = True
        if n < 2:
            status = False
        else:
            for i in range(2,n):
                if n % i == 0:
                    status = False
        return status

    if is_prime(n):
       print(n, '', sep=',', end='')
is_prime()
