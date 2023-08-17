class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        # self.completedAt = update_time()

    
    def mark_complete(self):
        self.completed = True
    
    def __str__(self) -> str:
        status = "✓" if self.completed else "✗"
        return f"{status} {self.title} - {self.description}"