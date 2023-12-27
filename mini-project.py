import tkinter as tk
class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        
        self.display = tk.Entry(self.master, width=100,font=20, justify="right") #creates an entry box(answer display box) for the wndow(self.master) with given parameters,justify property is used to align the content(numbers) not the bix
        self.display.grid(row=0, column=0,columnspan=4) 
        
        # create buttons for digits and operators
        button_list = [
            "7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", ".", "C", "+", "="
        ]
 
        row_index = 2      #starting from 3rd row of the grid
        col_index = 0      #starting from 0th col of the grid
        
        for button_text in button_list:
            #Displaying the buttons
            button = tk.Button(self.master, text=button_text, width=10, height=5,
                               command=lambda text=button_text: self.button_click(text)) 
            #command property displays what happens when the button is clicked
            #The lambda keyword is used to define an anonymous function. In this case, the text=button_text parameter sets a default value for the text parameter of the anonymous function
            #the lambda function after determinig the parameter calls the button_click function with parameter text 
            button.grid(row=row_index, column=col_index, padx=5, pady=5)  #converts the entire window into grid.padx and pady are for the entre grid wrt window.
            
            col_index += 1
            if col_index > 3:
                col_index = 0
                row_index += 1
                
    def button_click(self, text):
        if text == "C":
            self.display.delete(0, tk.END)
        elif text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                # The first argument to delete specifies the starting index of the range to be deleted, and the second argument specifies the ending index of the range to be deleted.
                #0-first index and tk.END-last index
                self.display.insert(0, str(result))
            except:
                #If the content(numbers+symbols) is not arranged correctly
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        else:
            #Make the entry in the display section
            self.display.insert(tk.END, text)
            
# creating the main window
root = tk.Tk()

# creating the calculator app
#creating the instance and passing in the root window object as an argument. This allows the Calculator class to know which window to add the calculator display and buttons to.
#it acts as a void function which creates changes in root
Calculator(root)

# starting the event loop
root.mainloop()