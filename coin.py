import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageSequence
import random
import threading
import time

class CoinFlipApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🪙 Coin Toss Game")
        self.root.geometry("400x500")
        self.root.configure(bg="#202020")

        self.choice = tk.StringVar()

        self.label = tk.Label(root, text="Choose Heads or Tails", font=("Arial", 16), bg="#202020", fg="white")
        self.label.pack(pady=10)

        self.radio_heads = tk.Radiobutton(root, text="Heads", variable=self.choice, value="Heads",
                                          font=("Arial", 14), bg="#202020", fg="white", selectcolor="#303030")
        self.radio_heads.pack()

        self.radio_tails = tk.Radiobutton(root, text="Tails", variable=self.choice, value="Tails",
                                          font=("Arial", 14), bg="#202020", fg="white", selectcolor="#303030")
        self.radio_tails.pack()

        self.coin_label = tk.Label(root, bg="#202020")
        self.coin_label.pack(pady=20)

        self.flip_button = tk.Button(root, text="Flip the Coin", command=self.start_flip,
                                     font=("Arial", 14), bg="#4CAF50", fg="white", padx=10, pady=5)
        self.flip_button.pack(pady=20)

        # Load images
        try:
            self.heads_img = ImageTk.PhotoImage(Image.open("head.png").resize((200, 200)))
            self.tails_img = ImageTk.PhotoImage(Image.open("tail.png").resize((200, 200)))

            # Load GIF frames for animation
            self.flip_gif = Image.open("coinflip.gif")
            self.frames = [ImageTk.PhotoImage(frame.resize((200, 200)))
                           for frame in ImageSequence.Iterator(self.flip_gif)]

        except Exception as e:
            messagebox.showerror("Image Load Error", f"Make sure heads.png, tails.png, and coin_flip.gif exist.\n\n{e}")
            self.root.destroy()

    def start_flip(self):
        if not self.choice.get():
            messagebox.showwarning("Choose one!", "Please select Heads or Tails before flipping.")
            return
        threading.Thread(target=self.flip_coin).start()

    def animate_gif(self):
        for frame in self.frames:
            self.coin_label.config(image=frame)
            time.sleep(0.05)

    def flip_coin(self):
        self.animate_gif()

        # Simulate flipping time
        time.sleep(0.5)

        result = random.choice(["Heads", "Tails"])
        final_img = self.heads_img if result == "Heads" else self.tails_img
        self.coin_label.config(image=final_img)

        if self.choice.get() == result:
            messagebox.showinfo("Result", f"It's {result}! 🎉 You won!")
        else:
            messagebox.showinfo("Result", f"It's {result}. 😢 You lost!")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CoinFlipApp(root)
    root.mainloop()
