from tkinter import*
from deep_translator import GoogleTranslator
from tkinter import messagebox

root = Tk()
root.title("language_Translator")
root.geometry = ('1020 x 300')
root['bg'] = ("#B4A9D9")

main_frame = Frame(root,bg="#B4A9D9")
main_frame.grid(row=0,column=0)


left_frame = Frame(main_frame,width=400,height=400)
left_frame.grid(row=0,column=1,padx=50,pady=50)
Label(left_frame,text="enter input",bg="#B4A9D9",fg="black").grid(row=0,column=1,pady=10)

input_text = Text(left_frame,width=40,height=30,bg="#0C0A15",fg="white")
input_text.grid(row=1,column=1)


middle_frame = Frame(main_frame,width=200,height=200)
middle_frame.grid(row=0,column=3,padx=200,pady=20)
Label(middle_frame,text='select language').grid(row=0,column=2,pady=4)

lang_dict = GoogleTranslator().get_supported_languages(as_dict=True)
languages = list(lang_dict.keys())

selected_lang = StringVar(value='en')
OptionMenu(middle_frame,selected_lang,*languages).grid(row=1,column=2,pady=4)


def translate():
    text = input_text.get("1.0", END).strip()
    if text:
        translated = GoogleTranslator(source='auto',target=selected_lang.get()).translate(text)
        output_text.delete('1.0',END)
        output_text.insert(END,translated)

Button(middle_frame,text='TRANSLATE',command=translate).grid(row=3,column=2,pady=2)

right_frame = Frame(main_frame,width=200,height=200)
right_frame.grid(row=0,column=4,padx=40,pady=40)
Label(right_frame,text="Translated text",bg="#B4A9D9",fg="black").grid(row=0,column=1,pady=10)

output_text = Text(right_frame,width=40,height=30,bg="#0C0A15",fg="white")
output_text.grid(row=1,column=1)


root.mainloop()