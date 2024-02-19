def get_rainfall():
    num_years = int(input("Enter number of years: "))
    monthly_rainfall = 0
    total_rainfall = 0
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    i = 1
    while i <= num_years:
        for month in months:
            monthly_rainfall = int(input(f"Enter inches of rainfall for {month} in year {i}: "))
            total_rainfall += monthly_rainfall
        i = i + 1

    return num_years, total_rainfall

def calculate_avg_rainfall(num_years, total_rainfall):
    num_months = num_years * 12
    avg_monthly_rainfall = total_rainfall / num_months
    print(f"The average monthly rainfall is {avg_monthly_rainfall}")

num_years, total_rainfall = get_rainfall()
calculate_avg_rainfall(num_years, total_rainfall)