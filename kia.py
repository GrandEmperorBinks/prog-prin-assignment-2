# https://github.com/GrandEmperorBinks

# Import the necessary module(s).
import tkinter
import tkinter.messagebox
import json


class ProgramGUI:

    def __init__(self):
        # This is the constructor of the class.
        #Load JSON file
        try:
            self.file = open('data.txt', 'r')
            self.data = json.load(self.file)
            self.file.close()
        except:
            tkinter.messagebox.showerror('Error', 'Missing/Invalid file')
            return
        
        #Create main window
        self.main = tkinter.Tk()
        self.main.title('Know It All Game')

        self.index = 0
        self.total_score = 0
        #Implement GUI
        #Create frame widgets
        self.frame = tkinter.Frame(self.main)
        #Create and pack messages
        self.heading_text = tkinter.Label(text='The Category is...')
        self.category_text = tkinter.Label(text=' ')
        self.heading_text.pack()
        self.category_text.pack()
        #Create and pack answer line
        self.answer_text = tkinter.Label(self.frame, width=7, justify='center', text='Answer:')
        self.answer_entry = tkinter.Entry(self.frame, width=25)
        self.button = tkinter.Button(self.frame, text='Submit', command=self.check_answer)
        self.answer_text.pack(side='left')
        self.answer_entry.pack(side='left', padx=5)
        self.button.pack(side='right')
        #Pack frame
        self.frame.pack()

        self.set_category()
        self.answer_entry.focus_set()
        tkinter.mainloop()


    def set_category(self):
        # This method displays the name of the current category in the GUI.
        # It also creates some useful attributes and ends the program after the final category.
        #Create attribute to keep track of score for this category
        self.category_score = 0
        
        #Try to display current category name in GUI and get correct answers into a list, or end game if there are no categories left
        try:
            self.correct_answer = self.data[self.index]['answers']
            self.correct_answers = []
            for value in self.correct_answer:
                self.correct_answers.append(value.lower())
            
            self.category = self.data[self.index]['category']
            self.category_text.configure(text=self.category)
        except IndexError:
            tkinter.messagebox.showinfo('Game Over', f'Your total score was {self.total_score}')
            self.main.destroy()


    def check_answer(self):
        # This method evaluates the user's answer, records their score, and displays appropriate messageboxes.
        #Get users answer, and get list of correct answers
        self.current_answer = self.answer_entry.get().lower()

        #Check if answer is correct and take action
        if self.current_answer in self.correct_answers:
            self.category_score += self.data[self.index]['difficulty']
            self.correct_answers.remove(self.current_answer)
            tkinter.messagebox.showinfo('Result', 'Correct answer!')
            #If no more answers left, end category with double score
            if self.correct_answers == []:
                self.category_score = self.category_score*2
                tkinter.messagebox.showinfo('Category Over', f'You scored {self.category_score} point(s) in this category.\n Category complete!')
                self.total_score += self.category_score
                self.index += 1
                self.set_category()
        #If incorrect answer, end category immediately
        else:
            tkinter.messagebox.showerror('Result', 'Incorrect answer!')
            tkinter.messagebox.showinfo('Category Over', f'You scored {self.category_score} point(s) in this category.')
            self.total_score += self.category_score
            self.index += 1
            self.set_category()

        self.answer_entry.delete(0,tkinter.END)

#Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()
