class Task:
    def __init__(self, task, answer, level, topic, defined = True):
        self.task = task
        self.answer = answer
        self.level = level
        self.topic = topic
        self.defined = defined

    def __str__(self):
        return f'{self.task} = {self.answer}'

    def __repr__(self):
        return f'{self.task} = {self.answer}'