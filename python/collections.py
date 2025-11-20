cart = ["apples", "bananas", "cherries"]
print(cart)
cart.append("donuts")
cart.append("milk")
cart.append("eggs")
print(cart)

cart.remove("cherries")
cart.pop(1)
print(cart)
cart.pop()
print(cart)
cart.append("bananas")
cart.append("bananas")
print(cart)
cart.sort()
print(cart)

fruit=cart[0:3]
print(fruit)

count=cart.count("bananas")
print(count)

squares=[]
for i in range(1,10):
    squares.append(i*i)
print(squares)

'List Comprehension: Faster than a for loop, super common in python'
'syntax: [Thing thats assigned for var range]'
'can have optional if-clause [x for x in values if x% 2 == 0]'
squares_faster = [x * x for x in range(1,10)]
print(squares_faster)

test = [item for item in cart if item.startswith("b")]
print(test)

inventory=[0] * 10
inventory[4] = 100
print(inventory)

book_genre = {"romance"}
book_genre.add("science fiction")
book_genre.add("mystery")
print(book_genre)
aset = set()

lst= [1,1,1,1,2,3,4,5,6,6,6,7,7,5,4,3,23,456,54]
uniqueList = set(lst)
print(uniqueList)

fav_snacks = {"Kathleen" : "pizza", "Steve" : "chips", "Patrick" : "Nutella"}

steve=fav_snacks["Steve"]
print(steve)

for key in fav_snacks:
    print(fav_snacks[key])

'If you want key AND values, use .items(), otherwise you will just get the keys'

for key, value in fav_snacks.items():
    print(key, value)

if "Jack" in fav_snacks:
    print(fav_snacks["Jack"])
else:
    fav_snacks["Jack"] = "ice cream"

print("hello world")