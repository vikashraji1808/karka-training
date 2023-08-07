# Grouping Elements by Category
# Description: Given a list of items, group them into categories using a dictionary, where the keys are the categories and the values are lists of items belonging to each category.

# Example usage:

items_lists = [
    {'name': 'Apple', 'category': 'Fruits'},
    {'name': 'Carrot', 'category': 'Vegetables'},
    {'name': 'Banana', 'category': 'Fruits'},
    {'name': 'Broccoli', 'category': 'Vegetables'},
]

def category(item):
    result={}
    fruits=[]
    Vegetables=[]
    add=[]
    for items_list in item:
        name=items_list["name"]
        cat=items_list["category"]
        if cat=="Vegetables":
            Vegetables.append(name)
        elif cat=="Fruits":
            fruits.append(name)
        result.update({"fruits":fruits,"Vegetables":Vegetables})
        add.append(result)
    
    # print(fruits)
    # print(Vegetables)
    print(result)
    print("\n",add)


category(items_lists)

        
            



  