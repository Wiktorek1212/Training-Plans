import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


class Exercise:
    def __init__(self, name, sets, reps, tempo, notes):
        self.name = name
        self.sets = sets
        self.reps = reps
        self.tempo = tempo
        self.notes = notes


class TrainingPlan:
    def __init__(self, name):
        self.name = name
        self.exercises = []


class TrainingApp:
    def __init__(self, master):
        self.master = master
        master.title("Grub Program")
        self.master.geometry("800x600")

        image = Image.open("hehe.png")
        photo = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(self.master, image=photo)
        self.background_label.image = photo
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.filename_label = Label(master, text="Nazwa pliku:")
        self.filename_label.grid(row=0, column=0)

        self.filename_entry = tk.Entry(master)
        self.filename_entry.grid(row=0, column=1)

        self.filename_label = tk.Label(
            master, text="Nazwa pliku:", bg="red", fg="white"
        )
        self.filename_label.grid(row=0, column=0)

        self.filename_entry = tk.Entry(
            master, highlightthickness=3, highlightbackground="red"
        )
        self.filename_entry.grid(row=0, column=1)

        self.training_label = tk.Label(
            master, text="Typ treningu:", bg="grey", fg="white"
        )
        self.training_label.grid(row=1, column=0)

        self.training_entry = tk.Entry(
            master, highlightthickness=3, highlightbackground="grey"
        )
        self.training_entry.grid(row=1, column=1)

        self.exercise_label = tk.Label(
            master, text="Nazwa ćwiczenia:", bg="black", fg="white"
        )
        self.exercise_label.grid(row=3, column=0)

        self.exercise_entry = tk.Entry(
            master, highlightthickness=3, highlightbackground="black"
        )
        self.exercise_entry.grid(row=3, column=1)

        self.sets_label = tk.Label(master, text="Ilość serii:", bg="black", fg="white")
        self.sets_label.grid(row=4, column=0)

        self.sets_entry = tk.Entry(
            master, highlightthickness=3, highlightbackground="black"
        )
        self.sets_entry.grid(row=4, column=1)

        self.reps_label = tk.Label(
            master, text="Ilość powtórzeń:", bg="black", fg="white"
        )
        self.reps_label.grid(row=5, column=0)

        self.reps_entry = tk.Entry(
            master, highlightthickness=3, highlightbackground="black"
        )
        self.reps_entry.grid(row=5, column=1)

        self.tempo_label = tk.Label(master, text="Tempo:", bg="black", fg="white")
        self.tempo_label.grid(row=6, column=0)

        self.tempo_entry = tk.Entry(
            master, highlightthickness=3, highlightbackground="black"
        )
        self.tempo_entry.grid(row=6, column=1)

        self.notes_label = tk.Label(master, text="Notatki:", bg="black", fg="white")
        self.notes_label.grid(row=7, column=0)

        self.notes_entry = tk.Entry(
            master, highlightthickness=3, highlightbackground="black"
        )
        self.notes_entry.grid(row=7, column=1)

        self.add_exercise_button = tk.Button(
            master,
            text="Dodaj ćwiczenie",
            command=self.add_exercise,
            bg="black",
            fg="white",
        )
        self.add_exercise_button.grid(row=8, column=1)

        self.exercises_label = tk.Label(
            master, text="Ćwiczenia:", bg="black", fg="white"
        )
        self.exercises_label.grid(row=9, column=0)

        self.add_exercise_button = tk.Button(
            master,
            text="Usuń ćwiczenie",
            command=self.add_exercise,
            bg="red",
            fg="white",
        )
        self.add_exercise_button.grid(row=10, column=2)

        self.exercises_listbox = tk.Listbox(
            master,
            highlightthickness=3,
            highlightbackground="black",
            highlightcolor="black",
        )
        self.exercises_listbox.grid(row=10, column=0, columnspan=2)

        self.add_training_button = tk.Button(
            master,
            text="**DODAJ TYP TRENINGU**",
            command=self.add_training,
            bg="grey",
            fg="white",
        )
        self.add_training_button.grid(row=1, column=2)

        self.training_types_listbox = tk.Listbox(
            master, highlightthickness=3, highlightbackground="grey"
        )
        self.training_types_listbox.grid(row=2, column=0, columnspan=2)

        self.save_button = tk.Button(
            master, text="Zapisz", command=self.save, bg="red", fg="white"
        )
        self.save_button.grid(row=13, column=3)

        self.training_plans = []

    def add_exercise(self):
        name = self.exercise_entry.get()
        sets = self.sets_entry.get()
        reps = self.reps_entry.get()
        tempo = self.tempo_entry.get()
        notes = self.notes_entry.get()
        exercise = Exercise(name, sets, reps, tempo, notes)
        self.training_plans[-1].exercises.append(exercise)

        self.exercises_listbox.insert(
            tk.END, f"{len(self.training_plans[-1].exercises)}. {name}"
        )

        self.exercise_entry.delete(0, END)
        self.sets_entry.delete(0, END)
        self.reps_entry.delete(0, END)
        self.tempo_entry.delete(0, END)
        self.notes_entry.delete(0, END)

    def add_training(self):
        training_type = self.training_entry.get()
        self.training_plans.append(TrainingPlan(training_type))

        self.training_types_listbox.insert(tk.END, training_type)

    def save(self):
        filename = self.filename_entry.get()
        with open(filename + ".odt", "w") as f:
            for training_plan in self.training_plans:
                f.write(f"\n{training_plan.name}\n")
                for i, exercise in enumerate(training_plan.exercises):
                    f.write(f"{i+1}. {exercise.name}\n")
                    f.write(f"    Serii: {exercise.sets}")
                    f.write(f"    Powtórzeń: {exercise.reps}")
                    f.write(f"    Tempo(s): {exercise.tempo}")
                    f.write(f"    Notatki: {exercise.notes}\n\n")

        messagebox.showinfo("elegancko ", f"Plik {filename} został zapisany ;)")

        self.master.destroy()


root = tk.Tk()
app = TrainingApp(root)
root.mainloop()
