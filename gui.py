import tkinter as tk
from tkinter import ttk
from apis import *
from utils import *




def start_gui():
    # Creating the app
    root = tk.Tk()
    # Creating the app title
    root.title('API Exchange Platform')
    # Creating the framework for the tabs
    my_notebook = ttk.Notebook(root)
    my_notebook.grid(row=0, column=0)
    # Creating the tabs
    first_tab = ttk.Frame(my_notebook)
    second_tab = ttk.Frame(my_notebook)
    my_notebook.add(first_tab, text='Main menu')
    my_notebook.add(second_tab, text='Exchange List')
    # Hiding the Exchange List tab until it is called from the button
    my_notebook.hide(1)


    # ---------------- GUI Interaction functions ---------------- #
    # Hiding all other tabs, showing the main menu tab
    def go_to_main():
        my_notebook.select(0)
        my_notebook.hide(1)
        return

    # Hiding all other tabs, showing the second tab
    def go_to_second_tab():
        my_notebook.select(1)
        my_notebook.hide(0)
        return

    # function to automatically get the id based on the url selected in the dropdown
    def get_id_for_exchange(e):
        url = dropdown.get()
        global id_for_exchange
        dictionar = all_exchanges(3)
        for i, j in dictionar.items():
            if url == j:
                id_for_exchange = i
        return id_for_exchange

    def help():
        f = open('README.MD','r')
        output = f.read()
        return output

    # ---------------- Defining the dropdown list ---------------- #

    # Creating a list for the dropdown
    def dropdownlist():
        list = apis.all_exchanges(2)
        unique_list = []
        for i in list:
            if i not in unique_list:
                unique_list.append(i)
        return unique_list

    # --- Calling the function once the gui is started to populate the dropdown box ---- #
    dropdownlist()

    def text_box(location,output):

        text_box = tk.Text(location, height=20, width=60, yscrollcommand=1, xscrollcommand=1, bd=3)
        text_box.grid(row=1, column=1, rowspan=4, columnspan=2, padx=10, pady=10)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center",1.0,"end")
        # HOW TO INSERT DATA IN THE DATA BOX
        text_box.insert(1.0,output)

    # -- Inserting the TEXT Boxes into the tabs --
    text_box(first_tab, "")
    text_box(second_tab, "")


    def button_function(location, button_text, command, row, column):
        l_button_text = tk.StringVar()
        l_button = tk.Button(location, textvariable=l_button_text, command=command)
        l_button_text.set(button_text)
        l_button.grid(row=row, column=column, padx=10, pady=10)


    def label_function(location, label_text, row, column, columnspan):
        l_label = tk.Label(location, text=label_text)
        l_label.grid(row=row, column=column)


    # ----------------  Creating second_tab labels ---------------- #
    label_function(second_tab, "-- Fetch Exchange --", 0, 1, 2)
    label_function(second_tab, "Please select an exchange", 1, 0, 1)

    # ----------------  Creating the second_tab dropdown box  ---------------- #

    dropdown = ttk.Combobox(second_tab, value=dropdownlist())
    dropdown.grid(row=2, column=0, columnspan=1, padx=10, pady=10)
    dropdown.current(0)

    # --- Binding the dropdown to the go_button option --- #
    dropdown.bind("<<ComboboxSelected>>", get_id_for_exchange)

    # ----------------  Creating the second_tab buttons  ---------------- #

    # --- Fetch Exchange button ---#
    button_function(second_tab, "Fetch Exchange", lambda: text_box(second_tab,fetch_exchange(id_for_exchange)), 3, 0)


    # --- Back button ---#
    button_function(second_tab, "Back to main menu", go_to_main, 5, 0)

    # --- Quit Button ---#
    button_function(second_tab, "Quit", root.quit, 5, 2)

    # Creating the main window title:
    # Creating the main window label
    label_function(first_tab, "--Cryptocurrencies--", 0, 1, 2)

    # ---------------- Defining the buttons in the main window ---------------- #

    # --- Market Info button creation --- #
    button_function(first_tab, "Market Info", lambda: (text_box(first_tab,global_api())), 1, 0)

    # --- Coin Info button creation ---#
    button_function(first_tab, "Coin Info", lambda: (text_box(first_tab,all_coins())), 2, 0)

    # --- Coin Market button creation ---#
    button_function(second_tab, "Coin Markets", lambda: (text_box(second_tab,market_for_coins(id_for_exchange))), 4, 0)
    '''
    La butonul asta ar trebui sa fac la fel cum fac la exchange rates.
    Butonul sa duca pe second tab, iar acolo sa ne folosesc de dropdown sa luam id-ul si sa il aplic la un 
    buton numit Coin Markets. De discutat.
    '''

    # --- Fetch Exchange Rates button creation ---#
    button_function(first_tab, "Go To Market details", go_to_second_tab, 5, 1)
    # --- Help Button ---#
    button_function(first_tab, "Help", lambda: text_box(first_tab,help()), 5, 0)
    # --- Save to CSV button ---#
    # button_function(first_tab, "Save Coin Info", lambda: save_output_to_csv(1,'coin_info'), 4, 0)
    button_function(second_tab, "Save Exchange",lambda: (save_to_csv('exchange/?id=','fetch_exchange',id_for_exchange),text_box(second_tab,"CSV saved")), 5, 1)
    # --- Quit Button ---#
    button_function(first_tab, "Quit", root.quit, 5, 2)

    root.mainloop()


start_gui()
