from datetime import datetime
from app.user.comment import Comment
from app import store


class User:
    """user models"""
    users = []

    @classmethod
    def indexView(cls):
        user_input = input(
            '''
            Select an option
                1. Post comment
                2. Edit comment
                3. View comments 
                4. Log-out
                ''')

        input_action = {
            '1': {'type': 'post_comment'},
            '2': {'type': 'edit_comment'},
            '3': {'type': 'view_comments'},
            '4': {'type': 'logout'}
        }.get(user_input)

        return input_action

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.id = self.users[-1]['id'] + 1
        self.isAuthenticated = False
        self.lastLoggedInAt = None

    def post_comment(self, msg):
        timestamp = datetime.now()
        comment = Comment(msg, timestamp, self.id, self.username)
        return comment

    def view_comments(self):
        comments = store.comments

        for comment in sorted(comments.values(), key=lambda comment: comment.id):
            print(comment)

    def edit_comment(self, comm_id, new_msg):
        comments = store.comments
        target = comments.get(comm_id)

        if not target:
            print('\nUNSUCCESSFUL Comment id NOT found')
            return None

        if target.author_id == self.id or self.__class__.__name__ == 'Admin':
            target.msg = new_msg
            print('\nComment edited successfully\n')
            return target.msg

        print('Comment NOT edited. You can only edit your own comments')
        return None


class Moderator(User):
    moderators = []

    @classmethod
    def indexView(cls):
        user_input = input(
            '''
            select an option
                1. Post a comment
                2. Edit a comment
                3. View comments
                4. Delete a comment
                5. Logout
                ''')

        input_action = {
            '1': {'type': 'post_comment'},
            '2': {'type': 'edit_comment'},
            '3': {'type': 'view_comments'},
            '4': {'type': 'delete_comment'},
            '5': {'type': 'logout'}
        }.get(user_input)

        return input_action

    def delete_comment(self, comm_id):
        comments = store.comments
        try:
            comments.pop(comm_id)
            print('\nDELETED successfully')
        except KeyError:
            print('\nUNSUCCESSFUL: comment not found')


class Admin(Moderator, User):
    admin = []

    @classmethod
    def indexView(cls):
        user_input = input(
            '''
            select an option
                1. Post a comment
                2. Edit a comment
                3. View comments
                4. Delete a comment
                5. Logout
                ''')

        input_action = {
            '1': {'type': 'post_comment'},
            '2': {'type': 'edit_comment'},
            '3': {'type': 'view_comments'},
            '4': {'type': 'delete_comment'},
            '5': {'type': 'logout'}
        }.get(user_input)

        return input_action

    def delete_comment(self, comm_id):
        comments = store.comments
        try:
            comments.pop(comm_id)
            print('\nDELETED successfully')
        except KeyError:
            print('\nUNSUCCESSFUL: comment not found')
