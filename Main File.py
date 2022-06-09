'''
Author: Auston Pawell
Prog:   Main File.py
Date:   12/7/2020
Descr:
    Program simulating order food from a restaurant
'''

from tkinter import *               # tkinter used for creating GUI
from tkinter import messagebox      # messagebox used for confirmaition buttons
import ChickenWings as ck           # class to define types of chicken wings
import Pizza as pz                  # class to define types of pizzas
import Drinks as dr                 # class to define types of drinks
import random                       # random used to simulate a order # on the receipt


wing_list = []      # list holding types of chicken wings on the order
pizza_list = []     # list holding types of pizzas on the order
drink_list = []     # list holding types of drinks on the order

class Start:
    ''' GUI to server as a main menu for navigation '''
    
    def __init__(self):

        # create window with title
        self.root = Tk()
        self.root.title('Peter Parker\'s Pizza Time Parlor')


        # create photo on the start window
        self.Photo1 = PhotoImage(file = "pizza_time.gif")
        self.photoLabel = Label(self.root, image = self.Photo1, bg="black").grid(row = 0, column = 0, sticky = E)

        # create frame for intro text
        self.intro_frame = Frame(self.root)
        self.text1 = Label (self.intro_frame,
                            text = "Welcome to Peter Parker's Pizza Time Parlor!\nThe best pizza in all of Queens New York!")
        self.text2 = Label(self.intro_frame,
                            text = 'Where our motto is:\n"Everytime is Pizza Time!')
        self.text3 = Label(self.intro_frame,
                            text = '\nLets create your order!')
        self.text1.grid(row = 0, column = 0)
        self.text2.grid(row = 1, column = 0)
        self.text3.grid(row = 2, column = 0, sticky = S)
        
        # Buttons for naviagation
        self.nav_frame = Frame(self.root)
        self.pizza_button = Button(self.nav_frame, text="Add a Pizza", width = 15, command = self.open_pizza_screen)
        self.wing_button = Button(self.nav_frame, text="Add chicken Wings", width = 15, command = self.open_wings_screen)
        self.drinks_button = Button(self.nav_frame, text="Add drinks", width = 15, command = self.open_drinks_screen)
        self.view_order_button = Button(self.nav_frame, text="View Order", width = 15, command = self.view_order)
        self.clear_order_button = Button(self.nav_frame, text="Clear Order", width = 15, command = self.clear_order)
        self.confirm_order_button = Button(self.nav_frame, text="Confirm Order", width = 15, command = self.confirm_order)
        self.close_button = Button(self.nav_frame, text="Exit", width = 15, command = self.close)        

        self.pizza_button.grid(row = 0, column = 0)
        self.wing_button.grid(row = 1, column = 0)
        self.drinks_button.grid(row = 2, column = 0)
        self.view_order_button.grid(row = 3, column = 0)
        self.clear_order_button.grid(row = 4, column = 0)
        self.confirm_order_button.grid(row = 5, column = 0)
        self.close_button.grid(row = 6, column = 0)

        # Place the frame
        self.intro_frame.grid(row = 0, column = 1, sticky = N)
        self.nav_frame.grid(row = 0, column = 1, sticky = S)

    def open_pizza_screen(self):
        PizzaGUI()
        
    def open_wings_screen(self):
        WingGUI()

    def open_drinks_screen(self):
        DrinkGUI()
    
    def view_order(self):
        OrderGUI()

    def clear_order(self):
        response = messagebox.askyesno('Confirmation', 'Are you sure you want to reset your order?')
        if response == True:
            wing_list.clear()     
            pizza_list.clear()  
            drink_list.clear()
            messagebox.showinfo('Order Reset', 'Your order has been reset!')
            
    def confirm_order(self):
        if len(wing_list) == 0 and len(pizza_list) == 0 and len(drink_list) == 0:
            messagebox.showerror('Empty Order',
                                'Your order is empty!\nPlease add something to order before confirming purchase')
        else:
            ConfirmGUI()

    def close(self):
        response = messagebox.askyesno('Confirmation', 'Are you sure you want to exit?')
        if response == True:
            self.root.destroy()
            
