import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import csv
global userInput
global passInput
global passwords
global fn
global window
global benjamin
global infoBody
global itemInfo

#create admin window, 1280x640, non resizable
def make_admin():
    global information
    window.destroy()
    root=tk.Tk()
    root.title('Little Shoppe')
    root.geometry("1280x640")
    root.configure(bg='#D58936')
    root.resizable(False, False)

    #create title text, center it at top of page
    Title=tk.Label(root, text="Little Shoppe", fg="#3c1518", bg="#D58936", anchor="center", font=("Book Antiqua", 40))
    Title.grid(columnspan=2, row=0, column=1, sticky="ew", pady=10)

    #create content frame below title text, all main content will be placed within this frame
    content=tk.Frame(root, bg='#D58936')
    content.grid(row=1, column=1)

    #create frame within content, user and shop lists will go in this frame
    left=tk.Frame(content, bg="#f2f3ae", width=400, height=450)
    left.grid(row=0, column=0, rowspan=2, padx=15, pady=15)

    #create frame for tabs at the top of the "left" frame, tabs allow user to switch between the store and users tab
    leftButtons=tk.Frame(left, bg="#f2f3ae", width=390, height=100)
    leftButtons.grid(row=0, column=0, sticky="ew")

    #create a frame for the list, essentially just sets a consistent size for the listbox, no matter the number of listed items
    userList= tk.Frame(left, bg="#f2f3ae", width=382, height=350)
    userList.grid(row=1, column=0, sticky="nsew")

    #make a listbox to contain the content within the list (both store list and user list)
    shopList=tk.Listbox(userList,height=23)
    shopList.grid(column=0,row=0,sticky='nsew')
    shopList.config(bg="#f2f3ae")
    #add scrollbar and link it to the listbox
    sBar=tk.Scrollbar(userList,orient="vertical")
    sBar.grid(row=0, column=1, sticky="ns")
    shopList.config(yscrollcommand=sBar.set)
    sBar.config(command=shopList.yview)

    #create frame to contain the information and action frames
    right=tk.Frame(content, bg="#D58936", width=400, height=450)
    right.grid(row=0,column=3,rowspan=2, padx=15)

    #create frame for information
    information=tk.Frame(content, bg="green", width=400, height=205)
    information.grid(row=0, column=2, padx=15, pady=8)

    #Header for information
    infoHeader=tk.Label(information, bg="#69140e", fg="#d58936", text="Information", font=("Book Antiqua", 15), width=32, height=2)
    infoHeader.grid(row=0,sticky="ew")

    #Body frame, will contain actual information
    infoBody=tk.Frame(information, width=32, height=205)
    infoBody.grid(row=1, column=0, sticky="nsew")

    #Make listbox for information
    itemInfo=tk.Listbox(infoBody,height=8)
    itemInfo.grid(column=0,row=0,sticky='nsew')
    itemInfo.config(bg="#f2f3ae")

    #Create scrollbar and link it to information listbox
    ssBar=tk.Scrollbar(infoBody,orient="vertical")
    ssBar.grid(row=0, column=2, sticky="ns")
    itemInfo.config(yscrollcommand=ssBar.set)
    ssBar.config(command=itemInfo.yview)

    #Create function for deleting the text within the listbox when information needs to be replaced
    def refresh_info():
        itemInfo.delete(0, tk.END)
    
    #Create frame for our shopkeeper, benjamin
    imgFrame=tk.Frame(right, bg="#D58936", width=375, height=225)
    imgFrame.grid(row=0,column=0)

    #Create frame for Benjamin's name
    nameFrame=tk.Frame(right, bg="#D58936", width=375, height=100)
    nameFrame.grid(row=1,column=0)

    #place and format benjamin image
    rawBenjamin=Image.open("image001.png")
    benjamin=rawBenjamin.resize((375,350))
    benjaminDisplay=ImageTk.PhotoImage(benjamin)
    benjaminPlace=tk.Label(imgFrame, image=benjaminDisplay, highlightbackground="#D58936", highlightthickness=2)
    benjaminPlace.image=benjaminDisplay
    benjaminPlace.grid(row=0, column=0)

    #Create function to iterate through inventory.csv and adds each line to the shop list
    def set_items():
        shopList.delete(0, tk.END)
        with open("inventory.csv",mode="r") as file:
            items = csv.reader(file)
            for item in items:
                if (item != []):
                    id1="{0}".format(item[1])
                    s=" "
                    n="{0}".format(item[0])
                    i=id1+s+n
                    shopList.insert(tk.END,i)

    #Create function to iterate through credentials.csv and add each line to the shop list
    def set_users():
            shopList.delete(0, tk.END)
            with open("credentials.csv",mode="r") as file:
                items = csv.reader(file)
                for item in items:
                    if (item != []):
                        shopList.insert(tk.END, "{0}".format(item[0]))

    #Create function to iterate through requests.csv and add each line to the shop list
    def set_requests():
            shopList.delete(0, tk.END)
            with open("requests.csv",mode="r") as file:
                items = csv.reader(file)
                for item in items:
                    if (item != []):
                        shopList.insert(tk.END, "{0}".format(item[0]))

    #This function opens the users tab, changing the tab colors and action buttons to reflect that
    def showUsers():
        refresh_info()
        storeButton.configure(bg="#a44200", fg="#d58936")
        usersButton.configure(bg="#69140e", fg="#d58936")
        requestsButton.configure(bg="#a44200", fg="#d58936")     
        
        addButton.configure(text="Add User", command=addUser)
        editButton.configure(text="Edit User", command=editUser)
        removeButton.configure(text="Remove User", command=removeUser)
        showButton.configure(text="Show User", command=showUser)

        set_users()

    #This function opens the store tab, changing the tab colors and action buttons to reflect that
    def showStore():
        refresh_info()
        storeButton.configure(bg="#69140e", fg="#d58936")
        usersButton.configure(bg="#a44200", fg="#d58936")
        requestsButton.configure(bg="#a44200", fg="#d58936")

        addButton.configure(text="Add Item", command=addItem)
        editButton.configure(text="Edit Item", command=editItem)
        removeButton.configure(text="Remove Item", command=delItem)
        showButton.configure(text="Show Item", command=showItem)

        set_items()

    #This function opens the requests tab, changing the tab colors and action buttons to reflect that
    def showRequests():
        refresh_info()
        storeButton.configure(bg="#a44200", fg="#d58936")
        usersButton.configure(bg="#a44200", fg="#d58936")
        requestsButton.configure(bg="#69140e", fg="#d58936")
        
        addButton.configure(text="Accept Request", command=acceptReq)
        editButton.configure(text="Counter offer", command=editReq)
        removeButton.configure(text="Deny Requests", command=denyReq)
        showButton.configure(text="Show Request", command=showRequests)

        set_requests()

    #Accepts requests and removes them from the requests lists
    def acceptReq():
        try:
            content = shopList.selection_get()

        except:
            tk.messagebox.showinfo("ERROR", "No request selected")
            return

        with open("requests.csv", "r") as file:
            reqs = csv.reader(file)

        newReqs = []

        for item in reqs:
            if (item != content):
                newReqs.append(item)

        with open("requests.csv","w") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerows(newReqs)

    #Denies requests and removes them from requests list
    def denyReq():
        pass

    #Allows admin to edit the details of the request, this will be sent back to the guest user who can then accept or deny the offer
    def editReq():
        pass

    #Default configuration of the left frame tabs
    storeButton=tk.Button(leftButtons, text="Store", command=showStore, width=10, height=1, font=("Book Antiqua", 15))
    storeButton.grid(row=0, column=0, padx=0, sticky="ew")

    usersButton=tk.Button(leftButtons, text="Users", command=showUsers, width=10,height=1, font=("Book Antiqua", 15))
    usersButton.grid(row=0, column=1, padx=0, sticky="ew")

    requestsButton=tk.Button(leftButtons, text="Requests", command=showRequests, width=10, height=1, font=("Book Antiqua", 15))
    requestsButton.grid(row=0, column=2, padx=0, sticky="ew")

    #Creates search box and the necessary elements within
    def showSearch():
        shopList.configure(height=18)

        #Creates the frame for the search box
        search=tk.Frame(left, width=400, height=100, bg="#D58936", highlightbackground="#69140e", highlightthickness=2)
        search.grid(row=2, column=0, sticky="s")

        #Labels the search bar and defines which elements can be entered
        searchLabel=tk.Label(search, text="Enter name of item, id, item type, or () below:", font=("Book Antiqua", 10), width=45, height=1, bg="#D58936", fg="#69140e")
        searchLabel.grid(row=1, column=1, columnspan=3, pady=2)

        #Create a text input for the search bar, let its contents be accessible globally
        global searchInput
        searchInput=tk.Text(search, width=30, height=1)
        searchInput.grid(row=2, column=0, columnspan=3, pady=10)

        #Enter button that brings up the search info in the information box
        enterSearch=tk.Button(search, width=8, height=0, text="Enter", bg="#D58936", fg="#69140e", command=createSearchInfo)
        enterSearch.grid(row=2, column=3, padx=2, pady=3)

        #Closes the search frame
        exitSearch=tk.Button(search, width=2, height=0, text="X", font=("Arial", 8), command=lambda: [search.grid_forget(), closeSearch()], bg="#69140e", fg="#f2f3ae")
        exitSearch.grid(row=0, column=4, padx=2, pady=2)

    #Used when a search has been made, displays information gathered from search in the information box
    def createSearchInfo():
        global searchDisplay
        global searchInfo

        #Create the frame for the search info to be displayed in, must be different than information box so that it can have a scrollbar
        searchInfo=tk.Frame(content, bg="#f2f3ae", width=400, height=205)
        searchInfo.grid(row=0, column=2, padx=15, pady=8)

        #Create text within the frame to contain the information found by search
        searchDisplay=tk.Text(searchInfo, height=8, width=48, bg="#f2f3ae", fg="#69140e")
        searchDisplay.grid(row=1, column=0, columnspan=3)

        #Compare searchInput to items in inventory.csv
        with open("inventory.csv",mode="r") as file:
            items = csv.reader(file)
            for item in items:
                #Check to make sure that the item isn't blank (which some are for some reason, must be fixed)
                if (item != []):
                    for i in item:
                        find=searchInput.get("1.0", END).lower().strip()
                        compareTo=i.lower().strip()
                        if find == compareTo:
                            #Format each part of the item into a string with a label
                            n="{0}".format(item[0])
                            nameInfo='NAME: '+n
                            id1="{0}".format(item[1])
                            idInfo="ID: "+id1
                            prov="{0}".format(item[2])
                            provInfo="PROVIDER: "+prov
                            loc="{0}".format(item[3])
                            locInfo="LOCATION: "+loc
                            price="{0}".format(item[4])
                            priceInfo="PRICE: "+price
                            quan="{0}".format(item[5])
                            quanInfo="QUANTITY: "+quan
                            desc="{0}".format(item[6])
                            descInfo="DESC: "+desc
                            #Print each item and label on a different line, add a separator at the end in case there are multiple results
                            itemString=f"{nameInfo}\n{idInfo}\n{provInfo}\n{locInfo}\n{priceInfo}\n{quanInfo}\n{descInfo}\n******************\n"
                            #Insert the string at the end of the text in the search display
                            searchDisplay.insert(END, itemString)
        #Create a header for the search results
        searchInfoHeader=tk.Label(searchInfo, bg="#69140e", fg="#d58936", text="Search Results", font=("Book Antiqua", 15), width=32, height=2)
        searchInfoHeader.grid(row=0, column=0, columnspan=3, sticky="ew")

        #Create a button to close the search info and return to the normal information display
        searchClose=tk.Button(searchInfo, text=" Close Search Info ", font=("Book Antiqua", 8), command=closeSearchInfo)
        searchClose.grid(row=2, column=0, columnspan=2)

    #Deletes info displayed in the information frame after a user is done with their search
    def closeSearchInfo():
        searchInfo.grid_forget()
        searchDisplay.grid_forget()

        showStore()

    #resets shop list to original size upon closing the search box
    def closeSearch():
        shopList.configure(height=23)

    #Creates user add window
    def addUser():
        add=tk.Toplevel(root)
        add.title('addUser')
        add.geometry("300x100")
        add.configure(bg='#D58936')
        add.resizable(False, False)

        #Create and grid user input label
        lbl=tk.Label(add,text='User Input')
        lbl.configure(bg='#D58936')
        lbl.grid(columnspan=2,column=0,row=0)

        #Create a label for the username
        nLabel=tk.Label(add, text="Name")
        nLabel.grid(row=1, column=0)
        nLabel.configure(bg='#D58936')

        #Create a name entry field and the set the textvariable equal to a variable representing StringVar(), which will allow us to access the text entered when accAddUser is called
        nameVar = StringVar()
        name = Entry(add, textvariable=nameVar)
        name.grid(row=1, column=1)
        
        #Create a label for the password
        passLabel=tk.Label(add, text="Password")
        passLabel.grid(row=2, column=0)
        passLabel.configure(bg='#D58936')

        #Create a password entry field and the set the textvariable equal to a variable representing StringVar(), which will allow us to access the text entered when accAddUser is called
        passVar = StringVar()
        passE = Entry(add, textvariable=passVar)
        passE.grid(row=2, column=1)

        #Adds users to users.csv and updates the user tab
        def accAddUser():
            #Check if the entry fields are empty first
            if(nameVar.get()=="" or passVar.get()==""):
                tk.messagebox.showinfo("ERROR", "Please Enter Correctly,Nothing Added") 
                return
            
            #Read through credentials.csv
            with open("credentials.csv",mode="r") as file:
                items = csv.reader(file)
                for item in items:
                    #Check if item is empty
                    if (item != []):
                        #If the name of the user equals the entered name, return an error messagebox letting the admin know the name is already in use and will not be added
                        if(item[0]==nameVar.get()):
                            tk.messagebox.showinfo("ERROR", "NAME ALREADY USED,Nothing Added")
            #MAKE INTO ELSE, THIS SHOULDNT RUN IF THERE IS ALREADY AN EXISTING USER
            #The new users' name and password are stored as list items in itemA, which will then be added to the list startingUsers
            itemA=[nameVar.get(), passVar.get(),'guest']
            startingUsers.append(itemA)
            #Destroy the add window
            add.destroy()
            #Open and write in the credentials.csv file, set it to the user list that now includes the added user
            with open("credentials.csv",mode='w')as file:
                csvwriter = csv.writer(file)
                csvwriter.writerows(startingUsers)
            set_users()

        #Create a button in the add window that will go through with the command to add the entered username and password to the userlist
        addButton=tk.Button(add,text='Add User',command=accAddUser,bg='#D58936')
        addButton.grid(columnspan=2,column=0,row=3)

    #Create new window for the admin to edit a user's information
    def editUser():
        edit=tk.Toplevel(root)
        edit.title('editUser')
        edit.geometry("200x100")
        edit.configure(bg='#D58936')
        edit.resizable(False, False)

        #Create a label with instructions
        lbl=tk.Label(edit,text='Input Edit and What''s Staying The Same')
        lbl.configure(bg='#D58936')
        lbl.grid(columnspan=2,column=0,row=0)

        #Label the name entry field
        nLabel=tk.Label(edit, text="Name")
        nLabel.grid(row=1, column=0)
        nLabel.configure(bg='#D58936')

        #Create a name entry field and the set the textvariable equal to a variable representing StringVar(), which will allow us to access the text entered when accEditUser is called
        nameVar = StringVar()
        name = Entry(edit, textvariable=nameVar)
        name.grid(row=1, column=1)
        
        #Label the password entry field
        #MAKE THE LABEL UNDER A PASSWORD VARIABLE, NOT ID
        idLabel=tk.Label(edit, text="Password")
        idLabel.grid(row=2, column=0)
        idLabel.configure(bg='#D58936')

        #Create a password entry field and the set the textvariable equal to a variable representing StringVar(), which will allow us to access the text entered when accEditUser is called
        idVar = StringVar()
        idE = Entry(edit, textvariable=idVar)
        idE.grid(row=2, column=1)

        #Create an edit button that will execute the edit user command
        eButton=tk.Button(edit,text='Confirm Edit',command=editUserConfirm,bg='#D58936')
        eButton.grid(columnspan=2,column=0,row=3)

        #Edits the information in users.csv and updates the users tab
        def editUserConfirm():
            if(idVar.get()=="" or nameVar.get()==''):
                tk.messagebox.showinfo("ERROR", "BOTH NEED INPUTS") 
                return
            #AGAIN, WHY ISNT THIS AN ELSE
            current=[nameVar.get(),idVar.get(),'user']
            c=-1
            index=0

            #Find a match, check if that match is a password or username match, replace the thing that does not match
            for row in startingUsers:
                c=c+1
                if(nameVar.get()==row[0]):
                    current[1]=idVar.get()
                    index=c
                if(idVar.get()==row[1]):
                    current[0]==nameVar.get()
                    index=c
            startingUsers[index]=current

            #Write in the credentials file and set the user list with the updated user
            with open("credentials.csv",mode='w')as file:
                csvwriter = csv.writer(file)
                csvwriter.writerows(startingUsers)
            set_users()
        
    #Shows user info in the information frame
    def showUser():
        #Get the selected user
        #SHOULD BE TRY EXCEPT IN CASE NO SELECTION HAS BEEN MADE
        content = shopList.selection_get()
        #Delete whatever info was previously being shown in the information box
        itemInfo.delete(0, tk.END)
        #Find that user in the credentials file and insert the matching name and password from the file into the information box
        with open("credentials.csv",mode="r") as file:
            items = csv.reader(file)
            for item in items:
                if(item!=[]):
                    if(item[0]==content):
                        n="{0}".format(item[0])
                        nI="NAME: "+n
                        p="{0}".format(item[1])
                        pI="PASSWORD: "+p
                        itemInfo.insert(tk.END,nI)
                        itemInfo.insert(tk.END,pI)

    #Creates popup for user removal process
    def removeUser():
        remUs=tk.Toplevel(root)
        remUs.title('Remove User')
        remUs.geometry("200x100")
        remUs.configure(bg='#D58936')
        remUs.resizable(False, False)

        #Create a label with instructions
        lbl=tk.Label(remUs,text='Input Username')
        lbl.configure(bg='#D58936')
        lbl.grid(columnspan=2,column=0,row=0)

        #Create a name entry field and the set the textvariable equal to a variable representing StringVar(), which will allow us to access the text entered when deleteUser is called
        usVar = StringVar()
        usE = Entry(remUs, textvariable=usVar)
        usE.grid(row=1, column=1)

        #Create button in popup that executes the deleteUser command once necessary info has been entered
        delButton=tk.Button(remUs,text='Delete',command=deleteUser,bg='#D58936')
        delButton.grid(columnspan=2,column=0,row=2)

        #Deletes user from users.csv and updates users tab
        def deleteUser():
            #Let found be false, will allow an error to pop up if there is no such user
            found = False
            #Make sure field is not empty
            if(usVar.get()==""):
                tk.messagebox.showinfo("ERROR", "Please enter a user to be deleted") 
                return
            usern=usVar.get()
            index=-1

            #Find the user in the users list
            for row in startingUsers:
                index=index+1
                #When found, check if admin, admin users cannot be deleted
                if(row[0].lower()==usern.lower()):
                    if(row[2]=="admin"):
                        tk.messagebox.showinfo("ERROR","Admin user cannot be removed")
                        found = True
                    else:
                        del startingUsers[index]
                        found = True
            
            #Send error to admin if the user cannot be found
            if not found:
                tk.messagebox.showinfo("ERROR","User with this username could not be found")
            
            #Destroy the remove user window
            remUs.destroy()

            #Write in credentials.csv witht the updated user list
            with open("credentials.csv",mode='w')as file:
                csvwriter = csv.writer(file)
                csvwriter.writerows(startingUsers)
            set_users()

    #Displays item information in the information frame
    def showItem():
        #Make sure an item is selected
        try:
            content = shopList.selection_get()
        except:
            tk.messagebox.showinfo("ERROR", "No item selected")
            return
        
        #Get the id of the selection and ONLY the id
        idd=content[:4]
        #Delete information currently being shown in the information box
        refresh_info()

        #Open the inventory file, find the selected item, and display all of its information
        with open("inventory.csv",mode="r") as file:
            items = csv.reader(file)
            for item in items:
                #Check if item is blank
                if (item != []):
                    #When id match is found, foramt each piece of info and insert into the information box
                    if(item[1]==idd):
                        id1="{0}".format(item[1])
                        n="{0}".format(item[0])
                        nameInfo='NAME: '+n
                        idInfo="ID: "+id1
                        itemInfo.insert(tk.END,nameInfo)
                        itemInfo.insert(tk.END,idInfo)
                        prov="{0}".format(item[2])
                        provInfo="PROVIDER: "+prov
                        loc="{0}".format(item[3])
                        locInfo="LOCATION: "+loc
                        price="{0}".format(item[4])
                        priceInfo="PRICE: "+price
                        quan="{0}".format(item[5])
                        quanInfo="QUANTITY: "+quan
                        desc="{0}".format(item[6])
                        descInfo="DESC: "+desc
                        itemInfo.insert(tk.END,provInfo)
                        itemInfo.insert(tk.END,locInfo)
                        itemInfo.insert(tk.END,priceInfo)
                        itemInfo.insert(tk.END,quanInfo)
                        itemInfo.insert(tk.END,descInfo)
        
    #Creates item edit window
    def editItem():
        edit=tk.Toplevel(root)
        edit.title('editItem')
        edit.geometry("400x400")
        edit.configure(bg='#D58936')
        edit.resizable(False, False)

        #Create label with edit instructions
        lbl=tk.Label(edit,text='Input Item ID and What You Want To Edit')
        lbl.configure(bg='#D58936')
        lbl.grid(columnspan=2,column=0,row=0)

        #A label and working entry field must be created for name, ID, provider, location, price, quantity, and description
        nLabel=tk.Label(edit, text="Name")
        nLabel.grid(row=2, column=0)
        nLabel.configure(bg='#D58936')
        nameVar = StringVar()
        name = Entry(edit, textvariable=nameVar)
        name.grid(row=2, column=1)
        
        idLabel=tk.Label(edit, text="ID:NECESSARY")
        idLabel.grid(row=1, column=0)
        idLabel.configure(bg='#D58936')
        idVar = StringVar()
        idE = Entry(edit, textvariable=idVar)
        idE.grid(row=1, column=1)

        provLabel=tk.Label(edit, text="Provider")
        provLabel.grid(row=3, column=0)
        provLabel.configure(bg='#D58936')
        provVar = StringVar()
        prov = Entry(edit, textvariable=provVar)
        prov.grid(row=3, column=1)

        locLabel=tk.Label(edit, text="Location")
        locLabel.grid(row=4, column=0)
        locLabel.configure(bg='#D58936')
        locVar = StringVar()
        loc = Entry(edit, textvariable=locVar)
        loc.grid(row=4, column=1)
        
        priceLabel=tk.Label(edit, text="Price")
        priceLabel.grid(row=5, column=0)
        priceLabel.configure(bg='#D58936')
        priceVar = StringVar()
        price = Entry(edit, textvariable=priceVar)
        price.grid(row=5, column=1)

        quanLabel=tk.Label(edit, text="Quantity")
        quanLabel.grid(row=6, column=0)
        quanLabel.configure(bg='#D58936')
        quanVar = StringVar()
        quan = Entry(edit, textvariable=quanVar)
        quan.grid(row=6, column=1)

        descLabel=tk.Label(edit, text="Description")
        descLabel.grid(row=7, column=0)
        descLabel.configure(bg='#D58936')
        descVar = StringVar()
        desc = Entry(edit, textvariable=descVar)
        desc.grid(row=7, column=1)

        #Create button that can execute the edit command
        eButton=tk.Button(edit,text='Confirm Edit',command=editConfirm,bg='#D58936')
        eButton.grid(columnspan=2,column=0,row=8)

        #Edits the item's information in inventory.csv and updates the store tab
        def editConfirm():
            count=0
            i=[]

            #Check to make sure that an id has been entered
            if(idVar.get()==""):
                tk.messagebox.showinfo("ERROR", "ID NEEDED TO EDIT") 
                return
            
            #Get all info from entry fields, store them in a list itemA
            itemA=[nameVar.get(), idVar.get(),provVar.get(),locVar.get(),priceVar.get(),quanVar.get(),descVar.get()]
            
            #Make sure at least one edit is made
            for smt in itemA:
                if(smt!=''):
                    count += 1
            if(count<2):
                tk.messagebox.showinfo("ERROR", "AT LEAST ONE EDIT NEEDED") 
                return
            
            #Find the item that matches the id entered
            for w in storeItems:
                if(w[1]==idVar.get()):
                    i=w
            inn=-1

            #If something has been entered in a certain entry category (ie. name), update the value of that category in the current listed item
            for it in i:
                inn=inn+1
                if(itemA[inn]!=''):
                    i[inn]=itemA[inn]
            innn=-1

            #Update that item in the list of items
            for w in storeItems:
                innn=innn+1
                if(w[1]==i[1]):
                    storeItems[innn]=i

            #Update the inventory file with the updated list
            with open("inventory.csv",mode='w')as file:
                csvwriter = csv.writer(file)
                csvwriter.writerows(storeItems)
            set_items()
            
    #Creates item delete window  
    def delItem():
        delete=tk.Toplevel(root)
        delete.title('deleteItem')
        delete.geometry("200x100")
        delete.configure(bg='#D58936')
        delete.resizable(False, False)

        #Create label with instructions
        lbl=tk.Label(delete,text='Input Item ID')
        lbl.configure(bg='#D58936')
        lbl.grid(columnspan=2,column=0,row=0)

        #Create a labeled entry field for the user to input the id of the item they wish to delete
        idLabel=tk.Label(delete, text="ID")
        idLabel.grid(row=1, column=0)
        idLabel.configure(bg='#D58936')
        idVar = StringVar()
        idE = Entry(delete, textvariable=idVar)
        idE.grid(row=1, column=1)

        #Create a button that can execute accDelItem
        delButton=tk.Button(delete,text='Delete',command=accDelItem,bg='#D58936')
        delButton.grid(columnspan=2,column=0,row=2)

        #Deletes item from inventory.csv and updates the store tab
        def accDelItem():
            #Check to make sure that an id has been entered
            if(idVar.get()==""):
                tk.messagebox.showinfo("ERROR", "Please Enter Correctly,Nothing Added") 
                return
            itemID=idVar.get()
            index=-1

            #Find the item with that id in the list of store items
            for row in storeItems:
                index=index+1
                if(row[1]==itemID):
                    del storeItems[index]
            #Destroy the item within that lsit
            delete.destroy()

            #Open inventory.csv and update the file so that it no longer contains the deleted element
            with open("inventory.csv",mode='w')as file:
                csvwriter = csv.writer(file)
                csvwriter.writerows(storeItems)
            set_items()            
        
    #Creates add item window
    def addItem():
        add=tk.Toplevel(root)
        add.title('addItem')
        add.geometry("400x400")
        add.configure(bg='#D58936')
        add.resizable(False, False)

        #Create an item input label
        lbl=tk.Label(add,text='Item Input')
        lbl.configure(bg='#D58936')
        lbl.grid(columnspan=2,column=0,row=0)

        #Create a labled entry field for the user to input the name, ID, provider, location, price, quantity, and description
        nLabel=tk.Label(add, text="Name")
        nLabel.grid(row=1, column=0)
        nLabel.configure(bg='#D58936')
        nameVar = StringVar()
        name = Entry(add, textvariable=nameVar)
        name.grid(row=1, column=1)
        
        idLabel=tk.Label(add, text="ID")
        idLabel.grid(row=2, column=0)
        idLabel.configure(bg='#D58936')
        idVar = StringVar()
        idE = Entry(add, textvariable=idVar)
        idE.grid(row=2, column=1)

        provLabel=tk.Label(add, text="Provider")
        provLabel.grid(row=3, column=0)
        provLabel.configure(bg='#D58936')
        provVar = StringVar()
        prov = Entry(add, textvariable=provVar)
        prov.grid(row=3, column=1)

        locLabel=tk.Label(add, text="Location")
        locLabel.grid(row=4, column=0)
        locLabel.configure(bg='#D58936')
        locVar = StringVar()
        loc = Entry(add, textvariable=locVar)
        loc.grid(row=4, column=1)
        
        priceLabel=tk.Label(add, text="Price")
        priceLabel.grid(row=5, column=0)
        priceLabel.configure(bg='#D58936')
        priceVar = StringVar()
        price = Entry(add, textvariable=priceVar)
        price.grid(row=5, column=1)

        quanLabel=tk.Label(add, text="Quantity")
        quanLabel.grid(row=6, column=0)
        quanLabel.configure(bg='#D58936')
        quanVar = StringVar()
        quan = Entry(add, textvariable=quanVar)
        quan.grid(row=6, column=1)

        descLabel=tk.Label(add, text="Description")
        descLabel.grid(row=7, column=0)
        descLabel.configure(bg='#D58936')
        descVar = StringVar()
        desc = Entry(add, textvariable=descVar)
        desc.grid(row=7, column=1)

        #Create a button that can execute accAddItem and begin the adding process
        enterButton=tk.Button(add,text='Enter',command=accAddItem,bg='#D58936')
        enterButton.grid(columnspan=2,column=0,row=8)

        #Adds item to inventory.csv and updates the store tab
        def accAddItem():
            #Make sure that all categories of information are filled
            if(nameVar.get()=="" or idVar.get()==""
               or descVar.get()=="" or quanVar.get()==""
               or priceVar.get()=="" or provVar.get()=="" or locVar.get()==""):
                tk.messagebox.showinfo("ERROR", "Please Enter Correctly,Nothing Added") 
                return
            
            #Get all the information from the entries and store them in list itemA
            itemA=[nameVar.get(), idVar.get(),provVar.get(),
                              locVar.get(),priceVar.get(),quanVar.get(),
                              descVar.get()]
            
            #Add this new item to the end of the items list
            storeItems.append(itemA)

            #Make sure that there isn't already an item with that id in the inventory
            with open("inventory.csv",mode="r") as file:
                items = csv.reader(file)
                for item in items:
                    if (item != []):
                        if(item[1]==idVar.get()):
                            tk.messagebox.showinfo("ERROR", "ID ALREADY USED,Nothing Added") 
                            return
            
            #Destroy the add window
            add.destroy()

            #Update inventory.csv with the new item
            with open("inventory.csv",mode='w')as file:
                csvwriter = csv.writer(file)
                csvwriter.writerows(storeItems)
            set_items()

    #Create search button
    searchButton=tk.Button(left, text="Search", command=showSearch, bg="#a44200", fg="#d58936", width=33, height=1, font=("Book Antiqua", 15))
    searchButton.grid(row=3, column=0, columnspan=2)

    #Create frame for action buttons
    actions=tk.Frame(content, bg="#f2f3ae", width=400, height=205,)
    actions.grid(row=1, column=2, padx=15)
    actions.grid_rowconfigure(1, weight=1)
    actions.grid_columnconfigure(0, weight=1)

    #Header for action buttons
    actionsHeader=tk.Label(actions, bg="#69140e", fg="#d58936", text="Actions", font=("Book Antiqua", 15), width=32, height=2)
    actionsHeader.grid(row=0, sticky="ew")

    #Creates the frame that action buttons will be placed within
    actionsBody=tk.Frame(actions, bg="#f2f3ae", width=32, height=10)
    actionsBody.grid(row=1, column=0, sticky="ew")

    #Default action buttons configured below
    addButton=tk.Button(actionsBody,text="Add Item",bg="#D58936",width=23,height=3, font=("Book Antiqua", 8))
    addButton.grid(row=0, column=0, padx=15, pady=10)

    showButton=tk.Button(actionsBody,text="Show Item",bg="#D58936",width=23,height=3, font=("Book Antiqua", 8))
    showButton.grid(row=1, column=1, padx=15, pady=10)

    removeButton=tk.Button(actionsBody,text="Remove Item",bg="#D58936",width=23,height=3,command="remItem", font=("Book Antiqua", 8))
    removeButton.grid(row=0, column=1, padx=15, pady=10)

    editButton=tk.Button(actionsBody,text="Edit Item",bg="#D58936",width=23,height=3,command="editItm", font=("Book Antiqua", 8))
    editButton.grid(row=1, column=0, padx=15, pady=10)

    #Frame below main content, used to contain the logout and about us buttons
    bottom=tk.Frame(root, bg="#D58936", width=960, height=100)
    bottom.grid(row=2, column=1)

    #Creates log out window and allows user to log out or cancel and stay
    def logoutPrompt():
        logoutBox= tk.Toplevel(root)
        logoutBox.geometry("600x250")
        logoutBox.title("Logout?")
        logoutBox.configure(bg="#D58936")
        
        #Create a label asking user if they are sure they would like to log out
        logoutConfirm=tk.Label(logoutBox, text= "Are you sure you would like to log out?", bg="#D58936", font=("Book Antiqua", 15))
        logoutConfirm.grid(row=0, column=0, pady=40, columnspan=2)

        #Creates a frame for the yes or no options
        yesOrNo=tk.Frame(logoutBox, bg="#D58936", width=600, height=150)
        yesOrNo.grid(row=1, column=0, columnspan=2, pady=30, padx=20)

        #Destroys the main window and takes users back to the login page
        def log_out():
            make_logIn()
            root.destroy()

        #Just destroys the login page, taking users back to the main page
        def stay():
            logoutBox.destroy()

        #Button that can execute log_out command
        logoutYes=tk.Button(yesOrNo, text="Yes", width=8, height=1, bg="#69140e", fg="#d58936", font=("Book Antiqua", 15),command=log_out)
        logoutYes.grid(row=2, column=0, padx=20)

        #Button that can execute stay command
        logoutNo=tk.Button(yesOrNo, text="No", width=8, height=1, bg="#69140e", fg="#d58936", font=("Book Antiqua", 15),command=stay)
        logoutNo.grid(row=2, column=1, padx=10)
              
    #Button that can pull up the log out window
    logoutButton=tk.Button(bottom, bg="#69140e", fg="#d58936", text="Log Out", command=logoutPrompt, font=("Book Antiqua", 15), width=13, height=1)
    logoutButton.grid(row=1, column=1, padx=20)

    #Creates about us window
    def openAboutUs():
        aboutPage= tk.Toplevel(root)
        aboutPage.geometry("1000x500")
        aboutPage.title("About Us")
        aboutPage.configure(bg="#69140e")
        aboutPage.resizable(False, False)

        #About us label
        aboutLabel=tk.Label(aboutPage, text="About Us: BDGS", font=("Book Antiqua", 50), bg="#69140e", fg="#D58936")
        aboutLabel.grid(row=0, column=2, columnspan=2)

        #Creates and formats an image for a group member
        rawBeck = Image.open("beck.png")
        beck=rawBeck.resize((200, 200))
        beckDisplay = ImageTk.PhotoImage(beck)
        beckPlace = tk.Label(aboutPage, image=beckDisplay, highlightbackground="#D58936", highlightthickness=2)
        beckPlace.image=beckDisplay
        beckPlace.grid(row=1, column=0, padx=20, pady=20)

        #Member's name and desc
        beckName=tk.Label(aboutPage, text="Beck Towne", font=("Book Antiqua", 25), bg="#69140e", fg="#D58936")
        beckName.grid(row=2, column=0, padx=20)
        beckDescription=tk.Label(aboutPage, text="Team Member\nComputer Science\nMarist '27\nrebecca.towne1@marist.edu", font=("Book Antiqua", 18), bg="#69140e", fg="#f2f3ae")
        beckDescription.grid(row=3, column=0, padx=20)

        #Creates and formats an image for a group member
        rawDevin=Image.open("DevinPlaceholder.png")
        devin=rawDevin.resize((200, 200))
        devinDisplay=ImageTk.PhotoImage(devin)
        devinPlace=tk.Label(aboutPage, image=devinDisplay, highlightbackground="#D58936", highlightthickness=2)
        devinPlace.image=devinDisplay
        devinPlace.grid(row=1, column=1, columnspan=2, padx=10, pady=20)

        #Member's name and desc
        devinName=tk.Label(aboutPage, text="Devin Melillo", font=("Book Antiqua", 25), bg="#69140e", fg="#D58936")
        devinName.grid(row=2, column=1, columnspan=2, padx=20)
        devinDescription=tk.Label(aboutPage, text="Team Member\nDigital Media\nMarist '27\ndevin.melillo1@marist.edu", font=("Book Antiqua", 18), bg="#69140e", fg="#f2f3ae")
        devinDescription.grid(row=3, column=1, columnspan=2, padx=10)

        #Creates and formats an image for a group member
        rawGrace=Image.open("Grace.png")
        grace=rawGrace.resize((200,200))
        graceDisplay=ImageTk.PhotoImage(grace)
        gracePlace=tk.Label(aboutPage, image=graceDisplay, highlightbackground="#D58936", highlightthickness=2)
        gracePlace.image=graceDisplay
        gracePlace.grid(row=1, column=3, columnspan=2, padx=10, pady=10)

        #Member's name and desc
        graceName=tk.Label(aboutPage, text="Grace Markus", font=("Book Antiqua", 25), bg="#69140e", fg="#D58936")
        graceName.grid(row=2, column=3, columnspan=2, padx=20)
        graceDescription=tk.Label(aboutPage, text="Team Member\nData Science\nMarist '27\ngrace.markus1@marist.edu", font=("Book Antiqua", 18), bg="#69140e", fg="#f2f3ae")
        graceDescription.grid(row=3, column=3, columnspan=2, padx=10)

        #Creates and formats an image for a group member
        rawSoph=Image.open("Soph.png")
        soph=rawSoph.resize((200,200))
        sophDisplay=ImageTk.PhotoImage(soph)
        sophPlace=tk.Label(aboutPage, image=sophDisplay, highlightbackground="#D58936", highlightthickness=2)
        sophPlace.image=sophDisplay
        sophPlace.grid(row=1, column=5, padx=10, pady=10)

        #Member's name and desc
        sophName=tk.Label(aboutPage, text="Sophia Masone", font=("Book Antiqua", 25), bg="#69140e", fg="#D58936")
        sophName.grid(row=2, column=5, padx=20)
        sophDescription=tk.Label(aboutPage, text="Group Leader\nComputer Science\nMarist '27\nsophia.masone1@marist.edu", font=("Book Antiqua", 18), bg="#69140e", fg="#f2f3ae")
        sophDescription.grid(row=3, column=5, padx=10)

    #Button that opens the about us page
    aboutUsButton=tk.Button(bottom, bg="#69140e", fg="#d58936", text="About Us", command=openAboutUs, font=("Book Antiqua", 15), width=13, height=1)
    aboutUsButton.grid(row=1, column=0, padx=20)

    #showStore is called so that the store tab is open by default when the admin window is created
    showStore()

