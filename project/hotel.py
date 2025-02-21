rateCard = {
  'coffee': 80,
  'bread': 50,
  'maggi': 100,
  'burger': 120,
  'pizza': 200
}

totalBill = 0  # Initialize the totalBill variable here.

def display_items(rate): 
  for index, (items, key) in enumerate(rateCard.items()):
    print(f" {index + 1}. Item Name: {items}, Price: {key}")

def select_item(card):
  global totalBill
  display_items(rateCard)
  choice = int(input("Select an item number to add to your bill: ")) - 1
  item = list(rateCard.items())[choice]
  totalBill += item[1]
  print(f"Added {item[0]} to your bill. Price: {item[1]}")
  print(f"Total Bill: {totalBill}")

def add_item(card):
  item_name = input("Enter the name of the new item: ")
  item_price = int(input("Enter the price of the new item: "))
  rateCard[item_name] = item_price
  print(f"Added new item: {item_name} with price: {item_price}")
  display_items(rateCard)

def main():
    global totalBill  # To ensure we modify the global variable
    while True:
        print("\n1. Select an item")
        print("2. Add a new item")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            select_item(rateCard)
        elif choice == 2:
            add_item(rateCard)
        elif choice == 3:
            print(f"Final Total Bill: {totalBill}")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
