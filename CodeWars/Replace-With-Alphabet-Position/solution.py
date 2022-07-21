def alphabet_position(text):
    #make a dictionary of letters and numbers
    letters=[chr(i) for i in range(ord('a'),ord('z')+1)]
    numbers=[i for i in range(27) if i>=1]
    new_dict = dict(zip(letters, numbers))
    #change into lower case
    text=text.lower()
    lst=list(text)
    p=[str(new_dict[value]) for value in lst if value.isalpha()   ]
    return " ".join(p)

## or just 
return " ".join([str(new_dict[value]) for value in list(text.lower()) if value.isalpha()   ])
## after creating the dictionary
