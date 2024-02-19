def get_num_books_purchased():
    num_books = int(input("How many books have you purchased this month: "))
    if num_books < 2:
        points = 0
        return points
    elif num_books < 4 and num_books >= 2:
        points = 5
        return points
    elif num_books < 6 and num_books >= 4:
        points = 15
        return points
    elif num_books < 8 and num_books >= 6:
        points = 30
        return points
    else:
        points = 60
        return points
    
points = get_num_books_purchased()
print(f"You've earned {points} points this month.")