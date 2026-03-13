# List of country names
countries = ['Wales', 'Denmark', 'Belgium', 'Japan', 'South Korea', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Turkey', 'Greece', 'Netherlands', 'Finland', 'Monako', 'United Arab Emirates', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Thailand', 'Luxemburg', 'New Zealand', 'France', 'Italy', 'Germany', 'China', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# List to hold selected countries
selected = []

i = 0 

while i < len(countries):
    if countries[i][0] != "S":
        i += 1
        continue
        
    selected.append(countries[i])

    if len(selected) == 3:
        break  
# Testing
print('First three countries starting with "S":', selected)


#travel_list = ['Monako', 'Luxemburg', 'Liverpool', 'Barcelona', 'Munchen']

# Initialize the index
#i = 0

# Search for "Barcelona"
#while i < len(travel_list):
#    if travel_list[i] == 'Barcelona':
 #       print('Found Barcelona!')
 #       break
 #   print(travel_list[i])
 #   i += 1


#travel_list = ['Monako', 'Barcelona', 'Liverpool', 'Barcelona', 'Munchen', 'Barcelona']

# Initialize variables
#i = 0
#counter = 0

# Count occurrences of "Barcelona"
#while i < len(travel_list):
#    if travel_list[i] != 'Barcelona':
#        i += 1
#        continue
#€else:
       #counter += 1
  #  i += 1

#print('Total occurrences of Barcelona:', counter)