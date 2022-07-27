## my initial solution 

def anagrams(word, words):
    def is_anagram(strng):
        return (set(word)== set(strng)) and  len(word) == len(strng)
    return list(filter(is_anagram, words))
  
  ### better version
def anagrams(word, words):
    f = lambda x: (set(word)== set(x)) and  len(word) == len(x)
    return list(filter(f, words))
  
  ### even better
  def anagrams(word, words):
    f = lambda x: sorted(word)== sorted(x)
    return list(filter(f, words))
  
  ## not my solutions
  def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]
  ##
  def anagrams(word, words):
    return filter(lambda x: sorted(word) == sorted(x), words)
  
