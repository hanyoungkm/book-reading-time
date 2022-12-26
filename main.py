# Declare Constant Integer MAX = 5

# Module main() calls functions and modules
#     Declare String book_name[MAX]
#     Declare Integer book_pages[MAX]
#     Declare Float avg_reading_speed
#     Declare Integer total_read_hour[MAX]
#     Declare Integer total_read_min[MAX]
#     Declare String answer = "yes"
#     Declare Integer num_books = 0
#
#     Call welcome_message()
#     Set average_reading_speed = get_average_reading_speed()
#
#     While String answer = "yes" AND num_books <= MAX - 1:
#           Set book_name[total_books] = get_book_name()
#           Set book_pages[total_books] = get_book_pages()
#
#           Set total_hour[total_books] = calculate_hour(book_pages[num_books], avg_reading_speed)
#           Set total_min[total_books] = calculate_min(book_pages[num_books], avg_reading_speed)
#           Set answer = more_books()
#           Set num_books = num_books + 1
#     End While
#
#     Call output_total_reading_time(book_name, total_hour, total_min, num_books)
#     Call output_end()
# End Module

MAX = 5

def main():
    book_name = [""] * MAX
    book_pages = [0] * MAX
    total_hour = [0] * MAX
    total_min = [0] * MAX
    answer = 'yes'
    num_books = 0  # number of elements in the array

    welcome_message()
    avg_reading_speed = get_avg_reading_speed()

    while answer == 'yes' and num_books <= MAX - 1:
        book_name[num_books] = get_book_name()
        book_pages[num_books] = get_book_pages()

        total_hour[num_books] = calculate_hour(book_pages[num_books], avg_reading_speed)
        total_min[num_books] = calculate_min(book_pages[num_books], avg_reading_speed)
        answer = more_books()
        num_books = num_books + 1

    output_total_reading_time(book_name, total_hour, total_min, num_books)
    output_end()


# Function welcome_message() displays an introduction to the user
#     Display "Welcome to the reading time calculator!"
#     Display "We tell you the time it'll take to finish each book!"
# End Function
def welcome_message():
    print("Welcome to the reading time calculator!")
    print("We tell you the estimate time it'll take to finish each book!")


# Function String get_book_name():
#     Declare String book_name
#     While True
#           Display "What is the name of the book you're reading? "
#           Input String book_name
#           If answer is not a String Then
#                 Display "Please try again."
#           Else
#                 Return book_name
#     End While
# End Function
def get_book_name():
    while True:
        book_name = str(input("\nWhat is the name of the book you're reading? "))
        if book_name == "":
            print("You pressed the Enter key. Please try again")
        else:
            return book_name


# Function Integer get_book_pages() gets the length of the book from user (first input)
#     Declare book_pages
#     Display "How many pages are in your book? "
#     Input Integer book_pages
#     While book_pages <= 0 or book_pages is not integer
#           Display "Invalid input!"
#           Display "How many pages are in your books?"
#           Input Integer book_pages
#     End While
#     Return book_pages
# End Function
def get_book_pages():
    while True:
        try:
            book_pages = int(input("\nHow many pages are in your book? "))
            if book_pages <= 0:
                  print("Enter a positive number!")
            else:
                  return book_pages
        except:
            print("Invalid input. Please enter a positive whole number")


# Function Integer get_avg_reading_speed() gets the average reading speed from user (second input)
#     Declare Integer average_reading_speed
#     Display "How long does it take to finish reading a page? (in seconds)"
#     Input average_reading_speed
#     While avg_reading_speed <= 0 or avg_reading_speed is not integer
#           Display "Invalid input!"
#           Display "How long does it take to finish reading a page? (in seconds)"
#           Input Integer avg_reading_speed
#     End While
#     Return avg_reading_speed
# End Function
def get_avg_reading_speed():
    while True:
        try:
            avg_reading_speed = int(input("\nHow long does it take to finish reading a page? (in seconds): "))
            if avg_reading_speed <= 0:
                print("Must be > 0!")
            else:
                return avg_reading_speed
        except:
            print("Invalid input. Please enter a positive whole number.")


