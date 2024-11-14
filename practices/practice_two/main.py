# تمرین شماره 2
# برنامه ای بنویسید از کاربر تعداد روز رو از کاربر بگیرد و در خروجی محاسبه کنید  تعداد روز، چند ماه و چند روز می باشد رو نمایش دهد شرط ماه رو 31 روزه در نظر بگیرید
# از if

def calculate_months_and_days(days):
    # Check if the number of days is negative
    if days < 0:
        return "The number of days cannot be negative."

    # Calculate the number of months and remaining days
    months = days // 31
    remaining_days = days % 31

    # Return the formatted result
    return f"{days} days are equivalent to {months} months and {remaining_days} days."


# Prompt the user to input the number of days
try:
    days = int(input("Enter the number of days: "))
    # Call the function to calculate months and days
    result = calculate_months_and_days(days)
    # Print the result
    print(result)
except ValueError:
    # Handle the case where the input is not a valid integer
    print("Please enter a valid integer.")
