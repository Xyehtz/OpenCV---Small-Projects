import tkinter.filedialog
import cv2
import tkinter as tk
from tkinter import ttk

class ImageFilterApplication:
    def __init__(self, root):
        self.image_path = None
        self.original_image = None

        root.title("Image Filter Application")
        root.geometry("800x600")

        # Toolbar
        toolbar_frame = tk.Frame(root, bd=1, relief="raised")
        toolbar_frame.pack(side="top", fill="x")

        # Toolbar button
        open_button = ttk.Button(toolbar_frame, text="Open", command=self.open_image)
        open_button.pack(side="left")

    def open_image(self):
        # Open file dialog
        path = tk.filedialog.askopenfilenames(parent=root, initialdir="./", filetypes=(
            ("JPG", "*.jpg"),
            ("PNG", "*.png"),
            ("JPEG", "*.jpeg"),
            ("All files", "*")))

        if path:
            # Properly assign variables
            self.image_path = path
            self.original_image = cv2.imread(self.image_path[0], cv2.IMREAD_COLOR_BGR)
            cv2.imshow("Image", self.original_image)
            cv2.waitKey(0)
        else:
            print("No file selected and/or detected")


if __name__ == "__main__":
    # Basic GUI Setup
    root = tk.Tk()
    app = ImageFilterApplication(root)
    root.mainloop()
