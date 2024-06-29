import tkinter as tk
import MailProgram
import camera_program
window=tk.Tk()
dis=0
frame=tk.Frame(master=window, width=400, height=300)
label=tk.Label(master=frame, text="Please introduce your E-Mail", width=50)
entry=tk.Entry(master=frame, width=50)

def runapp():
    dis=camera_program.camera()
    print(dis)

def sendmail():
    MailProgram.SendEmail(dis, entry.get())
    print(entry.get())
    entry.delete(0, tk.END)

runbutton=tk.Button(master=frame, text="RUN APP", width=10, height=5, bg="gray", fg="blue", command=runapp)
emailbutton=tk.Button(master=frame, text="Enter E-Mail", width=20, height=2, bg="gray", fg="white", command=sendmail)
frame.pack(fill=tk.X)
runbutton.pack()
label.pack()
entry.pack()
emailbutton.pack()