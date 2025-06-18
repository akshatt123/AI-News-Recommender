#Defining Input Schemma
class User:
    def __init__(self, user_id, interests=None):
        self.user_id = user_id
        self.interests = interests or []
