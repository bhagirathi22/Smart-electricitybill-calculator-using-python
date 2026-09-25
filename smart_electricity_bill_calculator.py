def get_customer_details():
    """Get and validate the customer's basic details."""
    customer_name = input("Enter customer name: ").strip()
    customer_id = input("Enter customer ID: ").strip()

    while True:
        units_text = input("Enter electricity units consumed: ").strip()
        try:
            units_consumed = int(units_text)
            if units_consumed < 0:
                print("Units consumed cannot be negative. Please try again.")
            else:
                return customer_name, customer_id, units_consumed
        except ValueError:
            print("Please enter a whole number for units consumed.")


def Calculate_bill(units_consumed):
    """Calculate energy charge, service charge, and final bill amount."""
    if units_consumed <= 100:
        energy_charge = units_consumed * 2.0
    elif units_consumed <= 200:
        energy_charge = (100 * 2.0) + ((units_consumed - 100) * 4.0)
    elif units_consumed <= 500:
        energy_charge = (100 * 2.0) + (100 * 4.0) + ((units_consumed - 200) * 6.0)
    else:
        energy_charge = (100 * 2.0) + (100 * 4.0) + (300 * 6.0) + ((units_consumed - 500) * 8.0)

    service_charge = 100.0
    final_amount = energy_charge + service_charge
    return energy_charge, service_charge, final_amount


def Display_bill(customer_name, customer_id, units_consumed, energy_charge, service_charge, final_amount):
    """Display the customer's electricity bill."""
    print("\n" + "=" * 42)
    print("          SMART ELECTRICITY BILL")
    print("=" * 42)
    print(f"Customer name   : {customer_name}")
    print(f"Customer ID     : {customer_id}")
    print(f"Units consumed  : {units_consumed}")
    print("-" * 42)
    print(f"Energy charge   : ₹{energy_charge:.2f}")
    print(f"Service charge  : ₹{service_charge:.2f}")
    print("-" * 42)
    print(f"Final amount    : ₹{final_amount:.2f}")
    print("=" * 42)


def main():
    customer_name, customer_id, units_consumed = get_customer_details()
    energy_charge, service_charge, final_amount = Calculate_bill(units_consumed)
    Display_bill(
        customer_name,
        customer_id,
        units_consumed,
        energy_charge,
        service_charge,
        final_amount,
    )


if __name__ == "__main__":
    main()
