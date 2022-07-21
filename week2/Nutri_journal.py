def main():
    
    print("****WELCOME TO NUTRI-DIARIES!****")

    fname = "all_nutrients.csv"
    lst_nutrients = []

    lst_nutrients = load_nutrients(fname)


    while(True): 
        nutrition = insert_nutrition()
        if nutrition == None:
            break

        lst_nutrients.append(nutrition)
    
    print("\n\n*****Nutrional Logs*****")
    for elem in lst_nutrients:
        print(elem)

    save_nutrients(fname, lst_nutrients)
    print("\n\n")


def save_nutrients(fname, lst_nutrients):
    pass

def load_nutrients(fname):
    pass

def insert_nutrition():
    pass



if __name__ == "__main__":
    main()