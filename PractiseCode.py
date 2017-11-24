def factorial(x):
  fact=1
  while x!=0:
    fact=fact*x
    x-=1
  return fact
  
  #########################
  def digit_sum(n):
  sum=0
  while n!=0:
    sum
    sum+=n%10
    n=n/10
  return sum
  ###########################
  def is_prime(x):
    if x < 2:
        return False
    else:
        for n in range(2, x-1):
            if x % n == 0:
                return False
        return True
############################
def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word
###########################
def anti_vowel(text):
    t=""
    for c in text:
        for i in "ieaouIEAOU":
            if c==i:
                c=""
            else:
                c=c
        t=t+c
    return t
	###############################
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    print stars
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
	##################################
def product(numbers):
  result=1
  for num in numbers:
    result*=num
  return result
  ##################################
  def purify(numbers):
  a=[]
  for num in numbers:
    if num%2==0:
      a.append(num)
  return a
  ###################################
  