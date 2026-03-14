# Travel expenses for multiple trips
travel_costs = [[500, 150, 100, 50],[200, 300, 120, 80],
                [180, 220, 130, 170], [600, 250, 200, 90],
                [300, 180, 150, 70], [400, 320, 110, 100],
                [550, 270, 180, 60], [250, 190, 140, 120],
                [700, 350, 210, 110], [450, 230, 160, 95],
                [320, 280, 190, 85], [580, 260, 175, 75]]

# List to store processed expenses
processed_expenses = []

i = 0 

while i < len(travel_costs):
    trip_expenses = []
    j = 0 
    while j < len(travel_costs[i]):
        if travel_costs[i][j] <= 100:
             trip_expenses.append('Cheap')
        else:
             trip_expenses.append(travel_costs[i][j])
        j += 1 
    processed_expenses.append(trip_expenses)
    i += 1
            


# Testing
print('Processed Travel Expenses:', processed_expenses)




# Travel expenses for multiple trips
#travel_costs = [
#    [500, 150, 100, 50],   # Trip 1
#    [200, 300, 120, 80],   # Trip 2
 #   [180, 220, 130, 170]   # Trip 3
#]

# Setting outer while loop to work with rows (trips)
#i = 0
#while i < len(travel_costs):
  #  j = 0
 #   print(f"Trip {i + 1} expenses: ", end='')  # Label for the current trip

    # Setting inner while loop to work with expenses in the current trip
 #   while j < len(travel_costs[i]):
 #       if travel_costs[i][j] > 200:  # Check if expense is greater than 200
  #          print('Expensive', end=' ')
 #       else:
  #          print(travel_costs[i][j], end=' ')
 #       j += 1  # Move to the next expense
    
 #   print('')  # Move to the next line after each trip
 #   i += 1  # Move to the next trip