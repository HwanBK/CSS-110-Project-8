# CSC 110
# Project 8 - Texas River Pollution Data
# Hwansu Kim (Billy)
# Reads text file containing river pollution data and writes a summary text file based on user
# input.


# Collects user's river data selections as inputs.
def getUserInput():
    userRiverInput = ""
    while userRiverInput == "":
        userRiverInput = input("Which River? ")

    validMonthInput = False
    while not validMonthInput:
        try:
            userMonthInput = int(input("Which month (e.g., 1 for January)? "))
        except ValueError:
            pass
        else:
            if userMonthInput in range(1, 13):
                validMonthInput = True

    print("\nAvailable pollutants: ")
    print("1. Arsenic\n2. Lead\n3. Fertilizer\n4. Pesticides")

    validPollutantInput = False
    while not validPollutantInput:
        try:
            userPollutantInput = int(input("Which pollutant? "))
        except ValueError:
            pass
        else:
            if userPollutantInput in range(1, 5):
                validPollutantInput = True

    return userRiverInput, userMonthInput, userPollutantInput


# Returns the pollutant's name based on number.
def assignPollutant(pollutantNumber):
    if pollutantNumber == 1:
        pollutantType = "Arsenic"

    elif pollutantNumber == 2:
        pollutantType = "Lead"

    elif pollutantNumber == 3:
        pollutantType = "Fertilizer"

    elif pollutantNumber == 4:
        pollutantType = "Pesticides"

    return pollutantType


# Processes the river file and returns pertinent information.
def processRiverFile(riverFile, targetRiver, targetMonth, targetPollutant):
    totalReadings = 0
    pollutantAmount = 0
    lowestAmount = 999999
    highestAmount = 0
    rowsProcessed = 0
    newRiverFile = riverFile.readlines()[1:]

    pastTargetRiver = False
    while not pastTargetRiver:
        for line in newRiverFile:
            dataLine = line.split(",")
            riverName = dataLine[0]
            lineMonth = dataLine[1]
            arsenicAmount = float(dataLine[3])
            leadAmount = float(dataLine[4])
            fertilizerAmount = float(dataLine[5])
            pesticideAmount = float(dataLine[6])

            if riverName <= targetRiver:
                if riverName == targetRiver:
                    if lineMonth == str(targetMonth):
                        if targetPollutant == 1:
                            pollutantAmount += arsenicAmount
                            rowsProcessed += 1
                            if arsenicAmount > 0:
                                totalReadings += 1

                            if arsenicAmount < lowestAmount:
                                lowestAmount = arsenicAmount

                            if arsenicAmount > highestAmount:
                                highestAmount = arsenicAmount

                        elif targetPollutant == 2:
                            pollutantAmount += leadAmount
                            rowsProcessed += 1
                            if leadAmount > 0:
                                totalReadings += 1

                            if leadAmount < lowestAmount:
                                lowestAmount = leadAmount

                            if leadAmount > highestAmount:
                                highestAmount = leadAmount

                        elif targetPollutant == 3:
                            pollutantAmount += fertilizerAmount
                            rowsProcessed += 1
                            if fertilizerAmount > 0:
                                totalReadings += 1

                            if fertilizerAmount < lowestAmount:
                                lowestAmount = fertilizerAmount

                            if fertilizerAmount > highestAmount:
                                highestAmount = fertilizerAmount

                        elif targetPollutant == 4:
                            pollutantAmount += pesticideAmount
                            rowsProcessed += 1
                            if pesticideAmount > 0:
                                totalReadings += 1

                            if pesticideAmount < lowestAmount:
                                lowestAmount = pesticideAmount

                            if pesticideAmount > highestAmount:
                                highestAmount = pesticideAmount
            else:
                pastTargetRiver = True

    return totalReadings, pollutantAmount, lowestAmount, highestAmount, rowsProcessed


# Calculates the average amount of pollutants.
def calcPollutantAverage(numOfReadings, pollutantAmount):
    if numOfReadings > 0:
        calculatedAverage = pollutantAmount / numOfReadings
    else:
        calculatedAverage = 0

    roundedAverage = round(calculatedAverage, 3)

    return roundedAverage


