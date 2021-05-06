import tkinter as tk
from tkinter import messagebox
#from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

from main import File
from bitches_be_chordstreaming import bitches_be_chordstreaming
from bitches_be_delaying import bitches_be_custom
from bitches_be_chordjacking import bitches_be_chordjacking

root = tk.Tk()
root.title('Gorilla Trainer v1.2')
#root.iconbitmap('logo.ico')

canvas = tk.Canvas(root, width=370, height=450)
canvas.grid(columnspan=5, rowspan=9)

radioFrame = tk.Frame(root)

def pattern_check(patternStr):
    for x in range(len(patternStr)):
        if int(patternStr[x-1]) + int(patternStr[x]) > 7:
            return False
    return True


def open_file():
    global fileobj
    browse_text.set("loading...")
    fileobj = askopenfile(parent=root, mode="rb", title="Choose a file", filetype=[("osu file", "*.osu")])
    if fileobj:
        path_text.set(fileobj.name.split("/")[-1])
    browse_text.set("Browse")

def create_new_path(path, fileName):
    temp_list = path.split("/")
    temp_list = temp_list[:-1]
    new_path = ""
    for element in temp_list:
        new_path += element
        new_path += "/"
    new_path += fileName
    return new_path


def run():
    if fileobj:
        path = fileobj.name
        file = File(path)
        if patternChoice.get() == "Chord stream":
            if pattern_check(entryPattern.get()) == True:
                bitches_be_chordstreaming(file, entryPattern.get(), float(optionValue.get()))
                diffName = "AutoMap Chord Stream ({})".format(entryPattern.get())
                file.lines[file.diffIndex] = "Version:{}\n".format(diffName)
                fileName = "{} - {} ({}) [{}].osu".format(file.artist, file.title, file.mapper, diffName)
                path = create_new_path(file.path, fileName)
                file.save(path)
                messagebox.showinfo(title="Succes", message="Map created successfully")

            else:
                messagebox.showerror(title="Error", message="Specified pattern not possible without producing jacks")

        elif patternChoice.get() == "Chord jack":
            bitches_be_chordjacking(file, entryPattern.get(), float(optionValue.get()))
            diffName = "AutoMap Chord jack ({})".format(entryPattern.get())
            file.lines[file.diffIndex] = "Version:{}\n".format(diffName)
            fileName = "{} - {} ({}) [{}].osu".format(file.artist, file.title, file.mapper, diffName)
            path = create_new_path(file.path, fileName)
            file.save(path)
            messagebox.showinfo(title="Succes", message="Map created successfully")

        elif patternChoice.get() == "delay":
            if pattern_check(entryPattern.get()) == True:
                bitches_be_custom(file, entryPattern.get(), float(optionValue.get()))
                diffName = "AutoMap Delay ({})".format(entryPattern.get())
                file.lines[file.diffIndex] = "Version:{}\n".format(diffName)
                fileName = "{} - {} ({}) [{}].osu".format(file.artist, file.title, file.mapper, diffName)
                path = create_new_path(file.path, fileName)
                file.save(path)
                messagebox.showinfo(title="Succes", message="Map created successfully")

            else:
                messagebox.showerror(title="Error", message="Specified pattern not possible without producing jacks")
        else:
            messagebox.showerror(title="Error", message="Please select a pattern")
    else:
        messagebox.showerror(title="Error", message="Please select a referance chart")


entryPattern = tk.Entry(root)
entryPattern.grid(column=0, row=7)

#Radio buttons
patternChoice = tk.StringVar()
chordStream = tk.Radiobutton(radioFrame, text="Chord stream", variable=patternChoice)
chordStream.config(indicatoron=0, bd=4, width=12, value="Chord stream")
chordStream.grid(column=0, row=0)

chordJack = tk.Radiobutton(radioFrame, text="Chord jack", variable=patternChoice)
chordJack.config(indicatoron=0, bd=4, width=12, value="Chord jack")
chordJack.grid(column=1, row=0)

delay = tk.Radiobutton(radioFrame, text="delay", variable=patternChoice)
delay.config(indicatoron=0, bd=4, width=12, value="delay")
delay.grid(column=2, row=0)

radioFrame.grid(column=0, row=5)


#dropdown
OPTIONS = ["0.25", "0.50", "0.75", "1.00", "1.25", "1.50", "1.75", "2.00"]
optionValue = tk.StringVar()
optionValue.set(OPTIONS[3]) #1 default at 1

optionMenu = tk.OptionMenu(root, optionValue, *OPTIONS)
optionMenu.grid(column=2, row=7)

#Buttons
browse_text = tk.StringVar()
browse_text.set("Browse")
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#d5d9de")
browse_btn.grid(column=0, row=2)

go_text = tk.StringVar()
go_text.set("Go!")
go_btn = tk.Button(root, textvariable=go_text, command=lambda:run(),height=5, width=20, bg="#d5d9de")
go_btn.grid(column=0, row=8)

instruction = tk.Label(root, text="""Pattern string""")
instruction.grid(column=0, row=6)


path_text = tk.StringVar()
path_text.set("No .osu file selected")
pathLabel = tk.Label(root, textvariable=path_text)
pathLabel.grid(column=0, row=0)





root.mainloop()
