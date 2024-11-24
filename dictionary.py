# Grocery product list
book = dict()
book["apple"]   = 0.49
book["milk"]    = 1.59
book["avocado"] = 2.25
print(book)
print(book["apple"])

# Phonebook
conctact_list = {}
conctact_list["JT"]     = "123-456-7890"
conctact_list["Sam"]    = "547-572-0454"
print(conctact_list)
print(conctact_list["Sam"])

# Voter tracker
voted = {}

def check_voter(name):
    if voted.get(name):
        print(name + " already voted, kick the cheater out!")
    else:
        voted[name] = True
        print(name + " hasn't voted, let them vote!")

check_voter("Tom")
check_voter("Tom")
check_voter("Celeste")
"""Load = slots occupied / total slots 
    and if load > 0.7 
        resize
"""