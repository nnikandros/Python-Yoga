import numpy as np

lst=np.arange(100,1000)


products=[x*y for x in lst for y in lst]
max([x for x in products if len(str(x))%2 == 0 and  list(str(x))[0]==list(str(x))[-1] and list(str(x))[1]==list(str(x))[-2] and list(str(x))[2]==list(str(x))[3]] ) 
