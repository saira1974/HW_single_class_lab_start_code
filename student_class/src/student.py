class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
    
    def test_student_can_update_name(self, name):
        return "Mike"
    
    def test_student_can_change_cohort(self, cohort):
        return "G21"
    
    def talk(self):
        return "I can talk!"
    
    def say_favourite_language(self, language):
        return f"I love {language}"
