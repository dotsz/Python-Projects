# Lab 8 - Dealing with Data Structures

## Overview 

This lab exercises your knowledge of the concepts up to module 8 in CSD110. You will practice working with nested data structures, including lists, tuples, and dictionaries in Python programs. 

## Required Reading 

It is assumed that you have watched all lecture videos and completed readings and practice exercises up to the end of Chapter 12 (not including Chapter 4) in the course textbook.  If you have not done so yet, you should! 

##  Instructions 

### Running your code

In the `main.py` file you will see several lines of code that import the individual code files you will work on in this lab. You can manage which files run when you click the `Run` button by commenting all imports except the one you want to run. (And you can of course run multiple of your code files by leaving multiple lines uncommented.)

### Testing your code

A set of tests have been prepared for this lab that will help you determine if your code is correct or not. To run the tests...

1. Open the Shell (in the right side panel)
2. Run the command `python -m pytest .test/test_q#.py` (with the `#` replaced by the number of the code file you want to test). You can also run all the tests for the lab at once by running the command `python -m pytest .test`

The output of the tests will give you an indication of how many of the tests passed or failed. For any failed tests, you will also see error messages that should help you determine why the test failed. 

If all the tests passed, you can be reasonably sure that your code is correct, **BUT PASSING ALL TESTS DOES NOT NECESSARILY MEAN YOU WILL GET 100%** because some grades are assigned to non-coding tasks, and it is sometimes possible to create incorrect programs that do pass the tests.

### Other important notes

In any place where you are responsible for naming functions or variables, you MUST use meaningful names. You must also include appropriate docstrings for any non-trivial functions you create. Failing to do so will result in a lower grade.

### Part 1 - Exploring references in nested data structures

Examine `q1.py`. A nested data structure representing a person is being used to create 4 variables each representing a different person. (See the comment in `q1.y` for details on the structure.)

1. Copy the four variables into a Python REPL, then spend a couple minutes exploring them, including:

    - Try changing the name or birthdate
    - Try adding a nickname
    - Try setting the nicknames list to an entirely new list (this should fail with a runtime error)
    - Try changing the province of an address, or adding a `street2` item into one of the addresses
    - Try setting the address dictionary to an entirely new dictionary (this should fail with a runtime error)
    - Try using the `[:]` operator to copy the `ali` variable into a fifth variable, then add a new nickname to the copy or change the address in some way. Now show the `ali` variable again.  Has it changed too?  Why?
2. Answer the 3 questions indicated in `q1.py`.  Feel free to continue experimenting in the REPL to ensure that understand the results you are seeing.
3. **IMPORTANT:** Copy and paste your REPL session into `q1-repl.txt`
4. Complete the `deep_copy` function in `q1.py` as per the given docstring

### Part 2 - Build an app using nested data structures

**IMPORTANT:** Do all your work for this part in the `movieapp` folder.  A starting point has been created for you in `movieapp/app.py` which you can run from `main.py` using the code below:

```python
import movieapp.app as app
app.start()
```

