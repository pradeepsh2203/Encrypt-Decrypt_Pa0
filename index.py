# Import Python Tkinter library for GUI
from tkinter import *


def clear_text():
    enciper.delete("1.0", 'end')
    deciper.delete("1.0", "end")


# This function first convert the input text character into there ascii code (one by one) and then perform an airthmetic operation only when the characters are english alphabets.
def encrypt_decrypt_text(enciper, deciper):
    text = enciper.get("1.0", 'end')
    deciper.delete("1.0", 'end')
    res = ""
    for a in range(len(text) - 1):
        ascii = ord(text[a])
        if (ascii >= 65 and ascii <= 90):
            ascii = (25 - ascii + 65) % 26 + 65
        elif (ascii >= 97 and ascii <= 122):
            ascii = (25 - ascii + 97) % 26 + 97
        res += chr(ascii)
    deciper.insert("1.0", res)


root = Tk()
root.title("Encrypter and Decrypter")
# The main frame containing the Encipher and decipher text boxes
frame = LabelFrame(root, text="The App", padx=20, pady=20)
frame.pack(padx=10, pady=10)

label = Label(frame, text="Encipher and Decipher")
label.grid(row=0, column=2)

# The text box for the user to input the normal text
enciper = Text(frame, width=50, height=10, pady=5, padx=5)
enciper.grid(row=1, column=0, columnspan=2)

# The text box for the user to input the cryptic message
deciper = Text(frame, width=50, height=10, pady=5, padx=5)
deciper.grid(row=1, column=3, columnspan=2)

clear_btn = Button(frame, text="Clear All", command=clear_text)
clear_btn.grid(row=3, column=2, pady=5)

enciper_btn = Button(frame,
                     text="Encrypt",
                     command=lambda: encrypt_decrypt_text(enciper, deciper))
enciper_btn.grid(row=3, column=0, sticky="W", pady=5)

# Exploiting the symmetric nature of the used encryption algorithm because of which encryption of the crypted message results in the orignal text.
deciper_btn = Button(frame,
                     text="Decrypt",
                     command=lambda: encrypt_decrypt_text(deciper, enciper))
deciper_btn.grid(row=3, column=4, sticky="E", pady=5)

root.mainloop()