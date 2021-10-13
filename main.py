import math


# exercise 11
def get_leap_years(start: int, end: int):
    years = []

    for i in range(start + 1, end):
        if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
            years.append(i)

    return years


def test_get_leap_years():
    years = get_leap_years(1900, 2021)

    assert len(years) == 30
    assert years[len(years) - 1] == 2020


# exercise 12
def get_perfect_squares(start: int, end: int):
    perfect_squares = []

    for i in range(start, end+1):
        r = math.sqrt(i)
        if i % r == 0:
            perfect_squares.append(i)

    return perfect_squares


def test_get_perfect_squares():
    squares = get_perfect_squares(1, 20)

    assert squares[0] == 1
    assert squares[1] == 4
    assert squares[2] == 9
    assert squares[3] == 16


# exercise 8
def get_base_2(n: str):
    number = int(n)

    numbers = []
    while number != 0:
        numbers.append(number % 2)
        number = number // 2
    numbers.reverse()

    number_base_2 = ""
    for i in numbers:
        number_base_2 += str(i)

    return number_base_2


def test_get_base_2():
    number = get_base_2("25")

    assert number == "11001"


def menu():
    return "1. Afișează toți anii bisecți între doi ani dați (inclusiv anii dați).\n" \
           "2. Afișează toate pătratele perfecte dintr-un interval închis dat. \n" \
           "3. Teste 1 + 2\n" \
           "4. Transformă un număr dat din baza 10 în baza 2. Numărul se dă în baza 10.\n" \
           "5. Test 4\n" \
           "0. Stop.\n"


def main():
    ok = 1

    while ok == 1:
        print(menu())

        choice = int(input("choice = "))

        if choice == 1:
            start = int(input("start = "))
            end = int(input("end = "))

            years = get_leap_years(start, end)
            for year in years:
                print(year)

        elif choice == 2:
            start = int(input("start = "))
            end = int(input("end = "))

            perfect_squares = get_perfect_squares(start, end)
            for ps in perfect_squares:
                print(ps)

        elif choice == 3:
            test_get_perfect_squares()
            test_get_leap_years()

            print("The tests run!\n")

        elif choice == 4:
            number = input("number = ")
            print("The number in base 2 is " + get_base_2(number) + "\n")

        elif choice == 5:
            test_get_base_2()
            print("The test run!\n")

        else:
            ok = 0


main()