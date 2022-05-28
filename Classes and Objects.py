class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
    def change_name(self, new_name):
        self.name = new_name
        print("The student's new name is", new_name)
    def change_age(self, new_age):
        self.age = int(new_age)
        print("The student's new age is", new_age)
    def add_track(self, tracks):
        self.tracks.append(tracks)
        return self.tracks
    def get_score(self):
        return self.score
        pass

Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
print(Bob.add_track("UI/UX"))
print(Bob.get_score())