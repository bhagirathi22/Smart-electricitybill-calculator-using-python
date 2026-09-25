# Smart Electricity Bill Calculator

A beginner-friendly Python console program that calculates an electricity bill from the customer's name, ID, and units consumed.

## Features

- Collects customer name, customer ID, and electricity units consumed.
- Rejects negative units and asks again when the input is invalid.
- Uses progressive electricity slabs:
	- First 100 units: ₹2 per unit
	- Next 100 units: ₹4 per unit
	- Next 300 units: ₹6 per unit
	- Units above 500: ₹8 per unit
- Adds a fixed service charge of ₹100.
- Displays a formatted bill with customer details and amount breakdown.

## Program Flow

1. `main()` calls `get_customer_details()`.
2. `get_customer_details()` reads the customer name and ID as strings.
3. It converts the units input to an integer and checks that it is not negative. Invalid input is requested again.
4. `main()` sends the units to `Calculate_bill()`.
5. `Calculate_bill()` applies the correct slabs, adds the service charge, and returns the energy charge, service charge, and final amount as float values.
6. `Display_bill()` receives the returned values and prints a clean electricity bill.

## Run the Program

From this folder, run:

```bash
python smart_electricity_bill_calculator.py
```

The program uses only Python variables, strings, integers, floats, functions, parameters, return values, input, type conversion, comparisons, `if`/`elif`/`else`, and formatted output. It does not use databases, files, APIs, external libraries, or classes.