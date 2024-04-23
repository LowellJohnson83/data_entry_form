import tkinter as tk
import customtkinter as ctk
# ttk (themed tkinter) is to create themed widget. lower case and explicit
from tkinter import ttk
# message (themed tkinter) is also lower case and therefore excplicit
from tkinter import messagebox
import ttkbootstrap as tb




# Define the pushing button function ("enter_data()")
def enter_data():
    # print("Hi!")
    accepted = accept_var.get()

    if accepted == "Accepted":

        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        title = title_combobox.get()

        if firstname and lastname and title:   
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            numcourses = numcourses_spinbox.get()
            numsemesters = numsemesters_spinbox.get()
            registration_status = reg_status_var.get()

            print(f"First Name: {firstname}. Last Name: {lastname}")
            print(f"Title: {title}. Age: {age}. Nationality: {nationality}")
            print(f"Number of Courses: {numcourses}.")
            print(f"Number of Semesters: {numsemesters}")
            print(f"Registration Status: {registration_status}")
            print("-----------------")

        else:
            tk.messagebox.showwarning(
                title="Error",
                message="You must enter both your first and last names as well as your title!"
                )
        


    else:
        tk.messagebox.showwarning(
            title="Error",
            message="You must tick the box accepting terms and conditions to proceed!"
            )
        
        print("You must tick the box accepting terms and conditions to proceed!")


# Set Global (styling) variables
pad_x_ui_frame = 20
pad_y_ui_frame = 20
pad_x_widget = 10
pad_y_widget = 5
pad_x_crs_frame = 20
pad_y_crs_frame = 10

width_box = 160
height_box = 20

font_type = "Helvetica"
font_size = 12



window = ctk.CTk()
window.title("Data Entry Form")

frame = ctk.CTkFrame(window)
frame.pack()

# Will be part of the frame, not the window (gves it a nice border)
# Saving User Info
user_info_frame = tk.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=pad_x_ui_frame, pady=pad_y_ui_frame)

first_name_label = ctk.CTkLabel(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tk.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = ctk.CTkEntry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry = ctk.CTkEntry(user_info_frame)
last_name_entry.grid(row=1, column=1)

title_label = tk.Label(user_info_frame, text="Title")
title_label.grid(row=0, column=2)
title_combobox = ttk.Combobox(user_info_frame, values=["Mr.", "Mrs.", "Master", "Ms.", "Dr.", "Sir", "Dame"])
title_combobox.grid(row=1, column=2)

age_label = ctk.CTkLabel(user_info_frame, text="Age")
age_label.grid(row=2, column=0)
age_spinbox = tb.Spinbox(
    user_info_frame,
    bootstyle="success",
    size = (width_box, height_box)
    font=(font_type,font_size),
    from_=18, to=110
    )

test = tb.Spinbox()

age_spinbox.grid(row=3, column=0)

nationality_label = ctk.CTkLabel(user_info_frame, text="Nationality")
nationality_label.grid(row=2, column=1)
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving course info
# "news" below is actually an acronym for 'North, East, South and West'
courses_frame = tk.LabelFrame(frame)
courses_frame.grid(
    row=1,column=0, sticky="news",
    # padx=pad_x_ui_frame, pady=pad_y_ui_frame,
    )

registered_label = ctk.CTkLabel(courses_frame, text="Registration Status")
registered_label.grid(row=0, column=0)
registered_check = ctk.CTkCheckBox(
    courses_frame, text="Currently Registered")
registered_check.grid(row=1, column=0)


reg_status_var = ctk.StringVar(value="Not Registered")

numcourses_label = ctk.CTkLabel(courses_frame, text= "# Completed Courses")
numcourses_label.grid(row=0, column=1)
numcourses_spinbox = tb.Spinbox(
    courses_frame,
    bootstyle="success",
    font=(font_type,font_size),
    from_=0, to='infinity'
    )
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = ctk.CTkLabel(courses_frame, text="# Semesters")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox = tb.Spinbox(
    courses_frame,
    bootstyle="success",
    font=(font_type,font_size),
    from_=0, to="infinity"
    )
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=pad_x_widget, pady=pad_y_widget)


# Accept Terms
terms_frame = tk.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(
    row=2, column=0, sticky="news",
    padx=pad_x_widget,
    pady=pad_y_widget)

accept_var = ctk.StringVar(value="Not Accepted")
terms_check = ctk.CTkCheckBox(
    terms_frame,
    text= "I accept the terms and conditions.",
    variable=accept_var,
    onvalue="Accepted",
    offvalue="Not Accepted",
    )
terms_check.grid(row=0, column=0)


# Button
button = ctk.CTkButton(frame, text="Enter data", command= enter_data)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)


window.mainloop()