class OrderGUI:
    ''' GUI to server as a display for the current order '''
    
    def __init__(self):

        # create window with title
        self.order = Tk()
        self.order.title('View Order')
        self.title = Label(self.order, text = 'Here is your order').grid(row = 0, column = 1)

        self.total_price = 0        # variable to hold the total price of the order
        

        if len(wing_list) == 0 and len(pizza_list) == 0 and len(drink_list) == 0:
            Label(self.order, text = 'Your order is empty!\n').grid(row = 1, column = 1)
        else:

            self.wing_frame = Frame(self.order)
            self.wing_count = 0     # variable to hold how many types of chicken wings are on the order
            # displaying wings in the order
            Label(self.wing_frame, text = '***CHICKEN WINGS***').pack()
            if len(wing_list) == 0:
                Label(self.wing_frame, text = 'None\n').pack()
            else:
                for item in wing_list:
                    string = 'Chicken Wings Number: ' + str(self.wing_count + 1)
                    # create a label holding information about a chicken wing order
                    Label(self.wing_frame, text = string).pack()
                    Label(self.wing_frame, text = str(item), anchor = W).pack()
                    # append the price to the running total price
                    self.total_price += item.price
                    self.wing_count += 1

            self.pizza_frame = Frame(self.order)
            self.pizza_count = 0        # variable to hold how many types of pizzas are on the order
            # displaying pizzas in the order
            Label(self.pizza_frame, text = '***PIZZAS***').pack()
            if len(pizza_list) == 0:
                Label(self.pizza_frame, text = 'None\n').pack()
            else:
                for item in pizza_list:
        
                    string = 'Pizza Number: ' + str(self.pizza_count + 1)
                    # create a label holding information about a pizza order
                    Label(self.pizza_frame, text = string).pack()
                    Label(self.pizza_frame, text = str(item), anchor = W).pack()
                    # append the price to the running total price
                    temp = item.calc_price()
                    self.total_price += temp
                    self.pizza_count += 1

            self.drink_frame = Frame(self.order)
            self.drink_count = 0            # variable to hold how many types of drinks are on the order
            # displaying drinks in the order
            Label(self.drink_frame, text = '***DRINKS***').pack()
            if len(drink_list) == 0:
                Label(self.drink_frame, text = 'None\n').pack()
            else:
                for item in drink_list:
                    string = 'Drink Number: ' + str(self.drink_count + 1)
                    Label(self.drink_frame, text = string).pack()
                    Label(self.drink_frame, text = str(item), anchor = W).pack()
                    # append the price to the running total price
                    self.total_price += item.price
                    self.drink_count += 1
                
            # display the total price at the end
            string_price = 'Total Price: ' + str('${:,.2f}'.format(self.total_price))
            self.wing_frame.grid(row = 1, column = 0, sticky = N)
            self.pizza_frame.grid(row = 1, column = 1, sticky = N)
            self.drink_frame.grid(row = 1, column = 2, sticky = N)
            Label(self.order, text = string_price).grid(row = 2, column = 2)
        
        # button to close window and head back to main window
        self.back_button = Button(self.order, text = "Go Back", width = 15, command = self.close_window).grid(row = 2, column = 1)

    def close_window(self):
        self.order.destroy()

