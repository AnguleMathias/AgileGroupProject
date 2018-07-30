import datetime
comments = []
class Comment(object):
    """
    The COMMENT model for the APP
    """

    def add_comment(self, author, message):
        """
        CREATE a comment
        """
        if len(comments) == 0:
            id = 1
        else:
            id = comments[-1]["id"]+1
        comment = {
            "id": id,
            "author": author,
            "message": message,
            "date created": datetime.datetime.utcnow()
        }
        comments.append(comment)
        print("Comment has been successfully created!")

    def view_comments(self):
        """
        VIEW all comments
        """
        if len(comments) == 0:
            print("No comments available!")
        print(comments)

    def update_comment(self, comment_id):
        """
        UPDATE a comment
        """
        comment = [comment for comment in comments if comment["id"] == comment_id]
        if not comment:
            print("Comment not found!")
        message = input("Update comment: ")
        if message:
            comment["message"] = message
        comments.append(comment)

    def delete_comment(self, comment_id):
        """
        DELETE a comment
        """
        comment = [comment for comment in comments if comment["id"] == comment_id]
        if not comment:
            print("Comment not found!")
        comments.remove(comment)

   
author = input("Enter name: ")
message = input("Enter comment: ")
c = Comment()
c.add_comment(author, message)
c.view_comments()
c.update_comment(comment_id=1)



