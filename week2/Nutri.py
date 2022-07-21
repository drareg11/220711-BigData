# ******* JOURNAL APP********
#Data should be read and written to CSV or JSON files

#Command Line Interface where users can interact with the application while its running
#Application should read in data from a file and be displayed in some way
#Application should write data to a file
#All user input should be validated (program should not end with exceptions based on user input)
#Program must follow OOP design (classes/objects)
#Application should be uploaded to a GitHub repo.


#Personal Obj
#Nutri journal app to record/track nutrional information
#Records food item and nutrients info
#Nutrients = calories, fat, vit, carbs, proteins, sodium, sugar
#records nutrients and food name in file
#messages can exclaim when proceeding over daily limit



class Nutrition():
    def __init__(self, name_food, calorie, fat, vit, carb, protein, sodium=""):
        self.name_food = str(name_food)
        self.calorie = int(calorie)
        self.fat = int(fat)
        self.vit = int(vit)
        self.carb = int(carb)
        self.protein = int(protein)
        self.sodium = int(sodium)

    def __str__(self):
        return 