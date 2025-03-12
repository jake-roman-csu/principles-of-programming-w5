def calculate_points(books):
    if books < 0:
        raise ValueError("Number of books cannot be negative")

    if books == 0 or books == 1:
        return 0
    elif books >= 8:
        return 60
    elif books >= 6:
        return 30
    elif books >= 4:
        return 15
    elif books >= 2:
        return 5


def main():
    try:
        # Get input from user
        books_purchased = int(input("Enter the number of books purchased this month: "))

        # Calculate and display points
        points = calculate_points(books_purchased)
        print(f"Points awarded: {points}")

    except ValueError as e:
        # Handle specific ValueError from our function
        if str(e) == "Number of books cannot be negative":
            print("Error: Number of books cannot be negative.")
        else:
            # Handle invalid input (non-integer values)
            print("Error: Please enter a valid whole number.")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()