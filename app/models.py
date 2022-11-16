from django.db import models


class User(models.Model):
    login = models.CharField(max_length=30)
    password_hash = models.CharField(max_length=64)
    nickname = models.CharField(max_length=30)
    avatar_url = models.CharField(max_length=100)


class Post(models.Model):
    pass


class Question(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    asker = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=140)


class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    commentator = models.ForeignKey(User, on_delete=models.PROTECT)
    text = models.CharField(max_length=140)


class LikeCounter(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    value = models.IntegerField()


questions = {
    question_id: {
        "question_id": question_id,
        "name": "Why",
        "description": "Lorem ipsum dolor sit amet, consectetur adipisicing "
                       "elit. Accusantium aliquam architecto\
                autem culpa, cum, dolore doloremque ducimus enim "
                       "exercitationem libero maiores nemo vel\
                veniam. Eaque eveniet harum impedit itaque provident!",
    } for question_id in range(10)
}

users = {
    user_id: {
        "user_id": user_id,
        "nickname": "Mr. Cool NickName",
        "email": "cool@google.com",
        "login": "cool_login",
    } for user_id in range(10)
}