class ConfirmGUI:
    ''' GUI to server as the confirmation screen for the order '''
    
    def __init__(self):

        # create window with title
        self.confirm = Tk()
        self.confirm.title('Confirm Order')

        # create frame for holding label and text entry
        self.frame = Frame(self.confirm)
        self.name = Label(self.frame, text = 'Enter the name of the order:')
        self.name_entry = Entry(self.frame, width = 20)
        self.confirm_button = Button(self.frame, text = 'Confirm', command = self.confirm_order)

        self.name.grid(row = 0, column = 0)
        self.name_entry.grid(row = 0, column = 1)
        self.confirm_button.grid(row = 1, column = 0)

        self.frame.pack()
        
    def confirm_order(self):
        name = self.name_entry.get()
        response = messagebox.askyesno('Confirmation', 'Confirm your order?')
        if response == True:
            order_num = random.randint(1,99)
            fileName = name + '_receipt.txt'
            # If the user confirms that the order is correct,
            # write the data to the file
            outfile = open(fileName, 'w')
            outfile.write('Order Name: ')
            outfile.write(name)
            outfile.write('\nOrder No: ' + str(order_num) + '\n')
            
            
            total_price = 0
            wing_count = 0
            outfile.write('\n*** CHICKEN WINGS ***\n')
            if len(wing_list) == 0:
                outfile.write('None\n')
            for item in wing_list:
                # combine string information into one for outfile writing
                string = ''
                string = 'Wing Number: ' + str(wing_count + 1)
                outfile.write(string)
                outfile.write('\n')
                outfile.write(str(item)+'\n\n')
                total_price += item.price
                wing_count += 1

            pizza_count = 0
            outfile.write('\n*** PIZZA ***\n')
            if len(pizza_list) == 0:
                outfile.write('None\n')
            for item in pizza_list:
                # combine string information into one for outfile writing
                string = ''
                string = 'Pizza Number: ' + str(pizza_count + 1)
                outfile.write(string)
                outfile.write('\n')
                outfile.write(str(item)+'\n\n')
                temp = item.calc_price()
                total_price += temp
                pizza_count += 1

            drink_count = 0
            outfile.write('\n*** DRINKS ***\n')
            if len(drink_list) == 0:
                outfile.write('None\n')
            for item in drink_list:
                # combine string information into one for outfile writing
                string = ''
                string = 'Drink Number: ' + str(drink_count + 1)
                outfile.write(string)
                outfile.write('\n')
                outfile.write(str(item)+'\n\n')
                total_price += item.price
                drink_count += 1
                
            # combine string information into one for outfile writing
            temp_string = 'Total Price: ' + str('${:,.2f}'.format(total_price))
            outfile.write(temp_string)
            # close the file
            outfile.close()
            # display message box confirming the file has been created
            messagebox.showinfo('Thank You', 'Order Created! Thank You!')
            # clear the order lists for another potential order
            wing_list.clear()     
            pizza_list.clear()  
            drink_list.clear()

        # close the window after writing to file
        self.confirm.destroy()
        
class WingGUI:
    ''' GUI to serve as a window to create specific types of chicken wings '''
    
    def __init__(self):
        self.wings = Tk()
        self.wings.title('Add Chicken Wings')
        
        # variable to hold sauce choice *used for chicken wing class*
        self.spicy_var=StringVar(self.wings)
        self.spicy_var.set('Sweet BBQ')
        self.piece_var=DoubleVar(self.wings)
        self.piece_var.set(6.00)
        
        # Frame for sauce types
        self.spicy_frame = Frame(self.wings)
        self.sauce_label = Label(self.spicy_frame, text = 'Select a sauce')
        
        # Create button options for spicy choice
        self.sweetBBQ = Radiobutton(self.spicy_frame, text = 'Sweet BBQ', variable = self.spicy_var, value = 'Sweet BBQ')
        self.teriyaki= Radiobutton(self.spicy_frame, text = 'Teriyaki', variable = self.spicy_var, value = 'Teriyaki')
        self.mild = Radiobutton(self.spicy_frame, text = 'Mild', variable = self.spicy_var, value = 'Mild')
        self.medium = Radiobutton(self.spicy_frame, text = 'Medium', variable = self.spicy_var, value = 'Medium')
        self.spicyBBQ = Radiobutton(self.spicy_frame, text = 'Spicy BBQ', variable = self.spicy_var, value = 'Spicy BBQ')
        self.ghostPepper = Radiobutton(self.spicy_frame, text = 'Ghost Peppers', variable = self.spicy_var, value = 'Ghost Peppers')

        self.sauce_label.grid(row = 0, column = 0, sticky = W)
        self.sweetBBQ.grid(row = 1, column = 0, sticky = W)
        self.teriyaki.grid(row = 2, column = 0, sticky = W)
        self.mild.grid(row = 3, column = 0, sticky = W)
        self.medium.grid(row = 4, column = 0, sticky = W)
        self.spicyBBQ.grid(row = 5, column = 0, sticky = W)
        self.ghostPepper.grid(row = 6, column = 0, sticky = W)

        # Frame of pieces and price
        self.piece_frame = Frame(self.wings)
        self.piece_label = Label(self.piece_frame, text = 'Select how many pieces')
        
        # Bbuttons for piece choices
        self.pieces_6 = Radiobutton(self.piece_frame, text = '6 Pieces | $6.00', variable = self.piece_var, value = 6.00)
        self.pieces_10 = Radiobutton(self.piece_frame, text = '10 Pieces | $10.00', variable = self.piece_var, value = 10.00)
        self.pieces_15 = Radiobutton(self.piece_frame, text = '15 Pieces | $15.00', variable = self.piece_var, value = 15.00)
        self.pieces_20 = Radiobutton(self.piece_frame, text = '20 Pieces | $20.00', variable = self.piece_var, value = 20.00)
        self.pieces_25 = Radiobutton(self.piece_frame, text = '25 Pieces | $25.00', variable = self.piece_var, value = 25.00)

        # Place buttons onto the frame
        self.piece_label.grid(row = 0, column = 0, sticky = W)
        self.pieces_6.grid(row = 1, column = 0, sticky = W)
        self.pieces_10.grid(row = 2, column = 0, sticky = W)
        self.pieces_15.grid(row = 3, column = 0, sticky = W)
        self.pieces_20.grid(row = 4, column = 0, sticky = W)
        self.pieces_25.grid(row = 5, column = 0, sticky = W)
        
        # Frame for buttons
        self.button_frame = Frame(self.wings)
        self.confirm = Button(self.button_frame, text = "Confirm", command = self.confirm)
        self.back_button = Button(self.button_frame, text = "Cancel", command = self.close_window)

        self.confirm.grid(row = 0, column = 0)
        self.back_button.grid(row = 0, column = 1)
        
        # place frames on grid
        self.spicy_frame.grid(row = 0, column = 0, sticky = NW)
        self.piece_frame.grid(row = 0, column = 2, sticky = NE)
        self.button_frame.grid(row = 1, column = 1)

    def close_window(self):
        response = messagebox.askyesno('Confirmation', 'Are you sure you want to cancel?')
        if response == True:
            self.wings.destroy()
        
    def confirm(self):
        response = messagebox.askyesno('Confirmation', 'Are you ok with your selections?')
        if response == True:
            sauce = self.spicy_var.get()
            pieces = int(self.piece_var.get())
            price = self.piece_var.get()
            price = price + (price * .05)
            temp = ck.Wings(sauce, pieces, price)
            
            wing_list.append(temp)
            self.wings.destroy()
        elif response == False:
           
            self.wings.lift()

