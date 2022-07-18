def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True
  
  
  def primlist(n):
    lst=[]
    for i in range(2,n+1):
        if isprime(i)== True:
            lst.append(i)
    return lst 
  
  primlist(2000000)[10000]
