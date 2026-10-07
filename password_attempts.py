password = "python123"

attempt = input("Enter password: ")

count = 0

while count < 3:
    if attempt == password:
        count = 5
        print("Access granted")
    elif count < 2:
        attempt = input("Enter password: ")
        count += 1
    elif count == 2:
        count = 5
        print("Too many failed attempts.")

#password = "python123"
#count = 0

#while count < 3:
    #attempt = input("Enter password: ")
    #count += 1

    #if attempt == password:
        #print("Access granted")
        #print("Too many failed attempts.")
        
        
    