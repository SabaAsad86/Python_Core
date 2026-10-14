
bill = float(input("Enter total bill: "))
tip_percent = float(input("Enter tip percentage: "))
people = int(input("Enter number of people: "))

tip = bill * tip_percent / 100
total_bill = bill + tip
per_person = total_bill / people

print("Tip amount:", tip)
print("Total bill with tip:", total_bill)
print("Each person pays:", per_person)
