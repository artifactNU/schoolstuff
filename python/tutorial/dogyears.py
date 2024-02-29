print("Enter your dogs age in human years: ")
human_years = float(input())
if human_years <= 2:
    dog_years = human_years * 10.5
else:
    dog_years = 21 + (human_years - 2) * 4
print(f"Your dog is {dog_years} years old in dog years")
