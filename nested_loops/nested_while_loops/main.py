# List of travel costs (each sublist represents a trip)
travel_costs = [
    [5, 15, 10, 8, 25, 30, 55, 68, 75, 5],
    [60, 20, 60, 70, 80, 80, 80, 90, 90, 90],
    [100, 100, 100, 100, 50, 110, 110, 120, 120, 120, 130],
    [130, 140, 39, 140, 150, 150, 150, 150, 160, 160],
    [170, 180, 180, 190, 40, 190, 200],
    [200, 200, 200, 210, 11, 220, 220, 220, 250, 250, 250],
    [280, 300, 300, 110, 300, 320, 350, 400, 400, 450],
    [480, 500, 500, 90, 500, 550, 600, 700]
]

# List to store maximum costs per trip
max_costs = []

# variable to store Maximum costs and Maximum trip
max_trip = 0 

i = 0 

# the outer loop to iterate over trips 8 in total 
while i < len(travel_costs):
    # initalise the per-trip maximum identifying the highest expense 
    trip_max = travel_costs[i][0]
    j = 0 

    # the inner loop to iterate over the expenses in each trip 
    while j < len(travel_costs[i]):
        # compares each expense, update trip_max 
        if travel_costs[i][j] > trip_max:
            trip_max = travel_costs[i][j]
        j += 1 

    # now to store that trip's maximum 
    
    max_costs.append(trip_max)
    i += 1   
# Testing
print('Maximum Travel Costs:', max_costs)



# List of trips with their respective expenses
# travel_costs = [
#    [500, 200, 100, 150],  # Trip 1: Flights, Hotels, Food, Activities
#    [600, 250, 120, 200],  # Trip 2: Flights, Hotels, Food, Activities
 #   [550, 180, 130, 170]   # Trip 3: Flights, Hotels, Food, Activities
#]

# Variables to track the maximum cost
#max_cost = 0
#max_trip = 0

# Outer loop to iterate over trips
#i = 0
#while i < len(travel_costs):
#    total_cost = 0
 #   j = 0
    
    # Inner loop to iterate over expenses in each trip
#    while j < len(travel_costs[i]):
 #       total_cost += travel_costs[i][j]
 #       j += 1
    
    # Print the total cost for the current trip
#    print('Total cost for Trip', i + 1, ':', total_cost)
    
    # Check if this trip is the new maximum
#    if total_cost > max_cost:
#        max_cost = total_cost
#        max_trip = i + 1
    
 #   i += 1

# Final output: print the trip with the highest total cost
# print("Trip", max_trip, "has the highest total cost of", max_cost)

