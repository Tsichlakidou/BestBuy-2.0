import products
import promotions
import store


# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]
best_buy = store.Store(product_list)
# Create promotion catalog
second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)
product_list[1].set_promotion(third_one_free)
product_list[3].set_promotion(thirty_percent)


def start(store_odj):
    """Run the store user interface."""
    while True:
        print("\nStore Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            all_products = store_odj.get_all_products()

            for product in all_products:
                product.show()

        elif choice == "2":
            total_quantity = store_odj.get_total_quantity()
            print("Total of", total_quantity, "items in store")

        elif choice == "3":
            shopping_list = []

            all_products = store_odj.get_all_products()

            for index, product in enumerate(all_products, start=1):
                print(index, end=". ")
                product.show()

            while True:
                product_number = input(
                    "Which product do you want? Enter # or press Enter to finish: "
                )

                if product_number == "":
                    break

                quantity = int(input("What amount do you want? "))

                product = all_products[int(product_number) - 1]
                shopping_list.append((product, quantity))

            try:
                total_price = store_odj.order(shopping_list)
                print("Order made! Total payment:", total_price)

            except Exception as e:
                print("Error:", e)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


start(best_buy)
