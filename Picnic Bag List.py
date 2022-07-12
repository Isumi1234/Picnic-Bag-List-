from tkinter import*
import random

root=Tk()
root.title("List")
root.geometry("400x400")

random_food_list = Label(root)
random_food_sorted_list = Label(root)

def randomlist():
    randomlist = random.sample(range(0,3),1)
    random_food_list["text"] = "Listed_item : " + str(randomlist)
    randomlist.sort()
    label2["text"] = "Put Item no "+ str(random_list) + " In Bag"
    
btn=Button(root, text="liste_item : ",command=randomlist)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

random_food_list.place(relx=0.5,rely=0.5,anchor=CENTER)
random_food_sorted_list.place(relx=0.5,rely=0.6,anchor=CENTER) 

root.mainloop()