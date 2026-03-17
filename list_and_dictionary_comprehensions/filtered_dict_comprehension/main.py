# Given travel wishlist
travel_wishlist = [['Paris', 'France', 2000],['Tokyo', 'Japan', 3000],['New York', 'USA', 2500],
                   ['Kyoto', 'Japan', 1500],['Rome', 'Italy', 2200],['Sydney', 'Australia', 2800],
                   ['Barcelona', 'Spain', 1900],['London', 'UK', 2600],['Berlin', 'Germany', 2100],
                   ['Dubai', 'UAE', 3500],['Bangkok', 'Thailand', 1800],['Singapore', 'Singapore', 2900],
                   ['Los Angeles', 'USA', 2700],['Cape Town', 'South Africa', 2300],['Venice', 'Italy', 2000],
                   ['Istanbul', 'Turkey', 1750],['Toronto', 'Canada', 2250],['Rio de Janeiro', 'Brazil', 1950],
                   ['Athens', 'Greece', 1850]]

# Filter destinations in Japan using dictionary comprehension
japanese_destinations = {}

for city, country, cost in travel_wishlist:
    if country == "Japan":
        japanese_destinations[city] = cost



# Testing
print('Japanese Destinations:', japanese_destinations)

#travel_wishlist = [
 #   ['Paris', 'France', 2000],
 #   ['Tokyo', 'Japan', 3000],
 #   ['New York', 'USA', 2500],
  #  ['Kyoto', 'Japan', 1500],
 #   ['Sydney', 'Australia', 4000]
#]

# Filter destinations within a $2500 budget using a for loop
#affordable_destinations = {}

#for city, country, budget in travel_wishlist:
 #   if budget <= 2500:  # Check if the budget is within the limit
 #       affordable_destinations[city] = budget
#
#print(affordable_destinations)


#travel_wishlist = [
#    ['Paris', 'France', 2000],
#    ['Tokyo', 'Japan', 3000],
#    ['New York', 'USA', 2500],
#    ['Kyoto', 'Japan', 1500],
 #   ['Sydney', 'Australia', 4000]
#]

# Use dictionary comprehension to filter destinations
#affordable_destinations = {city: budget for city, country, budget in travel_wishlist if budget <= 2500}

#print(affordable_destinations)  # Output: {'Paris': 2000, 'New York': 2500, 'Kyoto': 1500}

