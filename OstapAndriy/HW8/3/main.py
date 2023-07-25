# main.py
import calculate_area

def main():
    print("Оберіть фігуру, площу якої ви хочете обчислити:")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")

    choice = int(input("Введіть ваш вибір (1/2/3): "))

    if choice == 1:
        a = float(input("Введіть довжину прямокутника: "))
        b = float(input("Введіть ширину прямокутника: "))
        result = calculate_area.rectangle_area(a, b)
        print(f"Площа прямокутника: {result}")
    elif choice == 2:
        base = float(input("Введіть основу трикутника: "))
        height = float(input("Введіть висоту трикутника: "))
        result = calculate_area.triangle_area(base, height)
        print(f"Площа трикутника: {result}")
    elif choice == 3:
        radius = float(input("Введіть радіус кола: "))
        result = calculate_area.circle_area(radius)
        print(f"Площа кола: {result}")
    else:
        print("Недійсний вибір. Будь ласка, оберіть правильну опцію.")

if __name__ == "__main__":
    main()
