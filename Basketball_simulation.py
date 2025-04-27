import random

def RNG(value, variance):
    return random.uniform(value-variance, value+variance)

def percent_chance(value):
    num = random.randrange(0, 100)
    if num < value:
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
    freethrow_rebound_chance = 25
    win_overtime_chance = 50
    three_point_percentage_deviation = 10
    two_point_percentage_deviation = 10
    freethrow_percentage_deviation = 10
    shot_rebound_chance_deviation = 10
    freethrow_rebound_chance_deviation = 7
    win_overtime_chance_deviation = 15

    def _input_percentage(string):
        percent_num = input(string)                             #Strips an input of '%' and ' '
        percent_num = percent_num.replace('%', '').replace(' ', '')
        try:                                                    #Tries to turn input into a float
            percent_num = float(percent_num)
        except:
            raise TypeError("Non-number inserted as a percentage")
        if 0.0 <= percent_num <= 100.0:                         #Returns float if between 0 and 100, raises ValueError if not
            return percent_num
        else:
            raise ValueError("Number inserted is not from 0-100.")
        
    def time_decrease(self, decrease_num):                      #Keeps track of time. Can't continue the game without time.
        self.time -= decrease_num
        if self.time <= 0:
            raise TimeoutError('Game over!')

    @staticmethod                                               #Learned this while working with ChatGPT the critic. I didn't copy-paste any of this code from ChatGPT.
    def change_variable():                                      #variable to edit certain stats(like if, for example, the opponent is bad at shooting free throws)
        #Starter stuff - Necessary to not break code. Sorry it's a bit messy.
        print(f'Current variables:\n'                           #First print of stats; necessary to look them over
              f'    1 - Three point shot chance: {default_variables.three_point_percentage}%\n'
              f'    2 - Two point shot chance: {default_variables.two_point_percentage}%\n'
              f'    3 - Opponent free throw chance: {default_variables.freethrow_percentage}%\n'
              f'    4 - Offensive rebound chance: {default_variables.shot_rebound_chance}%\n'
              f'    5 - Freethrow rebound chance: {default_variables.freethrow_rebound_chance}%\n')
        varchange = input('Which variable would you like to change? Pick a number or e to exit. ')    #First input
        while True:                                             #Repeats program until user stops changing variables.
            if varchange == 'e':                                #Validates input
                break
            try:
                varchange = int(varchange)
                if not (1 <= varchange <= 5):
                    varchange = input('That is not a valid number. Pick a number from 1 to 5.')
            except:
                try:
                    quit_num += 1
                except:
                    quit_num = 1
                if quit_num == 3:
                    print('That is not a valid input. Assuming that you want to exit the function.')
                    varchange = 'e'
                    continue
                varchange = input('That is not a valid input. Pick a number. ')
                continue
            print('Please input any number between 0% and 100%.')
            if varchange == 1:
                default_variables.three_point_percentage = default_variables._input_percentage('Please input a new three point shot chance: ')
            elif varchange == 2:
                default_variables.two_point_percentage = default_variables._input_percentage('Please input a new two point shot chance: ')
            elif varchange == 3:
                default_variables.freethrow_percentage = default_variables._input_percentage('Please input a new opponent free throw chance: ')
            elif varchange == 4:
                default_variables.shot_rebound_chance = default_variables._input_percentage('Please input a new offensive rebound chance: ')
            elif varchange == 5:
                default_variables.freethrow_rebound_chance = default_variables._input_percentage('Please input a new defensive rebound chance: ')

            print(f'Current variables:\n'                       #Prints stats; necessary to look them over
              f'    1 - Three point shot chance: {default_variables.three_point_percentage}%\n'
              f'    2 - Two point shot chance: {default_variables.two_point_percentage}%\n'
              f'    3 - Opponent free throw chance: {default_variables.freethrow_percentage}%\n'
              f'    4 - Offensive rebound chance: {default_variables.shot_rebound_chance}%\n'
              f'    5 - Defensive rebound chance: {default_variables.freethrow_rebound_chance}%\n')
            varchange = input('Would you like to pick another variable? If so, pick a number, or input e to exit. ')

    def determine_variables(self):
        self.three_point_percentage = RNG(self.three_point_percentage, self.three_point_percentage_deviation)
        self.two_point_percentage = RNG(self.two_point_percentage, self.two_point_percentage_deviation)
        self.freethrow_percentage = RNG(self.freethrow_percentage, self.freethrow_percentage_deviation)
        self.shot_rebound_chance = RNG(self.shot_rebound_chance, self.shot_rebound_chance_deviation)
        self.freethrow_rebound_chance = RNG(self.freethrow_rebound_chance, self.freethrow_rebound_chance_deviation)
        self.win_overtime_chance = RNG(self.win_overtime_chance, self.win_overtime_chance_deviation)

def three_point_shot(game):
    if percent_chance(game.three_point_percentage):
        return percent_chance(game.win_overtime_chance)
    else:
        return False
'''
Take a single 3-point shot when time is running out.
If the shot misses, the game is lost.
If the shot goes in, overtime is forced, where the outcome is a 50/50 chance.'''

def two_point_foul(game):
    try:
        while game.time > 0:
            game.time_decrease(RNG(8, 3))                   #Accounts for getting into a scoring position
                #Determines if the initial 2-point shot goes in, and accounts for rebounds.
            not_certain_turnover = True
            if percent_chance(game.two_point_percentage):
                game.score_needed_to_make -= 2
                not_certain_turnover = False
            while not_certain_turnover and percent_chance(game.shot_rebound_chance):
                game.time_decrease(RNG(3, 1))
                if percent_chance(game.two_point_percentage):
                    game.score_needed_to_make -= 2
                    not_certain_turnover = False
            #Determines if free throw makes it or not
            if percent_chance(game.freethrow_percentage):
                game.score_needed_to_make += 1
                certain_rebound = True
            else:
                certain_rebound = False
            if certain_rebound:
                game.time_decrease(RNG(6, 2.5))
            elif percent_chance(game.freethrow_rebound_chance):
                game.time_decrease(RNG(4, 1))
            else:
                game.time_decrease(RNG(8, 1))
    except TimeoutError:                                    #I know this isn't the way it should be used, but 1. I don't want to make my own error, and 2. It's funny.
        if game.score_needed_to_make > 0:
            return False
        elif game.score_needed_to_make == 0:
            return percent_chance(game.win_overtime_chance)
        else:
            return True
'''    Two-Point + Foul Strategy

Attempt a higher-percentage two-point shot.
If the shot goes in, foul the opponent to regain possession.
Track free throw outcomes and keep playing until time runs out.'''


sim_run_count = int(input('Please insert number of times to run simulation: '))
change_sim = input('Would you like to change the default parameters? y/n ')
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
print(f'Three point win percentage: {three_point_win_count/sim_run_count*100:.2f}%')
print(f'Two point and foul win percentage: {two_point_win_count/sim_run_count*100:.2f}%')