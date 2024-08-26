class Story:
    def __init__(self, title, author, category, download):
        self.title = title
        self.author = author
        self.category = category
        self.download = download


    def createStory(self, title, category, body):
        self.title = title
        self.category = category
        self.body = body
    
    # def downloadStory():
        # Downloads Story from the table that is displayed.

    # def deleteStory():
    