numbers = [1, 10, 5, 4, 9, 10]
letters = ["a", "k", "h", "s","b","t","y"]
val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)


val = numbers[3:6]
val = numbers[:3]
val =numbers[:4]
numbers[4] = 40
numbers.append("49") #sona eklenir
numbers.append("51")
numbers.insert(3, 78) #3. index'e 78 eklenir
numbers.insert(-4, 8) #sonda 4. indexe eklenir
#numbers.pop(0)
#numbers.pop(-1)
#numbers.remove(10)
numbers.sort()
letters.sort()
print(numbers)
print(letters)