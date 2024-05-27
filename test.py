import tkinter as tk
from forex_python.converter import CurrencyRates


def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    c = CurrencyRates()

    converted_amount = c.convert(from_currency, to_currency, amount)
    result_var.set(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")


# Set up the main application window
root = tk.Tk()
root.title("Currency Converter")

# Create and set the variables for the dropdowns and the result
from_currency_var = tk.StringVar(value="USD")
to_currency_var = tk.StringVar(value="CAD")
result_var = tk.StringVar()

# Create and place the widgets
tk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="From:").grid(row=1, column=0, padx=10, pady=10)
from_currency_menu = tk.OptionMenu(root, from_currency_var, "USD", "CAD", "EUR", "AUD")
from_currency_menu.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="To:").grid(row=2, column=0, padx=10, pady=10)
to_currency_menu = tk.OptionMenu(root, to_currency_var, "USD", "CAD", "EUR", "AUD")
to_currency_menu.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, textvariable=result_var)
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
