# num = 5

# match num:
#     case 1:
#         print("one")

#     case 2:
#         print("two")

#     case 3:
#         print("three")

#     case 4:    
#         print("four")

#     case 5:    
#         print("five")

#     case _:
#         print("number is not matching....")



num1 = 15
match num1 % 3:
    case 0:
        print("Divisible by 3")
    case 1:
        print("Remainder 1 when divided by 3")
    case _:
        print("Remainder 2 when divided by 3")
        
            