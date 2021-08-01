
print("NoLine is bootng up")
import datetime
print("datetime imported")
import os
print("os imported")
import sys 
print("sys imported")
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
print("tkinker imported, renamed to tk")
datetime.datetime.now()
datetime.datetime(2009, 1, 6, 15, 8, 24, 78915)
helpUseage = 0

print(" ")
SelectedPin = "0000"

Pin = input("Enter Pin >")

if Pin == SelectedPin:
    print("Welcome USER")
    print("Todays date and time:")
    print(datetime.datetime.now())
    
   
    while True :
        command = input("Input Command >")
        #commands
        if command == "help":
            if helpUseage == 10:
                print("You cant run from NoLine OS... No one can help you either...")
                helpUseage = helpUseage + 1
                print(" ")
            else:
                print("Commands:")
                print("help - Displays all documented commands")
                print("today - Displays date and time")
                print("open - opens files within the python code")
                print("files - shows all files (all files found in the folder this os is in)")
                print("customOpen - opens a file on your computer (all files found in the folder this os is in)")
                print("customWrite - edits a file on your computer (all files found in the folder this os is in)")
                print("customAppend - works like customWrite, but instead of overwriting the file, it appends to it (all files found in the folder this os is in)")
                print("customCreate - creates a new .txt document for you to put content in (the new faile will be in the same folder as the OS)")
                print("customRemove - removes a file, USE AT YOUR OWN RISK, NOLINE IS NOT RESPONSIBLE FOR ANY LOSS OF IMPORTANT INFORMATION (can oly remove files inside the folder the os is in)")
                print("tkNotepad - an aplication version of customCreate (the new faile will be in the same folder as the OS)")

                print("about - about this OS")
                print("whatsNew - update documentation")
                print("exit - quits the OS")
                helpUseage = helpUseage + 1
                print(" ")
        elif command == "open":
            print("Files")
            print("   -OS")
            print(" ")
            response = input("State directory name >")
            #dir sys
            if response == "OS":
                print(" ")
                print("OS")
                print("    -Test.txt")
                print("    -ReadMe.txt")
                print(" ")
                response = input("[OS] State directory name >")
                if response == "Test.txt":
                    print(" ")
                    print("Opening Test.txt")
                    print(" ")
                    print("[Test.txt] Hello world, this is a test!")
                    print(" ")
                elif response == "ReadMe.txt":
                    print(" ")
                    print("Opening Test.txt")
                    print(" ")
                    print("[ReadMe.txt] Thank you for choosing NoLine command line OS!")
                    print("This OS is made entirly out of python!")
                    print("You may edit this os, as long asyou dont break it or use it for ilegal stuff. Im watching you.")
                    print("To get started, type in <help>")
                    print("(without the <> of course)")
                    print(" ")
                    

            elif response == "exit":
                print("exited")
                print(" ")
            else:
                print(" ")
                print("Directory not found")
                print(" ")
        elif command == "today":
             print("Todays date and time:")
             print(datetime.datetime.now())
             print(" ")
        elif command == "about":
                print("NoLine")
                print("A mini Opreating system.")
                print("Doesnt Do Much")
                print("ver 0.6")
                print(" ")
        elif command == "customOpen":
            print(" ")
            entries = os.listdir(os.getcwd())
            print("[" + os.getcwd() + "]")
            for entry in entries:
                print(entry)
            print(" ")
            response = input("State directory name >")
            if response == "exit":
                print("exited")
                print(" ")
            else:
                if os.path.exists(response):
                    print(" ")
                    f = open(response, "r")
                    print(f.read())
                    print(" ")
                    input("Waiting for an input so the OS can close the file...>")
                    f.close()
                else:
                    print("File Does not exsist")
                    print(" ")

                
        elif command == "customWrite":
            print(" ")
            entries = os.listdir(os.getcwd())
            print("[" + os.getcwd() + "]")
            for entry in entries:
                print(entry)
            print(" ")
            response = input("State directory name >")
            if response == "exit":
                print("exited")
                print(" ")
            else:
                 if os.path.exists(response):
                    print(" ")
                    f = open(response, "r")
                    print(f.read())
                    f.close()
                    print(" ")
                    string = input("Input desired string >")
                    f = open(response, "w")
                    f.write(string)
                    f.close()
                    print(" ")
                    f = open(response, "r")
                    print(f.read())
                    input("Waiting for an input so the OS can close the file...>")
                    f.close()
                 else:
                    print("File Does not exsist")
                    print(" ")
                
        elif command == "customCreate":
            print(" ")
            response = input("Choose directory name >")
            if response == "exit":
                print("exited")
                print(" ")
            else:
                print(" ")
                print("The filename will be " + response + ".txt")
                print(" ")
                newF = open(response + ".txt","x")
                print(" ")
                content = input("Input Content >")
                newF.write(content)
                newF.close()
                print(" ")
                print("Content has been saved.")
                print(" ")
                print("Content:")
                f = open(response + ".txt","r")
                print(f.read())
                print(" ")
                input("Waiting for an input so the OS can close the file...>")

                f.close()
        elif command == "customAppend":
            print(" ")
            entries = os.listdir(os.getcwd())
            print("[" + os.getcwd() + "]")
            for entry in entries:
                print(entry)
            print(" ")
            response = input("State directory name >")
            if response == "exit":
                print("exited")
                print(" ")
            else:
                if os.path.exists(response):
                    print(" ")
                    f = open(response, "r")
                    print(f.read())
                    f.close()
                    print(" ")
                    string = input("Input desired string >")
                    f = open(response, "a")
                    f.write(string)
                    f.close()
                    print(" ")
                    f = open(response, "r")
                    print(f.read())
                    input("Waiting for an input so the OS can close the file...>")
                    f.close()
                else:
                    print("File Does not exsist")
                    print(" ")
        elif command == "customRemove":
            print(" ")
            entries = os.listdir(os.getcwd())
            print("[" + os.getcwd() + "]")
            for entry in entries:
                print(entry)
            print(" ")
            response = input("State directory name >")
            if response == "exit":
                print("exited")
                print(" ")
            else:
                if os.path.exists(response):
                    print("you are about to delete "+ response)
                    confirm = input("are you sure? (y/n) >")
                    if confirm == "y":
                        os.remove(response)
                        print("Successufly removed " + response)
                        print(" ")

                    else:
                        print(response + " was not removed")
                        print(" ")

                else:
                    print("File Does not exsist")
                    print(" ")
        elif command == "files":
            print(" ")
            entries = os.listdir(os.getcwd())
            print("[" + os.getcwd() + "]")
            for entry in entries:
                print(entry)
            print(" ")
        elif command == "tk":
            print(" ")
            def testButtn():
                print(entry.get())
            print("Summoning tkinter GUI window")
            window = tk.Tk()
            window.title = "NoLine tk enviroment"
            title = tk.Label(text="NoLine")
            entry = tk.Entry()
            button = tk.Button(text = "Ok",command = testButtn)
            title.pack()
            entry.pack()
            button.pack()
            window.mainloop()
        elif command == "tkGrid":
            print(" ")
            print("unfinished")

        elif command == "tkNotepad":
             npContent = ""
             def open_file():
                """Open a file for editing."""
                filepath = askopenfilename(
                filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
                )
                if not filepath:
                    return
                textBox.delete("1.0", tk.END)
                with open(filepath, "r") as input_file:
                    text = input_file.read()
                    textBox.insert(tk.END, text)

             def save_file():
                """Save the current file as a new file."""
                filepath = asksaveasfilename(
                    defaultextension="txt",
                    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
                )
                if not filepath:
                    return
                with open(filepath, "w") as output_file:
                    text = textBox.get(1.0, tk.END)
                    output_file.write(text)
                    print("Saved to " + filepath)
                    
  
             window = tk.Tk()
             window.title("NoLine tkNotepad")
             window.rowconfigure(0, minsize=800, weight=1)
             window.columnconfigure(1, minsize=800, weight=1)
             frbuttons = tk.Frame(window,bg="black")
             openButtn = tk.Button(frbuttons, text="Open",fg="white",bg="#3d3d3d",command = open_file)
             saveBttn = tk.Button(frbuttons,text = "Save",fg="white",bg="#3d3d3d",command = save_file)
             textBox = tk.Text(window,fg="white",bg="black")
             frbuttons.grid(row=0, column=0, sticky="ns")
             openButtn.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
             saveBttn.grid(row=1, column=0, sticky="ew", padx=5)
             textBox.grid(row=0, column=1, sticky="nsew")
             




            
             window.mainloop()
             print("closed")
             print(" ")
        

        elif command == "whatsNew":
            print("as of [2021-8-1][ver 0.6]")
            print("this command you are using has been added.")
            print("tkNotepad has been added. <help> for more info!")
            print("bug fixes. (like crashing when opening a non-exsistant file)")
            print("tkNotepad Improved")
            print(" ")
        elif command == "exit":
            print("exiting...")
            sys.exit()
               
        else:
            print(command + " is a invalid command")
            print(" ")

else:
    print("Incorrect Pin")
    input("After an input, thr program will shut down")


