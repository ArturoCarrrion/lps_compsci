print("How many people will you have at your party?")
p = int(raw_input())

print("How many donuts will you have at your party?")
d = int(raw_input())

per_person = d / p

print("Our party has " + str(p) + " people and " + str(d) + " donuts.") 
print("Each person at the party gets " + str(per_person) + " donuts")