class PizzaGUI:
    ''' GUI to serve as a window to create specific types of pizzas '''
    
    def __init__(self):
        self.pizza = Tk()
        self.pizza.title('Add a Pizza')

        # variable to hold choices
        self.size_var = StringVar(self.pizza)
        self.size_var.set('Small')
        self.meat_choices = []              # List to hold current user meat choices
        self.topping_choices = []           # List to hold current user topping choices
        
        # Frame to hold size
        self.size_frame = Frame(self.pizza)
        self.size_title = Label(self.size_frame, text = 'Select a size')
        # Button options for pizza sizes
        self.small = Radiobutton(self.size_frame, text = 'Small', variable = self.size_var, value = 'Small')
        self.medium = Radiobutton(self.size_frame, text = 'Medium', variable = self.size_var, value = 'Medium')
        self.large = Radiobutton(self.size_frame, text = 'Large', variable = self.size_var, value = 'Large')
        
        # Labels for pizza size pricings
        self.small_price = Label(self.size_frame, text = '$8.00')
        self.medium_price = Label(self.size_frame, text = '$10.00')
        self.large_price = Label(self.size_frame, text = '$12.00')

        self.size_title.grid(row = 0, column = 0, sticky = W)
        
        self.small.grid(row = 1, column = 0, sticky = W)
        self.medium.grid(row = 2, column = 0, sticky = W)
        self.large.grid(row = 3, column = 0, sticky = W)
        
        self.small_price.grid(row = 1, column = 1, sticky = W)
        self.medium_price.grid(row = 2, column = 1, sticky = W)
        self.large_price.grid(row = 3, column = 1, sticky = W)

        # Frame of meat choices
        self.meat_frame = Frame(self.pizza)
        self.meat_title1 = Label(self.meat_frame, text = 'Available Meats Options')
        self.meat_title2 = Label(self.meat_frame, text = 'Your Meat Choices')
        self.meat_title1.grid(row = 0, column = 0)
        self.meat_title2.grid(row = 0, column = 1)
        
        # List box to hold choices
        self.meat_listbox = Listbox(self.meat_frame)

        # List containing the meat options
        self.meat_list = ['Sausage', 'Anchovies', 'Bacon','Grilled Chicken', 'Meatballs',
                          'Pepperoni', 'Ham', 'Philly Steak' ,'Salami' ]
        
        # Loop to populate the listbox
        for item in self.meat_list:
            self.meat_listbox.insert(0, item)

        # listbox to hold current user choices
        self.current_meat = Listbox(self.meat_frame)

        self.add_meat = Button(self.meat_frame, text='Add', command = self.add_meat)
        self.remove_meat = Button(self.meat_frame, text='Remove', command = self.remove_meat)

        self.add_meat.grid(row = 2, column = 0)
        self.remove_meat.grid(row = 2, column = 1)
        self.meat_listbox.grid(row = 1, column = 0)
        self.current_meat.grid(row = 1, column = 1)

        # Frame for topping choices
        self.topping_frame = Frame(self.pizza)
        self.topping_title1 = Label(self.topping_frame, text = 'Available Topping Options')
        self.topping_title2 = Label(self.topping_frame, text = 'Your Topping Choices')
        self.topping_title1.grid(row = 0, column = 0)
        self.topping_title2.grid(row = 0, column = 1)
        
        # List box to hold choices
        self.topping_listbox = Listbox(self.topping_frame)

        # List containing the topping options
        self.topping_list = ['Mushroom', 'Pineapple', 'Onion' ,'Olives', 'Artichoke' , 'Garlic','Green Peppers' ,'Spinach' ]

        # Loop to populate the listbox
        for item in self.topping_list:
            self.topping_listbox.insert(0, item)

        # Listbox to hold current user choices
        self.current_topping = Listbox(self.topping_frame)

        self.add_topping = Button(self.topping_frame, text='Add', command = self.add_topping)
        self.remove_topping = Button(self.topping_frame, text='Remove', command = self.remove_topping)

        self.add_topping.grid(row = 2, column = 0)
        self.remove_topping.grid(row = 2, column = 1)
        self.topping_listbox.grid(row = 1, column = 0)
        self.current_topping.grid(row = 1, column = 1)
        
        # Frame for buttons
        self.button_frame = Frame(self.pizza)
        self.confirm = Button(self.button_frame, text = "Confirm", command = self.confirm)
        self.cancel = Button(self.button_frame, text = "Cancel", command = self.close_window)
        self.confirm.grid(row = 0, column = 0)
        self.cancel.grid(row = 0, column = 1)
        
        # Place frames on the window
        self.size_frame.grid(row = 0, column = 0)
        self.meat_frame.grid(row = 1, column = 0)
        self.topping_frame.grid(row = 1, column = 1)
        self.button_frame.grid(row = 0, column = 1)

    def close_window(self):
        response = messagebox.askyesno('Confirmation', 'Are you sure you want to cancel?')
        if response == True:
            self.pizza.destroy()
            
    def confirm(self):
        response = messagebox.askyesno('Confirmation', 'Are you ok with your selections?')
        if response == True:
            # create empty pizza object
            temp = pz.Pizza()
            # Using class method setters
            temp.size = self.size_var.get()
            temp.meats = self.meat_choices
            temp.toppings = self.topping_choices
        
            pizza_list.append(temp)
            self.pizza.destroy()
        elif response == False:
            
            self.pizza.lift()

    def add_topping(self):
        self.current_topping.insert(0, self.topping_listbox.get(ANCHOR))
        self.topping_choices.append(self.topping_listbox.get(ANCHOR))
        self.topping_listbox.delete(ANCHOR)

    def remove_topping(self):
        self.topping_listbox.insert(0, self.current_topping.get(ANCHOR))
        self.topping_choices.remove(self.current_topping.get(ANCHOR))
        self.current_topping.delete(ANCHOR)

    def add_meat(self):
        self.current_meat.insert(0, self.meat_listbox.get(ANCHOR))
        self.meat_choices.append(self.meat_listbox.get(ANCHOR))
        self.meat_listbox.delete(ANCHOR)

    def remove_meat(self):
        self.meat_listbox.insert(0, self.current_meat.get(ANCHOR))
        self.meat_choices.remove(self.current_meat.get(ANCHOR))
        self.current_meat.delete(ANCHOR)

