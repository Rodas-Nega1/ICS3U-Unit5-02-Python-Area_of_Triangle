# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Oct 2021
# This program asks the user for height and base for area of triangle


def area_of_triangle(height, base):
    # calculate area of triangle

    # process & output
    area = height * base / 2

    print("")
    print("The area of the triangle is {0} cm².".format(area))


def main():
    # this function calls the precedent function

    # input
    height_given = input("Enter your height (cm): ")
    base_given = input("Enter your base (cm): ")

    try:
        height_given_int = int(height_given)
        base_given_int = int(base_given)
        area_of_triangle(height_given_int, base_given_int)

    except Exception:
        print("")
        print("That is an invalid integer.")

    finally:
        # call function
        print("\nDone.")


if __name__ == "__main__":
    main()
