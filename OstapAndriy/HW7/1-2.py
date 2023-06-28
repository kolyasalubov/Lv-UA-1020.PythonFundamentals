import math
def calculate_rectangle_area(length, width):
    return length * width
def calculate_triangle_area(base, height):
    return 0.5 * base * height
def calculate_circle_area(radius):
    return math.pi * radius ** 2
def main():
    print("Якої фігури потрібно обчислити площу:")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")
    choice = input("Оберіть свійваріант (1-3): ")
    if choice == "1":
        length = float(input("Уведіть довжину прямокутника: "))
        width = float(input("Уведіть ширину прямокутника: "))
        area = calculate_rectangle_area(length, width)
        print("Площа прямокутника:", area)
    elif choice == "2":
        base = float(input("Уведіть основу трикутника: "))
        height = float(input("Уведіть висоту трикутника: "))
        area = calculate_triangle_area(base, height)
        print("Площа трикутника:", area)
    elif choice == "3":
        radius = float(input("Уведіть радіус кола: "))
        area = calculate_circle_area(radius)
        print("Площа кола:", round(area, 2))
    else:
        print("Неіснуюча функція!")
if __name__ == "__main__":
    main()