def spin_words(sentence):
    lst=sentence.split(" ")
    emptylst=[]
    for x in lst:
        if len(x) >=5 :
            emptylst.append(x[::-1])
        else:
            emptylst.append(x)
    return " ".join(emptylst) 
  
  
  ### more pythonic one-liner
  def spin_words(sentence):
      return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
