# Each person below is a tuple of the following format:
# (name, nicknames, birthdate, address)
# The nicknames item is a list of strings.
# The address is a dictionary with keys 'street', 'city', 'prov', 'postcode'
ali = ("Al G. Rhythm", ["Al", ""], "2000-01-01", {
    "street": "123 Awesome Ave",
    "city": "Anytown",
    "prov": "AB",
    "postcode": "A4B2C3"
})
billie = ("Beau Leon", ["Beau", "Bee"], "1998-09-23", {
    "street": "456 Beatiful Blvd",
    "city": "Belleville",
    "prov": "BC",
    "postcode": "B4M6F2"
})
charlie = ("Charlie Char", ["Chuck", "Char"], "2005-02-27", {
    "street": "789 Curvy Cresc",
    "city": "Cityville",
    "prov": "QC",
    "postcode": "C3B2M1"
})
dave = ("Dick-Shawn Airy", ["Shawn", "D-Shawn"], "1969-10-31", {
    "street": "321 Daring Dr",
    "city": "Dicton",
    "prov": "NB",
    "postcode": "D2L4S9"
})

# Explain in a comment below why you can NOT change the name of one
# of these people
# Explain in a comment below why you can NOT set the nicknames
# to a new list but you CAN change the existing list of nicknames
# OR why you can NOT set the address to a new dictionary but you CAN
# set new values in the existing dictionary
# For full marks, your answer must mention how references are involved

#1 Tuples are immutable
#2 I can append if I go 1 step deep into the list (which is a mutable type)
#3 The list being a part of a tuple makes it immutable, I have to go deeper into the list before I can change something
#4 In order for me to change the content of the dictionary, i have to go 1 step deeper into the list or the dictionary.
#5 using [:] to copy to a variable makes a shallow copy, which means it just copied the reference for each element.


def deep_copy(person):
  """Returns a deep copy of the given person
    person must be a tuple of the structure described in the comment above"""
  person_clone = ()
  for item in person:
    if isinstance(item, str):
      person_clone += (item, )  # append as a tuple
    elif isinstance(item, list):
      new_list = [element for element in item
                  ]  # list comprehension if the item to be copied is a list
      person_clone += (new_list, )  # append as a tuple
    elif isinstance(item, dict):
      new_dict = {
          key: value
          for key, value in item.items()
      }  # dictionary comprehension? if the item to be copied is a dictionary
      person_clone += (new_dict, )  # append as a tuple
  return person_clone
