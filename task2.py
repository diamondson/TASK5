class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.nickname = "noname"
        self.age = 0

    def describe_user(self):
        dic = {}
        dic["first_name"] = self.first_name
        dic["last_name"] = self.last_name
        print(dic)

    def greet_user(self):
        print(f"Good day, {self.first_name} {self.last_name}!")


admin = User("Manas", "Almazbekov")

admin.describe_user()
admin.greet_user()

print(admin.nickname)
admin.nickname = "diamondson95"
print(admin.nickname)