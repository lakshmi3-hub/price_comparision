from tkinter import * #Tkinter is used to create GUI applications
from tkinter import Scrollbar
from bs4 import BeautifulSoup#Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide ways of navigating, searching, and modifying the parse tree.
import requests #The requests module allows you to send HTTP requests using Python.
import webbrowser#The webbrowser module provides  interface to allow displaying Web-based documents to users
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
#The User-Agent request header is a characteristic string that lets servers and network peers identify the application, operating system, vendor and version of the requesting user agent.
flipkart=''
croma=''
amazon=''
def flipkart(name):
    try:
        global flipkart
        name1 = name.replace(" ","+")
        flipkart=f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off'
        res = requests.get(f'https://www.flipkart.com/search?q={name1}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off',headers=headers)
        #f-string evaluates at runtime of the program
        soup = BeautifulSoup(res.text,'html.parser')
        flipkart_name = soup.select('._4rR01T')[0].getText().strip()  #class for product_name
        flipkart_name = flipkart_name.upper()
        if name.upper() in flipkart_name:
            flipkart_price = soup.select('._1_WHN1')[0].getText().strip()  #class for product_price
            flipkart_name = soup.select('._4rR01T')[0].getText().strip()

            return f"{flipkart_name}\nPrice : {flipkart_price}\n"
        else:

            flipkart_price='Product not found for similar products check link'
        return flipkart_price
    except:

        flipkart_price= 'Product not found for similar products check link '
    return flipkart_price

def croma(name):
    try:
        global croma
        name1 = name.replace(" ","+")
        croma=f'https://www.croma.com/search/?text={name1}'
        res = requests.get(f'https://www.croma.com/search/?text={name1}',headers=headers)

        soup = BeautifulSoup(res.text,'html.parser')
        croma_name = soup.select('h3')

        croma_page_length = int( len(croma_name))
        for i in range (0,croma_page_length):
            name = name.upper()
            croma_name = soup.select('h3')[i].getText().strip().upper()
            if name in croma_name.upper()[:25]:
                croma_name = soup.select('h3')[i].getText().strip().upper()
                croma_price = soup.select('.pdpPrice')[i].getText().strip()

                break
            else:
                i+=1
                i=int(i)
                if i==croma_page_length:

                    croma_price = 'Product not found for similar products check link '
                    break

        return f"{croma_name}\nPrice : {croma_price}\n"
    except:

        croma_price = ' Product not found for similar products check link'
    return croma_price

def amazon(name):
    try:
        global amazon
        name1 = name.replace(" ","-")
        name2 = name.replace(" ","+")
        amazon=f'https://www.amazon.in/{name1}/s?k={name2}'
        res = requests.get(f'https://www.amazon.in/{name1}/s?k={name2}',headers=headers)

        soup = BeautifulSoup(res.text,'html.parser')
        amazon_page = soup.select('.a-color-base.a-text-normal')
        amazon_page_length = int(len(amazon_page))
        for i in range(0,amazon_page_length):
            name = name.upper()
            amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
            if name in amazon_name[0:20]:
                amazon_name = soup.select('.a-color-base.a-text-normal')[i].getText().strip().upper()
                amazon_price = soup.select('.a-price-whole')[i].getText().strip().upper()

                break
            else:
                i+=1
                i=int(i)
                if i==amazon_page_length:

                    amazon_price = 'Product not found for similar products check link'
                    break
        return f"{amazon_name}\nPrice : {amazon_price}\n"
    except:

        amazon_price = 'Product not found for similar products check link'
    return amazon_price
