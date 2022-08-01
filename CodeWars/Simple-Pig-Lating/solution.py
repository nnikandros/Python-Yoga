# my solution. Admitelly not very pythonic. 

def pig(text):
    final=[]
    lst=text.split(" ") 
    for value in lst:
        if value not in {"!", "?"}:
            z=list(value)
            z.append(z[0])
            z.pop(0)
            z[-1]=z[-1]+"ay"
            final.append("".join(z))
        else:
            final.append(value)
        
    return " ".join(final)    
  
  
  # pythonic solution. not mine
  
  def pig_it(text):
    lst = text.split()
    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])
