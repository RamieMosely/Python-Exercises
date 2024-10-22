#Collections

#List = [] ordered and changeable. Duplicate ok
#Set = {} unordered and immutable. Add/Remove OK. No duplicates.
# Tuple = () ordered and unchangeable. Duplicate OK. Faster

fruits = ["apple", "orange", "banana", "coconut"]
print(dir(fruits))

print(fruits[::1])


fruits[1] = "derpon"
fruits.append("watermelon")
fruits.remove("coconut")
fruits.insert(4, "Hell Yeah!")
fruits.sort()
fruits.reverse()
print(fruits.index("apple"))
print(fruits.count("apple"))


for fruit in fruits:
    print(f"{fruit}\n") 


fruits[1] = "derpon"
fruits.append("watermelon")

print("orange" in fruits)
print(fruits[1])
print(len(fruits))



#SETS (good to use when working with constants such as color for example)

vegetables = {"lettuce", "carrots", "tomatoes", "onions"}
print(vegetables)
vegetables.remove("tomatoes")
print(vegetables)

