trends_mart = [
    {"id": 101, "name": "T-shirt", "price": 15.99, "quantity_in_stock": 50, 
     "available_for": [{'categ' : 'male', 'qty' : 20},
                       {'categ' : 'female','qty' : 25},
                       {'categ' : 'child', 'qty' : 5}],
     "low_stock":[]},
    {"id": 102, "name": "Jeans", "price": 29.99, "quantity_in_stock": 40, 
     "available_for": [{'categ' : 'male', 'qty' : 20},
                       {'categ' : 'female','qty' : 10},
                       {'categ' : 'child', 'qty' : 10}],
     "low_stock":[]},
    {"id": 103, "name": "Shoes", "price": 49.99, "quantity_in_stock": 24, 
     "available_for": [{'categ' : 'male', 'qty' : 4},
                       {'categ' : 'female','qty' : 10},
                       {'categ' : 'child', 'qty' : 10}],
     "low_stock":[]},
    {"id": 104, "name": "Backpack", "price": 39.99, "quantity_in_stock": 14, 
     "available_for": [{'categ' : 'male', 'qty' : 0},
                       {'categ' : 'female','qty' : 4},
                       {'categ' : 'child', 'qty' : 10}],
    "low_stock":[]},
    {"id": 105, "name": "Headphones", "price": 59.99, "quantity_in_stock": 15, 
     "available_for": [{'categ' : 'male', 'qty' : 0},
                       {'categ' : 'female','qty' : 5},
                       {'categ' : 'child', 'qty' : 10}],
    "low_stock":[]},
    {"id": 106, "name": "Sunglasses", "price": 19.99, "quantity_in_stock": 26, 
     "available_for": [{'categ' : 'male', 'qty' : 15},
                       {'categ' : 'female','qty' : 1},
                       {'categ' : 'child', 'qty' : 10}],
    "low_stock":[]}
]
qty_level=0
cat_name=0 
availability=0                                                                
for t in trends_mart:                                                  
    for tr in t["available_for"]:
        if tr["qty"]<=5:
           qty_level=tr["qty"]
           cat_name=tr["categ"]
for x in trends_mart:
    x
        
           
         
            


           
           
           


            

            
        
                    
           
            