def olx(name):
    try:
        global olx
        name1 = name.replace(" ","-")
        olx=f'https://www.olx.in/items/q-{name1}?isSearchCall=true'
        res = requests.get(f'https://www.olx.in/items/q-{name1}?isSearchCall=true',headers=headers)

        soup = BeautifulSoup(res.text,'html.parser')
        olx_name = soup.select('._2tW1I')
        olx_page_length = len(olx_name)
        for i in range(0,olx_page_length):
            olx_name = soup.select('._2tW1I')[i].getText().strip()
            name = name.upper()
            olx_name = olx_name.upper()
            if name in olx_name:
                olx_price = soup.select('._89yzn')[i].getText().strip()
                olx_name = soup.select('._2tW1I')[i].getText().strip()
                olx_loc = soup.select('.tjgMj')[i].getText().strip()
                try:
                    label = soup.select('._2Vp0i span')[i].getText().strip()
                except:
                    label = "OLD"

                break
            else:
                i+=1
                i=int(i)
                if i==olx_page_length:

                    olx_price = 'Product not found for similar products check link'
                    break
        return f"{olx_name}\nPrise : {olx_price}\n"
    except:

        olx_price = 'Product not found for similar products check link'
    return olx_price


def urls():
    global flipkart
    global croma
    global amazon
    global olx
    return f"{flipkart}\n\n\n{croma}\n\n\n{amazon}\n\n\n{olx}"



def open_url(event):
        global flipkart
        global croma
        global amazon
        global olx
        webbrowser.open_new(flipkart)
        webbrowser.open_new(croma)
        webbrowser.open_new(amazon)
        webbrowser.open_new(olx)

def search():
    search_button.place_forget()
    t1=flipkart(product_name.get())
    box1.insert(1.0,t1)

    t2=croma(product_name.get())
    box2.insert(1.0,t2)

    t3=amazon(product_name.get())
    box3.insert(1.0,t2)

    t4=olx(product_name.get())
    box4.insert(1.0,t4)

    t5 = urls()
    box5.insert(1.0,t5)


window = Tk()
window.title("Prise comparison on ecommerce")
window.minsize(1000,700)

lableone =  Label(window, text="Enter Product Name :", font=("bold", 15))
lableone.place(relx=0.1, rely=0.1, anchor="center")

product_name =  StringVar()#It is used to table entry
product_name_entry =  Entry(window, textvariable=product_name, width=50)#To accept single line entry from users
product_name_entry.place(relx=0.5, rely=0.1, anchor="center")

search_button =  Button(window, text="Get Cost", width=12, command= search)
search_button.place(relx=0.5, rely=0.2, anchor="center")


l1 =  Label(window, text="flipkart", font=("bold", 20))
l2 =  Label(window, text="croma", font=("bold", 20))
l3 =  Label(window, text="amazon", font=("bold", 20))
l4 =  Label(window, text="olx", font=("bold", 20))
l5 =  Label(window, text="All urls", font=("bold", 20))

l1.place(relx=0.1, rely=0.3, anchor="center")
l2.place(relx=0.5, rely=0.3, anchor="center")
l3.place(relx=0.1, rely=0.6, anchor="center")
l4.place(relx=0.5, rely=0.6, anchor="center")
l5.place(relx=0.8,rely=0.3,anchor="center")

scrollbar = Scrollbar(window)
box1 =  Text(window, height=7, width=35, yscrollcommand=scrollbar.set)

box2 =  Text(window, height=7, width=35, yscrollcommand=scrollbar.set)

box3 =  Text(window, height=7, width=35, yscrollcommand=scrollbar.set)

box4 =  Text(window, height=7, width=35, yscrollcommand=scrollbar.set)

box5 =  Text(window, height=30, width=10, yscrollcommand=scrollbar.set)


box1.place(relx=0.2, rely=0.4, anchor="center")
box2.place(relx=0.5, rely=0.4, anchor="center")
#box3.place(relx=0.8, rely=0.4, anchor="center")
box3.place(relx=0.2, rely=0.7, anchor="center")
box4.place(relx=0.5, rely=0.7, anchor="center")

box5 =  Text(window, height=15, width=40, yscrollcommand=scrollbar.set, fg="blue", cursor="hand2")
box5.place(relx=0.85, rely=0.5, anchor="center")
box5.bind("<Button-1>", open_url)


window.mainloop()
