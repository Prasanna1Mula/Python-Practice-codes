#Break statements 
shopping_list = ["apple","banana","Carrot","Bread","Butter"]
item_to_find= "Bread"
for item in shopping_list:
    print("Checking item:", item)
    if item == item_to_find:
        print("Item found")
        break