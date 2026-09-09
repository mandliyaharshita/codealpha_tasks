# to CLACULATE INVESTMENT
def Calculate_invest(price,quantity):
    return price*quantity


#  to ADD STOCKS
def add_stock(stocks):
    stock=input("Enter the stock: ").upper()

    try:
            quantity=int(input("Enter the quantity: "))
    
            if quantity<=0:
                print("Quantity should be greater than 0 !")
                return None
    
    except ValueError:
        print("Please enter a valid number!")
        return None

    if stock in stocks:
            price=stocks[stock]
            invest=Calculate_invest(price,quantity)
            print(f"\n{stock}")
            print(f"price: {price}")
            print(f"Quantity: {quantity}")
            print(f"Investment: {invest}\n")
            
            portfolio_item=(f"{stock} | Price: ₹{price} | Quantity: {quantity} | Investment: ₹{invest}")
            return portfolio_item, invest
    else:
        print("Stock  is not available!")
        return None


# Save portfolio to file

def save_portfolio(portfolio,total):
    with open("stock_portfolio.txt", "w", encoding="utf-8") as file:
          file.write("========== STOCK PORTFOLIO ==========\n\n")
          for item in portfolio:
               file.write(item + "\n")
          file.write("\n--------------------------------------\n")
          file.write(f"Total Investment: ₹{total}\n")
          file.write("======================================\n")

    print("\nPortfolio saved successfully!")    

# Main function
   
def main():
    stocks={
    "AAPL":180,
    "TSLA":200,
    }
    
    total=0
    portfolio=[]

    try:
            number=int(input("Enter the number of stock to add: "))
    
            if number<=0:
                print("Number should be greater than 0!")
                return 
    except ValueError:
            print("Enter the valid number")
            return 
    print(f"\n--------------STOCK PORTFOLIO-------------\n")
    for i in range(number):
         result = add_stock(stocks)

         if result is not None:
            item, invest = result

            portfolio.append(item)
            total += invest

    print(f"------------------------------------------")
    print("Total investment: ",total)
    print(f"------------------------------------------")

    save_portfolio(portfolio,total)

if __name__ == "__main__":
    main()
