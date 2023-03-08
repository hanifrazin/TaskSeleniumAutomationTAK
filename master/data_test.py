import random

class DataTest():
    base_url = "https://demowebshop.tricentis.com"
    firstname = "Tony"
    lastname = "Chopper"
    data_random = str(random.randint(0, 1000))
    email = "tonny.chopper"+data_random+"@mail.com"
    email_invalid = "tony..chopper@@mailing.com"
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
