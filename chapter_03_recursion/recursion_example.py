def regressive(i):
    print(i)

    if i < 1:
        return

    else:
        regressive(i - 1)

regressive(3)