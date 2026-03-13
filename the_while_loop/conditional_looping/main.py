# List of country names
countries = ['Wales', 'Denmark', 'Belgium', 'Japan', 'South Korea', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Turkey', 'Greece', 'Netherlands', 'Finland', 'Monako', 'United Arab Emirates', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Thailand', 'Luxemburg', 'New Zealand', 'France', 'Italy', 'Germany', 'China', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# Counter variable
short_name_count = 0

i = 0 

while i < len(countries):
    if len(countries[i]) < 7:
        short_name_count += 1
    i += 1 



# Testing
print('Number of short country names:', short_name_count)

#travel_list = ['Monako', 'Luxemburg', 'Liverpool', 'Barcelona', 'Munchen']

# Initialize index
#i = 0

# Categorize cities by name length
#while i < len(travel_list):
 #   if len(travel_list[i]) < 8:
#        print(travel_list[i], 'has a short name.')
#    else:
#        print(travel_list[i], 'has a long name.')
#    i += 1