import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.geometry("500x350")
units = ["Kelvin","Fahrenheit","Celsius"]
def conv():
    unit = option.get()
    val = int(entry1.get())
    if(unit!="Kelvin"):
        if(unit=="Celsius"):
            val = val + 273.15
        elif(unit=="Fahrenheit"):
            val = (5/9) * (val - 32) + 273.15
    arr = [0, 0,0]
    arr[0] = val #kelvin
    arr[1] = val - 273.15 #celsius
    arr[2] = (9/5) * (val - 273.15) + 32 #fahrenheit
    result=""
    if(unit=="Kelvin"):
        result = "Celsius: "+str(arr[1]) + " | Fahrenheit: " + str(arr[2])
    elif(unit=="Celsius"):
        result = "Kelvin: "+str(arr[0]) + " | Fahrenheit: " + str(arr[2])
    else:
        result = "Kelvin: "+str(arr[0]) + " | Celsius: " + str(arr[1])
    res.configure(text=result)
    
    
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20,padx=60, fill="both", expand=True)
label = customtkinter.CTkLabel(master=frame, text="Conversion System", )
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="value")
entry1.pack(pady=12, padx=10)
option = customtkinter.CTkOptionMenu(master=frame,values=units) 
option.pack(pady=10)
button = customtkinter.CTkButton(master=frame, text="Convert", command=conv)
button.pack(pady=12, padx=10)
res = customtkinter.CTkLabel(master=frame,text="")
res.pack(pady=15)
root.mainloop()