import random as ran 

def roll_dice ():
    number =ran.randint(1,6)
    print("you rolled a " + str(number))
    return number

max_score = 20
max_trials = 7


def start_game():
    user_score =0
    current_trial = 1

    print("welcome to dodgo dice game")
    print ("try to reach exactly " + str(max_score)+ "point to win the game")
    input("press enter to begin")

    while True:
        input("press enter to roll")
        current_roll = roll_dice()
        current_trial += 1
        user_score += current_roll
        if user_score > max_score:
            print("your score is " + "user_score")
            print("you have extended tyhe max score of 20")
            break
        elif current_trial > max_trials:
            print("you have extended the max trial of 20")
            print("your score is " + str(user_score))
            break
        elif user_score == max_score:
            print("your score is " + str(user_score))
            print("congrats, you won")
            break
        else: 
            print("you rolled a " + str(current_roll))
            print("your score is " + str(user_score))

         

    
    # while user_score < max_score or current_trial < max_trials:
       
        
      
      
    #        current_roll = dice_roll()
    #        user_score += current_roll 
    #        current_trial = current_trial +1
 
    #        if user_score > max_score:
    #           print("your final score was" + str(user_score))
    #           print("you have exceeded the maximum score.")
    #           break
    #        elif user_score == max_score:
    #             print("your final score " + str(user_score) )
    #             print("congratulations, you have won")
    #             break
    #        if user_score < max_score:
    #            print("your final score was " + str(user_score))
  
              
start_game()   
        

