# Reads data file and writes summary file.
def main():
    riverDataFile = open("RiverPollutionData.txt", "r")
    summaryFile = open("PollutionSummary.txt", "w")

    riverName, monthNum, pollutantNum = getUserInput()
    pollutantName = assignPollutant(pollutantNum)

    readingCount, pollutantTotal, lowestReading, highestReading, numOfRows = \
        processRiverFile(riverDataFile, riverName, monthNum, pollutantNum)

    pollutantAverage = calcPollutantAverage(readingCount, pollutantTotal)

    summaryFile.write("Data for river: " + riverName + "\n")
    summaryFile.write("Data for month: " + str(monthNum) + "\n")
    summaryFile.write("Data for pollutant: " + str(pollutantName) + "\n\n")

    summaryFile.write("Number of readings  : " + str(readingCount) + "\n")
    summaryFile.write("Average of readings : " + format(pollutantAverage, ".3f") + "\n")
    summaryFile.write("Lowest reading      : " + format(lowestReading, ".3f") + "\n")
    summaryFile.write("Highest reading     : " + format(highestReading, ".3f") + "\n")

    print("\nProcessing of", numOfRows, "rows is complete. See summary file for results.")

    riverDataFile.close()
    summaryFile.close()


main()


# SUMMARY
#   I started this project by looking over the project's rubric, as usual, although I spent a lot
# more time analyzing and designing the program myself; since this is the first project where a
# list of function specifications and call hierarchy was not provided. Then, when I began coding,
# I first started with no helper functions and wrote everything in the main function. After
# finishing, and ensuring the project functioned, I felt as if the function was too long; it was
# about 120 lines of code after including line spacing. So, I went back and decided to create and
# implement helper functions, mostly for the sake of making the main function smaller; even if the
# overall program would become longer due to function definitions and returns.
#   Testing was done entirely manually, by comparing output to a copy of RiverPollutionData.txt
# that was kept outside the project's directory, calculations done on a calculator, and by using
# the rubric's example input and output. Initially, I had my output displayed on the IDE,
# before coding the program to write to PollutionSummary.txt, for the sake of testing. Then, after
# coding the program to write the output file, I tested by manually checking PollutionSummary.txt
# each time I ran the program to ensure it was writing/overwriting the correct output. As for
# testing to ensure each value in the output was correct, I either compared the output to the
# copy of RiverPollutionData.txt's data and used a calculator for all sum and average calculations.
# And as far as anything that doesn't work, I would have liked to have given the lowest reading
# value as 0 when the river name input is invalid and doesn't exist in RiverPollutionData.txt, but
# I felt as if coding this as well would have borderline made the processRiverFile function too
# long; and the entire reason I created helper functions was to shorten main, so making one of the
# helper functions as long as main used to be would go against the reason I created helper
# functions to begin with. I think this mostly boils down to me coding a little too inefficiently
# as I more than likely could have written code that results in the same output, but in a more
# condensed way; although, I do remember being told that if we have to choose between clarity
# of code and concise, "smart" code, we should choose clarity and readability.
#   This assignment was actually great in challenging me to design the project myself; prior to
# this project, we essentially had our hands held through the project because so much information
# was provided in regards to what each function should include as well as being provided a call
# hierarchy. This time, if we used helper functions, we had to design our own call hierarchy and
# function definitions. This time around, I had to redesign my program after FINISHING because
# I personally felt as if main was way too long, so next time I want to focus on spending more
# time on the design aspect of programming and get a better understanding and ability to
# estimate how long a program will be, in terms of lines/rows; this way I'll save myself time and
# grief from having to redesign despite having a properly working and functioning program.


# TEST CASES

