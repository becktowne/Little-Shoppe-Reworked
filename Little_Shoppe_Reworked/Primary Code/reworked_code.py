import tkinter as tk
import csv
from PIL import ImageTk
import os
from tkinter import messagebox

os.chdir("Little_Shoppe_Reworked")

#Create the log in page
def make_logIn():
    global login_window
    login_window = tk.Tk()
    login_window.title("Little Shoppe")
    login_window.geometry("800x400")
    login_window.configure(bg = "#D58936")
    login_window.resizable(width = False, height = False)

    Top = tk.Frame(login_window, bg = "#D58936", height = 100, width = 800)
    Body = tk.Frame(login_window, bg = "#D58936", height = 200, width = 800)
    Bottom = tk.Frame(login_window, bg = "#D58936", height = 200, width = 800)

    Top.grid(row = 0, sticky = "ew")
    Body.grid(row = 1, sticky = "nsew")
    Bottom.grid(row = 2, sticky = "ew")

    #Label the username entry field
    lblUsername = tk.Label(Body, text = "Username:", fg = "#3C1518", bg = "#D58936", font = ("Book Antiqua", 17, "bold"))
    lblUsername.grid(row = 0, column = 0, pady = 10, padx = 60)

    #Create entry field for username
    global enterUsernameInput
    enterUsernameInput = tk.Entry(Body, fg = "#D58936", bg = "#A44200", width = 25, font = ("Book Antiqua", 20))
    enterUsernameInput.grid(row = 0,column = 1)

    #Label the password entry field
    lblPassword = tk.Label(Body, text = "Password:", fg = "#3C1518", bg = "#D58936", font = ("Book Antiqua", 17, "bold"))
    lblPassword.grid(row = 3, column = 0, pady = 35, padx = 60)

    #Create entry field for password
    global enterPasswordInput
    enterPasswordInput = tk.Entry(Body, fg = "#D58936", bg = "#A44200", width = 25, font = ("Book Antiqua", 20), show = "*")
    enterPasswordInput.grid(row = 3, column = 1)

    #Title the login page
    title = tk.Label(Top, text = "Little Shoppe Login", fg = "#D58936", bg = "#69140E", font = ("Book Antiqua", 40, "bold", "italic"), justify="center")
    title.grid(row = 0, column = 0, pady = 50, padx = 165)

    #Create exit button that can close the login window
    exitButton = tk.Button(text = "X", width = 3, height = 1, bg = "#A44200", fg = "#3C1518", font = ("Arial", 25), command = login_window.destroy)
    exitButton.grid(row = 0, column = 0, pady = 0, padx = 700)

    #Create button that executes login command
    loginButton = tk.Button(Bottom, text = "LOG IN", width = 10, height = 1, bg = "#F2F3AE", fg = "#A44200", justify = "center", font = ("Book Antiqua", 14, "bold"), command = login)
    loginButton.grid(row = 0, column = 3, pady = 0, padx = 350)

