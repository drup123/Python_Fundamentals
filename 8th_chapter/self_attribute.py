class reject:
    age = 150
    name = "captain america"
    def calling(self):       #hence giving parameter is neccesary
        print(self.age)
        print(self.name)
    @staticmethod             #with the help of this no need to pass self parameter
    def marvel():             
        print("Hello India")

accept = reject()
accept.calling()              #it is calling as reject.calling(accept)
accept.marvel()