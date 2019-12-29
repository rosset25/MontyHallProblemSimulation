
import random


# Monty Hall Problem Simulation ------------------------------------

# creation of the scenario
def creating_scenario(repetitions):

    doors = [[0,0,0] for i in range(repetitions)]

    for i in range(repetitions):
        position_car = random.randint(0,2)
        doors[i][position_car] = 1

    return doors

#generating results depending on the decision that has been made
def solving_problem(array_of_doors, repetitions):

    sum_ch = 0
    sum_not_ch = 0

    decisions = [random.randint(0,2) for i in range(repetitions)]

    for i in range (len(decisions)):

        if array_of_doors[i][decisions[i]] == 1:    #decisions[i] refers to the chosen door
            sum_not_ch +=1
        else:                                       #if the prize is not in the chosen door, then add +1 when changing the door
            sum_ch +=1

        #print("Change: {0}, Not change: {1}".format(sum_ch,sum_not_ch))

    return sum_ch, sum_not_ch


# Main Program ------------------------------------------
if __name__ == "__main__":

    repetitions = 1000
    array_of_doors = creating_scenario(repetitions)

    #for i in range(repetitions):
    #    print(array_of_doors[i])

    result_change, result_not_change = solving_problem(array_of_doors, repetitions)

    per_result_change = round(result_change*100/repetitions, 2)
    per_result_not_change = round(result_not_change*100/repetitions,2)

    print("Percentages: change = {0}%, not change = {1}%".format(per_result_change,per_result_not_change))
