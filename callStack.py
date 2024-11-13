def greeting(name):
    print("hello, " + name + "!")
    greeting2(name)
    print("getting ready to say bye...")
    bye()

def greeting2(name):
    print("how are you, " + name + "?")

def bye():
    print("ok bye!")

greeting("Steve")