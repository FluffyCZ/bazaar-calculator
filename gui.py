from tkinter import *
from tkinter import messagebox
from tkinter import font
import os
import webbrowser

# Help GUI
def HelpMenu():
    messagebox.showinfo("Info", "A simple calculator for Bazaar")

def GetWebLink():
    url = "https://github.com/FluffyCZ/bazaar-calculator"
    webbrowser.open(url)

# Calculate the values
def Calculate(event=None): # Added 'event=None' to handle key binding
    try:
        npc_margin = float(entry_npc_margin.get())
        sell_price = float(entry_sell_price.get())
        amount = float(entry_amount.get())

        # Calculations
        sell_price_value = (sell_price + npc_margin)
        profit_value = ((amount * sell_price_value) - (amount * sell_price))
        money_spend_value = (sell_price * amount)
        money_made_value = (money_spend_value + profit_value)
        percentage_value = ((money_made_value * 100) // money_spend_value)

        # Vars
        sell_price_var.set(f"Sell Price: {sell_price_value:.2f}")
        money_spend_var.set(f"Money Spent: {money_spend_value:.2f}")
        profit_var.set(f"Profit: {profit_value:.2f}")
        money_made_var.set(f"Money Made: {money_made_value:.2f}")
        profit_percentage_var.set(f"Profit Percentage: {percentage_value:.2f}%")

        # Clear the entry fields after calculation
        entry_sell_price.delete(0, END)
        entry_npc_margin.delete(0, END)
        entry_amount.delete(0, END)

    except ValueError as Error:
        # Deletes the given values in the entry field
        entry_sell_price.delete(0, END)
        entry_npc_margin.delete(0, END)
        entry_amount.delete(0, END)

        messagebox.showinfo("Error", "Invalid number! Please try again!")

        # Console print
        print(Error)
        
# Creating the GUI
root = Tk()

# Icon
icon_path = os.path.join(os.getcwd(), "coin_icon.png")
root.iconphoto(False, PhotoImage(file=icon_path))

# Fonts
normal_font = font.Font(family='Source Code Pro Semibold', size=12)
big_font = font.Font(family="('Source Code Pro Black'", size=14, weight="bold")
title_font = font.Font(family='Source Code Pro Black', size=18, weight="bold")

# Configuring the window
root.title("Bazaar Calculator")
root.geometry("500x800")
root.configure(bg="#f2f2f2")

# Menu
menu = Menu(root)
root.config(menu=menu)

helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Info', command=HelpMenu)
helpmenu.add_command(label='Web', command=GetWebLink)

# Title
title_label = Label(root, text="Bazaar Calculator", font=title_font, bg="#f2f2f2", fg="#333")
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Entry variables
Label(root, height=2, width=15, text="Sell Price: ", font=normal_font, bg="#f2f2f2").grid(row=1, column=0, padx=10, pady=5, sticky=W)
Label(root, height=2, width=15, text="NPC Margin: ", font=normal_font, bg="#f2f2f2").grid(row=2, column=0, padx=10, pady=5, sticky=W)
Label(root, height=2, width=15, text="Amount: ", font=normal_font, bg="#f2f2f2").grid(row=3, column=0, padx=10, pady=5, sticky=W)

# Customize entries
entry_style = {"font": normal_font, "width": 20, "bd": 2, "relief": "groove", "bg": "#e6e6e6"}

entry_sell_price = Entry(root, **entry_style)
entry_npc_margin = Entry(root, **entry_style)
entry_amount = Entry(root, **entry_style)

entry_sell_price.grid(row=1, column=1, padx=10, pady=5)
entry_npc_margin.grid(row=2, column=1, padx=10, pady=5)
entry_amount.grid(row=3, column=1, padx=10, pady=5)

# Calculate button
calculate_button = Button(root, text="Calculate", command=Calculate, width=15, height=2, font=big_font, bg="#4CAF50", fg="white", bd=0, activebackground="#45a049")
calculate_button.grid(row=4, column=1, padx=(0, 150), pady=20)

# StringVars for dynamic labels
sell_price_var = StringVar()
money_spend_var = StringVar()
profit_var = StringVar()
money_made_var = StringVar()
profit_percentage_var = StringVar()

# Initialize with default values
sell_price_var.set("Sell Price: ")
money_spend_var.set("Money Spent: ")
profit_var.set("Profit: ")
money_made_var.set("Money Made: ")
profit_percentage_var.set("Profit Percentage: ")

# Custom style for changeable variables
variable_style = {"font": normal_font, "bg": "#e6e6e6", "bd": 2, "relief": "ridge", "anchor": W, "padx": 5, "pady": 5}

# Changeable variables labels
Label(root, height=2, width=30, textvariable=sell_price_var, **variable_style).grid(row=5, column=0, columnspan=2, padx=10, pady=5)
Label(root, height=2, width=30, textvariable=money_spend_var, **variable_style).grid(row=6, column=0, columnspan=2, padx=10, pady=5)
Label(root, height=2, width=30, textvariable=profit_var, **variable_style).grid(row=7, column=0, columnspan=2, padx=10, pady=5)
Label(root, height=2, width=30, textvariable=money_made_var, **variable_style).grid(row=8, column=0, columnspan=2, padx=10, pady=5)
Label(root, height=2, width=30, textvariable=profit_percentage_var, **variable_style).grid(row=9, column=0, columnspan=2, padx=10, pady=5)

# Web Link Button
web_link_button = Button(root, text="Open Web", command=GetWebLink, font=normal_font, bg="#2196F3", fg="white", bd=0, activebackground="#1976D2", width=15)
web_link_button.grid(row=10, column=0, columnspan=2, padx=10, pady=20)

# Binding Enter to call Calculate() function
root.bind('<Return>', Calculate)

# End
root.mainloop()
