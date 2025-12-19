from dataclasses import dataclass


@dataclass
class RentDetails:
    rent: float
    electricity_units: float
    cost_per_unit: float
    maintenance: float
    number_of_people: int


class RentCalculator:

    @staticmethod
    def calculate_electricity_bill(units, cost_per_unit):
        return units * cost_per_unit

    @staticmethod
    def calculate_total_amount(details: RentDetails):
        electricity_bill = RentCalculator.calculate_electricity_bill(
            details.electricity_units,
            details.cost_per_unit
        )
        total_amount = details.rent + electricity_bill + details.maintenance
        return electricity_bill, total_amount

    @staticmethod
    def calculate_per_person(total_amount, people):
        return total_amount / people


def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a valid positive number.")


def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a valid positive integer.")


def display_summary(details, electricity_bill, total_amount, per_person):
    print("\n====== Rent Summary ======")
    print(f"Base Rent              : ₹{details.rent:.2f}")
    print(f"Electricity Bill       : ₹{electricity_bill:.2f}")
    print(f"Maintenance Charges    : ₹{details.maintenance:.2f}")
    print("--------------------------------")
    print(f"Total Amount           : ₹{total_amount:.2f}")
    print(f"Number of People       : {details.number_of_people}")
    print(f"Amount Per Person      : ₹{per_person:.2f}")
    print("==============================")


def main():
    print("=== Professional Rent Calculator ===")

    rent = get_positive_float("Enter Monthly Rent (₹): ")
    units = get_positive_float("Enter Electricity Units Used: ")
    cost_per_unit = get_positive_float("Enter Cost per Electricity Unit (₹): ")
    maintenance = get_positive_float("Enter Maintenance Charges (₹): ")
    people = get_positive_int("Enter Number of People: ")

    details = RentDetails(
        rent=rent,
        electricity_units=units,
        cost_per_unit=cost_per_unit,
        maintenance=maintenance,
        number_of_people=people
    )

    electricity_bill, total_amount = RentCalculator.calculate_total_amount(details)
    per_person = RentCalculator.calculate_per_person(total_amount, people)

    display_summary(details, electricity_bill, total_amount, per_person)


if __name__ == "__main__":
    main()
