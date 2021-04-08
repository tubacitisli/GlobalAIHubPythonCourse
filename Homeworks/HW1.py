#HomeWork 1

#Answer 1

myList = list (range(10))

a = myList [:5]
b = myList [5:]

print ("My New List: ", b + a)


#Answer 2

n = int (input("Please enter number: " ))

if n < 10:

    print("Even Numbers: \n ")

    for i in range(0, n+1):
        
        if i % 2 == 0:
        
          print(i, end = " ")
