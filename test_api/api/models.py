from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Inquiry(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    start_date = models.DateField(auto_now_add=True, verbose_name='Дата начало')
    end_date = models.DateField(verbose_name='Дата окончания')
    description = models.TextField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.name


QUESTION_TYPES = (
    ('text_field', 'Ответ текстом'),
    ('radio', 'Один вариант'),
    ('check_boxes', 'Выбор нескольких вариантов'),
)


class Question(models.Model):
    text = models.TextField()
    type_question = models.CharField(
        max_length=20,
        choices=QUESTION_TYPES,
        verbose_name='Тип вопроса',
    )
    inquiry = models.ForeignKey(
        Inquiry, blank=True, on_delete=models.CASCADE,
        related_name="questions"
    )

    def __str__(self):
        return self.text


class Choice(models.Model):
    name = models.TextField(verbose_name='Вариант ответа')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")

    def __str__(self):
        return self.name


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    many_choice = models.ManyToManyField(Choice, null=True)
    one_choice = models.ForeignKey(Choice, null=True, on_delete=models.CASCADE, related_name="answers_one_choice")
    self_text = models.TextField(null=True)
