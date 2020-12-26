# This program takes a series of times in which a runner has completed their training
# calculates the average and presents the result to the user.

runs = 0
runTime = 0.0

while True:
    answer = input("Enter 10 km run time: ")

    if not answer:
        average = runTime / runs
        print(f"Average of {average: .2f} over {runs} runs.")
        break
    else:
        try:
            floatAnswer = float(answer)
        except ValueError as e:
            print("Hey! That's not a valid number!")
            continue

        runs += 1
        runTime += floatAnswer
