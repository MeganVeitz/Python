#Goal is to compair and sort out books in a dictionary by title, author, or sum of title and author with two different sort fucntions.
#Compairing two different types of sorts, bubble sort and quick sort. The result will show how much quicker the quick sort functions are. 

#Scipt.py
import utils
import sorts

# Loaded in csv files from outside sources
bookshelf = utils.load_books('books_small.csv')
long_bookshelf = utils.load_books('books_large.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()

#Sort by title
def by_title_ascending(book_a, book_b):
  return book_a['title_lower'] > book_b['title_lower']

#Sort by author
def by_author_ascending(book_a, book_b):
  return book_a['author_lower'] > book_b['author_lower']


#Sort by sum of title and author
def by_total_length(book_a, book_b):
  return len(book_a['author_lower']) + len(book_a['title_lower']) > len(book_b['author_lower']) + len(book_b['title_lower'])


# Will sort by title
sort_1 = sorts.bubble_sort(bookshelf, by_title_ascending)

# Will sort by author assending
sort_2 = sorts.bubble_sort(bookshelf, by_author_ascending)

# Will sort by total sum of title and author using long bookshelf
sort_3 = sorts.bubble_sort(long_bookshelf, by_total_length)

# Will sort by title
sorts.quicksort(bookshelf_v2, 0, len(bookshelf_v2) - 1, by_author_ascending)

sorts.quicksort(long_bookshelf, 0, len(long_bookshelf) - 1, by_total_length)

# Print out books by author or title
#for book in bookshelf_v2:
  #print(book["author_lower"])

# Print out books by author and title by bubble sort
#for book in sort_3:
  #print(len(book["author_lower"]) + len(book["title_lower"]))

#Print out books by author and title by quick sort
for book in long_bookshelf:
  print(len(book["author_lower"]) + len(book["title_lower"]))

#sorts.py
import random

def bubble_sort(arr, comparison_function):
  swaps = 0
  sorted = False
  while not sorted:
    sorted = True
    for idx in range(len(arr) - 1):
      # Compairison function to allow us to do a custom compairison ex: title or aurther
      if comparison_function(arr[idx], arr[idx + 1]):
        sorted = False
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        swaps += 1
  print("Bubble sort: There were {0} swaps".format(swaps))
  return arr


def quicksort(list, start, end, comparison_function):
  if start >= end:
    return
  pivot_idx = random.randrange(start, end + 1)
  pivot_element = list[pivot_idx]
  list[end], list[pivot_idx] = list[pivot_idx], list[end]
  less_than_pointer = start
  for i in range(start, end):
    # Want to compair elements under our comparison_function
    if comparison_function(pivot_element, list[i]):
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      less_than_pointer += 1
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  quicksort(list, start, less_than_pointer - 1, comparison_function)
  quicksort(list, less_than_pointer + 1, end, comparison_function)

#utils.py

import csv

# This code loads the current book
# shelf data from the csv file
def load_books(filename):
  bookshelf = []
  with open(filename) as file:
      shelf = csv.DictReader(file)
      for book in shelf:
          # Converting everything to lowercase prior to comparison
          book['author_lower'] = book['author'].lower()
          book['title_lower'] = book['title'].lower()
          
          bookshelf.append(book)
  return bookshelf
