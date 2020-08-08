# Working with Depth and Breath first search, recursion, getting user input, and working with graphs
# Goal: create a program to help commuters get from one landmark to another using Vancouver's public metro system. Build a "SkyRoute," a routing tool taht uses breadth-first search, depth-first search, and Python dictionaries.

from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

# Build your program below:
landmark_string = ""
stations_under_construction = ["Lansdowne", "Olympic Village" ]

# looping through landmark_choices so all choices are combined into a string
for letter, landmark in landmark_choices.items():
  landmark_string += letter + " - " + landmark + "\n"

def greet():
  print("Hi there and welcome to SkyRoute!")
  print("We'll help you find the shortest route between the following Vancouver landmarks:\n" + landmark_string)

def skyroute():
  greet()
  new_route()
  goodbye()

# Ask guest where they want to start
def get_start():
  start_point_letter = input("Where are you coming from? Type in the corresponding letter: ")
  if start_point_letter in landmark_choices:
    start_point = landmark_choices[start_point_letter]
    return start_point
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    return get_start()


# Where guest wants to get to
def get_end():
  end_point_letter = input("Okay, where are you headed? Type in the corresponding letter: ")
  if end_point_letter in landmark_choices:
    end_point = landmark_choices[end_point_letter]
    return end_point
  else:
    print("Sorry, that's not a landmark we have data on. Let's try this again...")
    return get_end()

def set_start_and_end(start_point, end_point):
  if start_point is not None:
    change_point = input("What would you like to change? You can enter 'o' for 'origin', 'd' for 'destination', or 'b' for 'both': ")
    # asking guest for a command on where they want to start/end
    if change_point == "b":
      start_point = get_start()
      end_point = get_end()
    elif change_point == "o":
      start_point = get_start()
    elif change_point == "d":
      end_point = get_end()
    else:
      print("Oops, that isn't 'o', 'd', or 'b'...")
      set_start_and_end(start_point, end_point)

  else:
    start_point = get_start()
    end_point = get_end()
  return start_point, end_point

def show_landmark():
  see_landmarks = input("Would you like to see the list of landmarks again? Enter y/n: ")
  if see_landmarks == "y":
    print(landmark_string)

# wrapper function to get and set origin and destination, call search to get recommended route, and allow users to search for another route
def new_route(start_point=None, end_point=None):
  start_point, end_point = set_start_and_end(start_point, end_point)
  shortest_route = get_route(start_point, end_point)
  
  # accomadating for stations being closed
  if shortest_route is not None:
    # more user friendly for guests to look at
    shortest_route_string = "\n".join(shortest_route)
    # string interpulation
    print("The shortest metro route from {0} to {1} is:\n{2}".format(start_point, end_point, shortest_route_string))
  else:
    print("Unfortunately, there is currently no path between {0} and {1} due to maintenance.".format(start_point, end_point))
  
  again = input("Would you like to see another route? Enter y/n: ")
  if again == "y":
    show_landmark()
    new_route(start_point, end_point)

# bredth-first function to find shortest route
def get_route(start_point, end_point):
  start_stations = vc_landmarks[start_point]
  end_stations = vc_landmarks[end_point]
  routes = []
  for start_station in start_stations:
    for end_station in end_stations:
      # accommodats ournew updated_metro graph if there are stations under construction
      metro_system = get_active_stations() if stations_under_construction else vc_metro
      # makes sure stations_under_constructions isn't empty
      if len(stations_under_construction) > 0:
        # using depth-first function to help find shortest route between points
        possible_route = dfs(metro_system, start_station, end_station)
        if possible_route is None:
          return None
      route = bfs(metro_system, start_station, end_station)
      if route is not None:
        routes.append(route)
  # find shortest route with little trick, 2D list
  shortest_route = min(routes, key=len)
  return shortest_route

# function to change routes if stations close/underconstruction
def get_active_stations():
  updated_metro = vc_metro
  for station_under_construction in stations_under_construction:
    for current_station, neighboring_station in vc_metro.items():
      if current_station != station_under_construction:
        updated_metro[current_station] -= set(stations_under_construction)
      else:
        updated_metro[current_station] = set([])
  return updated_metro

def goodbye():
  print("Thanks for using SkyRoute!")

#testing below

#active_stations = get_active_stations()
#for active_station, connections in active_stations.items():
  #print(active_station + " - " + str(connections))

#print(get_route('Marine Building', 'Robson Square'))
#print(set_start_and_end(8, None))
skyroute()
