def say_hi(name):
    print("Hi, ", name)
    say_hi_2(name)

    print("Getting ready to say bye...")
    bye()

def say_hi_2(name):
    print("How you doing " + name + "?")

def bye():
    print("Ok, bye!")

say_hi("Júlia")