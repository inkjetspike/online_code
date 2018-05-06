food = ["Feta cheese", "Kale", "Tomatoes","Cucumbers","Salad Dressing"]
for i in food:
    print(i)
    print(len(i))

print("\n")

for x in range(10):
    print(x + 1)

def beef():
    print("This function is cool")

beef()

print("\n")

def bitcoin_to_usd(btc):
    amount = btc * 527
    print(amount)

bitcoin_to_usd(3.65)

print("\n")

#return statement
def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age

Durells_limit = allowed_dating_age(27)
creepy_joe_limit = allowed_dating_age(45)
print("Durell can date women" , Durells_limit , " or older.")
print("Creepy Joe can date women" , creepy_joe_limit , " or older.")

print("\n")


#default value for arguments
def get_gender(sex ="unknown"):
    if sex is "m":
        sex ="Male"
    elif sex is "f":
            sex = "Female"
    print(sex)

get_gender("m")
get_gender("f")
get_gender()

print("\n")

#variable scope
a = 7823

def shoe():
    print(a)

def bow():
    print(a)

bow()
shoe()

print("\n")

#default values
def smart_sentence(name= "Durell" , action= "cooked" , item= "grits"):
    print(name, action, item)

smart_sentence()
smart_sentence("Gerald" , "Works" , "Hard")
smart_sentence(item= "awesome" , action="is")

print("\n")
#flexible number of arguments
def add_numbers(*args):
    total = 0
    for a in args:
        total+= a
    print(total)


add_numbers(3)
add_numbers(3, 32)
add_numbers(32, 14, 345, 367, 24, 6, 98, 4)

#unpacking arguments
def health_calculator(age, apples_eaten, cigs_smoked):
    answer =(100-age) + (apples_eaten * 3.5) - (cigs_smoked *2)
    print(answer)

#I could input my data like this or I can unpack the argument
durells_data =[27, 20,135]

health_calculator(durells_data[0], durells_data[1], durells_data[2])
#By using the askterisk I can unpack all of the data from this list and put it
#into the defined class. This saves a lot of time and lines of code
health_calculator(*durells_data)

print("\n")

