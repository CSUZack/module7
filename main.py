classRoomNumbers = {
    "CSC101": 3004,
    "CSC102": 4501,
    "CSC103": 6755,
    "NET110": 1244,
    "COM241": 1411
}

classInstructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee"
}

classMeetingTime = {
    "CSC101": "8:00 a.m.",
    "CSC102": "9:00 a.m.",
    "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.",
    "COM241": "1:00 p.m."
}

classNumber = input("Please enter the class number you want details about. \n")

print(f"{classNumber} is taught by Professor {classInstructors[classNumber]} in room {classRoomNumbers[classNumber]} at {classMeetingTime[classNumber]}")