# shopping_cart.py

import os
from dotenv import load_dotenv
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71



# Cashier Inputs the products that are scanned


valid_ids = []
for p in products:
    valid_ids.append(str(p["id"]))

product_input_list = []

while True:
    product_input = input("Please input a product identifier, or 'DONE' if there are no more items:")
    if product_input.upper() == "DONE":
        break
    elif product_input not in valid_ids:
        print("Invalid Item")   
    else:   
        product_input_list.append(product_input)
#print("... ", product_input_list)
#print(type(product_input_list))


# Checkout Headers and Date

today = datetime.now()

print("------------------------------------")
print("SPINELLI'S SUPERMARKET \nwww.spinellissupermarket.com")
print("------------------------------------")
print("TODAY'S DATE:", today.strftime("%m/%d/%Y %H:%M:%S"))
print("------------------------------------")
print("SELECTED PRODUCTS:")


#Match product data to the product inputs


subtotal_price = 0
tax_rate = float(os.getenv("TAX_RATE", default = ".1"))

for product_input in product_input_list:
    matching_names = [x for x in products if str(x["id"]) == str(product_input)]
    matching_name = matching_names[0]
    subtotal_price = subtotal_price + matching_name["price"]
    print("+ " + matching_name["name"] + " | " + str(to_usd(matching_name["price"])))

print("------------------------------------")
print("SUBTOTAL: " + str(to_usd(subtotal_price)))
print("TAX: " + str(to_usd(tax_rate*subtotal_price)))
print("TOTAL: " + str(to_usd(subtotal_price + (tax_rate*subtotal_price))))
print("------------------------------------")
print("HAVE A NICE DAY!")




#Send email receipt (attempt at the email receipt)

#SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
#SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
#
##print(SENDER_ADDRESS)
##print(SENDGRID_API_KEY)
#
#client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
##print("CLIENT:", type(client))
#
#subject = "Your Receipt from Spinelli's Supermarket"
#html_content = { "SUBTOTAL": to_usd(subtotal_price),
#        "TAX": to_usd(tax_rate*subtotal_price),
#        "TOTAL PRICE": (to_usd(subtotal_price + (tax_rate*subtotal_price))),
#        "TIME": today.strftime("%m/%d/%Y %H:%M:%S"),
#        "ITEMS": product_input_list }
#
#print("HTML:", html_content)
#
#
#message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)
#
#try:
#    response = client.send(message)
#
#    #print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
#    if response.status_code == 202:
#        print("Receipt Successfully Sent") #> 202 indicates SUCCESS
#    #print(response.body)
#    #print(response.headers)
#
#except Exception as err:
#    print(type(err))
#    print(err)