name = input("Enter your name: ")

products = {}

for i in range(3):
    p_name = input("Enter Produch name: ")
    p_price = int(input("Enter Produch price: "))
    products[p_name] = p_price

sub_total = 0
for price in products.values():
    sub_total += price

discount = 0

if sub_total >= 5000: discount = 0.2
elif sub_total >= 3000 and sub_total <= 4999: discount = 0.1
elif sub_total >= 1000 and sub_total <= 2999: discount = 0.05

final_total = sub_total - sub_total*discount

print(f"Customer Name: {name}\n")

p_count = 1
for p_name, p_price in products.items():
    print(f"Product {p_count}: {p_name}")
    print(f"Price: {p_price}\n")
    p_count += 1

print("Subtotal: ", sub_total)
print("Discout: ", sub_total*discount)
print("Final Total: ", final_total)