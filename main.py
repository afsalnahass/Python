from bank_operations.bank import credit,debit,transfer

print("hello world")
print("new program")


class fruits:
    def _init_(self,name,color) -> None:
        self.name = name
        self.color = color

    def say_color(self):
        print("my color is", self.color)

    class apple(fruits):
        def my_type(self):
            print("i am an apple..")

a = apple("apple1", "red")

print(a.color)
                     
                    