# userInput Function
#   -userRiverInput
#       -If input is an empty string, the user will be re-prompted to enter the river name input.
#           -This happens indefinitely as long as an empty string is provided.
#       -If a river name, that doesn't exist in the RiverPollutionData.txt file, is provided, then
#        the summary file will result in zero total readings, average, and invalid min and max
#        values.
#           -Although, this isn't too important, since the project's guidelines say we may assume
#            the user will provide correct inputs.
#       -If a valid river name is provided the program will output the correct information in the
#        PollutionSummary.txt file.
#           -Tested with all river names in RiverPollutionData.txt.
#   -userMonthInput
#       -If input is less than 1 (January) or greater than 12 (December), the user will be
#        re-prompted to enter the month input.
#           -Floating-point numbers between 1 and 12 will also re-prompt the user.
#       -All integer inputs between 1 and 12, inclusive, progress the program as intended and
#        provides the correct output in PollutionSummary.txt.
#   -userPollutantInput
#       -If input is less than 1 or greater than 4, the user will be re-prompted to enter an input
#        for the pollutant selection.
#           -Floating-point numbers between 1 and 4 will also re-prompt the user.
#       -If provided a valid integer input of 1 through 4, the program will proceed as intended,
#        assign the correct pollutant name, and provide the correct output in PollutionSummary.txt.

# pollutantType Function
#   -Depending on the return from userPollutantInput, from the userInput function, this function
#    will assign and return the pollutant's name.
#       -It is not possible to get an invalid or incorrect choice, due to the range validation from
#        userPollutantInput.
#       -1 returns "Arsenic"
#       -2 returns "Lead"
#       -3 returns "Fertilizer"
#       -4 returns "Pesticides"

# processRiverFile Function
#   -If returns/arguments from previous function calls are valid the correct output will be provided
#    in PollutionSummary.txt.
#       -Number of readings tested and verified by manually counting correlated rows.
#           -If the reading is 0, then it is counted as there being no readings; i.e. reading count
#            is not incremented.
#       -Total pollutants tested and verified by calculating the sum externally
#           -Used a calculator. Sample test case below for calcPollutantAverage.
#       -Lowest and highest readings verified by manually checking RiverPollutionData.txt.
#           -If an invalid river name is provided, the lowest reading will return as a very high
#            number.
#       -Total rows processed, separate from number of readings, counts all the related rows that
#        are processed.
#           -i.e. if Lampasas River is the target river then it will only count the rows associated
#            with the Lampasas River.
#   -Used the newRiverFile variable and it's contents to skip the first line in the
#    RiverPollutionData.txt file because the first line is just a header.
#       -Did this mostly for the purpose of assigning the indexes of the split string to variables.
#           -Prior to skipping the first line the conversions to float would break the program
#            because everything in the first line is alphabetical.
#   -Loop design for stopping the loop once the target river's data has all been processed only
#    works if the river names in the RiverPollutionData.txt file is sorted in alphabetical order.
#       -Tested to verify the loop stops after the target river is all processed and past that
#        river by using a counter. (Coded this in a test copy of the project file since the project
#        doesn't ask us to display the total number of rows the program had to go through.
#           -When tested with "Blanco River" as the target river, the program ran through 510 rows;
#            Blanco river's final line is on row 511, but I skip the first row in the file, with
#            the newRiverFile = riverFile.readlines()[1:], so the total rows processed ends up as
#            510.

# calcPollutantAverage
#   -Average of readings tested and verified by calculating the average externally
#       -Used a calculator.
#           -Program output average of .083 for Lampasas River during May (5) for pesticides.
#               -Output of average from a graphing calculator was .0833684211
#           -Program output average of 106.087 for Prairie Dog Town Fork Red River during Jan. (1)
#            for lead.
#               -Output of average from a calculator was 106.0869565
#       -Also used the same inputs as the project rubric's example.
#        (Brazos River, Feb, pesticides).
#           -Program's output for average was 0.002 just like the example.
#   -If the number of readings is 0, which also results in a total sum of 0, then 0 is returned
#    as the average through a selection statement.
#       -Without the selection statement, trying to divide by 0 will result in a ZeroDivisionError.

# main Function
#   -Properly reads and closes RiverPollutionData.txt.
#       -Does not overwrite or append RiverPollutionData.txt
#           -Checked using a copy of RiverPollutionData.txt that was outside the project file's
#            directory by comparing.
#   -Properly makes function calls to helper functions.
#   -Properly writes and closes PollutionSummary.txt.
#       -Properly overwrites existing PollutionSummary.txt if the program is ran again.
#   -Properly displays a message informing the user the program has finished and to check the
#    PollutionSummary.txt file for the output.