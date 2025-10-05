def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
   
    if year % 4 !=0:
        return False
    elif year % 100 ==0 and year % 400 !=0:
        return False
        
    else:
        return True
        
leap_year = is_leap_year(2000)
print(leap_year)