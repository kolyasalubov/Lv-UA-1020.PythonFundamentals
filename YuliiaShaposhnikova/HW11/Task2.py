def day_of_week():
    weekdays = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    try:
        number = int(input("Enter the day of the week number: "))
        if number <= 7:
            for key in weekdays.keys():
                if number == key:
                    return weekdays.get(key)
        else:
            return "We have only 7 days a week"
    except ValueError:
        return "You did not enter a number "



