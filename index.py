from tkinter import *
from api import post_mindee_api
from extract_data import parse

def inital_form_submit():
    if path_of_image_field.get() == "":
        print("Empty Field - Cannot Continue")
    else:
        response = post_mindee_api( path_of_image_field.get() )
        parse( response.text )

if __name__ == "__main__":
    # create a GUI window
    root = Tk()

    # set the background colour of GUI window
    root.configure(background='light green')

    # set the title of GUI window
    root.title("registration form")

    # set the configuration of GUI window
    root.geometry("750x300")

    # create Form Labels
    heading = Label(root, text="Receipt Form", bg="light green")
    number_of_people = Label( root, text="Number of People", bg="light green")
    path_of_image = Label( root, text="Path of Image", bg="light green")

    # grid out the labels
    heading.grid(row=0, column=1)
    number_of_people.grid( row=1, column=0)
    path_of_image.grid( row=2, column=0)

    # create Form Fields
    number_of_people_field = Entry(root)
    path_of_image_field = Entry(root)

    # grid out Form Fields
    number_of_people_field.grid(row=1, column=1, ipadx="100")
    path_of_image_field.grid(row=2, column=1, ipadx="100")

    # create a Submit Button and place into the root window
    submit = Button(root, text="Submit", fg="Black",
                    bg="Red", command=inital_form_submit)
    submit.grid(row=3, column=1)

    # start the GUI
    root.mainloop()