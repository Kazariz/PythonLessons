def function(a, b, c):
    print(a, b, c)

    def plosh():
        s = 2 * (a * b + b * c + a * c)
        print(s)

    plosh()


function(2, 4, 6)
