import tkinter as tk
from tkinter import messagebox, simpledialog
from buy_computer import available_parts

class CartApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Computer Parts Cart")
        self.geometry("500x400")
        self.computer_parts = []
        self.create_widgets()

    def create_widgets(self):
        self.parts_label = tk.Label(self, text="Available Parts:")
        self.parts_label.pack()

        self.parts_listbox = tk.Listbox(self, width=60)
        for idx, (electronic, store, price, items) in enumerate(available_parts):
            self.parts_listbox.insert(tk.END, f"{idx+1}: {electronic} (Price: {price})")
        self.parts_listbox.pack()

        self.select_button = tk.Button(self, text="Select Part", command=self.select_part)
        self.select_button.pack(pady=5)

        self.cart_label = tk.Label(self, text="Your Cart:")
        self.cart_label.pack()

        self.cart_listbox = tk.Listbox(self, width=60)
        self.cart_listbox.pack()

    def select_part(self):
        selection = self.parts_listbox.curselection()
        if not selection:
            messagebox.showwarning("No selection", "Please select a part.")
            return
        part_index = selection[0]
        items = available_parts[part_index][3]
        item_names = [item[1] for item in items]
        item_choice = simpledialog.askinteger(
            "Select Item",
            "Choose item number:\n" + "\n".join(f"{i+1}: {name}" for i, name in enumerate(item_names)),
            minvalue=1, maxvalue=len(item_names)
        )
        if item_choice is None:
            return
        selected_item = items[item_choice - 1][1]
        if selected_item in self.computer_parts:
            self.computer_parts.remove(selected_item)
            messagebox.showinfo("Removed", f"Removed {selected_item} from cart.")
        else:
            self.computer_parts.append(selected_item)
            messagebox.showinfo("Added", f"Added {selected_item} to cart.")
        self.update_cart()

    def update_cart(self):
        self.cart_listbox.delete(0, tk.END)
        for item in self.computer_parts:
            self.cart_listbox.insert(tk.END, item)

if __name__ == "__main__":
    app = CartApp()
    app.mainloop()
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)

items_choice = ""
computer_parts = []
chosen_items = ""
PRICE_LIST_INDEX = 3
ITEM_NUMBER_INDEX = 1
while True:
    print("Select Items You want (invalid choice exits): ")
    for index, (electronic, store, price, items) in enumerate(available_parts):
        print("{} : {}. price = {}".format(index + 1, electronic,price))

    choice = int(input())
    if 1 <= choice <= len(available_parts):
        items = available_parts[choice -1][PRICE_LIST_INDEX]
    else:
        break
    
  
    print("Explore Types Of this Item: ")
    for index, (item_numbers,item) in enumerate(items):
        print("{} : {} ".format(index + 1, item))

    item_choice = int(input())
    if 1 <= item_choice <= len(items):
        selected_item = items[item_choice - 1][ITEM_NUMBER_INDEX]
        if selected_item in computer_parts:
            print("Removing {}".format(selected_item))
            computer_parts.remove(selected_item)
        else:
            print("Adding {}".format(selected_item))
            computer_parts.append(selected_item)
        print("Your list now contains: {}".format(computer_parts))