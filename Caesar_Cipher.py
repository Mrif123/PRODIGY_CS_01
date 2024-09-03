import tkinter as tk
from tkinter import messagebox

letters='abcdefghijklmnopqrstuvwxyz'
num_letters=len(letters)

def encrypt(plaintext,key):
   ciphertext=''
   for letter in plaintext:
       letter=letter.lower()
       if letter!=' ':
          index=letters.find(letter)
          if index== -1:
              ciphertext +=letter
          else:
              new_index=index + key 
              if  new_index >= num_letters:
                  new_index -=num_letters
              ciphertext +=letters[new_index]
   return ciphertext

def decrypt(ciphertext,key):
   plaintext=''
   for letter in ciphertext:
       letter=letter.lower()
       if letter!=' ':
          index=letters.find(letter)
          if index== -1:
              plaintext +=letter
          else:
              new_index=index - key 
              if  new_index <0:
                  new_index +=num_letters
              plaintext +=letters[new_index]
   return plaintext


class CaesarCipherApp:
    def __init__(self,root):
      self.root=root
      self.root.title("Caesar Cipher Program")

      tk.Label(root,text="Enter the key(1 to 26):").pack(pady=5)
      self.key_entry=tk.Entry(root)
      self.key_entry.pack(pady=5)

      tk.Label(root,text="Enter the Message:").pack(pady=5)
      self.message_entry=tk.Entry(root,width=50)
      self.message_entry.pack(pady=5)

      self.mode_var=tk.StringVar(value='e')
      tk.Radiobutton(root,text="Encrypt",variable=self.mode_var,value='e').pack(pady=5)
      tk.Radiobutton(root,text="Decrypt",variable=self.mode_var,value='d').pack(pady=5)
      tk.Button(root,text="Process",command=self.process).pack(pady=10)

      self.result_label=tk.Label(root,text="",wraplength=400)
      self.result_label.pack(pady=10)
    def process(self):
        key_str=self.key_entry.get()
        message=self.message_entry.get()
        if not key_str.isdigit():
            messagebox.showerror("Invalid Input","Key must be an Integer.")
            return
        key=int(key_str)
        if key < 1 or key > 26:
             messagebox.showerror("Invalid Input","Key must be between 1 and 26.")
             return
        mode=self.mode_var.get()
        if mode == 'e':
            result=encrypt(message,key)
            self.result_label.config(text=f'CIPHERTEXT:{result}')
        elif mode == 'd':
            result=decrypt(message,key)
            self.result_label.config(text=f'PLAINTEXT:{result}')
root=tk.Tk()
app=CaesarCipherApp(root)
root.mainloop()
    
                      
