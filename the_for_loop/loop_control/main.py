# List of countries you are considering for travel
countries = ['Wales', 'Denmark', 'Belgium', 'Japan', 'South Korea', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Turkey', 'Greece', 'Netherlands', 'Finland', 'Monako', 'United Arab Emirates', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Thailand', 'Luxemburg', 'New Zealand', 'France', 'Italy', 'Germany', 'China', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# List of countries that require a visa
visa_required = ['China', 'India', 'Saudi Arabia', 'Brazil', 'United Arab Emirates', 'Egypt']

# List of visa-free travel destinations
travel_list = []

for country in countries:
    if country in visa_required:
        continue
    travel_list.append(country)
    if len(travel_list) == 10:
        break

# Testing
print('Visa-free travel destinations:', travel_list)

# Using Break in loops 

#travel_list = ['Monako', 'Luxemburg', 'Liverpool', 'Barcelona', 'Munchen']

# Searching for a specific city
#for city in travel_list:
 #   if city == 'Barcelona':
 #       print('Found Barcelona!')
 #       break
 #   else:
  #      print(city, 'is not Barcelona')

# Skipping loop 

#travel_list = ['Monako', 'Luxemburg', 'Liverpool', 'Barcelona', 'Munchen']

#short_name_count = 0

#for city in travel_list:
#    if len(city) >= 8:
 #       continue  # Skip cities with names 8 or more characters long
 #   short_name_count += 1

#print('Number of cities with names shorter than 8 characters:',  short_name_count)

# to Pass a already selected variable in a loop 

#travel_list = ['Monaco', 'Luxembourg', 'Liverpool', 'Barcelona', 'Munich']
#already_visited = ['Barcelona', 'Monaco']

#for city in travel_list:
#    if city in already_visited:
 #       pass
 #   else:
  #      print('Going to visit', city)



