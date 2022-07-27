def increment_string(strng):
    if len(strng)==0:
        return "1"
    else:
        if strng[-1].isalpha() :
            return strng + "1"
        else:
            head=strng.rstrip("0123456789")
            tail=strng[len(strng.rstrip("0123456789")):]
            n=len(strng[len(strng.rstrip("0123456789")):])- len(str(int(strng[len(strng.rstrip("0123456789")):])+1))
            int(tail)+1
            return head + n*"0" + str(int(tail)+1)
          
          
##### 

def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))
