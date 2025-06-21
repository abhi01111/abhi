char = input("Enter a character : ")

vowels = "aeiou"
result = "vowels" if char in vowels else "consonent"

print(f"The given Character {char}, is {result}")