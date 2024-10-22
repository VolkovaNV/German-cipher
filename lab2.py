import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
import string
import numpy as np

window = Tk()
window.title("Лабораторная №2 шифр")
window.geometry("500x550")

# from pycipher import ADFGVX

# adfgvx = ADFGVX(key='PH0QG64MEA1YL2NOFDXKR3CVS5ZW7BJ9UTI8', keyword='GERMAN')

ADFGVX = 'ADFGVX'
alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
random.seed(42) 


# table = [
#     ['A', 'B', 'C', 'D', 'E', 'F'],
#     ['G', 'H', 'I', 'J', 'K', 'L'],
#     ['M', 'N', 'O', 'P', 'Q', 'R'],
#     ['S', 'T', 'U', 'V', 'W', 'X'],
#     ['Y', 'Z', '0', '1', '2', '3'],
#     ['4', '5', '6', '7', '8', '9']
# ]

# ADFGVX = 'ADFGVX'
# polybius_square = {
#     'A': 'ph0qg64mea1yl2nofdzxr3bvs5t7c8uk9w',
#     'D': 'a1yl2nofdzxr3bvs5t7c8uk9wph0qg64mea',
#     'F': 'l2nofdzxr3bvs5t7c8uk9wph0qg64mea1y',
#     'G': 'nofdzxr3bvs5t7c8uk9wph0qg64mea1yl2',
#     'V': 'ofdzxr3bvs5t7c8uk9wph0qg64mea1yl2n',
#     'X': 'dzxr3bvs5t7c8uk9wph0qg64mea1yl2nof'
# }

def generate_polybius_square():
    shuffled = list(alphabet)
    random.shuffle(shuffled)
    return {ADFGVX[i]: shuffled[i*6:(i+1)*6] for i in range(6)}

polybius_square = generate_polybius_square()


def Zah():
    global n
    message = e.get() 
    key = n.get()

    # validate_key(key)
    message = message.lower().replace(" ", "")
    encrypted = ''
    for char in message:
        for row in ADFGVX:
            if char in polybius_square[row]:
                col = ADFGVX[polybius_square[row].index(char)]
                encrypted += row + col
                break

    n = len(encrypted)
    key_len = len(key)
    padding_length = key_len - (n % key_len)
    encrypted += 'x' * padding_length  # Добавление символов-заполнителей
    sorted_key_indices = sorted(range(len(key)), key=lambda k: key[k])
    sorted_columns = [''] * key_len

    for i in range(key_len):
        sorted_columns[sorted_key_indices[i]] = encrypted[i::key_len]
            
    txt['text'] = ''.join(sorted_columns)
    print(''.join(sorted_columns))


def Rah():
    global n
    ciphertext = e.get()
    key = n.get()
    
    key_len = len(key)
    sorted_key_indices = sorted(range(len(key)), key=lambda k: key[k])
    n = len(ciphertext) // key_len
    sorted_columns = [''] * key_len

    idx = 0
    for i in sorted_key_indices:
        sorted_columns[i] = ciphertext[idx:idx+n]
        idx += n

    decrypted = ''
    for i in range(n):
        for j in range(key_len):
            decrypted += sorted_columns[j][i]

    decoded = ''
    for i in range(0, len(decrypted), 2):
        row = decrypted[i]
        col = decrypted[i+1]
        if row in polybius_square and col in ADFGVX:
            decoded += polybius_square[row][ADFGVX.index(col)]

    txt['text'] = decoded

Label( text = "Введите  сообщение: ").pack()
e = Entry( width=90, bd=50)
e.pack()
e.focus_set()
Label( text = "Введите  ключ: ").pack()
n = Entry( width=90, bd=50)
n.pack()
n.focus_set()
go = Button( text = "Зашифровать",command=Zah )
go.pack()
go1 = Button( text = "Расшифровать",command=Rah)
go1.pack()


# B1.bind("<Button>", Zah)
#Button(window, text='Выйти', command=window.destroy).pack()
txt = Label(window, text="Результат", height=10, width=60)
txt.pack()

# go.bind("<Button>", command = FixedSubstitutionCipher)
#GBACGFGFMSECMSMFGFAD secret hello world

window.mainloop()