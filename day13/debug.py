# Debugging Exercise

def calculate_total_price(price, tax_rate):
    total = price + (price * tax_rate)
    return total

def main():
    price = 100
    tax_rate = 0.15
    total_price = calculate_total_price(price, tax_rate)
    print("Total price:", total_price)

if __name__ == "__main__":
    main()
