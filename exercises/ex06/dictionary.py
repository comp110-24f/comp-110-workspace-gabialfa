"""Dictionary Exercise"""

__author__ = "740736935"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    og_keys: list[str] = []
    inverted: dict[str, str] = {}
    for key in dictionary:
        # Save original key values
        og_keys.append(key)
        # Error if keys repeat
        # func here
        # raise KeyError("Keys must be unique -- No repeats allowed!")

        # Reassign values to become keys
        new_key: str = dictionary[key]
        # print(new_key) FOR TESTING
        new_key = dictionary[key]
        # print(new_key) FOR TESTING
        # Reassign keys to values
        new_value: str = key
        # print(new_value) FOR TESTING
        new_value = key
        # print(new_value) FOR TESTING
        # Push into new inverted dict
        inverted[new_key] = new_value

    return inverted


def favorite_color(names_and_colors: dict[str, str]) -> str:
    fav_color_tally: dict[str, int] = {}
    name: str = ""
    for name in names_and_colors:
        color = names_and_colors[name]
        if color not in fav_color_tally:
            # Add new color to fav_color_tally on first instance
            fav_color_tally[color] = 1
        else:  # Color is already in fav_color_tally, so just add to existing count
            fav_color_tally[names_and_colors[name]] += 1
        print(fav_color_tally[name])
    return name
    # Add instance when max counts are equal


# TESTING
# print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))


def count(input: list[str]) -> dict[str, int]:
    # Each key is a unique value from list and each value is the count
    # of occurances of that value in input list
    values: dict[str, int] = {}
    for value in input:
        if value in values:
            values[value] += 1
        else:
            values[value] = 1
    return values


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    # Each key is a unique letter and each value is a list of the words
    # That begin with that letter
    alphabetized: dict[str, list[str]] = {}
    for word in words:
        # first letter sabed
        letter: str = word[0].lower()
        if letter not in alphabetized:
            # Create empty list first time letter occurs
            alphabetized[letter] = []
        alphabetized[letter].append(word)
    return alphabetized


# FOR TESTING
# print(alphabetizer(["cat", "apple", "boy", "angry", "bad", "car"]))


def update_attendance(
    attendance_log: dict[str, list[str]], day: str, student: str
) -> None:
    # Mutate attendance log to reflect neq info from days and students
    # Attendance log with days and students in attendance
    updated_attendance_log = {}
    for day in attendance_log:
        if day not in updated_attendance_log:
            added_day: list[str] = []
            updated_attendance_log[day] = added_day
        if student not in attendance_log:
            updated_attendance_log[day].append(student)
        attendance_log = updated_attendance_log


attendance_log: dict = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
# update_attendance(attendance_log, "Tuesday", "Vrinda")
