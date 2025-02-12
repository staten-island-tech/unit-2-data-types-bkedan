""" x = 3
y = float(3)
print(x,y) """

""" values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(i) """


""" x = "this is a thing" # [this, is, a, thing]
y= x.split( )
z = y[2]
print(y)
print(z)
 """

""" verb1 = input("Verb1 = ")
verb2 = input("Verb2 = ")
noun1 = input("Noun1 = ")
number1 = input("Number1 = ")
celebrity1 = input("Celebrity1 = ")
print(f"{celebrity1} {verb1} to school then {verb2} because he was running {number1} minutes late. He then brought a {noun1}") """

""" user_input = input("write something:")
def word_count(sentence):
    words = sentence.split()
    word_count = len(words)
    return word_count
word_count = word_count(user_input)
print(f"number of words is: {word_count}") """

""" bill = input("Enter the bill amount")
tip = input("Enter the tip amount")
bill = float(bill)
tip = int(tip)
total = bill + tip
print(f"The total amount to be paid is: ${total:.2f}")
:.2f = tells python how to display the total """


""" def check_odd_even(number): 
    if number % 2 == 0:
        return "Even"
    else: 
        return "Odd"
    
number = int(input("Enter a number: "))
result = check_odd_even(number)
print(f"The number {number} is {result}.") """

def tip_calculate(bill, service):
    bill = float(bill)
    if service == "bad":
        tip_percentage = 0 * bill
    elif service == "okay":
        tip_percentage = 0.15 * bill
    elif service == "good":
        tip_percentage = 0.2 * bill
    elif service == "great":
        tip_percentage = 0.25 * bill
    else:
        return "Please choose from 'bad', 'okay', 'good', or 'great'."
    return tip, bill + tip
bill_amount = float(input("Enter bill: "))
rating = input("service (only accepts bad, okay, good, great):)")
tip, total = tip_calculate(bill_amount, rating)
print(f"Tip: ${tip:.2f}, Total: ${total:.2f}")

tip_calculate()
