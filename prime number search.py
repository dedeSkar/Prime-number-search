import math
i = 3 
prime_number_search = int(input('Which prime number do you want to find?: '))
if prime_number_search == 1: #This is some bad code
    print(2)
prime_number_count = 1
while prime_number_search != 1 and prime_number_search != prime_number_count:
    div_count = 0 
    for y in range(1, (round(math.sqrt(i))+1)): #some math stuff, that
        if i % y == 0:                          #im too lazy to explain, but it works
            div_count += 1
    if div_count == 1: #if div_count == 1 that means it's a prime number
        prime_number_count += 1
    if prime_number_count == prime_number_search:
        print(i) #Prints out the prime number that user searched for
    i += 2