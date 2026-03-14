# List of trips
trips = [['france', 'germany', 'italy', 'spain', 'netherlands', 'sweden', 'norway', 'switzerland', 'austria', 'portugal', 'belgium'],
         ['japan', 'china', 'thailand', 'vietnam', 'ndonesia', 'india', 'malaysia', 'philippines', 'singapore', 'mongolia'],
         ['usa', 'canada', 'mexico', 'brazil', 'argentina', 'colombia', 'peru', 'chile', 'ecuador'],
         ['egypt', 'morocco', 'south africa', 'tunisia', 'algeria', 'kenya', 'nigeria', 'ethiopia'],
         ['australia', 'new zealand', 'fiji', 'papua new guinea', 'samoa']]

# List of all countries 
countries = []
for trip in trips:        # trip is a list of country-strings
    for country in trip:  # country is now a string  
        countries.append(country.capitalize())



# Testing
print('List of Countries:', countries)


#travel_list = ['Monako', 'Luxemburg', 'Liverpool', 'Barcelona', 'Munchen']

# Outer loop for controlling rows
#for i in range(1, len(travel_list) + 1):
    # Inner loop for controlling columns
#    for j in range(i):
 #       print(travel_list[j], end=' ')  # Print cities in a row
 #   print('')  # Move to the next line after each row

# Define a nested list containing sublists with words starting with 'A' and 'T'
#nested_list = [
 #   ["Apple", "Avocado", "Apricot"],
 #   ["Tomato", "Tangerine", "Tea"],
 #   ["Almond", "Thyme", "Tuna"]
#]

# Iterate through each sublist in the nested list
#for sublist in nested_list:
    # Iterate through each item in the current sublist
 #   for item in sublist:
        # Convert the item to lowercase and print it
   #     print(item.lower(), end=' ')