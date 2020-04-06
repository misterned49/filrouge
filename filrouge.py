import requests
import mysql.connector

page = ("https://ssl-api.openfoodfacts.org/category/viandes/1.json")
r = requests.get(page)
data = r.json()

num_product = 1
code = data["products"][num_product]["code"]
name = data["products"][num_product]["product_name"]
brand = data["products"][num_product]["brands"]
nutri = data["products"][num_product]["nutrition_grades"]
stores = data["products"][num_product]["stores"]
dtq = data["products"][num_product]["data_quality_tags"]
sources = data["products"][num_product]["sources"]
ingredients = data["products"][num_product]["ingredients_text"]
link = "https://fr.openfoodfacts.org/produit/" + code

print(name)
print(dtq)
print(ingredients)
print(type(data))
print(type(ingredients))

