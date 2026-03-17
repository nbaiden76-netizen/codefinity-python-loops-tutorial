# Given travel wishlist
travel_wishlist = [['Paris', 'France', 2000],['Tokyo', 'Japan', 3000],['New York', 'USA', 2500],
                   ['Kyoto', 'Japan', 1500],['Rome', 'Italy', 2200],['Sydney', 'Australia', 2800],
                   ['Barcelona', 'Spain', 1900],['London', 'UK', 2600],['Berlin', 'Germany', 2100],
                   ['Dubai', 'UAE', 3500],['Bangkok', 'Thailand', 1800],['Singapore', 'Singapore', 2900],
                   ['Los Angeles', 'USA', 2700],['Cape Town', 'South Africa', 2300],['Venice', 'Italy', 2000],
                   ['Istanbul', 'Turkey', 1750],['Toronto', 'Canada', 2250],['Rio de Janeiro', 'Brazil', 1950],
                   ['Athens', 'Greece', 1850]]

# Create a dictionary mapping city to country
city_to_country = {}

# Populate the dictionary using a for loop 
for city, country, cost in travel_wishlist:
    city_to_country[city] = country

# Testing
print('City to Country Mapping:', city_to_country)

#travel_wishlist = [
#    ['Paris', 2000],
#    ['Tokyo', 3000],
#    ['New York', 2500],
#    ['Kyoto', 1500],
#    ['Sydney', 4000]
#]

# Initialize an empty dictionary
#travel_budget = {}

# Populate the dictionary using a for loop
#for destination, cost in travel_wishlist:
#    travel_budget[destination] = cost

#print(travel_budget)

#travel_wishlist = [
#    ['Paris', 2000],
#    ['Tokyo', 3000],
#    ['New York', 2500],
#    ['Kyoto', 1500],
#    ['Sydney', 4000]
#]

# Create the dictionary using dictionary comprehension
#travel_budget = {destination: cost for destination, cost in travel_wishlist}

#print(travel_budget)



