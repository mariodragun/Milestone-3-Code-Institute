import mongoengine as me
import datetime


class User(me.Document):
    first_name = me.StringField(required=True)
    last_name = me.StringField(required=True)
    #  username is set to be unique to prevent multiple users to have same
    # username
    username = me.StringField(required=True, unique=True)
    # email is set to be unique to prevent multiple users to have same email
    email = me.EmailField(required=True, unique=True)
    # password is set to be a plain text field - because we will use
    # generate_password_hash so
    #  there is no need to hash it again
    password = me.StringField(max_length=256)

    is_active = me.BooleanField(default=True)
    is_admin = me.BooleanField(default=False)


# Question - list of answers (one or many can be true)
class Answer(me.EmbeddedDocument):
    # answer basic text
    answer = me.StringField(required=True)
    # is correct boolean, will signify if the answer is correct or not
    is_correct = me.BooleanField(default=False)

    # standard datetime field which will be updated every time Question is
    # modified
    # and that is why the default value datetime.datetime.now which is the now
    # date/time (server time)
    date_modified = me.DateTimeField(default=datetime.datetime.now)


class Question(me.Document):
    # stanard question text title
    title = me.StringField(required=True, unique=True)
    # help text for the question - additional explanation of the question, not
    # required
    description = me.StringField(default="")
    # url field for the images, also additional explanations of the questions
    image = me.URLField(required=False)
    # embeded document, one question can have many answers (List of answers)
    answers = me.ListField(me.EmbeddedDocumentField(Answer))

    # standard datetime field which will be updated every time Question is
    # modified
    # and that is why the default value datetime.datetime.now which is the now
    # date/time (server time)
    date_modified = me.DateTimeField(default=datetime.datetime.now)


# Embeded model for QuizTaken - holds questions and chosen answers
class QuestionsAnswered(me.EmbeddedDocument):
    question = me.ReferenceField(Question)
    chosen_answer = me.StringField()
    is_correct = me.BooleanField(default=False)


class QuizTaken(me.Document):
    user = me.ReferenceField(User)
    list_of_questions = me.ListField(
        me.EmbeddedDocumentField(QuestionsAnswered)
    )
    number_of_questions = me.IntField()
    correct_answers = me.IntField(default=0)

    is_done = me.BooleanField(default=False)

    date_started = me.DateTimeField()
    date_modified = me.DateTimeField(default=datetime.datetime.now)

    @property
    def overall_score(self):
        return f"{self.correct_answers}/{self.number_of_questions}"