#Creates the main window and all visual contents within
def make_window():
    main=tk.Tk()
    main.title("Little Shoppe")
    main.geometry("1280x640")
    main.configure(bg = "#D58936")

    #create title text, center it at top of page
    Title = tk.Label(main, text = "Little Shoppe", fg = "#3c1518", bg = "#D58936", anchor = "center", font = ("Book Antiqua", 40))
    Title.grid(row = 0, column = 1)

    #create frame within content, user and shop lists will go in this frame
    shopFrame = tk.Frame(main, bg = "#f2f3ae", width = 390, height = 450)
    shopFrame.grid(row = 1, column = 0, rowspan = 2, padx = 15, pady = 15)

    #create frame for tabs at the top of the "left" frame, tabs allow user to switch between the store and users tab
    shopTabs = tk.Frame(shopFrame, bg = "#f2f3ae", width = 390, height = 100)
    shopTabs.grid(row = 0, column = 0, sticky = "ew", columnspan = 2)

    #Default configuration of the left frame tabs
    global storeTab
    storeTab = tk.Button(shopTabs, text = "Store", command = show_store, width = 10, height = 1, font = ("Book Antiqua", 15))
    storeTab.grid(row = 0, column = 0, padx = 0, sticky = "ew")

    if (isAdmin):
        global usersTab
        usersTab = tk.Button(shopTabs, text = "Users", command = show_middle, width = 10, height = 1, font = ("Book Antiqua", 15))
        usersTab.grid(row = 0, column = 1, padx = 0, sticky = "ew")
    else:
        global favoritesTab
        favoritesTab = tk.Button(shopTabs, text = "Favorites", command = show_middle, width = 10, height = 1, font = ("Book Antiqua", 15))
        favoritesTab.grid(row = 0, column = 1, padx = 0, sticky = "ew")

    global requestsTab
    requestsTab = tk.Button(shopTabs, text = "Requests", command = show_requests, width = 10, height = 1, font = ("Book Antiqua", 15))
    requestsTab.grid(row = 0, column = 2, padx = 0, sticky = "ew")

    #make a listbox to contain the content within the list (both store list and user list)
    shopList = tk.Listbox(shopFrame, height = 23, bg = "#f2f3ae", width=60)
    shopList.grid(column = 0, row = 1, sticky = "nsew")

    #add scrollbar and link it to the listbox
    shopScrollbar = tk.Scrollbar(shopFrame, orient = "vertical")
    shopScrollbar.grid(row = 1, column = 1, sticky = "ns")
    shopList.config(yscrollcommand = shopScrollbar.set)
    shopScrollbar.config(command = shopList.yview)

    #create frame to contain the information and action frames
    shopkeepFrame = tk.Frame(main, bg = "#D58936", width = 400, height = 450)
    shopkeepFrame.grid(row = 1, column = 2, rowspan = 2, padx = 15)

    #create frame for information
    information = tk.Frame(main, bg = "green", width = 400, height = 215)
    information.grid(row = 1, column = 1, padx = 15)

    info_body = tk.Frame(information, bg = "green", width = 400, height = 215)
    info_body.grid(row = 1, column = 0, sticky = "nsew")

    #Header for information
    infoHeader = tk.Label(information, bg = "#69140e", fg = "#d58936", text = "Information", font = ("Book Antiqua", 15), width = 32, height = 2)
    infoHeader.grid(row = 0, sticky = "ew")
    infoHeader.grid_rowconfigure(400, weight = 1)

    #Make listbox for information
    infoListbox = tk.Listbox(info_body, height = 10, width = 62, bg = "#f2f3ae")
    infoListbox.grid(column = 0, row = 0, sticky = "nsew")
    infoListbox.grid_rowconfigure(390, weight = 1)

    #Create scrollbar and link it to information listbox
    infoScrollbar=tk.Scrollbar(info_body, orient = "vertical")
    infoScrollbar.grid(row = 0, column = 1, sticky = "ns")
    infoListbox.config(yscrollcommand = infoScrollbar.set)
    infoScrollbar.config(command = infoListbox.yview)

    #Create frame for our shopkeeper, benjamin
    imgFrame = tk.Frame(shopkeepFrame, bg = "#D58936", width = 375, height = 200, borderwidth = 2, relief = "solid")
    imgFrame.grid(row = 0, column = 0)

    #Create frame for Benjamin's name
    name_frame = tk.Frame(shopkeepFrame, bg="#D58936", width = 375, height = 100)
    name_frame.grid(row = 1, column = 0, pady = 10)
    name_frame.grid_rowconfigure(375, weight=1)

    #Label for benjamin little's name
    benName = tk.Label(name_frame, text="Benjamin Little", fg="#3c1518", bg="#f2f3ae", anchor="center", font=("Book Antiqua", 25, "bold"), width = 17, borderwidth = 2, relief = "solid")
    benName.grid(row=0, column=0, sticky="ew", pady=2)

    ben_text = tk.Label(name_frame, text = "Welcome to my humble shop! My name's Benjamin Little.\nI'll get yer shoppin' done in time as \"little\" as my name!", bg = "#69140e", fg = "#d58936", width = 38, height = 6, font = ("Book Antiqua", 12, "bold"), wraplength = 350, justify = "center")
    ben_text.grid(row=1, column=0)

    #Place and format benjamin image
    benjamin_canvas = tk.Canvas(imgFrame, height = 275, width = 375)
    benjamin_canvas.pack()
    benjamin_image = ImageTk.PhotoImage(file = "image001.png", master = benjamin_canvas)
    benjamin_canvas.image = benjamin_image
    benjamin_canvas.create_image((0,0), image=benjamin_image, anchor="nw")
    
    #Create search button
    #TODO create show_search command
    searchButton = tk.Button(shopFrame, text = "Search", command ="showSearch", bg = "#a44200", fg = "#d58936", width = 31, height = 1, font = ("Book Antiqua", 15), borderwidth=6, relief="raised")
    searchButton.grid(row = 3, column = 0, columnspan = 2)

    #Create frame for action buttons
    actions=tk.Frame(main, bg = "#f2f3ae", width = 400, height = 215)
    actions.grid(row = 2, column = 1, padx = 15)

    #Header for action buttons
    actionsHeader = tk.Label(actions, bg = "#69140e", fg = "#d58936", text = "Actions", font = ("Book Antiqua", 15), width = 32, height = 2)
    actionsHeader.grid(row = 0, sticky = "ew")

    #Creates the frame that action buttons will be placed within
    actionsBody = tk.Frame(actions, bg="#f2f3ae", width=32, height=12)
    actionsBody.grid(row=1, column=0, sticky="ew")

    #Default action buttons configured below
    global addButton
    addButton = tk.Button(actionsBody, text = "Add Item", bg = "#D58936", width = 23, height = 3, font = ("Book Antiqua", 8))
    addButton.grid(row = 0, column = 0, padx = 15, pady = 10)

    global showButton
    showButton = tk.Button(actionsBody, text = "Show Item", bg = "#D58936", width = 23, height = 3, font = ("Book Antiqua", 8))
    showButton.grid(row = 1, column = 1, padx = 15, pady = 10)

    global removeButton
    removeButton = tk.Button(actionsBody, text = "Remove Item", bg = "#D58936", width = 23, height = 3, command = "remItem", font = ("Book Antiqua", 8))
    removeButton.grid(row = 0, column = 1, padx = 15, pady = 10)

    global editButton
    editButton = tk.Button(actionsBody, text = "Edit Item", bg = "#D58936", width = 23, height = 3, command = "editItm", font = ("Book Antiqua", 8))
    editButton.grid(row = 1, column = 0, padx = 15, pady = 10)

    #Frame below main content, used to contain the logout and about us buttons
    bottom = tk.Frame(main, bg = "#D58936", width = 960, height = 100)
    bottom.grid(row = 3, column = 1, pady=5)

    #Button that can pull up the log out window
    #TODO create logout_prompt func
    logoutButton = tk.Button(bottom, bg = "#69140e", fg = "#d58936", text = "Log Out", command ="logoutPrompt", font = ("Book Antiqua", 15), width = 13, height = 1)
    logoutButton.grid(row = 1, column = 1, padx = 20)

    #Button that opens the about us page
    #TODO create open_about_us func
    about_us_button=tk.Button(bottom, bg="#69140e", fg="#d58936", text="About Us", command="openAboutUs", font=("Book Antiqua", 15), width=13, height=1)
    about_us_button.grid(row=1, column=0, padx=20)

    show_store()

