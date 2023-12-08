# You can test your functions here if you like
# import q1
import movieapp.app as app
import os
import time

# print(
#     f"Here's a deep copy: \n{q1.deep_copy(q1.ali)} \n{q1.deep_copy(q1.billie)} \n{q1.deep_copy(q1.charlie)} \n{q1.deep_copy(q1.dave)}"
# )

while True:  # Loops the application.
  print("To quit, press Ctrl+C\n ")
  print(app.start())

  time.sleep(
      5
  )  # delay before clearing the screen and starting the application again.
  if os.name == 'nt' or 'replit' in os.environ:
    _ = os.system('cls')
  else:
    _ = os.system('clear')

# for testing purposes
# response = get("http://www.omdbapi.com", params={"apikey": "4a20872c", "t": "breaking bad","Season":"1", "Episode":"1"})
# response = get("http://www.omdbapi.com", params={"apikey": "4a20872c", "s": "star wars","type":"movie"})
# json = response.json()
# print(json['Search'])
# my API key 4a20872c
