from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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
                   width=15).place(x=215, y=300)

        ttk.Button(self.main_frame, text="Регистрация", command=lambda: self.show_frame(self.signup_frame),
                   width=15).place(x=650, y=300)

        # Login Frame
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

        ttk.Button(self.health_frame, text="Обновить", command=self.update_data,
                   width=15).place(x=400, y=300)

        self.show_frame(self.main_frame)

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

    def update_data(self):
        num1 = self.health_entry.get()
        num2 = self.health_entry1.get()
        print(f"Сердечное❤️: {num1} \nУровень кровяного давления🩸: {num2}")

if __name__ == "__main__":
    root = Tk()
    app = HealthMonitorApp(root)
    root.mainloop()
