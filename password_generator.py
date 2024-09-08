import secrets
import string

def generate_password(min_length, numbers=True, special_characters=True): #minlength is num, numbers and specialcharacters are optional parameters to specify if we want the pw to include these 2 parameters
  letters = string.ascii_letters
  digits = string.digits
  special = string.punctuation

  characters = letters #we use letters cuz no matter what we gonna include letters in pw
  if numbers:
    characters += digits #numbers T then add digits to characters
  if special_characters: 
    characters += special #special T then add special to characters

  pwd = "" #store pw 
  meets_criteria = False #we gonna set the variable true once the pw meets the criteria
  has_number = False #update
  has_special = False #update

  while not meets_criteria or len(pwd) < min_length:
    new_char = secrets.choice(characters)
    pwd += new_char

    if new_char in digits:
      has_number = True
    elif new_char in special:
      has_special = True

    meets_criteria = True
    if numbers:
      meets_criteria = has_number #if we should include nums we should set this equal to if we do have a num or not(if we have then T if not its F (both meetscrieria and hasnumber))
    if special_characters:
      meets_criteria = meets_criteria and has_special #if we should include speicalcharacters then meetcriteria is equal to meetcriteria and has special, add meetcriteria cuz above we're supposed to include a num but we dont meet the criteria so it doesnt matter what has special this should meetcrieria return F

  return pwd


  #print(letters, digits, special) #letters:lower/uppercharacters, digits:nums, special:symbol

min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers? (y/n) ").lower() == "y"
has_special = input("Do you want to have special characters? (y/n) ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print("The generated password is:", pwd)
  

#generate_password(8) #if (8, False, False) means we'd have a pw of min8 length, wouldn;t include num and specialcharacters