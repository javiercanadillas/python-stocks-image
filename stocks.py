import csv


def load_data():
  list = []

  with open("all_stocks_5yr.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
      row["open"] = float(row["open"]) if row["open"] != "" else row["open"]
      row["close"] = float(row["close"]) if row["close"] != "" else row["close"]
      row["high"] = float(row["high"]) if row["high"] != "" else row["high"]
      row["low"] = float(row["low"]) if row["low"] != "" else row["low"]
      row["volume"] = float(row["volume"]) if row["volume"] != "" else row["volume"]
      list.append(row)

    return list


def highest_closing_price(data):
  acc = 0.0
  date = None

  for row in data:
    if row["close"] > acc:
      acc = row["close"]
      date = row["date"]
  
  return acc, date


def lowest_closing_price(data):
  acc = float('inf')
  date = None

  for row in data:
    if row["close"] < acc:
      acc = row["close"]
      date = row["date"]  

  return acc, date


def average_volume(data):
    sum_volume = 0

    for row in data:
        sum_volume += row["volume"]
        
    return sum_volume / len(data)


def price_on_date(data, date, symbol):
    for row in data:
        if date == row["date"] and symbol == row["Name"]:
            return row

    raise Exception("date-symbol combo not in dataset")


if __name__ == "__main__":
  data = load_data()

  should_keep_going = True

  menu = """
  Stock Analysis Tool:
  1. View Highest Closing Price
  2. View Lowest Closing Price
  3. Calculate Average Trading Volume
  4. Get Stock Details for a Specific Date
  5. Exit

  """

  while should_keep_going:

    choice = input(menu)
    if choice == "1":
      print(highest_closing_price(data))
    elif choice == "2":
      print(lowest_closing_price(data))
    elif choice == "3":
      print(average_volume(data))
    elif choice == "4":
      date = input("give me the date: ")
      symbol = input("give me the symbol: ")
      print(price_on_date(data, date, symbol))
    elif choice == "5":
      print("Exiting")
      break
    else:
      print("please write a number from 1 to 5")