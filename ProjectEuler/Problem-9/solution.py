#So basically we want to solve the system of equations

#a^2+b^2=c^2
#a+b+c=1000
#given the condition that a<b<c.

#So, we set c=1000-a^2-b^2 and place in first equation. We get the equation
#0=1000^2-2000b-2000a +2ab.
#So in python we do a list comprehension

lst=np.arange(1000)
[[a,b] for a in lst for b in lst if 2*a*b-2000*a-2000*b==-1000**2  ]

#from this list only [200, 375] satisfies a<b.
