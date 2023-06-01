import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os

win = tk.Tk()
win.title('GUI')

# create labels
name_label = ttk.Label(win, text='Enter your name : ')
name_label.grid(row=0, column=0, sticky=tk.W)
# to change colour
name_label.configure(foreground='blue')

email_label = ttk.Label(win, text='Enter your email : ')
email_label.grid(row=1, column=0, sticky=tk.W)
email_label.configure(foreground='red')

age_label = ttk.Label(win, text='Enter your age : ')
age_label.grid(row=2, column=0, sticky=tk.W)
age_label.configure(foreground='pink')

gender_label = ttk.Label(win, text='select your gender : ')
gender_label.grid(row=3, column=0)
gender_label.configure(foreground='brown')

# create entry box
name_var = tk.StringVar()
name_entry_box = ttk.Entry(win, width=16, textvariable=name_var)
name_entry_box.grid(row=0, column=1)
name_entry_box.focus()

email_var = tk.StringVar()
email_entry_box = ttk.Entry(win, width=16, textvariable=email_var)
email_entry_box.grid(row=1, column=1)

age_var = tk.StringVar()
age_entry_box = ttk.Entry(win, width=16, textvariable=age_var)
age_entry_box.grid(row=2, column=1)

# create radio buttons
# student, Teacher
usertype = tk.StringVar()
radio_button1 = ttk.Radiobutton(win, text='student', value='student', variable=usertype)
radio_button1.grid(row=4, column=0)

radio_button2 = ttk.Radiobutton(win, text='Teacher', value='Teacher', variable=usertype)
radio_button2.grid(row=4, column=1)

# check button
check_btn_var = tk.IntVar()
check_btn = ttk.Checkbutton(win, text='check if you want to subscribe', variable=check_btn_var)
check_btn.grid(row=5, columnspan=2)

# create combo box
gender_var = tk.StringVar()
gender_combo_box = ttk.Combobox(win, width=13, textvariable=gender_var, state='readonly')
gender_combo_box['values'] = ('male', 'Female', 'others')
gender_combo_box.current(0)
gender_combo_box.grid(row=3, column=1)

# to print what we typed in the name,age,email boxes


def action():
    user_name = name_var.get()
    user_email = email_var.get()
    user_age = age_var.get()
    user_gender = gender_var.get()
    user_type = usertype.get()
    if check_btn_var.get() == 0:
        subscribed = 'Not Subscribed'
    else:
        subscribed = 'Yes Subscribed'
    print(f'{user_name} is {user_age} years old, email is {user_email}, gender is {user_gender},'
          f'type is {user_type} and {subscribed}')

    # to store in a file
    with open('file.txt', 'a', newline='') as f:
        f.write(f'{user_name} is {user_age} years old, email is {user_email}, gender is {user_gender},'
                f'type is {user_type} and {subscribed}\n')

    # to write in a csv file
    with open('file.csv', 'a', newline='') as f:
        dict_writer = DictWriter(f, fieldnames=['User Name', 'User Email address', 'User Age',
                                                'User Gender', 'User Type', 'subscribed'])
        if os.stat('file.csv').st_size == 0:
            dict_writer.writeheader()
        dict_writer.writerow({
             'User Name': user_name,
             'User Email address': user_email,
             'User Age': user_age,
             'User Gender': user_gender,
             'User Type': user_type,
             'subscribed': subscribed
        })
    # to clear typed information from the boxes after submitting
    name_entry_box.delete(0, tk.END)
    email_entry_box.delete(0, tk.END)
    age_entry_box.delete(0, tk.END)

# create buttons


submit_button = ttk.Button(win, text='submit', command=action)
# to change colour of submit button you
# have to write tk instead of ttk
# because foreground is not available in submit button but is available in tk
submit_button.grid(row=6, column=0)


win.mainloop()
