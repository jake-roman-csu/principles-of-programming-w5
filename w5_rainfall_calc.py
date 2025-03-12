def main():
    # Get the number of years from the user with validation
    years = get_valid_integer("Enter the number of years: ", min_value=1)

    total_months = years * 12
    total_rainfall = 0.0

    # Outer loop for each year
    for year in range(1, years + 1):
        print(f"\nYear {year}:")

        # Inner loop for each month in the year
        for month in range(1, 13):
            month_name = get_month_name(month)

            # Get rainfall for this month with validation
            try:
                rainfall = get_valid_float(f"Enter rainfall (in inches) for {month_name}: ", min_value=0)
                total_rainfall += rainfall
            except ValueError as e:
                print(f"Error: {e}")
                # Re-prompt for the same month
                month -= 1
                continue

    # Calculate the average rainfall
    try:
        average_rainfall = total_rainfall / total_months

        # Display results
        print("\nResults:")
        print(f"Total number of months: {total_months}")
        print(f"Total rainfall (inches): {total_rainfall:.2f}")
        print(f"Average monthly rainfall (inches): {average_rainfall:.2f}")
    except ZeroDivisionError:
        print("Error: No valid months were entered.")


def get_valid_integer(prompt, min_value=None, max_value=None):
    """
    Get a valid integer from the user within specified range.
    """
    while True:
        try:
            value = int(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Error: Value must be at least {min_value}.")
                continue

            if max_value is not None and value > max_value:
                print(f"Error: Value must be at most {max_value}.")
                continue

            return value
        except ValueError:
            print("Error: Please enter a valid integer.")


def get_valid_float(prompt, min_value=None, max_value=None):
    """
    Get a valid float from the user within specified range.
    """
    while True:
        try:
            value = float(input(prompt))

            if min_value is not None and value < min_value:
                print(f"Error: Value must be at least {min_value}.")
                continue

            if max_value is not None and value > max_value:
                print(f"Error: Value must be at most {max_value}.")
                continue

            return value
        except ValueError:
            print("Error: Please enter a valid number.")


def get_month_name(month_number):
    """
    Convert month number (1-12) to month name.
    """
    month_names = [
        "January", "February", "March", "April",
        "May", "June", "July", "August",
        "September", "October", "November", "December"
    ]
    return month_names[month_number - 1]


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")