def get_course():
    course = str(input("Enter a course number to view the room number, instructor, and lecture time:\nCSC101\nCSC102\nCSC103\nNET110\nCOM241\n>>>")).upper()
    return course

def output_info_by_course(course):
    course_room_num_dict = {
        'CSC101': '3004',
        'CSC102': '4501',
        'CSC103': '6755',
        'NET110': '1244',
        'COM241': '1411',
    }

    course_instructor_dict = {
        'CSC101': 'Haynes',
        'CSC102': 'Alvarado',
        'CSC103': 'Rich',
        'NET110': 'Burke',
        'COM241': 'Lee',
    }

    course_time_dict = {
        'CSC101': '8:00 a.m.',
        'CSC102': '9:00 a.m.',
        'CSC103': '10:00 a.m.',
        'NET110': '11:00 a.m.',
        'COM241': '1:00 p.m.',
    }

    room_num = course_room_num_dict[course]
    instructor = course_instructor_dict[course]
    time = course_time_dict[course]

    print(f"For course {course}, your room number is {room_num} with instructor {instructor} at {time}")

def main():
    course = get_course()
    try:
        output_info_by_course(course)
    except:
        print("An invalid course was entered.")

main()