#create guest window    
def make_window():
    window.destroy()
    root=tk.Tk()
    root.title('Little Shoppe')
    root.geometry("1390x640")
    root.configure(bg='#D58936', height=1080, width=1920)
    root.resizable(False, False)

    #Shop title
    Title=tk.Label(root, text="Little Shoppe", fg="#3c1518", bg="#D58936", anchor="center", font=("Book Antiqua", 40))
    Title.grid(columnspan=2, row=0, column=1, sticky="ew", pady=10)

    #This frame contains all the main content
    content=tk.Frame(root, bg='#D58936')
    content.grid(row=1, column=1)

    #Store and favorites tab
    left=tk.Frame(content, bg="#f2f3ae", width=400, height=450)
    left.grid(row=0, column=0, rowspan=2, padx=15, pady=15)

    #Frame to contain the store and favorites tab
    leftButtons=tk.Frame(left, bg="#f2f3ae", width=390, height=100)
    leftButtons.grid(row=0, column=0, sticky="ew")

    #Makes a frame for the store and favorites listbox, making this frame keeps these boxes at a consistent size no matter what content it contains
    userList= tk.Frame(left, bg="#f2f3ae", width=382, height=350)
    userList.grid(row=1, column=0, sticky="nsew")

    #Creates a listbox to contain the store or favorites content
    shopList=tk.Listbox(userList,height=23)
    shopList.grid(column=0,row=0,sticky='nsew')
    shopList.config(bg="#f2f3ae")

    #Creates a scrollbar and connects it to the shoplist listbox
    sBar=tk.Scrollbar(userList,orient="vertical")
    sBar.grid(row=0, column=1, sticky="ns")
    shopList.config(yscrollcommand=sBar.set)
    sBar.config(command=shopList.yview)

    #This frame will contain the shopkeeper, benjamin
    right=tk.Frame(content, bg="#D58936", width=400, height=450)
    right.grid(row=0,column=3,rowspan=2, padx=15)

    #This frame will contain the benjamin images
    imgFrame=tk.Frame(right, bg="#D58936", width=375, height=225)
    imgFrame.grid(row=0,column=0)

    #This frame will contain benjamin little's name
    nameFrame=tk.Frame(right, bg="#D58936", width=375, height=100)
    nameFrame.grid(row=1,column=0)

    #Label for benjamin little's name
    benName=tk.Label(nameFrame, text="Benjamin Little", fg="#3c1518", bg="#D58936", anchor="center", font=("Book Antiqua", 20))
    benName.grid(row=0, column=0, sticky="ew", pady=5)

    #Creates and formats the benjamin image
    rawBenjamin=Image.open("image001.png")
    benjamin=rawBenjamin.resize((375,350))
    benjaminDisplay=ImageTk.PhotoImage(benjamin)
    benjaminPlace=tk.Label(imgFrame, image=benjaminDisplay, highlightbackground="#D58936", highlightthickness=2)
    benjaminPlace.image=benjaminDisplay
    benjaminPlace.grid(row=0, column=0)

    #Frame for the information box
    information=tk.Frame(content, bg="#f2f3ae", width=400, height=205)
    information.grid(row=0, column=2, padx=15, pady=8)

    #Labels the information box
    infoHeader=tk.Label(information, bg="#69140e", fg="#d58936", text="Information", font=("Book Antiqua", 15), width=32, height=2)
    infoHeader.grid(row=0, sticky="ew")

    #Frame for the information, keeps the information box at a consistent size, no matter the length of the content in the listbox
    infoBody=tk.Frame(information, width=32, height=205)
    infoBody.grid(row=1, column=0, sticky="nsew")

    #Creates a listbox for the information
    itemInfo=tk.Listbox(infoBody,height=8)
    itemInfo.grid(column=0,row=0,sticky='nsew')
    itemInfo.config(bg="#f2f3ae")

    #Creates a scrollbar and links it to 
    ssBar=tk.Scrollbar(infoBody,orient="vertical")
    ssBar.grid(row=0, column=2, sticky="ns")
    itemInfo.config(yscrollcommand=ssBar.set)
    ssBar.config(command=itemInfo.yview)

    #Deletes whatever information is currently being displayed in the information box
    def refresh_info():
        itemInfo.delete(0, tk.END)

    #Sets the correct list of items in the store list
    def set_items():
        #Delete current shoplist
        shopList.delete(0, tk.END)
        #Read through inventory.csv
        with open("inventory.csv",mode="r") as file:
            items = csv.reader(file)
            for item in items:
                if (item != []):
                    #So long as the item isn't blank, the item's id and name will be displayed
                    id1="{0}".format(item[1])
                    s=" "
                    n="{0}".format(item[0])
                    i=id1+s+n
                    shopList.insert(tk.END,i)

    #Sets the correct list of favorites in the favorites list
    def set_favs():
        #create new window for the favorites to be entered
        add=tk.Toplevel(root)
        add.title('setFav')
        add.geometry("200x100")
        add.configure(bg='#D58936')
        add.resizable(False, False)

        #Labels the purpose of the add window
        lbl=tk.Label(add,text='Please input your username')
        lbl.configure(bg='#D58936')
        lbl.grid(columnspan=2,column=0,row=0)

        #Labels the username entry field
        nLabel=tk.Label(add, text="Username")
        nLabel.grid(row=1, column=0)
        nLabel.configure(bg='#D58936')
        loggedIn = StringVar()

        #Creates the entry field for the user to enter their name
        name = Entry(add, textvariable=loggedIn)
        name.grid(row=1, column=1)

        #Wipes the current shoplist display
        shopList.delete(0, tk.END)


        def acc():
            count=-1
            i=0
            #Getting the index of user to get index in favs
            for row in startingUsers:
                count=count+1
                if(row[0]==loggedIn):
                    i=count
            f=favorites[i]
            #Wipe current shopList information and destroy the add window
            shopList.delete(0, tk.END)
            add.destroy()
            #Read inventory and insert all favorited items into shoplist
            with open("inventory.csv",mode="r") as file:
                items = csv.reader(file)
                for item in items:
                    if (item != []):
                        for a in f:
                            if(item[1]==a):
                                id1="{0}".format(item[1])
                                s=" "
                                n="{0}".format(item[0])
                                i=id1+s+n
                                shopList.insert(tk.END,i)

        #Creates a button that can execute acc and begin the favorite adding process            
        enterButton=tk.Button(add,text='Enter',command=acc,bg='#D58936')
        enterButton.grid(columnspan=2,column=0,row=8)

    #Creates a window to remove an item from a user's favorites
    #Why is this double indented? Fix this.
    #Make this function simply remove the selected item. The only popup should be a "Are you sure you want to remove this item from your favorites?" confirmation
    def remFav():
            #Create window for the user to enter the information for the item they want removed
            add=tk.Toplevel(root)
            add.title('addFav')
            add.geometry("200x100")
            add.configure(bg='#D58936')
            add.resizable(False, False)
            add.grid_columnconfigure(1,weight=1)
            add.grid_rowconfigure(3,weight=1)

            #Label the window 
            lbl=tk.Label(add,text='Name Input')
            lbl.configure(bg='#D58936')
            lbl.grid(columnspan=2,column=0,row=0)

            #Label and create the user name entry field
            nLabel=tk.Label(add, text="NAME: ")
            nLabel.grid(row=1, column=0)
            nLabel.configure(bg='#D58936')
            loggedIn = StringVar()
            name = Entry(add, textvariable=loggedIn)
            name.grid(row=1, column=1)

            #Label and create the item id entry field
            idLabel=tk.Label(add, text="ITEM ID:")
            idLabel.grid(row=2, column=0)
            idLabel.configure(bg='#D58936')
            ID = StringVar()
            IDD = Entry(add, textvariable=ID)
            IDD.grid(row=2, column=1)

            #Wipe the current list displayed in shoplist
            shopList.delete(0, tk.END)

            #Removes the item from favorites
            def acc():
                add.destroy()
                count=-1
                i=0
                #getting the index of the user to get the index in favs
                for row in startingUsers:
                    count=count+1
                    if(row[0]==loggedIn):
                        i=count
                cFavs=favorites[i]
                cnt=-1

                #Find the corrisponding item in favorites and remove it from favorites list
                for p in favorites[i]:
                    cnt=cnt+1
                    if(p==ID.get()):
                        cFavs.pop(cnt)
                favorites[i]=cFavs

            #Create a button that executes the acc command and begins the process of removing the item from favorites
            enterButton=tk.Button(add,text='Enter',command=acc,bg='#D58936')
            enterButton.grid(columnspan=2,column=0,row=8)

    #Creates a window that starts the add favorite process
    def favItem():
            #Create the add fav window
            add=tk.Toplevel(root)
            add.title('addFav')
            add.geometry("200x100")
            add.configure(bg='#D58936')
            add.resizable(False, False)
            add.grid_columnconfigure(1,weight=1)
            add.grid_rowconfigure(3,weight=1)

            #Label the window
            lbl=tk.Label(add,text='Name Input')
            lbl.configure(bg='#D58936')
            lbl.grid(columnspan=2,column=0,row=0)

            #Label and create the user name entry field
            nLabel=tk.Label(add, text="NAME: ")
            nLabel.grid(row=1, column=0)
            nLabel.configure(bg='#D58936')
            loggedIn = StringVar()
            name = Entry(add, textvariable=loggedIn)
            name.grid(row=1, column=1)

            #Label and create the item id entry field
            idLabel=tk.Label(add, text="ITEM ID:")
            idLabel.grid(row=2, column=0)
            idLabel.configure(bg='#D58936')
            ID = StringVar()
            IDD = Entry(add, textvariable=ID)
            IDD.grid(row=2, column=1)

            #Wipe the current list displayed in shopList
            shopList.delete(0, tk.END)

            #Adds the item to favorites
            def acc():
                add.destroy()
                count=-1
                i=0
                #getting the index of user to get index in favs
                for row in startingUsers:
                    count=count+1
                    if(row[0]==loggedIn):
                        i=count
                #Add the item to the correct index in favorites
                favorites[i].append(ID.get())

            #Creates a button that can execute the acc command and begin the favorite add process 
            enterButton=tk.Button(add,text='Enter',command=acc,bg='#D58936')
            enterButton.grid(columnspan=2,column=0,row=8)

    #Makes the tabs to switch between the favorites and store page, the colors of the tabs also change to indicate which one is open                
    def showFavorites():
        storeButton.configure(bg="#a44200", fg="#d58936")
        favoritesButton.configure(bg="#69140e", fg="#d58936")
        set_favs()

    def showStore():
        storeButton.configure(bg="#69140e", fg="#d58936")
        favoritesButton.configure(bg="#a44200", fg="#d58936")
        set_items()
    
    #Creates the default store and favorites tab configurated
    storeButton=tk.Button(leftButtons, text="Store", command=showStore, width=16, height=1, font=("Book Antiqua", 15))
    storeButton.grid(row=0, column=0)

    favoritesButton=tk.Button(leftButtons, text="Favorites", command=showFavorites, width=16,height=1, font=("Book Antiqua", 15))
    favoritesButton.grid(row=0, column=1)

    storeButton.configure(bg="#69140e", fg="#d58936")
    favoritesButton.configure(bg="#a44200", fg="#d58936")

    #Store is open by default
    showStore()

    #Removes the search info from the information tab and returns to the store display
    def closeSearchInfo():
        searchInfo.grid_forget()
        searchDisplay.grid_forget()

        showStore()     

    #Shows the info gathered by search in the information tab
    def createSearchInfo():
        global information
        global userInfo
        global requestsInfo
        global searchDisplay
        global searchInfo

        #Create the frame over the information frame
        searchInfo=tk.Frame(content, bg="#f2f3ae", width=400, height=205)
        searchInfo.grid(row=0, column=2, padx=15, pady=8)
        searchInfo.grid_rowconfigure(3, weight=1)
        searchInfo.grid_columnconfigure(1, weight=1)

        #Make the display a textbox
        searchDisplay=tk.Text(searchInfo, height=8, width=48, bg="#f2f3ae", fg="#69140e")
        searchDisplay.grid(row=1, column=0, columnspan=3)

        #Read through inventory
        with open("inventory.csv",mode="r") as file:
            items = csv.reader(file)
            for item in items:
                #Check if item is empty first
                if (item != []):
                    #Check if item matches what was entered in search input
                    for i in item:
                        find=searchInput.get("1.0", END).lower().strip()
                        compareTo=i.lower().strip()
                        if find != compareTo:
                            continue
                        else:
                            #If it matches, label and insert all the item information into the search display
                            id1="{0}".format(item[1])
                            n="{0}".format(item[0])
                            nameInfo='NAME: '+n
                            idInfo="ID: "+id1
                            prov="{0}".format(item[2])
                            provInfo="PROVIDER: "+prov
                            loc="{0}".format(item[3])
                            locInfo="LOCATION: "+loc
                            price="{0}".format(item[4])
                            priceInfo="PRICE: "+price
                            quan="{0}".format(item[5])
                            quanInfo="QUANTITY: "+quan
                            desc="{0}".format(item[6])
                            descInfo="DESC: "+desc
                            itemString=f"{nameInfo}\n{idInfo}\n{provInfo}\n{locInfo}\n{priceInfo}\n{quanInfo}\n{descInfo}\n******************\n"
                            searchDisplay.insert(END, itemString)
        
        #Create label for the search info display
        searchInfoHeader=tk.Label(searchInfo, bg="#69140e", fg="#d58936", text="Search Results", font=("Book Antiqua", 15), width=32, height=2)
        searchInfoHeader.grid(row=0, column=0, columnspan=3, sticky="ew")

        #Create a button that will close the search info
        searchClose=tk.Button(searchInfo, text=" Close Search Info ", font=("Book Antiqua", 8), command=closeSearchInfo)
        searchClose.grid(row=2, column=0, columnspan=2)

    #Creates the search bar display
    def showSearch():
        #Shorten the shoplist to make room for the search
        shopList.configure(height=18)

        #Create a frame for the search
        search=tk.Frame(left, width=400, height=100, bg="#D58936", highlightbackground="#69140e", highlightthickness=2)
        search.grid(row=2, column=0, sticky="s")

        #Label the search bar
        searchLabel=tk.Label(search, text="Enter name of item, id, item type, or () below:", font=("Book Antiqua", 10), width=45, height=1, bg="#D58936", fg="#69140e")
        searchLabel.grid(row=1, column=1, columnspan=3, pady=2)

        #Creates a text entry field for the search
        global searchInput
        searchInput=tk.Text(search, width=30, height=1)
        searchInput.grid(row=2, column=0, columnspan=3, pady=10)

        #Create the enter button that will gather and show the search results when pressed
        enterSearch=tk.Button(search, width=8, height=0, text="Enter", bg="#D58936", fg="#69140e", command=createSearchInfo)
        enterSearch.grid(row=2, column=3, padx=2, pady=3)

        #Create a button that closes the search and returns the shop list to normal size
        exitSearch=tk.Button(search, width=2, height=0, text="X", font=("Arial", 8), command=lambda: [search.grid_forget(), closeSearch()], bg="#69140e", fg="#f2f3ae")
        exitSearch.grid(row=0, column=4, padx=2, pady=2)

    #Returns the shoplist to it's original size
    def closeSearch():
        shopList.configure(height=23)

    #Show an item's information in the information frame
    def showItem():
        #Make sure that an item has been selected
        try:
            content = shopList.selection_get()
        except:
            tk.messagebox.showinfo("ERROR", "No item selected")
            return
        
        #Get the item's id from the selection
        idd=content[:4]

        #Wipe whatever is currently being displayed in the information tab
        refresh_info()

        #Read the inventory file
        with open("inventory.csv",mode="r") as file:
            items = csv.reader(file)
            for item in items:
                #Make sure the item isnt empty
                if (item != []):
                    #If the item id matches the id from the selection, lable the item's information and display the information in the information frame
                    if(item[1]==idd):
                        id1="{0}".format(item[1])
                        s=" "
                        n="{0}".format(item[0])
                        nameInfo='NAME: '+n
                        idInfo="ID: "+id1
                        itemInfo.insert(tk.END,nameInfo)
                        itemInfo.insert(tk.END,idInfo)
                        prov="{0}".format(item[2])
                        provInfo="PROVIDER: "+prov
                        loc="{0}".format(item[3])
                        locInfo="LOCATION: "+loc
                        price="{0}".format(item[4])
                        priceInfo="PRICE: "+price
                        quan="{0}".format(item[5])
                        quanInfo="QUANTITY: "+quan
                        desc="{0}".format(item[6])
                        descInfo="DESC: "+desc
                        itemInfo.insert(tk.END,provInfo)
                        itemInfo.insert(tk.END,locInfo)
                        itemInfo.insert(tk.END,priceInfo)
                        itemInfo.insert(tk.END,quanInfo)
                        itemInfo.insert(tk.END,descInfo)

    #Creates the window for an item request
    def reqItm():
        #Create the window
        req=tk.Toplevel(root)
        req.title('Request Item')
        req.geometry("200x100")
        req.configure(bg='#D58936')
        req.resizable(False, False)
        req.grid_columnconfigure(1,weight=1)
        req.grid_rowconfigure(2,weight=1)

        #Label and create the entry field for request quantity
        lbl=tk.Label(req,text='Input desired quantity')
        lbl.configure(bg='#D58936')
        lbl.grid(columnspan=2,column=0,row=0)
        quanVar = StringVar()
        quantity = Entry(req, textvariable=quanVar)
        quantity.grid(row=1, column=1)

        #Creates the item request
        def sendReq():
            #Make sure an item is selected
            try:
                itemInfo = shopList.selection_get()
            except:
                tk.messagebox.showinfo("ERROR", "No item selected")
                return
            #Make sure a quantity has been entered
            if(quantity.get()==""):
                tk.messagebox.showinfo("ERROR", "Quantity cannot be left blank.") 
                return
            #Format the request
            newReq =[username, itemInfo, quantity.get()]
            #Destroy request window
            req.destroy()
            #Read the requests field
            with open("requests.csv",mode="r") as file:
                items = csv.reader(file)
                for item in items:
                    #Make sure the item isnt empty
                    if (item != []):
                        #Make sure that there is enough of the item in stock to fulfil the request
                        #Maybe this should be changed to a step in accepting the request on the admin page?
                        if(item[5]<quantity.get()):
                            tk.messagebox.showinfo("ERROR", "Quantity requested is greater than quantity available") 
            #Add the new request to requests.csv
            with open("requests.csv",mode='a')as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(newReq)
        
        #Create the enter button that executes the sendReq command
        enterButton=tk.Button(req,text='Enter',command=sendReq,bg='#D58936')
        enterButton.grid(column=1,row=2)
        
    #Create the search button that can open the search frame
    searchButton=tk.Button(left, text="Search", command=showSearch, bg="#a44200", fg="#d58936", width=33, height=1, font=("Book Antiqua", 15))
    searchButton.grid(row=3, column=0, columnspan=2)

    #Create a frame that holds the action buttons
    actions=tk.Frame(content, bg="#f2f3ae", width=400, height=205,)
    actions.grid(row=1, column=2, padx=15)

    #Label the actions frame
    actionsHeader=tk.Label(actions, bg="#69140e", fg="#d58936", text="Actions", font=("Book Antiqua", 15), width=32, height=2)
    actionsHeader.grid(row=0, sticky="ew")

    #Create a frame within the actions frame to hold the buttons
    actionsBody=tk.Frame(actions, bg="#f2f3ae", width=32, height=10)
    actionsBody.grid(row=1, column=0, sticky="ew")

    #Create buttons to add favorites, remove favorites, request an item, and show item info, put these in the action frame
    favButton=tk.Button(actionsBody,text="Favorite Item",bg="#D58936",width=23,height=3,command="favItem", font=("Book Antiqua", 8))
    favButton.grid(row=0, column=0, padx=15, pady=10)

    remFavButton=tk.Button(actionsBody,text="Remove Favorite",bg="#D58936",width=23,height=3,command="remFav", font=("Book Antiqua", 8))
    remFavButton.grid(row=0, column=1, padx=15, pady=10)

    reqItmButton=tk.Button(actionsBody,text="Request Item",bg="#D58936",width=23,height=3,command=reqItm, font=("Book Antiqua", 8))
    reqItmButton.grid(row=1, column=0, padx=15, pady=10)

    showItmButton=tk.Button(actionsBody,text="Show Item",bg="#D58936",width=23,height=3,command=showItem,font=("Book Antiqua", 8))
    showItmButton.grid(row=1, column=1, padx=15, pady=10)

    #Create a bottom frame to hold the "about us" and "log out" buttons
    bottom=tk.Frame(root, bg="#D58936", width=960, height=100)
    bottom.grid(row=2, column=1)

    #Create a window that lets the user decide if they are ready to log out
    def logoutPrompt():
        #Create log out window
        logoutBox= tk.Toplevel(root)
        logoutBox.geometry("600x250")
        logoutBox.title("Log out?")
        logoutBox.configure(bg="#D58936")
        
        #Label the log out options
        logoutConfirm=tk.Label(logoutBox, text= "Are you sure you would like to log out?", bg="#D58936", font=("Book Antiqua", 15))
        logoutConfirm.grid(row=0, column=0, pady=40, columnspan=2)

        #Create a frame to contain both log out buttons
        yesOrNo=tk.Frame(logoutBox, bg="#D58936", width=600, height=150)
        yesOrNo.grid(row=1, column=0, columnspan=2, pady=30, padx=20)

        #Destroy the main page and send users back to the log in page
        def log_out():
            make_logIn()
            root.destroy()

        #Destroy log out page
        def stay():
            logoutBox.destroy()

        #Create button that executes the log out command
        logoutYes=tk.Button(yesOrNo, text="Yes", width=8, height=1, bg="#69140e", fg="#d58936", font=("Book Antiqua", 15),command=log_out)
        logoutYes.grid(row=2, column=0, padx=20)

        #Create button that quits the log out and returns to the main page
        logoutNo=tk.Button(yesOrNo, text="No", width=8, height=1, bg="#69140e", fg="#d58936", font=("Book Antiqua", 15),command=stay)
        logoutNo.grid(row=2, column=1, padx=10)
              
    #Create the log out button that can make the log out window
    logoutButton=tk.Button(bottom, bg="#69140e", fg="#d58936", text="Log Out", command=logoutPrompt, font=("Book Antiqua", 15), width=13, height=1)
    logoutButton.grid(row=1, column=1, padx=20)

    #Creates the about us window
    #Change about us so that it differentiates between the original team and details about my fixes and general update
    def openAboutUs():
        #Create window
        aboutPage= tk.Toplevel(root)
        aboutPage.geometry("1000x500")
        aboutPage.title("About Us")
        aboutPage.configure(bg="#69140e")
        aboutPage.resizable(False, False)

        #Label the window
        aboutLabel=tk.Label(aboutPage, text="About Us: BDGS", font=("Book Antiqua", 50), bg="#69140e", fg="#D58936")
        aboutLabel.grid(row=0, column=2, columnspan=2)

        #Create and format my image
        rawBeck = Image.open("beck.png")
        beck=rawBeck.resize((200, 200))
        beckDisplay = ImageTk.PhotoImage(beck)
        beckPlace = tk.Label(aboutPage, image=beckDisplay, highlightbackground="#D58936", highlightthickness=2)
        beckPlace.image=beckDisplay
        beckPlace.grid(row=1, column=0, padx=20, pady=20)

        #Create and label my description
        beckName=tk.Label(aboutPage, text="Beck Towne", font=("Book Antiqua", 25), bg="#69140e", fg="#D58936")
        beckName.grid(row=2, column=0, padx=20)
        beckDescription=tk.Label(aboutPage, text="Team Member\nComputer Science\nMarist '27\nrebecca.towne1@marist.edu", font=("Book Antiqua", 18), bg="#69140e", fg="#f2f3ae")
        beckDescription.grid(row=3, column=0, padx=20)

        #Create and format devin's image
        rawDevin=Image.open("DevinPlaceholder.png")
        devin=rawDevin.resize((200, 200))
        devinDisplay=ImageTk.PhotoImage(devin)
        devinPlace=tk.Label(aboutPage, image=devinDisplay, highlightbackground="#D58936", highlightthickness=2)
        devinPlace.image=devinDisplay
        devinPlace.grid(row=1, column=1, columnspan=2, padx=10, pady=20)

        #Create and format devin's description
        devinName=tk.Label(aboutPage, text="Devin Melillo", font=("Book Antiqua", 25), bg="#69140e", fg="#D58936")
        devinName.grid(row=2, column=1, columnspan=2, padx=20)
        devinDescription=tk.Label(aboutPage, text="Team Member\nDigital Media\nMarist '27\ndevin.melillo1@marist.edu", font=("Book Antiqua", 18), bg="#69140e", fg="#f2f3ae")
        devinDescription.grid(row=3, column=1, columnspan=2, padx=10)

        #Create and format grace's image
        rawGrace=Image.open("Grace.png")
        grace=rawGrace.resize((200,200))
        graceDisplay=ImageTk.PhotoImage(grace)
        gracePlace=tk.Label(aboutPage, image=graceDisplay, highlightbackground="#D58936", highlightthickness=2)
        gracePlace.image=graceDisplay
        gracePlace.grid(row=1, column=3, columnspan=2, padx=10, pady=10)

        #Create and format grace's description
        graceName=tk.Label(aboutPage, text="Grace Markus", font=("Book Antiqua", 25), bg="#69140e", fg="#D58936")
        graceName.grid(row=2, column=3, columnspan=2, padx=20)
        graceDescription=tk.Label(aboutPage, text="Team Member\nData Science\nMarist '27\ngrace.markus1@marist.edu", font=("Book Antiqua", 18), bg="#69140e", fg="#f2f3ae")
        graceDescription.grid(row=3, column=3, columnspan=2, padx=10)

        #Create and format ren's image
        #Ask ren which name they want on this page
        rawSoph=Image.open("Soph.png")
        soph=rawSoph.resize((200,200))
        sophDisplay=ImageTk.PhotoImage(soph)
        sophPlace=tk.Label(aboutPage, image=sophDisplay, highlightbackground="#D58936", highlightthickness=2)
        sophPlace.image=sophDisplay
        sophPlace.grid(row=1, column=5, padx=10, pady=10)

        #Create and format ren's description
        sophName=tk.Label(aboutPage, text="Sophia Masone", font=("Book Antiqua", 25), bg="#69140e", fg="#D58936")
        sophName.grid(row=2, column=5, padx=20)
        sophDescription=tk.Label(aboutPage, text="Group Leader\nComputer Science\nMarist '27\nsophia.masone1@marist.edu", font=("Book Antiqua", 18), bg="#69140e", fg="#f2f3ae")
        sophDescription.grid(row=3, column=5, padx=10)

    #Create a button that brings up the about us page
    aboutUsButton=tk.Button(bottom, bg="#69140e", fg="#d58936", text="About Us", command=openAboutUs, font=("Book Antiqua", 15), width=13, height=1)
    aboutUsButton.grid(row=1, column=0, padx=20)
    