# Function Integer calculate_hour(length, speed) calculates the hour part of total time using both inputs.
#     Declare Integer total_read_sec
#     Declare Float total_read_min
#     Declare Integer total_hour
#
#     total_read_sec = book_pages * avg_reading_speed
#     total_read_min = total_read_sec // int(60)
#     total_hour = int(total_read_min // 60)
#     return total_hour
#
# End Function
def calculate_hour(book_pages, avg_reading_speed):
    total_read_sec = book_pages * avg_reading_speed
    total_read_min = total_read_sec // int(60)
    total_hour = int(total_read_min // 60)
    return total_hour

# Function Integer calculate_min(length, speed) calculates the minutes part of total time using both inputs.
#     Declare Integer total_read_sec
#     Declare Float total_read_min
#     Declare Float total_read_hour
#     Declare Integer total_min
#
#     Import Math
#
#     total_read_sec = book_pages * avg_reading_speed
#     total_read_min = total_read_sec // int(60)
#     total_read_hour = total_read_min / 60
#     total_min = int(math.ceil((total_read_hour % 1) * 60))
#     return total_min
#
# End Function
def calculate_min(book_pages, avg_reading_speed):
    import math
    total_read_sec = book_pages * avg_reading_speed
    total_read_min = total_read_sec // int(60)
    total_read_hour = total_read_min / 60
    total_min = int(math.ceil((total_read_hour % 1) * 60))
    return total_min

# Module output_total_reading_time(book_name, total_hour, total_minute, total_books)
# displays the output and an additional message
# that depends on the total reading time.
#
#     Declare Integer count = 0
#
#     While count < num_books:
#       If total_hour[count] < 1 AND total_min[count] < 1 Then
#           Display "It will take you less than a minute to finish", book_name[count]
#       Else If total_hour[count] < 1 Then
#           Display "It will take you about", total_min[count], "minutes to finish", book_name[count]
#       Else If 1 <= total_hour[count] < 2 Then
#           Display "It will take you about", total_hour[count], "hour and", total_min[count],
#           minutes to finish", book_name[count]
#       Else If total_hour[count] >= 1 and total_min[count] == 0:
#           Display "It will take you about", total_hour[count], "hours to finish", book_name[count])
#       Else
#           Display "It will take you about", total_hour[count], "hours and", total_min[count]
#           "minutes to finish", book_name[count])
#       count = count + 1
#     End While
#
# End Module
def output_total_reading_time(book_name, total_hour, total_min, num_books):
    count = 0

    while count < num_books:
        if total_hour[count] < 1 and total_min[count] < 1:
            print("\nIt will take you less than a minute to finish", book_name[count])
        elif total_hour[count] < 1:
            print("\n It will take you about", total_min[count], "minutes to finish", book_name[count])
        elif 1 <= total_hour[count] < 2:
            print("\n It will take you about", total_hour[count], "hour and",
                  total_min[count], "minutes to finish", book_name[count])
        elif total_hour[count] >= 1 and total_min[count] == 0:
            print("\n It will take you about", total_hour[count], "hours to finish", book_name[count])
        else:
            print("\n It will take you about", total_hour[count], "hours and",
                  total_min[count], "minutes to finish", book_name[count])
        count += 1


# Function String more_books() asks the user for another round of calculation and returns the answer to main()
#     Declare String answer
#     While True
#           Display "Do you have more books to find out the reading time? (yes/no): "
#           Input String answer
#           If answer is not a String Then
#                 Display "Invalid input. Please try again."
#           Else
#                 If answer is "yes" Then
#                       answer = String yes
#                       return answer
#                 Else If answer is "no" Then
#                       answer String no
#                       return answer
#                 Else
#                       Display "Answer in terms of 'yes' or 'no'"
# End Function
def more_books():
    while True:
        try:
            answer = input("\nDo you have more books? (yes/no): ")
            if answer.lower() == "yes":
                answer = str("yes")
                return answer
            elif answer.lower() == "no":
                answer = str("no")
                return answer
            else:
                print("Answer in terms of 'yes' or 'no'")
        except:
            print("\nInvalid input. Please try again.")


# module output_end() ends the program with a goodbye
#     Display "Goodbye!"
def output_end():
    print("\nGoodbye!")


main()
