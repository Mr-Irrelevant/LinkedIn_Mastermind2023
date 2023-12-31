import os
import requests
import random
import time
import winsound

def modok_selected():
    """ Plays random MODOK intro when difficulty is selected """

    x = random.randint(1,3)

    if x == 1:

        winsound.PlaySound('Come on.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)

        time.sleep(4)

    elif x == 2:

        winsound.PlaySound("Break you.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

        #Gives audio time to play out before contuining. 
        time.sleep(4)

    elif x == 3:

        winsound.PlaySound('Brain vs Brawn.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)

        time.sleep(6)

def doom_selected():
    """ Plays random DOOM intro when difficulty is selected """

    x = random.randint(1,3)

    if x == 1:
        winsound.PlaySound('Do as I choose.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(7)

    elif x == 2:
        winsound.PlaySound('To face doom.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(6)

    elif x == 3:
        winsound.PlaySound('Magneto.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(5)
      
def galactus_selected():

    """ Plays random Galactus intro when difficulty is selected """

    x = random.randint(1,3)

    if x == 1:
        winsound.PlaySound('Force of nature.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(4)

    elif x == 2:
        winsound.PlaySound('Ant vs sun.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(6)

    elif x == 3:
        winsound.PlaySound('Training for galactus.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(6)



def modok_wins():
    """ Plays random MODOK taunt when player loses on easy difficulty """

    x = random.randint(1,4)

    if x == 1:
        winsound.PlaySound('Feeble minded fool modok.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(4)

    elif x == 2:
        winsound.PlaySound('Defeat is not in my vocabulary.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(4)

    elif x == 3:
        winsound.PlaySound('You are no match modok.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(4)

    elif x == 4:
        winsound.PlaySound('Maniacle Laugh .wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(5)

def modok_loses():
    """ Plays random MODOK lamentation when player wins on easy difficulty """

    x = random.randint(1,2)
    if x == 1:
        winsound.PlaySound('Mind over matter modok.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(5)
    elif x == 2:
        winsound.PlaySound('This isnt over modok.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(3)

def doom_wins():
    """ Plays random Doom taunt when player loses on medium difficulty """

    x = random.randint(1,4)
    
    if x == 1:
        winsound.PlaySound('This game is over.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(5)

    elif x == 2:
        winsound.PlaySound("Child's play doom.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(4)

    elif x == 3:
        winsound.PlaySound('Earths mightiest doom.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(4)

    elif x == 4:
        winsound.PlaySound('No one defeats doom.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(4)
    


def doom_loses():
    """ Plays random DOOM lamentation when player wins on medium difficulty """

    x = random.randint(1,3)

    if x == 1:
        winsound.PlaySound('Failure is beneath doom.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(4)

    elif x == 2:
        winsound.PlaySound('This is impossible doom.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(4)

    elif x == 3:
        winsound.PlaySound('You have angered doom.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(4)

def galactus_wins():
    """ Plays random Galactus taunt when player loses on hard difficulty """

    x = random.randint(1,4)

    if x == 1:
        winsound.PlaySound('Accept your fate galactus.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(4)

    elif x == 2:
        winsound.PlaySound('What does EMH mean.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(7)

    elif x == 3:
        winsound.PlaySound('You haved doomed your world.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(9)

    elif x ==4:
        winsound.PlaySound('Begin consumption galactus.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(8)

def galactus_loses():
    """ Plays random Galactus lamentation when player wins on hard difficulty """

    x = random.randint(1,3)
    
    if x == 1:
        winsound.PlaySound('Impossible galactus.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(3)

    elif x == 2:
        winsound.PlaySound('Rue this day galactus.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(4)

    elif x == 3:
        winsound.PlaySound('Squash you galactus.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
        time.sleep(6)



def rand_num_generator():
    """ Generates a sequence of numbers between 0 and 7 using API. """

    my_list = [0,0,0,0]
    
    response = requests.get('https://www.random.org/integers/?num=4&min=0&max=7&col=1&base=10&format=plain&rnd=new')
    data = response.text
    new_data=data.replace("\n", "")

    for i in range(4):
        my_list[i] = int(new_data[i])

    print(my_list)

    return my_list

def player_input():
    """ Recieves player input as a sequence """

    this_list = ['','','','']

    while True:

        inp1 = input("Please input the first number in your sequence (0-7): " )

        if not inp1.isdigit():

            print("Only numbers 0-7 are valid")    

            continue

        this_list[0] = int(inp1)

        if this_list[0] > 7 or this_list[0] < 0:

            print("Only numbers 0-7 are valid")

            continue

        break
    

    while True:

        inp2 = input("Please input the second number in your sequence (0-7): ")

        if not inp2.isdigit():

            print("Only numbers 0-7 are valid")    

            continue

        this_list[1] = int(inp2)

        if this_list[1] > 7 or this_list[1] < 0:

            print("Only numbers 0-7 are valid")

            continue

        break
        

    while True:

        inp3 = input("Please input the third number in your sequence (0-7): " )

        if not inp3.isdigit():

            print("Only numbers 0-7 are valid")    

            continue

        this_list[2] = int(inp3)

        if this_list[2] > 7 or this_list[2] < 0:

            print("Only numbers 0-7 are valid")

            continue

        break
       
    while True:   

        inp4 = input("Please input the fourth number in your sequence (0-7): ")

        if not inp4.isdigit():

            print("Only numbers 0-7 are valid")    

            continue

        this_list[3] = int(inp4)

        if this_list[3] > 7 or this_list[3] < 0:

            print("Only numbers 0-7 are valid")

            continue

        break
    
    print("You said: ", this_list)
    return this_list


def guess_check():
    """ Assesses player guess and returns feedback """

    correct = 0
    right = 0

    if player_list != newnumlist:

        if player_list[0] == newnumlist[0]:
            correct += 1
        if player_list[1] == newnumlist[1]:
            correct += 1
        if player_list[2] == newnumlist[2]:
            correct += 1
        if player_list[3] == newnumlist[3]:
            correct += 1


        if player_list[0] in newnumlist and player_list[0] != newnumlist[0]:
            right += 1
        if player_list[1] in newnumlist and player_list[1] != newnumlist[1]:
            right += 1
        if player_list[2] in newnumlist and player_list[2] != newnumlist[2]:
            right += 1
        if player_list[3] in newnumlist and player_list[3] != newnumlist[3]:
            right += 1

        
        if right == 1: 

            print(str(right) + " correct number")

        elif right > 1 or right == 0:

            print(str(right) + " correct numbers")

        if correct == 1: 

            print(str(correct) + " correct location")

        elif correct > 1 or correct == 0 :

            print(str(correct) + " correct locations")

    return True
            


def play_again():
    """Asks player to play again."""

    cont = ""
    
    while cont not in "Y" or "N":
        
        cont = input("Do you want to play again? [Y/N]:  ")

        if cont == "Y":

            return True

        elif cont == "N":

            return False

EZ = 120
MD = 90
HD = 60

if __name__ == "__main__":
    # Game Start
    game_on = ''
    guesses = 10

    while True:

        #Music plays while game runs simoultaneously 
        winsound.PlaySound('07. Player Select.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)

        print("Welcome to Marvel Mastermind")

        play_game = input("Ready to play? y or n: ")

        if play_game == 'y' or play_game == 'Y':

            game_on = True

        elif play_game == 'n' or play_game == 'N':

            game_on = False  

        else:
            print("Please input y or n") 
            continue

        if game_on == True:

            dif = input("What level of villainy are you prepared to face? M.O.D.O.K(ez), Dr.Doom(md), Galactus(hd): ")
            if dif == "ez":
                #Timer is set according to difficulty
                t = EZ
                modok_selected()
                winsound.PlaySound('509 - Theme of M.O.D.O.K.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)       
         
            elif dif == "md":
                t = MD
                doom_selected()
                winsound.PlaySound('213 - Arcade Ending -Type A-.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
                
            elif dif == "hd":
                t = HD
                galactus_selected()
                winsound.PlaySound('211 - Theme of Galactus _The Fate of Two Worlds_.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)
                
            else:
                print("Not a valid input")
                continue
           
            print(str(guesses) + " guesses left")
        
            
            run_once = 0
            #Clears terminal of previous clutter at game start.
            os.system('cls')

            while 1:
                #Prevents sequence and beggining of game text from being duplicated with each guess.
                if run_once == 0:

                    if dif == "ez":
                        print("You have " + str(t) + " seconds before M.O.D.O.K Destroys New York City with his new device! \nhack his device and stop him before time runs out!")
                    
                    if dif == "md":
                        print("You have " + str(t) + " seconds before Dr. Doom accesses U.S. missile codes! \nhack into the U.S. system before he can and lock him out!")

                    if dif == "hd":
                        print("You have " + str(t) + " seconds before Galactus consumes the earth! \nhack into his ship and send him back into space before earth is destroyed!")

                    newnumlist = rand_num_generator() 

                    run_once = 1

                if run_once == 1:
                    # get starting time
                    start_time = time.time()

                    # player makes guesses
                    player_list = player_input()

                    # end time
                    end_time = time.time()
                    
                    # number of seconds took to guess
                    time_to_guess = end_time - start_time

                    # subtract time_to_guess from total time, t
                    newtime = t - time_to_guess
                    t = newtime

                    # Conditions are checked before player gives next guess to prevent bugs.
                    if newtime <= 0:

                        print("Too late. You've run out of time!")
                        print("You Lose!")

                        if dif == "ez":

                            modok_wins()

                        if dif == "md":

                            doom_wins()

                        if dif == "hd":

                            galactus_wins()

                        winsound.PlaySound('114 - Game Over.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)

                        time.sleep(5)

                        if play_again():

                            winsound.PlaySound('112 - Retry.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)

                            time.sleep(7)

                            break

                        else:
                            exit()

                    if player_list == newnumlist:

                        if dif == "ez":

                           modok_loses()

                        if dif == "md":

                           doom_loses()

                        if dif == "hd":

                            galactus_loses()

                        print("You Win!")

                        winsound.PlaySound('322 - Victory _Ultimate - Normal_.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)

                        time.sleep(5)

                        if play_again():

                            winsound.PlaySound('112 - Retry.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)

                            time.sleep(7)

                            break

                        else:

                            exit()

                    if player_list != newnumlist and guesses == 0:

                        print("Out of guesses")
                        print("You lose!")
                        print("The secret passcode was " + str(newnumlist) )

                        if dif == "ez":

                            modok_wins()

                        if dif == "md":

                            doom_wins() 

                        if dif == "hd":

                            galactus_wins()

                        winsound.PlaySound('114 - Game Over.wav', winsound.SND_ASYNC | winsound.SND_ALIAS)

                        time.sleep(5)

                        if play_again():

                            winsound.PlaySound('112 - Retry.wav', winsound.SND_ASYNC | winsound.SND_ALIAS) 

                            time.sleep(7)

                            break

                        else:
                            exit()

                    guess_check()


                    guesses -= 1

                    print(str(guesses) + " guesses left")
                    print(str(newtime) + " seconds left")
                    
        
        else:
            exit()
