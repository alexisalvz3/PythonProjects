## This project is to find out how many pages I have to read per week from each class (5) this semester. ##


 # Get input for each classes' first and last pages
 
# Kin_331_firstPage = float(input("What is the first page number for this class? "))
# Kin_331_lastPage = float(input("What is the last page number for this class? "))

Psy_400_firstPage = float(input("What is the first page number for Psy 400? "))
Psy_400_lastPage = float(input("What is the last page number for Psy 400? "))

Psy_452_firstPage = float(input("What is the first page number for Psy 452? "))
Psy_452_lastPage = float(input("What is the last page number for Psy 452? "))

Psy_494_firstPage = float(input("What is the first page number for Psy 494? "))
Psy_494_lastPage = float(input("What is the last page number for Psy 494? "))

Psy_540_firstPage = float(input("What is the first page number for Psy 540? "))
Psy_540_lastPage = float(input("What is the last page number for Psy 540? "))

# variables for each class readings
# Kin_331 = (Kin_331_lastPage - Kin_331_firstPage) / 4
Psy_400 = (Psy_400_lastPage - Psy_400_firstPage) / 5
Psy_452 = (Psy_452_lastPage - Psy_452_firstPage) / 5
Psy_494 = (Psy_494_lastPage - Psy_494_firstPage) / 5
Psy_540 = (Psy_540_lastPage - Psy_540_firstPage) / 5
totalReadings = Psy_400 + Psy_452 + Psy_494 + Psy_540

# print("For Kin 331, you should read " + str(Kin_331) + " pages each day for 5 days this week.")
print("For Psy 400, you should read " + str(Psy_400) + " pages each day for 5 days this week.")
print("For Psy 452, you should read " + str(Psy_452) + " pages each day for 5 days this week.")
print("For Psy 494, you should read " + str(Psy_494) + " pages each day for 5 days this week.")
print("For Psy 540, you should read " + str(Psy_540) + " pages each day for 5 days this week.")

print("You should read " + str(totalReadings) + " each day for 5 days this week.")