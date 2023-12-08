from requests import get

# The three types that the OMDB API can search for
TYPES = ["movie", "series", "episode"]


def test(apikey):
  """Returns True if the given apikey is able to successfully
  connect to the OMDB API

  apikey must be a string
  """

  response = get("http://www.omdbapi.com",
                 params={
                     "apikey": apikey,
                     "s": "test"
                 })
  return response.status_code == 200 and response.json()["Response"] == "True"


def search(params):
  """Returns the OMDB items matching the given parameters.
  
  params must be a dictionary with at least the following keys:
  apikey: your OMDB API key
  s: the search string, a title to search for
  type: the type to search for, one of the TYPES declared above

  e.g. {"apikey":"bkj28dh2", "s":"Star Wars", "type":"movie"}

  If an error occurs, returns an empty list.
  Otherwise, the returned data is a LIST OF dictionaries.
  Each dictionary in the list will have at least the following keys:
  Title
  imdbID
  """

  if not params:
    params = {"apikey": "bad"}

  # Call the OMDB API and get the response data
  response = get("http://www.omdbapi.com", params=params)

  # Make sure the call succeeded
  if response.status_code == 200:
    # Convert the response data into a Python data structure
    # Use the debugger and expand the json variable in the watch panel
    # to see its structure
    json = response.json()

    if json["Response"] == "True":
      # Return just the search results part of the response data
      if "Season" in params and "Episode" in params:
        return [json]
      else:
        return json.get('Search')
    else:
      return []
  else:
    return []


def get_info(params):
  """Returns the item matching the given parameters.
  
  params must be a dictionary with at least the following keys:
  apikey: your OMDB API key
  i: The IMDB ID of the desired item

  e.g. {"apikey":"bkj28dh2", "i":"tt0468569"}

  If an error occurs, returns an empty dictionary.
  Otherwise, returns a dictionary of the structure shown below:

  NOTE:
  - The Awards key is not always present!
  - The Ratings key is not always present, or may be empty!
  
  {
    "Title":"E.T. the Extra-Terrestrial",
    "Year":"1982",
    "Rated":"PG",
    "Released":"11 Jun 1982",
    "Runtime":"115 min",
    "Genre":"Adventure, Family, Sci-Fi",
    "Director":"Steven Spielberg",
    "Writer":"Melissa Mathison",
    "Actors":"Henry Thomas, Drew Barrymore, Peter Coyote",
    "Plot":"A troubled child summons the courage to help a friendly alien escape from Earth and return to his home planet.",
    "Language":"English",
    "Country":"United States",
    "Awards":"Won 4 Oscars. 52 wins & 36 nominations total",
    "Poster":"https://m.media-amazon.com/images/M/MV5BMTQ2ODFlMDAtNzdhOC00ZDYzLWE3YTMtNDU4ZGFmZmJmYTczXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg",
    "Ratings":[
      {"Source":"Internet Movie Database","Value":"7.9/10"},
      {"Source":"Rotten Tomatoes","Value":"99%"},
      {"Source":"Metacritic","Value":"92/100"}
    ],    
    "Metascore":"92",
    "imdbRating":"7.9",
    "imdbVotes":"428,799",
    "imdbID":"tt0083866",
    "Type":"movie",
    "DVD":"22 Jul 2015",
    "BoxOffice":"$437,141,279",
    "Production":"N/A",
    "Website":"N/A",
    "Response":"True"
  }
  """

  if not params:
    params = {"apikey": "bad"}

  response = get("http://www.omdbapi.com", params=params)
  if response.status_code == 200:
    json = response.json()
    if json["Response"] == "True":
      return json
    else:
      return {}
  else:
    return {}