class DrinkGUI:
    ''' GUI to serve as a window to create specific types of drinks '''
    
    def __init__(self):
        self.drinks = Tk()
        self.drinks.title('Add Drinks')
        
        # variable to hold user choices
        self.size_var=StringVar(self.drinks)
        self.size_var.set('Small')
        self.type_var=StringVar(self.drinks)
        self.type_var.set('Water')
        
        # Frame for size types
        self.size_frame = Frame(self.drinks)
        self.size_label = Label(self.size_frame, text = 'Select a size')
        
        # Create button options for size choices
        self.small = Radiobutton(self.size_frame, text = 'Small', variable = self.size_var, value = 'Small')
        self.medium= Radiobutton(self.size_frame, text = 'Medium', variable = self.size_var, value = 'Medium')
        self.large = Radiobutton(self.size_frame, text = 'Large', variable = self.size_var, value = 'Large')

        self.size_label.grid(row = 0, column = 0, sticky = W)
        self.small.grid(row = 1, column = 0, sticky = W)
        self.medium.grid(row = 2, column = 0, sticky = W)
        self.large.grid(row = 3, column = 0, sticky = W)

        # Frame for drink types
        self.type_frame = Frame(self.drinks)
        self.type_label = Label(self.type_frame, text = 'Select a drink')
        
        # Create button options for drink type choices
        self.water = Radiobutton(self.type_frame, text = 'Water', variable = self.type_var, value = 'Water')
        self.pepsi = Radiobutton(self.type_frame, text = 'Pepsi', variable = self.type_var, value = 'Pepsi')
        self.coke = Radiobutton(self.type_frame, text = 'Coke', variable = self.type_var, value = 'Coke')
        self.sprite = Radiobutton(self.type_frame, text = 'Sprite', variable = self.type_var, value = 'Sprite')
        self.dr_pepper= Radiobutton(self.type_frame, text = 'Dr. Pepper', variable = self.type_var, value = 'Dr. Pepper')
        self.fanta = Radiobutton(self.type_frame, text = 'Fanta', variable = self.type_var, value = 'Fanta')
        self.diet_pepsi = Radiobutton(self.type_frame, text = 'Diet Pepsi', variable = self.type_var, value = 'Diet Pepsi')
        self.diest_coke = Radiobutton(self.type_frame, text = 'Diet Coke', variable = self.type_var, value = 'Diet Coke')
        self.diet_dr_pepper = Radiobutton(self.type_frame, text = 'Diet Dr. Pepper', variable = self.type_var, value = 'Diet Dr. Pepper')

        self.type_label.grid(row = 0, column = 0, sticky = W)
        self.water.grid(row = 1, column = 0)
        self.pepsi.grid(row = 2, column = 0)
        self.coke.grid(row = 3, column = 0)
        self.sprite.grid(row = 4, column = 0)
        self.dr_pepper.grid(row = 5, column = 0)
        self.fanta.grid(row = 1, column = 1)
        self.diet_pepsi.grid(row = 2, column = 1)
        self.diest_coke.grid(row = 3, column = 1)
        self.diet_dr_pepper.grid(row = 4, column = 1)

        # Frame for buttons
        self.button_frame = Frame(self.drinks)
        self.confirm = Button(self.button_frame, text = "Confirm", command = self.confirm)
        self.cancel = Button(self.button_frame, text = "Cancel", command = self.close_window)
        self.confirm.grid(row = 0, column = 0)
        self.cancel.grid(row = 0, column = 1)
        
        # place frames on grid
        self.size_frame.grid(row = 0, column = 0, sticky = NW)
        self.type_frame.grid(row = 0, column = 2, sticky = NE)
        self.button_frame.grid(row = 1, column = 0)

    def close_window(self):
        response = messagebox.askyesno('Confirmation', 'Are you sure you want to cancel?')
        if response == True:
            self.drinks.destroy()
            
    def confirm(self):
        response = messagebox.askyesno('Confirmation', 'Are you ok with your selections?')
        if response == True:
            temp = dr.Drink()
            size = self.size_var.get()
            choice = self.type_var.get()
            if self.size_var.get() == 'Small':
                price = 1.00
            elif self.size_var.get() == 'Medium':
                price = 1.29
            elif self.size_var.get() == 'Large':
                price = 1.49
            price = price + (price * .05)
            temp.size = size
            temp.choice = choice
            temp.price = price
            
            drink_list.append(temp)
            self.drinks.destroy()
        elif response == False:
            
            self.drinks.lift()
            
if __name__ == '__main__':
    my_gui = Start()
