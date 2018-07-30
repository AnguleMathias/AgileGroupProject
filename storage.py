class Comment():
    """
    This class stores comments and also have methods that will manipulate
    those comments.
    """
    Comments = []

    @classmethod
    def get_by_id(cls,comment_id):
        cls.comment = next(filter(lambda x: x['id'] == comment_id, cls.Comments), None)
        return cls.comment

    def save(self,comment):
        self.Comments.append(comment)

    def delete_comment(self,entry):
        self.Comments.remove(entry)

    def update_comment(self,new_comment,id_):
        self.comment = next(filter(lambda x: x['id'] == id_, self.Comments), None)
        self.comment.update(new_comment)

    def __str__(self):
        """returns an object as a string"""
        return(str(self.Comments))

    def __len__(self):
        """returns the length of an object"""
        return len(self.Comments)

    def __getitem__(self,i):
        """this method allows us to undex an object"""
        return self.Comments[i]

    def all_items(self):
        """fetches all comments"""
        return self.Comments