import random
from datetime import datetime

class DataTest():
    base_url = "https://demowebshop.tricentis.com"
    firstname = "Tony"
    lastname = "Chopper"
    add_to_cart = "Add to cart"
    dt_string = datetime.now().strftime("%Y%m%d-%H%M%S")
    email = "tonny.chopper."+dt_string+"@mail.com"
    email_static = "tonny.chopper414@gmail.com"
    password = "tony123"
    wrong_password = "TonY123"
    empty_field = ""
    validasi_firstname = "First name is required."
    validasi_lastname = "Last name is required."
    validasi_email = "Email is required."
    validasi_password = "Password is required."
    success_message = "Your registration completed"
    welcome = "Welcome to our store"
    error_login = "Login was unsuccessful. Please correct the errors and try again"
    laptop = "14.1-inch Laptop"
    shopping = "Shopping cart"
    shipping = "Estimate shipping"
