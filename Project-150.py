from tkinter import *
import random
root = Tk()

root.title("Countries and Capitals")
root.geometry("500x500")
enter_country=Entry(root)
enter_capital=Entry(root)
country_list=Label(root)
capital_list=Label(root)
random_country_label=Label(root)
random_capital_label=Label(root)
listcountry=[]
listcapital=[]
def addcountry():
    country_name=enter_name.get()
    listcountry.append(country_name)
    country_list["text"]="Your Country List: " + str(listcountry)
def addcapital():
    capital_name=enter_name.get()
    listcapital.append(capital_name)
    capital_list["text"]="Your Capital List: " + str(listcapital)
def random_number():
    length=len(listcountry)
    random_no=random.randint(0, length-1)
    generated_random_co=listcountry[random_no]
    generated_random_ca=listcapital[random_no]
    random_country_label["text"]="Your Country is "+generated_random_co
    random_capital_label["text"]="Your Capital is "+generated_random_ca
btnco=Button(root, text="Add to the Country List", command=addcountry)
btnca=Button(root, text="Add to the Capital List", command=addcapital)
btn1=Button(root, text="Click to Find out your Countries and Capitals", command=random_number)
root.mainloop()