In this part you will complete a simple app that allows the user to search for information about movies. The app will make use of the [OMDB API](http://www.omdbapi.com/#usage), a freely available web API that can be used to obtain information about movies and TV series.

API stands for Application Programming Interface, and is a very general term used in a variety of programming contexts to mean, essentially, a library of code that other code can interact with. In this case, the API is a set of functions that can be called over the internet using the HTTP protocol. 

You will make use of the [Requests](https://requests.readthedocs.io/en/latest/user/quickstart/) module which is a module that can make calls to HTTP APIs. This module has already been installed in this Replit, and the `movieapp/api.py` module contains some helpful functions to get you started with making API calls correctly. (You may use these functions or ignore them and work directly with the `requests` module if you would prefer.)

This app will use two functions made available by the OMDB API: one to [search](http://www.omdbapi.com/#parameters) for a list of movies/series/episodes by title; and one to obtain information for [one specific](http://www.omdbapi.com/#parameters) movie/series/episode. The basic Python statements you will need in order to make these calls are shown below.

```python
import requests

# Search for a movie by title (replace movie title)
# params dictionary keys:
# apikey: your API key
# s: the search term (a title)
# type: one of 'movie', 'series', or 'episode'
search_results = requests.get("http://www.omdbapi.com", params={"apikey":"your_api_key", "s":"star wars", "type":"movie"}).json()

# Search for a specific movie/series/episode by IMDB ID
# params dictionary keys:
# apikey: your API key
# i: the IMDB ID (can be obtained from the search results 
# you get back in the call above)
info = requests.get("http://www.omdbapi.com", params={"apikey":"your_api_key", "i":"tt0083866"}).json()
```

#### Part 2a - Get set up

1. Create a free API key for yourself here: http://www.omdbapi.com/apikey.aspx . This key will allow your app to make calls to the OMDB API on your behalf.
2. Click the activation link in the email you receive after creating your key.
3. Confirm that your key is working by opening the Python REPL and running the following two statements (replace `your_api_key` with your API key):
    > ```
   > import movieapp.api as api
   > api.test("your_api_key")
   The second line should evaluate to `True`. If it does not, check that you entered your API key, and make sure that you did step 2 above.
4. Once you have a working API key, start investigating the structure of the data you get back from both the API functions shown above. (Again, feel free to use `requests` directly, or use the `api` functions that have been provided. They will both ultimately yield the same data structures.)

    **Some things to note:**
     - The data is a nested structure containing both lists and dictionaries.
     - Python's `print` function does no formatting of nested data structures, and it can be hard to understand the structure. A tool like [Python Formatter](https://formatter.org/python-formatter) can be useful. Or, Python has a module for that:
        ```python
       import pprint
       pp = pprint.PrettyPrinter(indent=2)
       pp.pprint(big_nasty_nested_structure)
        ```
     - And don't forget about the debugging tools to inspect the values you are obtaining from your function calls!
     - The search function returns at most 10 items even if more items would match the search terms. That is ok.

#### Part 2b - Build the main functionality

The ultimate goal is to build an app that lets the user search for movie/series titles, then select from among a list of search results to get detailed information. An example session is shown in Appendix A below. 

**For now, though, let's focus on the part that shows the detailed information for a specific item.**

1. Start by writing some code that can fetch the info for a specific movie of your choice (the IMDB ID `tt0083866`, for example)
2. Continue by writing code that extracts the information in the nested data structure you obtain and formats it into a paragraph of text like (but not necessarily exactly the same as) the one you see in the sample for Appendix A. Here are some goals you should aim for:
    - Your function should not cause an error for ANY result from the API (so test your function on a variety of different items to make sure it is robust)
    - You MUST include `Awards` information if present, but your code must not break if no `Awards` key is present
    - You MUST include `Ratings` information (**NOTE:** `RatINGS` not `RatED`, although you may include the latter if you wish), but your code must not break if no `Ratings` key is present OR if the `Ratings` list is empty
    - Some keys in the main dictionary have the value "N/A"; try to skip such values instead of including phrases like "...it was direted by N/A..."
    - In general, try to make your function produce text that reads like a human may have written it, no matter which OMDB item is passed to it.

#### Part 2c - Complete the app

Once you have the code for Part 2b working, polish your app by making it fully interactive. 

You should:

- Prompt the user for a search term
- Show the user a list of up to 10 title that match their search term as obtained from the OMDB API
- Allow the user to choose to view detailed information for one of the search results
- Continue prompting the user for more search requests until they exit the program by pressing `Ctrl+c`. (This key combination requires no extra coding; it will work in any Python program running in a shell.)
- Document your code with appropriate docstrings and comments
- Try to organize your code into meaningfully named functions that each have a specific purpose. (You may even split your code into separate files containing related functions.  The sample solution, for example, has a `ui.py` module that contains code specific to prompting the user and printing varoius data structures appropriately.)

Optionally:

- Prompt the user for which type (movie, series, or episode) they want to search for before prompting for their search term
- Allow the user to cycle to the next page of search results if the first 10 items did not list the item they were searching for

## Submission

1. **Be sure to test your code using the testing instructions above!**
2. Review your code and make sure that it is well organized, commented, and that **all your functions have appropriate docstrings**
3. Copy the URL for this lab from your address bar
4. Submit this URL in the appropriate lab folder on the LMS

## Rubric

See the rubric attached to this lab in the LMS

## Appendix A - Sample session of completed app

```
To quit, press Ctrl+c
1: movie
2: series
3: episode
What do you want to search for? (Enter a number) 
You must enter a number from 1 to 3
What do you want to search for? (Enter a number) 1
Enter a title to search for: star wars
1: Star Wars: Episode IV - A New Hope (1977)
2: Star Wars: Episode V - The Empire Strikes Back (1980)
3: Star Wars: Episode VI - Return of the Jedi (1983)
4: Star Wars: Episode VII - The Force Awakens (2015)
5: Star Wars: Episode I - The Phantom Menace (1999)
6: Star Wars: Episode III - Revenge of the Sith (2005)
7: Star Wars: Episode II - Attack of the Clones (2002)
8: Rogue One: A Star Wars Story (2016)
9: Star Wars: Episode VIII - The Last Jedi (2017)
10: Star Wars: Episode IX - The Rise of Skywalker (2019)
Enter the number of the movie you would like to view: 5

Star Wars: Episode I - The Phantom Menace is a 136 min action, adventure, fantasy movie starring Ewan McGregor, Liam Neeson, Natalie Portman.  It was written by George Lucas and directed by George Lucas. It was released on 19 May 1999. Two Jedi escape a hostile blockade to find allies and come across a young boy who may bring balance to the Force, but the long dormant Sith resurface to claim their original glory.
Awards:
Nominated for 3 Oscars. 28 wins & 71 nominations total
Ratings:
Internet Movie Database: 6.5/10
Rotten Tomatoes: 52%
Metacritic: 51/100

To quit, press Ctrl+c
1: movie
2: series
3: episode
What do you want to search for? (Enter a number) 2
Enter a title to search for: family matters
1: Family Matters (1989–1998)
2: Mathis Family Matters (2022–)
3: The Real Housewives of Atlanta: Porsha's Family Matters (2021–2022)
4: Family Matters (2014–2017)
5: Jo Frost: Family Matters (2014–)
6: Family Matters TV with Justice Harvey Brownstone (2011–)
7: Family Matters (2006)
8: Family Still Matters TV (2015–)
9: Family Matters on TV (2010–2015)
Enter the number of the movie you would like to view: 1

Family Matters is a 30 min adventure, comedy, drama series starring Reginald VelJohnson, Jaleel White, Darius McCrary.  It was written by William Bickley, Robert L. Boyett, Thomas L. Miller. It was released on 22 Sep 1989. The Winslow family deals with various misadventures, many of them caused by their pesky next-door neighbor, ultra-nerd Steve Urkel.
Awards:
Nominated for 1 Primetime Emmy. 9 wins & 17 nominations total
Ratings:
Internet Movie Database: 6.6/10

To quit, press Ctrl+c
1: movie
2: series
3: episode
What do you want to search for? (Enter a number)
```