#Create the log in page
def make_logIn():
    global userInput
    global passInput
    global passwords
    global fn
    global window
    fn='credentials.csv'
    passwords=[['G','1','U']]
    window=tk.Tk()
    window.title('Little Shoppe')
    window.geometry('800x400')
    window.configure(bg='#D58936')
    window.resizable(width=False,height=False)

    Top=tk.Frame(window,bg='#D58936',height=100,width=800)
    Body=tk.Frame(window,bg='#D58936',height=200,width=800)
    Bottom=tk.Frame(window,bg='#D58936',height=200,width=800)

    Top.grid(row=0, sticky="ew")
    Body.grid(row=1, sticky="nsew")
    Bottom.grid(row=2, sticky="ew")

    #Create entry field for username
    userInput=tk.Entry(Body, fg="#D58936", bg="#A44200", width=25, font=("Book Antiqua", 20))
    userInput.grid(row=0,column=1)

    #Create entry field for password
    passInput=tk.Entry(Body, fg="#D58936", bg="#A44200", width=25, font=("Book Antiqua", 20), show="*")
    passInput.grid(row=3,column=1)

    #When you fix this, put the entry fields and labels next to each other

    #Check if the usernames and passwords are correct, log in the user if true
    def login():
        with open("credentials.csv",mode="r") as file:
            users = csv.reader(file)
            logged= False
            #Check if the user is a guest or admin
            for item in users:
                if (item != []):
                    if (userInput.get().lower() == item[0].lower() and passInput.get() == item[1] and item[2] == "admin"):
                        #If admin, create admin window
                        make_admin()
                        logged=True
                        break
                    elif (userInput.get().lower() == item[0].lower() and passInput.get() == item[1] and item[2] == "guest"):
                        #If guest, create guest window
                        make_window()
                        global username
                        username = item[0]
                        logged=True
                        break
            #If login unsuccessful, show error explaining this to user
            if not logged:
                messagebox.showinfo("Contacts", "Invalid Username or Password")

    #Title the login page
    title=tk.Label(Top, text='Little Shoppe Login', fg="#D58936", bg="#69140E", font=("Book Antiqua", 40, "bold", "italic"), justify='center')
    title.grid(row=0,column=0,pady=50,padx=165)

    #Create exit button that can close the login window
    exitButton = tk.Button(text="X", width=3, height=1, bg="#A44200", fg="#3C1518", font=("Arial", 25), command=window.destroy)
    exitButton.grid(row=0,column=0,pady=0,padx=700)

    #Label the username entry field
    lblUsername=tk.Label(Body, text='Username:', fg="#3C1518", bg="#D58936", font=("Book Antiqua", 17, "bold"))
    lblUsername.grid(row=0,column=0,pady=10,padx=60)

    #Label the password entry field
    lblPassword=tk.Label(Body, text='Password:', fg="#3C1518", bg="#D58936", font=("Book Antiqua", 17, "bold"))
    lblPassword.grid(row=3,column=0,pady=35,padx=60)

    #Create button that executes login command
    loginButton = tk.Button(Bottom, text="LOG IN", width=10, height=1, bg="#F2F3AE", fg="#A44200", justify='center', font=("Book Antiqua", 14, "bold"),command=login)
    loginButton.grid(row=0,column=3,pady=0,padx=350)

#The program should start by creating the login by default
make_logIn()

#During fix, make sure the program checks to see if these files already exist so that they don't rewrite changes made during the program runtime when the program is reopened

#List of default users
startingUsers = [["Admin","123","admin"],["Guest","password","guest"]]

#Make sure starting users are written in credentials.csv
with open("credentials.csv",mode="w")as file:
    csvwriter = csv.writer(file)
    csvwriter.writerows(startingUsers)

#List of default store items
storeItems=[['Blue Potion','0001','Potions.Inc','location','30','7','desc'],
               ['Red Potion','0002','Potions.Inc','location','30','7','desc'],
               ['Blue Potion','0003','Potions.Inc','location','30','7','desc'],
               ['Dagger','0004','Old Man','Alley','30','7','desc']]

#List of favorites (favorites functionality must be finalized and improved)
favorites=[['0001'],['0001']]

#Make sure default items are written in inventory.csv
with open("inventory.csv",mode='w')as file:
    csvwriter = csv.writer(file)
    csvwriter.writerows(storeItems)

#Necessary for tkinter to run the code and continue allowing the user to interact with the gui until all windows are closed
tk.mainloop()
