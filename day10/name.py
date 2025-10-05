def fullname(first,last):
    if first=="" or last=="":
      print("You didn't provide valid inputs.")
    
    
    f_first = first.title()
    f_last = last.title()
    f_name = f"{f_first} {f_last}"
    return f_name

f=input("Enter your first name: ")
l=input("Enter your last name: ")
namee= fullname(f,l)
print(namee)
print(len(namee))