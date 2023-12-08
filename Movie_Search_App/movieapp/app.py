"""
The module handles the core functionality of the movie application. It includes 
functions to perform searches using the OMDB API, retrieve detailed information about 
movies, series, or episodes, and format this information for display to the user.
"""

import movieapp.api as api
import movieapp.ui as ui
import pprint

# pp = pprint.PrettyPrinter(indent=2)

my_key = "4a20872c"  # Api Key


def start():
  """
  Initiates the movie application's main flow. It handles user interactions for searching movies,
  series, or episodes, retrieves detailed information, and displays formatted results.

  Precondition:
  - The OMDB API key must be valid and correctly assigned to 'my_key'.
  - The 'movieapp.api' and 'movieapp.ui' modules must be correctly imported and functional.

  Postcondition:
  - Displays the search results and details of a selected movie, series, or episode to the user.
  - If no valid results are found or an error occurs, appropriate messages are displayed.
  """

  def do_search():
    """
    Conducts a search based on user input and returns the search results.
    Continuously prompts the user for a search string until valid results are found.

    Precondition:
    - The user must provide a valid search string.
    - Global variable 'my_key' must be set with a valid OMDB API key.
    - 'search_type' must be set to a valid type ('movie', 'series', etc.).

    Postcondition:
    - Returns a list of search results if found, or continues to prompt the user.
    - If no results are found, informs the user and prompts for a new search string.
    """
    while True:
      search_string = ui.get_search_string()
      search_result = api.search({
          "apikey": my_key,
          "s": search_string,
          "type": search_type
      })
      if search_result:
        for index, items in enumerate(search_result):
          print(f"{index+1}: {items['Title']} ({items['Year']})")
        return search_result
      else:
        print("No results found. Try another keyword?")

  def search_by_episode():
    """
    Handles searching for a specific episode of a series. Prompts the user for series title,
    season number, and episode number, and returns the search result.

    Precondition:
    - The user must input a valid series title, season number, and episode number.
    - Global variable 'my_key' must be set with a valid OMDB API key.

    Postcondition:
    - Returns detailed information about the specified episode if found.
    - If no result is found, informs the user and restarts the episode search process.
    """
    series_title = ui.get_search_string()
    season_number = input("\nSeason Number: ")
    episode_number = input("\nEpisode Number: ")
    episode_search_result = api.search({
        "apikey": my_key,
        "t": series_title,
        "Season": season_number,
        "Episode": episode_number
    })
    if episode_search_result:
      return episode_search_result
    else:
      print("No Search Result Found. Try again?")
      return search_by_episode()

  def get_details():
    """
    Retrieves detailed information about a movie, series, or episode based on the search type.
    Utilizes different search functions based on whether the search type is 'movie', 'series', or 'episode'.

    Precondition:
    - A valid 'search_type' must be set ('movie', 'series', 'episode').
    - For movies and series, 'do_search' must be able to return valid search results.
    - For episodes, 'search_by_episode' must be able to return valid search results.

    Postcondition:
    - Returns a dictionary containing detailed information about the selected item.
    - If no details are found, the function returns None.
    """
    if search_type == "movie" or search_type == "series":
      search_result = do_search()
      info = api.get_info({
          "apikey": my_key,
          "i": ui.get_selected_imdbID(search_result)
      })
      return info
    elif search_type == "episode":
      episode_search_result = search_by_episode()
      if episode_search_result and 'imdbID' in episode_search_result[0]:
        info = api.get_info({
            "apikey": my_key,
            "i": episode_search_result[0]['imdbID']
        })
        return info

  def format_details():
    """
    Formats the detailed information of a movie, series, or episode into a readable paragraph.
    Constructs a narrative based on available data fields like Title, Runtime, Genre, etc.

    Precondition:
    - The 'details_dict' dictionary must contain key details of a movie, series, or episode.

    Postcondition:
    - Returns a formatted string containing a comprehensive description of the item.
    - The description includes title, runtime, genre, type, actors, director, writer, release date, plot, awards, and ratings.
    """
    paragraph_parts = []
    if search_type == 'movie' or search_type == 'series':
      if 'Title' in details_dict and details_dict['Title'] != 'N/A':
        paragraph_parts.append(details_dict['Title'])

      if 'Runtime' in details_dict and details_dict['Runtime'] != 'N/A':
        paragraph_parts.append(f"is a {details_dict['Runtime']}")

      if 'Genre' in details_dict and details_dict['Genre'] != 'N/A':
        paragraph_parts.append(f"{details_dict['Genre']}")

      if 'Type' in details_dict and details_dict['Type'] != 'N/A':
        paragraph_parts.append(f"{details_dict['Type']}.")

      if 'Actors' in details_dict and details_dict['Actors'] != 'N/A':
        paragraph_parts.append(f"Starring {details_dict['Actors']}.")

      if 'Director' in details_dict and details_dict['Director'] != 'N/A':
        paragraph_parts.append(f"Directed by {details_dict['Director']}.")

      if 'Writer' in details_dict and details_dict['Writer'] != 'N/A':
        paragraph_parts.append(f"Written by {details_dict['Writer']}.")

      if 'Released' in details_dict and details_dict['Released'] != 'N/A':
        paragraph_parts.append(f"Released in {details_dict['Released']}.")

    elif search_type == 'episode':
      if 'Title' in details_dict and details_dict['Title'] != 'N/A':
        paragraph_parts.append(details_dict['Title'])

      if 'Runtime' in details_dict and details_dict['Runtime'] != 'N/A':
        paragraph_parts.append(f"is a {details_dict['Runtime']}")

      if 'Type' in details_dict and details_dict['Type'] != 'N/A':
        paragraph_parts.append(f"{details_dict['Type']}.")

      if 'Actors' in details_dict and details_dict['Actors'] != 'N/A':
        paragraph_parts.append(f"Starring {details_dict['Actors']}.")

      if 'Director' in details_dict and details_dict['Director'] != 'N/A':
        paragraph_parts.append(f"Directed by {details_dict['Director']}.")

      if 'Writer' in details_dict and details_dict['Writer'] != 'N/A':
        paragraph_parts.append(f"Written by {details_dict['Writer']}.")

      if 'Released' in details_dict and details_dict['Released'] != 'N/A':
        paragraph_parts.append(f"Released in {details_dict['Released']}.")

    if 'Plot' in details_dict and details_dict['Plot'] != 'N/A':
      paragraph_parts.append(f"\n\nPlot Summary:\n{details_dict['Plot']}.")

    if 'Awards' in details_dict and details_dict['Awards'] != 'N/A':
      paragraph_parts.append(f"\n\nAwards:\n{details_dict['Awards']}.")

    if 'Ratings' in details_dict and details_dict['Ratings'] != 'N/A':
      ratings_parts = []
      for ratings in details_dict['Ratings']:
        ratings_parts.append(f"\n{ratings['Source']}: {ratings['Value']}")
      paragraph_parts.append("\n\nRatings:" + " ".join(ratings_parts))

    formatted = " ".join(paragraph_parts)
    return formatted

  search_type = ui.get_search_type()  # Get search type from user
  details_dict = get_details(
  )  # Retrieve detailed information based on the search type
  return f"\n{format_details()}\n\n"  # Display the formatted details to the user
