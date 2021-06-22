from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.widget import Widget



class Principal(BoxLayout):
    label_number = StringProperty('0')
    label_text = StringProperty()
    numb = 0
    texto = ''
    
    
    def show_slider(self, widget):
        self.numb = int(widget.value)
        self.label_number = str((self.numb))
        
        return

        
    def input_text(self, widget):
        self.texto =(widget.text)
        return


    def do_click(self):
        self.label_text = Principal.code_cesar(self)
        return

    def code_cesar(self):
        buff = []
        for c in self.texto:
            num = ord(c)
            if 65 <= num < 91:
                new_num = ((num - 65 + self.numb) % 26) + 65
                buff.append(str(chr(new_num)))
            elif 97 <= num < 123:
                new_num = ((num - 97 + self.numb) % 26) + 97
                buff.append(str(chr(new_num)))
            else:
                buff.append(c)
        return ''.join(buff)      
   

class CifradoApp(App):
    pass
    

def main():
    app = CifradoApp()
    app.run()
    


if __name__ == '__main__':
    main()