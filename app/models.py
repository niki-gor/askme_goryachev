from django.db import models

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