def valid_ISBN10(isbn):
    sum=0
    if len(isbn) == 10  and isbn[:9].isdigit():
        if isbn[-1] == "X":
            for count, value in enumerate(isbn[:9]):
                sum+=(count+1)*int(value)
            sum+=100
            return sum%11 == 0
        elif isbn[-1].isdigit():
            for count, value in enumerate(isbn):
                sum+= (count+1)*int(value)
            return sum%11 == 0
        else:
            return False
    else:
        return False
        
        
