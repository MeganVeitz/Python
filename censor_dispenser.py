# Below are four emails that will be censored. For each email, there will be a different list of words to censor and the final email will include all censored lists plus each word before and after those censored words. 

email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# lists of words
censor = "learning algorithms"
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

# email 1 function; censors a phrase
def email_one_censor(phrase):
    return phrase.replace(censor, "XXX")    
#print(email_one_censor(email_one))

# email 2 function; censor a whole list & phrases from the "proprietary" list above then return email
def email_two_censor(proprietary):
  # loops through all possible case sensitive words
  for terms in proprietary_terms:
    proprietary = proprietary.replace(terms.upper(), "XXX")
    proprietary = proprietary.replace(terms.lower(), "XXX")
    proprietary = proprietary.replace(terms.title(), "XXX")
    proprietary = proprietary.replace(terms, "XXX")
  return proprietary
#print(email_two_censor(email_two))

# email 3 function; censor everthing from the previous list and any word from the "negative" list that occurs twice.
def email_three_censor(email):
  for negative_word in negative_words:
    # finding if the negative words was used twice
    if len(email.lower().split(negative_word.lower())) > 2:
      email = email_three_censor_new(email)
  return email_two_censor(email)
#print(email_three_censor(email_three))

#break up the function above,to apply that when creating email 4 function. 
def email_three_censor_new(email):
  for negative_word in negative_words:
    email = email.replace(negative_word.upper(), "XXX")
    email = email.replace(negative_word.lower(), "XXX")
    email = email.replace(negative_word.title(), "XXX")
    email = email.replace(negative_word, "XXX")
  return email


#email 4 function; censors all of the words from lists above and the words before & after a term from those two lists. 
def email_four_censor(email, new_censor_char="###"):
  censor_3_email = email_three_censor_new(email)
  censor_2_email = email_two_censor(censor_3_email)
  email_four_list = censor_2_email.split(" ")
  # looping through the entire list
  for idx in range(0,len(email_four_list)):
    # finding the string "XXX" index and the index of the words that comes before and after string "XXX"
    if "XXX" in email_four_list[idx]:  
      email_four_list[idx] = new_censor_char
      email_four_list[idx-1] = new_censor_char
      email_four_list[idx+1] = new_censor_char
  email_four_list2 = " ".join(email_four_list)
  return email_four_list2
print(email_four_censor(email_four,"****"))
