def to_camel_case(text):
    text=text.replace("_","-")
    textlist=text.rsplit("-")
    i=1
    while i< len(textlist):
        textlist[i]=textlist[i].capitalize()
        i+=1
    sum=""
    for i,j in enumerate(textlist):
        sum+=j
    return sum    


######
def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])
