# #function
def say_hello(to = 'Amin', receiver='Jose'):
    print (f'Helo {to},my friend, I am {receiver}')
if __name__ == '__main__':
    say_hello('Budi',
              'Tono')
    
#class
class Student:
    def __init__(self, name=""):
        self.name = name
    def say_hello(self):
        print(f"Hello my name is {self.name}")
if __name__ == '__main__' :
    student = Student(name='Tono')
    student.say_hello()
    student2 = Student(name='Amin')
    student2.say_hello()
