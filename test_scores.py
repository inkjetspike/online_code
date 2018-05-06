# Display opening message and boarder
def display():
    message = "Welcome this is a test score program"
    boarder = "*"
    line = boarder * len(message)
    print(message)
    print("To exit the program enter 999")
    print(line)

# Take the score input


def score_input():
    score_total = 0
    score_counter = 0  # initiate important values
    key = "y"
    while key.lower == 'y':
        score = float(input("Enter your scores here:"))
        if score >= 0 and score <= 100:  # input valudation
            score_total += score
            score_counter += 1
            key = str(input("Would you like to continue? (y or n)"))
        elif score == 999:
            key == "n"
        else:
            print("Error score must be between 0 and 100.")
    return (score_counter, score_total)
# Display the average scores


def print_scores(score_total, score_counter):
    score_average = round(score_total / score_counter)
    print(score_average)

# call the functions of the program


def main():
    display()
    score_input()
    #print_scores()

# make sure test_scores can be run from the terminal
if __name__ == "__main__":
    main()
