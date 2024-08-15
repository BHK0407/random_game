import random
import tkinter as tk

class RandomNumberGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("***Bốc Thăm Trúng Thưởng***")

        # Center the window on the screen
        self.root.geometry("400x300")
        self.root.eval('tk::PlaceWindow . center')

        # Create and configure the result label
        self.result_label = tk.Label(root, text="", font=('Helvetica', 80), width=5, height=2, bg='white', fg='black')
        self.result_label.pack(expand=True)

        # Create a frame for buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20)

        # Create the Generate button
        self.generate_button = tk.Button(button_frame, text="Khách Hàng May Mắn Là Ai?", command=self.start_animation)
        self.generate_button.pack(side=tk.LEFT, padx=10)

        # Create the Reset button
        self.reset_button = tk.Button(button_frame, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)

        self.running = False

    def start_animation(self):
        if not self.running:
            self.running = True
            self.animate_numbers()

    def animate_numbers(self):
        if not self.running:
            return

        random_number = random.randint(1, 200)
        self.result_label.config(text=str(random_number))
        
        self.root.after(50, self.animate_numbers)  # Update every 50 ms

        self.root.after(2000, self.stop_animation)  # Stop after 2 seconds

    def stop_animation(self):
        self.running = False
        final_number = random.randint(1, 200)
        self.result_label.config(text=str(final_number))

    def reset(self):
        self.result_label.config(text="")
        if self.running:
            self.running = False

# Create the main window
root = tk.Tk()
app = RandomNumberGenerator(root)

# Run the application
root.mainloop()