#Check if the usernames and passwords are correct, log in the user if true
def login():
    with open("credentials.csv",mode="r") as file:
        users = csv.reader(file)
        logged = False
        #Check if the user is a guest or admin
        global isAdmin
        isAdmin = 0
        for user in users:
            if (user!= []):
                if (enterUsernameInput.get().lower() == user[0].lower() and enterPasswordInput.get() == user[1] and user[2] == "admin"):
                    #If admin, create admin window
                    make_window()
                    login_window.destroy()
                    logged=True
                    isAdmin = 1
                    break
                elif (enterUsernameInput.get().lower() == user[0].lower() and enterPasswordInput.get() == user[1] and user[2] == "guest"):
                    #If guest, create guest window
                    make_window()
                    login_window.destroy()
                    global username
                    username = user[0]
                    logged=True
                    break
        #If login unsuccessful, show error explaining this to user
        if not logged:
            messagebox.showinfo("Contacts", "Invalid Username or Password")

#The program should always start by creating the login
make_logIn()

#This function opens the store tab, changing the tab colors and action buttons to reflect this
def show_store():
    #refresh_info()

    storeTab.configure(bg = "#69140e", fg = "#d58936")

    requestsTab.configure(bg = "#a44200", fg = "#d58936")

    if (isAdmin):
        usersTab.configure(bg = "#a44200", fg = "#d58936")
        addButton.configure(text = "Add Item", command = "add_item")
        editButton.configure(text = "Edit Item", command = "edit_item")
        removeButton.configure(text = "Remove Item", command = "remove_item")
        showButton.configure(text = "Item Info", command = "show_item")
    else:
        favoritesTab.configure(bg = "#a44200", fg = "#d58936")
        addButton.configure(text = "Add Favorite", command = "add_favorite")
        editButton.configure(text = "Request Item", command = "request_item")
        removeButton.configure(text = "Remove Favorite", command = "remove_favorite")
        showButton.configure(text = "Item Info", command = "show_item")

    #set_items()
        
