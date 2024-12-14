from flask import Flask, request
import json
app = Flask(__name__)
@app.get("/")
def home():
    return "hello from flask"
# this is just an example
# @app.post("/")
# def homePost():
# return "hello from flask post"

# Endpoints
@app.get("/test")
def test():
    return "hello from the test server"
# Endpoint using Json
@app.get("/api/about")
def aboutGet():
    name = {"name": "Adrian"}
    return json.dumps(name)
# create a new route /greet/{name}, this route should accept name 
# as part of the url and return an html message saying hello {name}
@app.get("/greet/<name>")
def greet(name):
    return f"""
<h1 style=color:blue>Hello {name}!</h1>"""
# by creating the farewell message
@app.get("/farewell/<name>")
def farewell(name): 
    return f"""
<h1 style=color:red>bye bye {name}!</h1>"""
app.run(debug=True)

# by creatin the farewell message
@app.get("/farewell/<name>")
def farewell(name):
    return f"""
<h1 style=color:red>bye bye {name}!</h1>"""

# Creating a POST Request
products = []

def fix_id(obj):
    obj["id"] =str(obj["_id"])
    return obj 

# #######################################
@app.get("/api/products")
def get_products():
    products_db = []
cursor = db.products.find({})
for prod in cursor:
# products_db.append(fix_id(prod))
#  return json.dumps(products_db)

# @pp.post('/api/products')
# def save_products():
    item = request.get_json()
# print(item)
# products.append(item)
# db.products.insert_one(item)
# return json.dumps(fix_id(item))

@app.put("/api/products/<int:index>")
def update_products(index):
    updated_item = request.get_json()
    if 0<= index <= len(products):
# products[index] = (updated-item)
# else:
        return"The index does not exist"
    
    #@app.delete('/api/products/<int:index>')
#def delete_product(index):
delete_item = request.get_json()
# if 0<= index <= len(products):
# delete_item = products.pop(index)
# return json.dumps(delete_item)
# else:
# return"That index does not exist"


#@app.patch('/api/products/<int:index>')
def patch_products(index):
    updated_field = request.get_json()
    if 0<=index<=len(products):
        updated_field(index).update(updated_field)
        return json.dumps(updated_field)
    else:
        return "That index does not exist"
    
   # Final Report
    products = []

    def fix_id(obj):
        obj["_id"] = str(obj["_id"])
        return obj
    
    @app.get('/app/catalog')
    def get_objects():
        products_db = []
        cursor = db.products.find({})
        for prod in cursor:
            products_db.append(fix_id(prod))
            return json.dumps(products_db)
        
        @app.post('/api/products')
        def save_products():
            item = request.get_json()
            print(item)
            #products.append(item)
            db.products.insert_one(item)
            return json.dumps(fix-id(item))
        
        app.run(debug=True)