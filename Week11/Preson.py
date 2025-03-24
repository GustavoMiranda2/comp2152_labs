class Persson:
    def __init__(self, p_name, p_age, p_height):
        self.name = p_name
        self.age = p_age
        self.height = p_height
        self.public_prop = "I'm public"


        #getter for name
        @property
        def name(self):
            return self.__name
        

        #setter for name
        @name.setter
        def name(self, new_name):
            self.__name = new_name

        def __del__(self):
            print("The grabage collector is automatically destroying the person object")

person1 = Persson("mark", 20, 6)

#verson 1
print("The name of the person is: " + str(person1.name))

person1.name = "Alfred"
print("The name of the person is: " + str(person1.name))

print("public "+ str(person1.public_prop))

git checkout master
git pull origin master
git merge lab_week11
git push origin master


git push delete origin lab_week11
git branch 