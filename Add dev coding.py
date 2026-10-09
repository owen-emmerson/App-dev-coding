def opening_page ():
    #checking if the user has an account, if not they get the option to make one or continue without#
    have_an_account = input("Do you have an account?")
    if have_an_account == "yes":
        use_account = input("Do you want to use it?")
        if use_account == "yes":
            log_in('Banker2029', 'Pr3p_R3ady_94100!*')
        else:
            name = input("What is your name?")
            homepage(name)
    else:
        new_account = input("Do you want to create an account?")
        if new_account == "yes":
            create_account('Banker2029')
        else:
            name = input("What is your name?")
            homepage(name)

def log_in(username,password):
    #Logging the user in#
    got_access = False
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")
    while got_access == False:
        if entered_username == username and entered_password == password:
            print('Welcome, logging you in!')
            got_access = True
        else:
            print('Wrong username or password! Please check your inputs and try again.')

    homepage('Owen')

def create_account(existing_username):
    #creating an account for a user#
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    new_username = input("Enter your username: ")
    new_password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")
    allow_credentials = False
    while allow_credentials == False:
        if new_password == confirm_password:
            if new_username == existing_username:
                print("This username is already taken.")
                new_username = input("Enter your new username: ")
            else:
                allow_credentials = True
                print("Welcome, creating your account and logging you in.")
        else:
            print("Your passwords don't match.")
            new_password = input("Enter your password: ")
            confirm_password = input("Confirm your password: ")


    homepage(first_name)


def homepage(Firstname):
    #the user's homepage#
    print(f"Welcome {Firstname}")

    #Selecting whether the user wants meal prep or foodbank locator#
    progressed = False
    select_section = input("Please enter which section you want to go to, press 1 for meal prep, press 2 for foodbank loactor, press 3 to close the app")
    while progressed == False:
        if select_section == "1":
            print("Relocating to meal prep tool")
            progressed = True
            meal_prep()

        elif select_section == "2":
            print("Relocating to foodbank loactor")
            progressed = True
            foodbank()

        #allowing the user to quit the app#
        elif select_section == "3":
            print("Closing the app, thanks for using Bank-Prep!")
            progressed = True
            opening_page()

        else:
            print("Please enter a valid option")
            select_section = input("Please enter which section you want to go to, press 1 for meal prep, press 2 for foodbank loactor, press 3 to close the app")

def meal_prep():
    ingredients = []
    amount_of_ingredients = int(input("How many ingredients do you have?"))

    for i in range(0, (amount_of_ingredients)):
           user_ingredient = input("Enter an ingredient you have")
           ingredients.append(user_ingredient)



def foodbank():
    user_purpose = input("Do you want to donate or use a foodbank? Press 1 for donation, press 2 for use of foodbank")
    foodbank_locations = ['SR4 6EX', 'SR1 1UN', 'NE6 3DP', 'DH2 1AG', 'SR3 4JQ']
    user_location = input("Enter your Postcode to find your local ")





    if user_purpose == "1":
        donation_list = []
        donations_amount = int(input("How many donations do you have?"))

        for i in range(0,donations_amount):
            donation = input("Enter your donation")
            donation_list.append(donation)

        print(f"Thank you for donating, your local foodbank {foodbank} is waiting for your donations of {donation_list} and is very appreciative!")



