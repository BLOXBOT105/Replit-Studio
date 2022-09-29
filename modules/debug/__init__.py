class debug:
    class enable:
        def __init__(self):
            f = open("modules/debug/value.txt","w")
            f.write("True")
            f.close()

    class disable:
        def __init__(self):
            f = open("modules/debug/value.txt","w")
            f.write("")
            f.close()
        
    def out(txt):
        f = open("modules/debug/value.txt","r")
        if bool(f.read()) :
            print(txt)
        f.close()