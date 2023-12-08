def get_search_type():
  """
  Prompt the user to select a search type (movie, series, or episode).

  Returns:
  - The selected search type as a lowercase string ('movie', 'series', or 'episode').

  Note:
  - The function provides a menu for selecting the search type and handles input validation.
  - If an invalid input is provided, the user is prompted to select again.
  """
  types = {"1": "movie", "2": "series", "3": "episode"}
  selected_type = input(
      f"1: {types['1']} \n2: {types['2']} \n3: {types['3']}\n\nYour selection: "
  ).lower()
  if selected_type in types.values():
    return selected_type.lower()
  if selected_type not in types:
    print("Invalid Input. Select again.")
    return get_search_type()
  return types[selected_type]


def get_search_string():
  """
  Prompt the user to enter a search string (e.g., movie title).

  Returns:
  - The user's input as a string.

  Note:
  - The function trims leading and trailing whitespace from the user's input.
  """
  search_string = input("\nWhat do you want to search: ").strip('')
  return search_string


def get_selected_imdbID(search_result):
  """
  Prompt the user to select a title from the search results.

  Args:
  - search_result (list of dictionaries): A list of search results.

  Returns:
  - The IMDb ID (imdbID) of the selected title as a string, or None if the user chooses to exit.

  Note:
  - The function allows the user to select a title either by entering a number or the title itself.
  - If the input is 'exit', the function returns None.
  - If the input is invalid or doesn't match any title, the user is prompted to try again.
  """
  while True:
    selected_title = input("\nSelect which one you want more details for: ")
    if selected_title.lower() == 'exit':
      return None

    if selected_title.isdigit():
      index = int(selected_title) - 1
      if 0 <= index < len(search_result):
        return search_result[index]['imdbID']

    for item in search_result:
      if item['Title'].lower() == selected_title.lower():
        return item['imdbID']
    print(
        "\nInvalid input. Please select from the list or type a valid title.")
