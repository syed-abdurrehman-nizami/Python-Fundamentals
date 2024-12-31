#   Used to test if a value is in a sequence (eg:- string , list)


#     in          returns true if found
#     not in      returns true if not found 


name = input('Enter your name : ')

if 'a' not in name : 
    print("The word 'a' is not present in your name.")
else :
    print("The word 'a' is present in your name.")
    
    
country = input('Enter your country name : ')
if 'a' in country : 
    print("The word 'a' is present in your country name.")
else :
    print("The word 'a' is not present in your country name.")

