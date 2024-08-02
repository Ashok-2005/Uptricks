def calculate_loan_details(annual_salary, duration_years=None, emi_amount=None):
    interest_rate = 6.95  # Interest rate in percentage
    max_emi_percentage = 90  # Maximum percentage of annual salary for EMIs
    extended_duration_interest_rate = 0.15  # Additional interest rate for duration > 15 years

    # Calculate maximum loan amount
    max_loan_amount = (annual_salary * max_emi_percentage / 100) / ((1 + interest_rate / 100) ** duration_years)

    if emi_amount is not None:
        # Calculate duration for given EMI
        numerator = annual_salary * max_emi_percentage / 100
        denominator = emi_amount * (1 + interest_rate / 100)
        duration_years = -(1 / 12) * (numerator / denominator - 1)

    elif duration_years is not None:
        # Check if duration is more than 15 years and adjust interest rate
        if duration_years > 15:
            interest_rate += extended_duration_interest_rate

        # Calculate EMI for given duration
        emi_amount = (annual_salary * max_emi_percentage / 100) / (
                (1 - (1 + interest_rate / 100) ** (-duration_years)) / (interest_rate / 100)
        )

    return max_loan_amount, emi_amount, duration_years


# Get user input
annual_salary = float(input("Enter your annual salary: "))
choice = input("Choose input type (duration or emi): ").lower()

if choice == "duration":
    duration_years = float(input("Enter the duration in years: "))
    result = calculate_loan_details(annual_salary, duration_years=duration_years)
    print(f"Maximum Loan Amount: {result[0]:.2f} INR\nEMI: {result[1]:.2f} INR\nDuration: {result[2]:.2f} years")
elif choice == "emi":
    emi_amount = float(input("Enter the desired EMI amount: "))
    result = calculate_loan_details(annual_salary, emi_amount=emi_amount)
    print(f"Maximum Loan Amount: {result[0]:.2f} INR\nEMI: {result[1]:.2f} INR\nDuration: {result[2]:.2f} years")
else:
    print("Invalid choice. Please choose 'duration' or 'emi'.")
