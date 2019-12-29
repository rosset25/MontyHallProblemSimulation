
import random
import matplotlib.pyplot as plt

# global variable
repetitions = 1000

# Monty Hall Problem Simulation ------------------------------------

# creating the different scenarios
# car = 1, goat = 0
def creating_scenario():

    # every scenario has 3 doors
    doors = [[0, 0, 0] for i in range(repetitions)]  # all the doors contain goats by default

    for i in range(repetitions):
        position_car = random.randint(0,2)
        doors[i][position_car] = 1                   # put the car in a random door in every scenario

    return doors

# generating results depending on the decision that has been made
def solving_problem(array_of_doors, plot_y_change, plot_y_not_change):

    sum_ch = 0
    sum_not_ch = 0

    decisions = [random.randint(0, 2) for i in range(repetitions)]

    for i in range (len(decisions)):

        if array_of_doors[i][decisions[i]] == 1:    # decisions[i] refers to the chosen door in first place
            sum_not_ch += 1
        else:                                       # if the prize is not in the chosen door, then add +1 when changing the door
            sum_ch += 1

        plot_y_change.append(sum_ch)
        plot_y_not_change.append(sum_not_ch)
        print("Change: {0}, Not change: {1}".format(sum_ch,sum_not_ch))

    return sum_ch, sum_not_ch

# to plot the results (graph)
def plot_results(plot_x, plot_y_change, plot_y_not_change):

    # plotting the blue line
    plt.plot(plot_x, plot_y_change, label = "change the door")

    # plotting the orange line
    plt.plot(plot_x, plot_y_not_change, label = "not change the door")

    # naming the x axis and y axis, add a title
    plt.xlabel('scenarios')
    plt.ylabel('wins')
    plt.title('Contest results')

    plt.legend()
    plt.show()

# to plot the final result percentages
def plot_pie_chart(result_change, result_not_change):

    # defining labels
    results = ['change', 'not change']

    # portion covered by each label
    slices = [result_change, result_not_change]

    # plotting the pie chart
    plt.pie(slices, labels = results, autopct = '%1.2f%%')

    plt.legend()
    plt.tight_layout()
    plt.axis('equal')

    # showing the plot
    plt.show()

# Main Program ------------------------------------------
if __name__ == "__main__":

    array_of_doors = creating_scenario()

    # uncomment these lines to show the scenario
    #for i in range(repetitions):
    #    print(array_of_doors[i])

    plot_x = [i for i in range(repetitions)]    # creating axis x
    plot_y_change = []                          # creating axis y for results when it changes the chosen door
    plot_y_not_change = []                      # creating axis y for results when it does not change the chosen door

    result_change, result_not_change = solving_problem(array_of_doors, plot_y_change, plot_y_not_change)

    # creating percentages
    per_result_change = round(result_change*100/repetitions, 2)
    per_result_not_change = round(result_not_change*100/repetitions, 2)

    # plotting results on a graph
    plot_results(plot_x, plot_y_change, plot_y_not_change)

    print("Percentages: change = {0}%, not change = {1}%".format(per_result_change,per_result_not_change))

    # plotting final results on a pie-chart
    plot_pie_chart(result_change, result_not_change)
