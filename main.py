from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk


class HealthMonitorApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1024x600")
        self.master.iconbitmap("icon/monitor.ico")
        self.master.title("Монитор Здоровья❤️")
        self.master.config(bg="#34ebdb")
        self.create_widgets()

    def create_widgets(self):
        # Main Frame
        self.main_frame = Frame(self.master, width=1366, height=768)
        self.main_frame.place(x=0, y=0)

        self.main_image = PhotoImage(file="images/med1.png")
        self.main_image_label = Label(self.main_frame, image=self.main_image)
        self.main_image_label.place(x=0, y=0, relwidth=1, relheight=1)

        Label(self.main_frame, text="Войдите для Проверки", bg="white", fg="blue",
              font=("Comic Sans MS", 35, "italic bold")).place(x=200, y=50)

        ttk.Button(self.main_frame, text="Войти", command=lambda: self.show_frame(self.login_frame),
                   width=15).place(x=201, y=300)

        ttk.Button(self.main_frame, text="Регистрация", command=lambda: self.show_frame(self.signup_frame),
                   width=15).place(x=657, y=300)

        ttk.Button(self.main_frame, text="Админ панель", command=lambda: self.show_frame(self.admin_frame),
                   width=15).place(x=430, y=300)

        self.login_frame = Frame(self.master, width=1366, height=768)
        self.login_frame.place(x=0, y=0)

        self.login_image = PhotoImage(file="images/med2.png")
        self.login_image_label = Label(self.login_frame, image=self.login_image)
        self.login_image_label.place(x=0, y=0, relwidth=1, relheight=1)

        Label(self.login_frame, text="Логин:", bg="white", fg="blue",
              font=("Comic Sans MS", 20)).place(x=213, y=100)
        self.login_entry = Entry(self.login_frame, font=("Comic Sans MS", 20))
        self.login_entry.place(x=400, y=100)

        Label(self.login_frame, text="Пароль:", bg="white", fg="blue",
              font=("Comic Sans MS", 20)).place(x=213, y=200)
        self.password_entry = Entry(self.login_frame, show="*", font=("Comic Sans MS", 20))
        self.password_entry.place(x=400, y=200)

        self.show_password = False

        self.toggle_button = ttk.Button(self.login_frame, text="Показать пароль", command=self.toggle_password)
        self.toggle_button.place(x=400, y=250)

        ttk.Button(self.login_frame, text="Войти", command=self.login,
                   width=15).place(x=400, y=300)

        self.signup_frame = Frame(self.master, width=1366, height=768)
        self.signup_frame.place(x=0, y=0)

        self.signup_image = PhotoImage(file="images/med3.png")
        self.signup_image_label = Label(self.signup_frame, image=self.signup_image)
        self.signup_image_label.place(x=0, y=0, relwidth=1, relheight=1)

        Label(self.signup_frame, text="Логин:", bg="white", fg="blue",
              font=("Comic Sans MS", 20)).place(x=213, y=100)
        self.signup_login_entry = Entry(self.signup_frame, font=("Comic Sans MS", 20))
        self.signup_login_entry.place(x=400, y=100)

        Label(self.signup_frame, text="Пароль:", bg="white", fg="blue",
              font=("Comic Sans MS", 20)).place(x=213, y=200)
        self.signup_password_entry = Entry(self.signup_frame, show="*", font=("Comic Sans MS", 20))
        self.signup_password_entry.place(x=400, y=200)

        self.show_password = False

        self.toggle_button = ttk.Button(self.signup_frame, text="Показать пароль", command=self.toggle_password)
        self.toggle_button.place(x=400, y=250)

        ttk.Button(self.signup_frame, text="Регистрация", command=self.save,
                   width=15).place(x=400, y=300)

        self.health_frame = Frame(self.master, width=1366, height=768)
        self.health_frame.place(x=0, y=0)

        self.health_image = PhotoImage(file="images/med4.png")
        self.health_image_label = Label(self.health_frame, image=self.health_image)
        self.health_image_label.place(x=0, y=0, relwidth=1, relheight=1)

        Label(self.health_frame, text="Сердечное:", bg="white", fg="blue",
              font=("Comic Sans MS", 20)).place(x=213, y=100)
        self.health_entry = Entry(self.health_frame, font=("Comic Sans MS", 20))
        self.health_entry.place(x=400, y=100)

        Label(self.health_frame, text="АД:", bg="white", fg="blue",
              font=("Comic Sans MS", 20)).place(x=213, y=200)
        self.health_entry1 = Entry(self.health_frame, font=("Comic Sans MS", 20))
        self.health_entry1.place(x=400, y=200)

        ttk.Button(self.health_frame, text="Обновить", command=self.save_health_data,
                   width=15).place(x=400, y=300)

        ttk.Button(self.health_frame, text="На главную", command=lambda: self.show_frame(self.main_frame),
                   width=15).place(x=623, y=300)

        ttk.Button(self.health_frame, text="Удалить данные", command=self.clear_file,
                   width=15).place(x=213, y=300)

        self.admin_frame = Frame(self.master, width=1366, height=768)
        self.admin_frame.place(x=0, y=0)

        self.admin_image = PhotoImage(file="images/admin.png")
        self.admin_image_label = Label(self.admin_frame, image=self.admin_image)
        self.admin_image_label.place(x=0, y=0, relwidth=1, relheight=1)

        Label(self.admin_frame, text="Админ Панель", bg="white", fg="blue",
              font=("Comic Sans MS", 30, "bold")).place(x=400, y=0)

        Label(self.admin_frame, text="Логин:", bg="white", fg="blue",
              font=("Comic Sans MS", 20)).place(x=250, y=100)
        self.admin_login_entry = Entry(self.admin_frame, font=("Comic Sans MS", 20))
        self.admin_login_entry.place(x=400, y=100)

        Label(self.admin_frame, text="Пароль:", bg="white", fg="blue",
              font=("Comic Sans MS", 20)).place(x=250, y=200)
        self.admin_password_entry = Entry(self.admin_frame, show="*", font=("Comic Sans MS", 20))
        self.admin_password_entry.place(x=400, y=200)

        self.show_password = False

        self.toggle_button = ttk.Button(self.admin_frame, text="Показать пароль", command=self.toggle_password)
        self.toggle_button.place(x=400, y=250)

        ttk.Button(self.admin_frame, text="Добавить", command=self.add_user,
                   width=15).place(x=400, y=300)

        ttk.Button(self.admin_frame, text="Удалить", command=self.remove_user,
                   width=15).place(x=400, y=350)

        ttk.Button(self.admin_frame, text="Поиск", command=self.search_user,
                   width=15).place(x=400, y=400)

        ttk.Button(self.health_frame, text="Назад", command=lambda: self.show_frame(self.login_frame),
               width=15).place(x=10, y=500)

        ttk.Button(self.signup_frame, text="Назад", command=lambda: self.show_frame(self.main_frame),
                   width=15).place(x=10, y=500)

        ttk.Button(self.login_frame, text="Назад", command=lambda: self.show_frame(self.main_frame),
                   width=15).place(x=10, y=500)

        ttk.Button(self.admin_frame, text="На главную", command=lambda: self.show_frame(self.main_frame),
                   width=15).place(x=400, y=450)

    def show_frame(self, frame):
        frame.tkraise()

    def login(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        try:
            with open("account.txt", "r") as file:
                accounts = file.readlines()
        except FileNotFoundError:
            accounts = []

        user_found = any(f"{login}:{password}\n" == user for user in accounts)

        if user_found:
            self.show_frame(self.health_frame)
        else:
            messagebox.showerror("Ошибка👎", "Введенные данные неверны❌")

    def save(self):
        login = self.signup_login_entry.get()
        password = self.signup_password_entry.get()
        with open("account.txt", "a") as file:
            file.write(f"{login}:{password}\n")
        messagebox.showinfo("Выполнено😎", "Регистрация пройдена✅😎")
        self.show_frame(self.login_frame)

    def save_health_data(self):
        heart_rate = self.health_entry.get()
        blood_pressure = self.health_entry1.get()
        with open("account.txt", "a", encoding="utf-8") as file:
            file.write(f"Сердечное❤️: {heart_rate} \nУровень кровяного давления🩸: {blood_pressure}\n")
        messagebox.showinfo("Успех😎", "Данные сохранены✅")

    def toggle_password(self):
        if self.show_password:
            self.admin_password_entry.config(show="*")
            self.password_entry.config(show="*")
            self.signup_password_entry.config(show="*")
            self.toggle_button.config(text="Показать пароль")
        else:
            self.admin_password_entry.config(show="")
            self.password_entry.config(show="")
            self.signup_password_entry.config(show="")
            self.toggle_button.config(text="Скрыть пароль")
        self.show_password = not self.show_password

    accounts = []
    def add_user(self):
        login = self.admin_login_entry.get()
        password = self.admin_password_entry.get()
        with open("account.txt", "a") as file:
            file.write(f"{login}:{password}\n")
        self.accounts.append([login, password])
        messagebox.showinfo("Успех😎", f"Пользователь {login} добавлен♻️")
        self.admin_login_entry.delete(0, tk.END)
        self.admin_password_entry.delete(0, tk.END)

    def remove_user(self):
        login = self.admin_login_entry.get()
        if any(user[0] == login for user in self.accounts):
            self.users = [user for user in self.accounts if user[0] != login]
            with open("account.txt", "w") as file:
                for user in self.users:
                    file.write(f"{user[0]}:{user[1]}\n")
            messagebox.showinfo("Успех😎", f"Пользователь {login} удален♻️")
        else:
            messagebox.showerror("Ошибка", "Пользователь не найден!❌")
        self.admin_login_entry.delete(0, tk.END)

    def clear_file(self):
        with open("account.txt", "w", encoding="utf-8") as file:
            pass
        messagebox.showinfo("Успех😎", "Файл очищен✅")

    def search_user(self):
        username = self.admin_login_entry.get()
        if any(user[0] == username for user in self.accounts):
            messagebox.showinfo("Результат🔍", f"Пользователь {username} найден✅")
        else:
            messagebox.showerror("Ошибка", f"Пользователь {username} не найден!❌")
        self.admin_login_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = HealthMonitorApp(root)
    root.mainloop()