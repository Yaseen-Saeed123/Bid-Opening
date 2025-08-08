import time

print()
print("---------- Offer unpacking ----------")
print()

names = []

while len(names) <= 1:
    names = input("Write down all bidders (Separate them with a space): ").strip().title().split(" ")
    print()
    if len(names) <= 1:
        print("There must be at least Two bidders")
        print()

print("-"*30)
print()
print("Now write the cost provided by each bidder")
print()

costs = []

for i in range(len(names)):
    while True:
        try:
            cost = float(input(f"Write down the cost of {names[i]}: "))
            print()
            costs.append(cost)
            break
        except:
            print()
            print("Invalid cost please try again")
            print()

print("-"*30)
print("Now write the bid provided by each bidder")
print()

bids = []
accepted_names = []
accepted_costs = []

for i in range(len(names)):
    while True:
        try:
            bid = float(input(f"Write the bid of {names[i]}, with cost {costs[i]}: "))
            print()
            if bid >= 10:
                bids.append(bid)
                accepted_names.append(names[i])
                accepted_costs.append(costs[i])
                break
            else:
                break
        except:
            print()
            print("Invalid bid please try again")
            print()

if accepted_names:
    winner_cost = min(accepted_costs)
    winner_index = accepted_costs.index(winner_cost)
    print("-"*30)
    print()
    print(f"The winning offer was from {accepted_names[winner_index]}, whose cost was {winner_cost}, and bid rate was {bids[winner_index]}")
    print()
    print("-"*30)
    time.sleep(30)

else:
    print("No body wins 😢😢")
    print()
    exit()