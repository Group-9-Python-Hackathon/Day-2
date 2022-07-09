
print("********Welcome to the Book Club Points Serendipity Booksellers**********")
# prompt for number of books purchased
number_of_books_purchased = int(
    input("Enter the number of books you purchased: "))

# if number of books are zero
if number_of_books_purchased == 0:
    print("We are Sorry You have not earned any points")

# if number of books are 1
elif number_of_books_purchased <= 1:
    print("Good You have earned 6 points")

# if number of books are 2
elif number_of_books_purchased <= 2:
    print("Very Good You have earned 16 points")

# if number of books are 3
elif number_of_books_purchased <= 3:
    print("Wonderful You have earned 32 points")

# if number of books greater than or equals 4
else:
    print("Congratulations You have earned 60 points")
