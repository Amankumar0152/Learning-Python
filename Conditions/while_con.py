# count =1
# while count <=100:
#     print(count)
#     count +=1
# print("Done")
#
count = 100
while count >=1:
    print(count)
    count -=1

#table
n = int(input("inter a number for table print: "))
i = 1
while i <= 10:
    print(n*i)
    i += 1

nums = [1,4,9,16,25,36,49,64,81,100]
heroes = ["pirates", "Avengers ", "Dark Knight", "Big Hero 6"]

i = 0
while i< len(heroes):
    print(heroes[i])
    i +=1

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx +=1

nums = (1,4,9,16,25,56,67,89,100)

x=25
i =0
while i< len(nums):
    if(nums[i] == x):
        print("Found idx number: ", i)
        break
    else:
        print("Finding")
    i += 1