class Database:
    """Simulates a basic user database"""
    def __init__(self):
        self.data = {} # Simutalting an in-memory database
    
    def add_user(self,user_id, name):
        if user_id in self.data:
            raise ValueError("User already exists")
    
    def get_user(self, user_id):
        return self.data.get(user_id, None)
    
    def delete_user(self, user_id):
        if user_id in self.data:
            del self.data[user_id]