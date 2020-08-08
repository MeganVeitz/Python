# Searchcademy; using Binary Search, While Loops, and Complex Conditionals
# Testing a product using sparsey sorted dataset to test its search engine

def sparse_search(data, search_val):
  print("Data: " + str(data))
  print("Search Value: " + str(search_val))
  first, last = 0, len(data) -1
  
  # checks to see if first is less than or equal to last
  while first <= last:
    mid = (first + last) // 2

    # check to see if the middle is empty
    if not data[mid]:

      # checking surrounding values
      left, right = mid - 1, mid + 1

      # check to see if surrounding values are empty and breaks once we found a non-empy value
      while True:
        # check to see if we have iterated through entire dataset and have NOT found a non-empty value
        if left < first and right > last:
          print(str(search_val) + " is not in the dataset")
          return 
        # checking value on the right
        elif right <= last and data[right]:
          mid = right
          break
        # checking value on the left
        elif left >= first and data[left]:
          mid = left
          break
          
        # if non above are true then we move our pointers
        right += 1
        left -= 1
    # check to see if value is equal to our search value
    if data[mid] == search_val:
      print(str(search_val) + " found at position" + str(mid))
      return

    # check if search value is less than middle
    elif search_val < data[mid]:
      last = mid - 1
    # check if search value is greater than middle
    elif search_val > data[mid]:
      first = mid + 1
  # returning "value not in data"
  print(str(search_val) + " is not in the dataset")
  
