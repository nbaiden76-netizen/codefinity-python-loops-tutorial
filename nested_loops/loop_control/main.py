# Travel expenses for multiple trips
travel_costs = [[500, 150, 100, 50], [200, 300, 120, 80], [180, 220, 130, 170], [600, 250, 200, 90], [300, 180, 150, 70], [400, 320, 110, 100], [550, 270, 180, 60], [250, 190, 140, 120], [700, 350, 210, 110], [450, 230, 160, 95], [320, 280, 190, 85], [580, 260, 175, 75], [630, 300, 220, 130], [280, 210, 125, 140], [490, 330, 145, 105], [520, 340, 190, 125], [750, 400, 250, 150], [340, 270, 160, 115], [620, 310, 225, 135], [410, 290, 135, 90]]

# List to store the first significant expense of each trip
significant_expenses = []

# Outer while loop to iterate through trips 
i = 0 
while i < len(travel_costs):
    # now for loop to iterate through the travel expenses
    for costs in travel_costs[i]:
        # if statement to ignore strictly less than $100 
        if costs < 100: 
            continue
        elif costs > 200:
                significant_expenses.append(costs)
                break
    #Move to the next trip 
    i += 1 
    print('') # add a new line for readability 
                
                
# Testing
print('First Significant Expenses:', significant_expenses)



# List of trips with their respective expenses
#travel_costs = [
#    [100, 150, 300, 50],   # Trip 1
#    [200, 500, 100, 80],   # Trip 2
#    [120, 180, 400, 150]   # Trip 3
#]

# Budget threshold
#budget = 200

# Outer while loop to iterate through trips
#i = 0
#while i < len(travel_costs):
#    print(f"Processing expenses for Trip {i + 1}:")
    
    # Inner for loop to iterate through expenses
#    for cost in travel_costs[i]:
        # If expense exceeds the budget
#        if cost > budget:  
#            print('Expense', cost, 'exceeds the budget. Stopping this trip.')
#            break
#        print('Expense:', cost)
    
#    i += 1  # Move to the next trip
#    print('')  # Add a new line for readability