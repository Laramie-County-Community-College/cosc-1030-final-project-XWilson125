import random

def RNG(value, variance):
    return value + random.randrange(0-variance, variance)

def percent_chance(value):
    num = random.randrange(0, 100)
    if num > value:
        return True
    else:
        return False

class default_variables():          #Defines every last variable. Note: all variables are taken from NBA stats and are rough guesstimates for the variation. Classed purely for storage.
    time = 30
    score_needed_to_make = 3
    three_point_percentage = 30
    two_point_percentage = 55
    freethrow_percentage = 80
    shot_rebound_chance = 25
    freethrow_rebound_chance = 75
    win_overtime_chance = 50
    three_point_percentage_deviation = 10
    two_point_percentage_deviation = 10
    freethrow_percentage_deviation = 10
    shot_rebound_chance_deviation = 10
    freethrow_rebound_chance_deviation = 7
    win_overtime_chance_deviation = 15
    def _input_percentage():                                    #NOT COMPLETE!
        percent_num = input(input)
        try:
            percent_num = float(percent_num)
        except:
            raise TypeError("Non-number inserted as a percentage")
        if 0 <= percent_num <= 100:
            raise ValueError("Number inserted is not from 0-100")
        
    def change_variable():                                      #variable to edit certain stats(like if, for example, the opponent is bad at shooting free throws)
        print(f'Current variables:\n'                           #Prints stats; necessary to look them over
              f'    1 - Three point shot chance: {default_variables.three_point_percentage}%\n'
              f'    2 - Two point shot chance: {default_variables.two_point_percentage}%\n'
              f'    3 - Opponent free throw chance: {default_variables.freethrow_percentage}%\n'
              f'    4 - Offensive rebound chance: {default_variables.shot_rebound_chance}%\n'
              f'    5 - Defensive rebound chance: {default_variables.freethrow_rebound_chance}%\n')
    #Gathers and validates input
        varchange = input('Which variable would you like to change? Pick a number or e to exit. ')
        valid_input = False
        quit_num = 0
        while valid_input == False:
            try:
                varchange = int(varchange)
                if 1 <= varchange <= 5:
                    valid_input = True
                else:
                    varchange = input('That is not a valid number. Pick a number from 1 to 5.')
            except:
                if quit_num == 3 or varchange == 'e':
                    print('Assuming that you want to exit the function.')
                    break
                print('That is not a valid input. Pick a number.')
                quit_num += 1

        if varchange == 1:
            default_variables.three_point_percentage = default_variables._input_percentage()
        elif varchange == 2:
            pass
        elif varchange == 3:
            pass
        elif varchange == 4:
            pass
        elif varchange == 5:
            pass

    def determine_variables(self):
        self.three_point_percentage = RNG(default_variables.three_point_percentage, default_variables.three_point_percentage_deviation)
        self.two_point_percentage = RNG(default_variables.two_point_percentage, default_variables.two_point_percentage_deviation)
        self.freethrow_percentage = RNG(default_variables.freethrow_percentage, default_variables.freethrow_percentage_deviation)
        self.shot_rebound_chance = RNG(default_variables.shot_rebound_chance, default_variables.shot_rebound_chance_deviation)
        self.freethrow_rebound_chance = RNG(default_variables.freethrow_rebound_chance, default_variables.freethrow_rebound_chance_deviation)
        self.win_overtime_chance = RNG(default_variables.win_overtime_chance, default_variables.win_overtime_chance_deviation)

def three_point_shot(game):
    print('tpstest')                #REMOVE: USED FOR TESTING!
    if percent_chance(game.three_point_percentage):
        return percent_chance(game.win_overtime_chance)
    else:
        return False
'''
Take a single 3-point shot when time is running out.
If the shot misses, the game is lost.
If the shot goes in, overtime is forced, where the outcome is a 50/50 chance.'''

def two_point_foul(game):
    print('tpftest')                #REMOVE: USED FOR TESTING!
    not_certain_turnover = True
    if percent_chance(game.two_point_percentage):
        game.score_needed_to_make -= 2
        not_certain_turnover = False
    while not_certain_turnover and percent_chance(game.shot_rebound_chance):
        if percent_chance(game.two_point_percentage):
            game.score_needed_to_make -= 2
            not_certain_turnover = False
    
    while game.time > 0:
        if percent_chance(game.freethrow_percentage):
            game.score_needed_to_make += 1
            certain_rebound = True
        else:
            certain_rebound = False
        if percent_chance(game.freethrow_rebound_chance) or certain_rebound:
            pass
'''    Two-Point + Foul Strategy

Attempt a higher-percentage two-point shot.
If the shot goes in, foul the opponent to regain possession.
Track free throw outcomes and keep playing until time runs out.'''

sim_run_count = int(input('Please insert number of times to run simulation: '))
change_sim = input('Would you like to change the default parameters? y/n')
if change_sim == 'y' or change_sim == 'Y':
    default_variables.change_variable()
elif change_sim == 'n' or change_sim == 'N':
    print('Keeping default variables.')
else:
    print("Unknown input. Assuming 'n' as your answer. Keeping default variables")
three_point_win_count = 0
two_point_win_count = 0
for unused in range(sim_run_count):
    game = default_variables()
    game.determine_variables()
    if three_point_shot(game) == True: #will use variables to calculate 3-point plan, then add outcome to list
        three_point_win_count += 1
    if two_point_foul(game) == True: #will use variables to calculate 2-point-and-foul plan, then add outcome to list
        two_point_win_count += 1
print(f'Three point win percentage: {three_point_win_count/sim_run_count}')
print(f'Two point and foul win percentage: {two_point_win_count/sim_run_count}')




'''
The primary idea behind a trial is to model the strategy - either a two point or three point strategy as outlined below.

This is done with randomness.  The two and three point shots, along with the free throw attempts, will all be determined by whether a random number falls above or below the chance you assign to it up front.  That success or failure helps determine the combined event probability that the strategy succeeds or fails on a given trial.

Three-Point Strategy

Take a single 3-point shot when time is running out.
If the shot misses, the game is lost.
If the shot goes in, overtime is forced, where the outcome is a 50/50 chance.

Two-Point + Foul Strategy

Attempt a higher-percentage two-point shot.
If the shot goes in, foul the opponent to regain possession.
Track free throw outcomes and keep playing until time runs out.

Monte Carlo Simulation Process
Run thousands of trials for each strategy.
Record win/loss outcomes for both strategies.
Compare success rates to see which approach has a higher probability of winning.'''