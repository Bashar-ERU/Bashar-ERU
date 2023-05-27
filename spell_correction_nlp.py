#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


from tkinter import *
from textblob import TextBlob

# Define the clearAll() function.
def clearAll():

    # Delete the text from the input and corrected word fields.
    word1_field.delete(0, END)
    word2_field.delete(0, END)

# Define the correction() function.
def correction():

    # Get the word from the input field.
    input_word = word1_field.get()

    # Create a TextBlob object from the word.
    blob_obj = TextBlob(input_word)

    # Get the corrected word from the TextBlob object.
    corrected_word = str(blob_obj.correct())

    # Insert the corrected word into the corrected word field.
    word2_field.insert(0, corrected_word)

# Define the main() function.
if __name__ == "__main__":

    # Create a root window.
    root = Tk()

    # Configure the root window.
    root.configure(background = "light blue")
    root.geometry("600x300")
    root.title("Spell Corrector")

    # Create a label for the input word.
    headlabel = Label(root, text = "Welcome to Spell Corrector", fg = "black", bg = "red")
    headlabel.config(font=("Roboto"))

    # Create a label for the corrected word.
    label1 = Label(root, text = "Input Word", fg = "black", bg = "light green")
    label1.config(font=("Roboto"))

    # Create a label for the corrected word.
    label2 = Label(root, text = "Corrected Word", fg = "black", bg = "light green")
    label2.config(font=("Roboto"))

    # Place the labels on the root window.
    headlabel.grid(row = 0, column = 1)
    label1.grid(row = 1, column = 0)
    label2.grid(row = 3, column = 0, padx = 10)

    # Create an entry field for the input word.
    word1_field = Entry()

    # Create an entry field for the corrected word.
    word2_field = Entry()

    # Place the entry fields on the root window.
    word1_field.grid(row = 1, column = 1, padx = 10, pady = 10)
    word2_field.grid(row = 3, column = 1, padx = 10, pady = 10)

    # Create a button for the correction function.
    button1 = Button(root, text = "Correction", bg = "red", fg = "black", command = correction)

    # Place the button on the root window.
    button1.grid(row = 2, column = 1)

    # Create a button for the clearAll() function.
    button2 = Button(root, text = "Clear", bg = "red", fg = "black", command = clearAll)

    # Place the button on the root window.
    button2.grid(row = 4, column = 1)

    # Start the main loop.
    root.mainloop()


# In[ ]:





# In[ ]:




