import os
import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import tarfile

class BetaSuite:
    def __init__(self, root):
        self.root = root
        self.root.title("BetaSuite - File Compressor & Decompressor")
        self.root.geometry("400x200")

        self.file_path = ""

        # GUI Elements
        self.label = tk.Label(root, text="Select a file to compress/decompress:")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select File", command=self.select_file)
        self.select_button.pack(pady=5)

        self.compress_button = tk.Button(root, text="Compress", command=self.compress_file)
        self.compress_button.pack(pady=5)

        self.decompress_button = tk.Button(root, text="Decompress", command=self.decompress_file)
        self.decompress_button.pack(pady=5)

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            messagebox.showinfo("File Selected", f"File: {os.path.basename(self.file_path)}")

    def compress_file(self):
        if not self.file_path:
            messagebox.showwarning("No File Selected", "Please select a file to compress.")
            return

        file_name = os.path.basename(self.file_path)
        compressed_file_path = filedialog.asksaveasfilename(defaultextension=".zip", 
                                                            filetypes=[("ZIP files", "*.zip")])
        if compressed_file_path:
            with zipfile.ZipFile(compressed_file_path, 'w') as zipf:
                zipf.write(self.file_path, arcname=file_name)
            messagebox.showinfo("Success", f"File compressed to {compressed_file_path}")

    def decompress_file(self):
        if not self.file_path:
            messagebox.showwarning("No File Selected", "Please select a file to decompress.")
            return

        file_ext = os.path.splitext(self.file_path)[1]
        if file_ext not in ['.zip', '.tar', '.gz']:
            messagebox.showwarning("Unsupported Format", "The selected file format is not supported for decompression.")
            return

        output_dir = filedialog.askdirectory()
        if output_dir:
            try:
                if file_ext == '.zip':
                    with zipfile.ZipFile(self.file_path, 'r') as zipf:
                        zipf.extractall(output_dir)
                elif file_ext in ['.tar', '.gz']:
                    with tarfile.open(self.file_path, 'r:*') as tarf:
                        tarf.extractall(output_dir)
                messagebox.showinfo("Success", f"File decompressed to {output_dir}")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BetaSuite(root)
    root.mainloop()