def generate_hashtag(s):
    if len(s)==0: 
        return False
    s=s.title()
    lst=[x for x in s.split(" ") if x!=""]
    final="#"+"".join(lst)
    if len(final)>140:
        return False
    else:
        return final
