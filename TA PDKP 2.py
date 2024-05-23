import tkinter as tk
from tkinter import ttk, messagebox

class Product:
    def __init__(self, id, name, price, stock, category):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def __str__(self):
        return f'ID: {self.id}, Nama: {self.name}, Harga: {self.price}, Stok: {self.stock}, Kategori: {self.category}'

class Store:
    def __init__(self):
        self.products = []
        self.add_history = []

    def add_product(self, id, name, price, stock, category):
        # Cek apakah ID sudah ada
        for product in self.products:
            if product.id == id:
                messagebox.showerror("Error", f'Produk dengan ID {id} sudah ada.')
                return
        
        new_product = Product(id, name, price, stock, category)
        self.products.append(new_product)
        self.add_history.append(new_product)
        messagebox.showinfo("Sukses", f'Produk {name} berhasil ditambahkan.')

    def view_products(self):
        if not self.products:
            messagebox.showinfo("Daftar Produk", 'Tidak ada produk dalam toko.')
        else:
            product_list = "\n".join(str(product) for product in self.products)
            messagebox.showinfo("Daftar Produk", product_list)

    def view_products_by_category(self, category):
        filtered_products = [product for product in self.products if product.category == category]
        if not filtered_products:
            messagebox.showinfo("Daftar Produk", 'Tidak ada produk dalam kategori ini.')
        else:
            product_list = "\n".join(str(product) for product in filtered_products)
            messagebox.showinfo("Daftar Produk", product_list)

    def view_add_history(self):
        if not self.add_history:
            messagebox.showinfo("Riwayat Penambahan Produk", 'Tidak ada produk yang ditambahkan.')
        else:
            history_list = "\n".join(str(product) for product in reversed(self.add_history))
            messagebox.showinfo("Riwayat Penambahan Produk", history_list)

    def update_stock(self, id, new_stock):
        for product in self.products:
            if product.id == id:
                product.stock = new_stock
                messagebox.showinfo("Sukses", f'Stok produk dengan ID {id} berhasil diperbarui.')
                return
        messagebox.showerror("Error", 'Produk tidak ditemukan.')

class App:
    def __init__(self, root):
        self.store = Store()

        self.root = root
        self.root.title("Manajemen Toko Baju Online")
        self.root.configure(bg="#eb9534")

        self.style = ttk.Style()
        self.style.configure('TButton', background='#8f420b', foreground='red')

        self.frame = tk.Frame(root, bg="#eb9543")
        self.frame.pack(pady=20)

        self.title = tk.Label(self.frame, text="Manajemen Toko Baju Online", font=('georgia', 16, "bold"), bg="#8f420b", fg="#fcfcfc")
        self.title.grid(row=0, column=0, columnspan=2, pady=10)

        self.add_button = ttk.Button(self.frame, text="Tambah Produk", command=self.add_product)
        self.add_button.grid(row=1, column=0, pady=5)

        self.view_button = ttk.Button(self.frame, text="Lihat Daftar Produk", command=self.view_products)
        self.view_button.grid(row=1, column=1, pady=5)

        self.view_by_category_button = ttk.Button(self.frame, text="Lihat Produk per Kategori", command=self.view_products_by_category)
        self.view_by_category_button.grid(row=2, column=0, pady=5)

        self.view_add_history_button = ttk.Button(self.frame, text="Lihat Riwayat Penambahan", command=self.view_add_history)
        self.view_add_history_button.grid(row=2, column=1, pady=5)

        self.update_stock_button = ttk.Button(self.frame, text="Update Stok", command=self.update_stock)
        self.update_stock_button.grid(row=3, column=0, pady=5)

        self.exit_button = ttk.Button(self.frame, text="Keluar", command=root.quit)
        self.exit_button.grid(row=3, column=1, columnspan=2, pady=5)

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(1, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)
        self.frame.grid_rowconfigure(3, weight=1)
        self.frame.grid_rowconfigure(4, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

    def add_product(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Tambah Produk")

        tk.Label(self.new_window, text="ID Produk:").grid(row=0, column=0, pady=5)
        tk.Label(self.new_window, text="Nama Produk:").grid(row=1, column=0, pady=5)
        tk.Label(self.new_window, text="Harga Produk:").grid(row=2, column=0, pady=5)
        tk.Label(self.new_window, text="Stok Produk:").grid(row=3, column=0, pady=5)
        tk.Label(self.new_window, text="Kategori Produk:").grid(row=4, column=0, pady=5)

        self.id_entry_add = tk.Entry(self.new_window)
        self.id_entry_add.grid(row=0, column=1, pady=5)
        self.name_entry_add = tk.Entry(self.new_window)
        self.name_entry_add.grid(row=1, column=1, pady=5)
        self.price_entry_add = tk.Entry(self.new_window)
        self.price_entry_add.grid(row=2, column=1, pady=5)
        self.stock_entry_add = tk.Entry(self.new_window)
        self.stock_entry_add.grid(row=3, column=1, pady=5)
        self.category_entry_add = tk.Entry(self.new_window)
        self.category_entry_add.grid(row=4, column=1, pady=5)

        tk.Button(self.new_window, text="Tambah", command=self.save_product).grid(row=5, column=0, columnspan=2, pady=10)

    def save_product(self):
        id = self.id_entry_add.get()
        name = self.name_entry_add.get()
        price = float(self.price_entry_add.get())
        stock = int(self.stock_entry_add.get())
        category = self.category_entry_add.get()
        self.store.add_product(id, name, price, stock, category)
        self.new_window.destroy()

    def view_products(self):
        self.store.view_products()

    def view_products_by_category(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Lihat Produk per Kategori")

        tk.Label(self.new_window, text="Kategori:").grid(row=0, column=0, pady=5)
        self.category_entry_view = tk.Entry(self.new_window)
        self.category_entry_view.grid(row=0, column=1, pady=5)

        tk.Button(self.new_window, text="Lihat", command=self.view_products_by_category_action).grid(row=1, column=0, columnspan=2, pady=10)

    def view_products_by_category_action(self):
        category = self.category_entry_view.get()
        self.store.view_products_by_category(category)
        self.new_window.destroy()

    def view_add_history(self):
        self.store.view_add_history()

    def update_stock(self):
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Update Stok")

        tk.Label(self.new_window, text="ID Produk:").grid(row=0, column=0, pady=5)
        tk.Label(self.new_window, text="Stok Baru:").grid(row=1, column=0, pady=5)

        self.id_entry_update = tk.Entry(self.new_window)
        self.id_entry_update.grid(row=0, column=1, pady=5)
        self.stock_entry_update = tk.Entry(self.new_window)
        self.stock_entry_update.grid(row=1, column=1, pady=5)

        tk.Button(self.new_window, text="Update", command=self.update_stock_action).grid(row=2, column=0, columnspan=2, pady=10)

    def update_stock_action(self):
        id = self.id_entry_update.get()
        new_stock = int(self.stock_entry_update.get())
        self.store.update_stock(id, new_stock)
        self.new_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
