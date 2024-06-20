import tkinter as tk  # Import the tkinter module and alias it as tk
from time import time # Importing time for measuring the time spent for typing
from tkinter import messagebox # Importing messagebox from tkinter, later used for showing the results

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root  # Store the root window reference
        self.root.title("Typing Speed Test App")  # Set the window title
        self.root.geometry("800x400")  # Set the default window size
        self.root.configure(bg="#FF7F3E") # Setting a background color for the window
        self.root.maxsize(800, 400)  # Set the maximum window size
        
        windLabel = tk.Label(root, text='Welcome to Typing Speed Test App!', bg="#604CC3", font=("Arial", 14, "bold"), borderwidth=2, relief="raised", fg="white") # Creating a label for the window and styling it a bit
        windLabel.pack(pady=10)  # Add it to root and packing it with some padding around it
        
        self.text_area = tk.Text(root, height=15, width=80) # Creating a text ared widget for user input
        self.text_area.pack() # Adding it to root and packing it
        self.text_area.config(state=tk.DISABLED) # Intentionally disabling the text area to prevent typing before user clicks Start button

        self.start_button = tk.Button(root, text="Start Typing", command=self.start_typing) # Creating button to start the typing session by calling start_typing method when clicked
        self.start_button.pack() # Adding it to root and packing it

        self.finish_button = tk.Button(root, text="Finish", command=self.finish_typing) # Creating a button to end the typing session by calling finish_typing method when clicked
        self.finish_button.config(state=tk.DISABLED) # Disabling the finish button so that it is unclickable before the start of the typing session
        self.finish_button.pack() # Adding it to root and packing it

    def start_typing(self): # Method which starts the typing session
        self.start_time = time() # Taking the start time of the session
        self.input_text = [] # Empty list for storing the input text
        self.text_area.config(state=tk.NORMAL) # Changing state of text area back to normal which allows the user to type something in it
        self.text_area.delete(1.0, tk.END) # Clearing the text area just in case if there was some text in it
        self.start_button.config(state=tk.DISABLED) # Disabling the start button for unintentionally resetting the session (making it unclickable)
        self.finish_button.config(state=tk.NORMAL) # Enabling the finish button to be clickable


    def finish_typing(self): # Method which ends the typing session and contains the needed calculations
        self.end_time = time() # Taking the end time of the session
        self.total_time = round((self.end_time - self.start_time) / 60, 2) # Calculating the total time in minutes and rounding it to 2 floating points
        self.input_text = self.text_area.get(1.0, tk.END).strip() # Taking the input from text area starting from the first line till the end(1.0, tk.END) and removing whitespaces
        self.overall_words_count = len(self.input_text.split()) # Taking words by splitting the input text and assigning its length (which gives us the number of words) and assigning it to variable
        self.wpm = round(self.overall_words_count/ self.total_time,2) # Calculating the wpm by dividing word count to time spent and rounding it to 2 floating points
        
        if(self.wpm>=0 and self.wpm<40): # Deciding on result message based on WPM score
            self.wpm_message = "Below average, but you can improve with more practice!"
        elif(self.wpm>=40 and self.wpm<60):
            self.wpm_message = "You have average typing speed for most people!"
        elif(self.wpm>=60 and self.wpm<80):
            self.wpm_message = "Above average, your wpm is suitable for most professional work!"
        else:
            self.wpm_message = "Excellent, you can handle most high-speed typing tasks efficiently!"
            
        messagebox.showinfo("Results", f"You spent {self.total_time} in minutes in total\n"
                                          f"You entered {self.overall_words_count} words in total\n"
                                          f"Your WPM is: {self.wpm}. {self.wpm_message}") # Showing the results in a new messagebox
        
        self.start_button.config(state=tk.NORMAL) # Setting the state of start button back to normal (clickable)
        self.finish_button.config(state=tk.DISABLED) # Setting the state of the finish button to disabled (unclickable)
        self.text_area.config(state=tk.DISABLED) # Setting the state of the text area to disabled (prevent typing)
        
# Create the main application window
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = TypingSpeedTestApp(root)  # Create an instance of the TypingSpeedTestApp class
    root.mainloop()  # Start the Tkinter event loop to keep the window open and responsive