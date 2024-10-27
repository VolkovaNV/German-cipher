from random import shuffle, choice
from itertools import product, accumulate
from numpy import floor, sqrt
import tkinter as tk

class Shifr:
    def __init__(self, spoly, k, alph='ADFGVX'):
        self.polybius = [element.upper() for element in spoly]
        self.pdim = int(floor(sqrt(len(self.polybius))))
        self.key = list(k.upper())
        self.keylen = len(self.key)
        self.alphabet = list(alph)
        pairs = [p[0] + p[1] for p in product(self.alphabet, self.alphabet)]
        self.encode = dict(zip(self.polybius, pairs))
        self.decode = dict((v, k) for (k, v) in self.encode.items())

    def Zah1(self, msg):
        chars = list(''.join([self.encode[c] for c in msg.upper() if c in self.polybius]))
        colvecs = [(lett, chars[i:len(chars):self.keylen]) \
                   for (i, lett) in enumerate(self.key)]
        colvecs.sort(key=lambda x: x[0])
        return ''.join([''.join(a[1]) for a in colvecs])

    def Rah1(self, cod):
        chars = [c for c in cod if c in self.alphabet]
        sortedkey = sorted(self.key)
        order = [self.key.index(ch) for ch in sortedkey]
        originalorder = [sortedkey.index(ch) for ch in self.key]
        base, extra = divmod(len(chars), self.keylen)
        strides = [base + (1 if extra > i else 0) for i in order]
        starts = list(accumulate(strides[:-1], lambda x, y: x + y))
        starts = [0] + starts
        ends = [starts[i] + strides[i] for i in range(self.keylen)]
        cols = [chars[starts[i]:ends[i]] for i in originalorder]
        pairs = []
        for i in range((len(chars) - 1) // self.keylen + 1):
            for j in range(self.keylen):
                if i * self.keylen + j < len(chars):
                    pairs.append(cols[j][i])

        return ''.join([self.decode[pairs[i] + pairs[i + 1]] for i in range(0, len(pairs), 2)])

def Inteface():
    root = tk.Tk()
    root.title("Лабораторная №2")
    text_label = tk.Label(root, text="Сообщение:")
    text_label.grid(row=0, column=0)
    key_label = tk.Label(root, text="Ключ:")
    key_label.grid(row=1, column=0)
    result_label = tk.Label(root, text="Рузультат:")
    result_label.grid(row=3, column=0)
    text_entry = tk.Entry(root)
    text_entry.grid(row=0, column=1)
    key_entry = tk.Entry(root)
    key_entry.grid(row=1, column=1)
    Res = tk.Text(root, height=5, width=50)
    Res.grid(row=3, column=1)

    encrypt_button = tk.Button(root, text="Зашифровать", command=lambda: Zah2(text_entry.get(), key_entry.get(), Res))
    encrypt_button.grid(row=2, column=0)
    decrypt_button = tk.Button(root, text="Расшифровать", command=lambda: Rah2(text_entry.get(), key_entry.get(), Res))
    decrypt_button.grid(row=2, column=1)

    root.mainloop()

def Zah2(text, key, Res):
    adfgvx = Shifr(PCHARS, key)
    encrypted_text = adfgvx.Zah1(text)
    Res.delete(1.0, tk.END)
    Res.insert(tk.END, encrypted_text)

def Rah2(text, key, Res):
    adfgvx = Shifr(PCHARS, key)
    decrypted_text = adfgvx.Rah1(text)
    Res.delete(1.0, tk.END)
    Res.insert(tk.END, decrypted_text)


PCHARS = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
shuffle(PCHARS)

Inteface()

