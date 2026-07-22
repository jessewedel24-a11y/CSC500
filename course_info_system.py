"""
CSC500 Module 7 Critical Thinking Assignment
Course Information System

Looks up a course number across three dictionaries (room number,
instructor, meeting time) and displays the results. Handles invalid
course numbers with a friendly error message instead of crashing.
"""

# Dictionaries keyed by course number, as required by the assignment spec.
course_rooms = {
    "CSC101": "3004",
    "CSC102": "4501",
    "CSC103": "6755",
    "NET110": "1244",
    "COM241": "1411",
}

course_instructors = {
    "CSC101": "Haynes",
    "CSC102": "Alvarado",
    "CSC103": "Rich",
    "NET110": "Burke",
    "COM241": "Lee",
}

# Meeting times weren't in the provided data table, so I filled these in
# to satisfy the Step 2 output requirement.
course_meeting_times = {
    "CSC101": "MWF 9:00 AM - 9:50 AM",
    "CSC102": "TR 11:00 AM - 12:15 PM",
    "CSC103": "MWF 1:00 PM - 1:50 PM",
    "NET110": "TR 2:00 PM - 3:15 PM",
    "COM241": "MWF 10:00 AM - 10:50 AM",
}


def get_course_info(course_number, rooms, instructors, meeting_times):
    """Look up a course's room, instructor, and meeting time.

    Parameters:
        course_number (str): the course number to look up, e.g. "CSC101".
        rooms (dict): course number -> room number.
        instructors (dict): course number -> instructor name.
        meeting_times (dict): course number -> meeting time.

    Returns:
        tuple: (room_number, instructor, meeting_time) for the course.

    Raises:
        KeyError: if course_number is not found in the dictionaries.
    """
    if course_number not in rooms:
        raise KeyError(course_number)

    room_number = rooms[course_number]
    instructor = instructors[course_number]
    meeting_time = meeting_times[course_number]
    return room_number, instructor, meeting_time


def display_course_info(course_number, room_number, instructor, meeting_time):
    """Print a course's details in a readable format.

    Parameters:
        course_number (str): the course number being displayed.
        room_number (str): the room number for the course.
        instructor (str): the instructor teaching the course.
        meeting_time (str): the course's meeting time.

    Returns:
        None
    """
    print(f"\nCourse Number: {course_number}")
    print(f"Room Number:   {room_number}")
    print(f"Instructor:    {instructor}")
    print(f"Meeting Time:  {meeting_time}")


def main():
    """Run the course information system.

    Prompts the user for a course number, looks it up across the three
    dictionaries, and displays the result. Shows a friendly error
    message if the course number doesn't exist instead of crashing.

    Returns:
        None
    """
    course_number = input("Enter a course number (e.g., CSC101): ").strip().upper()

    try:
        room_number, instructor, meeting_time = get_course_info(
            course_number, course_rooms, course_instructors, course_meeting_times
        )
        display_course_info(course_number, room_number, instructor, meeting_time)
    except KeyError:
        print(f"\nNo course found with number '{course_number}'. "
              f"Please check the course number and try again.")


if __name__ == "__main__":
    main()