#This function opens the requests tab, changing the tab colors and action buttons to reflect this
def show_requests():
    #refresh_info()

    storeTab.configure(bg = "#a44200", fg = "#d58936")

    requestsTab.configure(bg = "#69140e", fg = "#d58936")

    if (isAdmin):
        usersTab.configure(bg = "#a44200", fg = "#d58936")
        addButton.configure(text = "Accept Request", command = "accept_request")
        editButton.configure(text = "Counteroffer", command = "edit_request")
        removeButton.configure(text = "Deny Request", command = "deny_request")
        showButton.configure(text = "Request Info", command = "show_request")
    else:
        favoritesTab.configure(bg = "#a44200", fg = "#d58936")
        addButton.configure(text = "Request History", command = "show_request_history")
        editButton.configure(text = "Edit Request", command = "request_item")
        removeButton.configure(text = "Delete Request", command = "remove_favorite")
        showButton.configure(text = "Request Info", command = "show_request")

    #set_items()

#This function opens either the users or favorites tab, depending on whether or not the user is an admin
def show_middle():
    #refresh_info()

    storeTab.configure(bg = "#a44200", fg = "#d58936")

    requestsTab.configure(bg = "#a44200", fg = "#d58936")

    if (isAdmin):
        usersTab.configure(bg = "#69140e", fg = "#d58936")
        addButton.configure(text = "Add User", command = "add_user")
        editButton.configure(text = "Change Password", command = "edit_user")
        removeButton.configure(text = "Delete User", command = "delete_user")
        showButton.configure(text = "User Info", command = "show_user")
    else:
        favoritesTab.configure(bg = "#69140e", fg = "#d58936")
        addButton.configure(text = "Add Favorite", command = "add_favorite")
        editButton.configure(text = "Request Item", command = "request_item")
        removeButton.configure(text = "Remove Favorite", command = "remove_favorite")
        showButton.configure(text = "Item Info", command = "show_request")

    #set_items()

tk.mainloop()
