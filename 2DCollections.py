guns =      ["Ak-47", "M-16", "Glock", "Sniper", "Uzi"]
animals =   ["parrot", "cat", "dog", "frog", "zebra"]
countries = ["Canada", "USA", "Russia", "China", "Korea"]

mine = [guns, animals, countries]

theMine = [["Ak-47", "M-16", "Glock", "Sniper", "Uzi"],
           ["parrot", "cat", "dog", "frog", "zebra"],
           ["Canada", "USA", "Russia", "China", "Korea"]]


for collection in theMine:
    for item in collection:
        print(item, end=" ")

    print("")


print(theMine[1][1])

#for item in mine:
    #print(item, end=" ")