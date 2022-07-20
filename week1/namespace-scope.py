x = 5 
#'x' has been added to global namspace

def main():
    y = 10
    print(x)
# 'y' has been added to local namespace 
    def funct():
        print(x)
        print(y)  # here 'y'  is enclosing namespace
        z = 5

#print(y)
 # 'y' couldnt be printed out here because its local





def main():
    x = 10

    def funct():
        x = 15
        print(x)

    print(x)
    funct()
    print(x)


print(x)

main()

print(x)
