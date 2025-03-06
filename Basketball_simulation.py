import random
sim_run_count = int(input('Please insert number of times to run simulation: '))
three_point_shot_list = []
two_point_foul_list = []
def variable_calc_function():           #Defines every last variable. Note: all variables are taken from NBA stats and are rough guesstimates for the variation.
    global three_point_percentage
    global two_point_percentage
    global freethrow_percentage
    global time
    global shot_rebound_chance
    global freethrow_rebound_chance
    global win_overtime_chance
    three_point_percentage = random.uniform(.30, .40)
    two_point_percentage = random.uniform(.50, .60)
    freethrow_percentage = random.uniform(.40, .60)             #The actual average is around 70-90%, but the opponent's free throw percentage is bad(40% is really bad).
    time = 30
    shot_rebound_chance = random.uniform(.20, .35)
    freethrow_rebound_chance = random.uniform(.65, .80)
    win_overtime_chance = random.uniform(.45, .55)

def three_point_shot():
    pass

def two_point_foul():
    pass

for unused in range(sim_run_count):
    variable_calc_function() #will pull all variables from likely ranges
    three_point_shot_list.append(three_point_shot()) #will use variables to calculate 3-point plan, then add outcome to list
    two_point_foul_list.append(two_point_foul()) #will use variables to calculate 2-point-and-foul plan, then add outcome to list
print(f'Three point win percentage: {sum(three_point_shot_list)/len(three_point_shot_list)}')
print(f'Two point and foul win percentage: {sum(two_point_foul_list)/len(two_point_foul_list)}')
