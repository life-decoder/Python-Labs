def q1():
    a = int(input())
    b = int(input())
    c = int(input())
    sides = sorted([a, b, c])
    if sides[0]**2 + sides[1]**2 == sides[2]**2:
        print(True)
    else:
        print(False)

def q2():
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    num = int(input())
    total = 0
    for i in range(2, num + 1):
        if is_prime(i):
            total += i
    print(total)

def q3():
    def reverse_string(s):
        result = ""
        for char in s:
            result = char + result
        return result
    s = input()
    print(reverse_string(s))

def q4a():
    def is_perfect_square(n):
        if n < 0:
            return False
        root = int(n**0.5)
        return root * root == n
    n = int(input())
    print(is_perfect_square(n))

def q4b():
    def list_perfect_squares(num):
        squares = []
        i = 1
        while len(squares) < num:
            squares.append(i * i)
            i += 1
        for val in squares:
            print(val)
    num = int(input())
    list_perfect_squares(num)

def q5():
    def is_password_strong(password):
        if len(password) < 8:
            return False
        has_digit = False
        has_upper = False
        for char in password:
            if char.isdigit():
                has_digit = True
            if char.isupper():
                has_upper = True
        return has_digit and has_upper
    password = input()
    print(is_password_strong(password))

def q6():
    def is_present(students, name):
        for student in students:
            if student == name:
                return True
        return False
    students = input().split()
    name = input()
    print(is_present(students, name))

def q1_analysis():
    import time
    def linear_algo(num):
        for i in range(num):
            print(end="")

    def quadratic_algo(num):
        for i in range(num):
            for j in range(num):
                print(end="")
                
    num = int(input())
    start = time.time()
    linear_algo(num)
    print("Linear time:", time.time() - start)
    start = time.time()
    quadratic_algo(num)
    print("Quadratic time:", time.time() - start)

def q2a_analysis():
    import time
    import random
    def calculate_total_loop(prices):
        total = 0
        for price in prices:
            total += price
        return total
    def calculate_total_builtin(prices):
        return sum(prices)
    sizes = [10, 1000, 100000]
    for size in sizes:
        prices = [random.uniform(10, 100) for _ in range(size)]
        start = time.time()
        calculate_total_loop(prices)
        loop_time = time.time() - start
        start = time.time()
        calculate_total_builtin(prices)
        builtin_time = time.time() - start
        print(f"Size {size}: Loop = {loop_time}, Built-in = {builtin_time}")

def q2b_analysis():
    print("Recommendation: Use calculate_total_builtin because it is faster.")

def menu():
    print("Select a question to run:")
    print("1.  Right-angle triangle check")
    print("2.  Sum of primes")
    print("3.  Reverse string")
    print("4a. Is perfect square")
    print("4b. List perfect squares")
    print("5.  Is password strong")
    print("6.  Is student present")
    print("7.  Compare linear vs quadratic algorithm")
    print("8.  Compare loop vs built-in sum")
    print("9.  Recommendation for sum function")
    choice = input("Enter choice: ")
    if choice == "1":
        q1()
    elif choice == "2":
        q2()
    elif choice == "3":
        q3()
    elif choice == "4a":
        q4a()
    elif choice == "4b":
        q4b()
    elif choice == "5":
        q5()
    elif choice == "6":
        q6()
    elif choice == "7":
        q1_analysis()
    elif choice == "8":
        q2a_analysis()
    elif choice == "9":
        q2b_analysis()

menu()