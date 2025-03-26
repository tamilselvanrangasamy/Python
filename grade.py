def calculate_grade(marks):
    match marks:
        case marks if 90<=marks<=100:
            print('A')
        case marks if 80<=marks<=89:
            print('B')
        case marks if 70<=marks<=79:
            print('C')
        case marks if 60<=marks<=69:
            print('D')
        case marks if 0<=marks<60:
            print('F')
        case _:
            print("Enter value from 1 to 100")

marks=int(input("Enter your mark: "))
calculate_grade(marks)
