def calc_compound_interest(initial, rate, years, balance=0):

    if years == 0:
        # Base case
        return balance
    else:
        # Recursive case
        balance += initial * rate
        return calc_compound_interest(initial, rate, years - 1, balance)


# Collect input from user
initial = float(input("Enter the initial amount: "))
rate = float(input("Enter the interest rate: "))
years = int(input("Enter the number of years: "))

# Calculate and print the final balance
final_balance = calc_compound_interest(initial, rate, years)
print(f"The final balance is: {final_balance}")


def reverse_list(lst):

  if not lst:
    # Base case
    return []
  else:
    # Recursive case
    return [lst[-1]] + reverse_list(lst[:-1])


# Read items from a text file into a list
with open("students.txt") as f:
  items = [line.strip() for line in f]

# Reverse the list
reversed_items = reverse_list(items)

# Print the reversed list
print(reversed_items)


def print_triangle(height, width=1):

  if width >= height:
    # Base case
    return
  else:
    # Recursive case
    print("*" * width)
    print_triangle(height, width + 1)


# Collect input from user
height = int(input("Enter the height of the triangle: "))

# Print the triangle
print(print_triangle)