class debug:
    class enable:
        f = open("modules/debug/value.txt","w")
        f.write("True")
        f.close()

    class disable:
        f = open("modules/debug/value.txt","w")
        f.write("False")
        f.close()
        
    def out(txt):
        f = open("modules/debug/value.txt","r")
        if bool(f.read()):
            print(txt)
        f.close()