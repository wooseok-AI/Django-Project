from django.db import models

# Create your models here.
# 모델 생성
# 모델을 테이블에 써 주기 위한 마이그레이션을 만든다.
# 모델에 맞는 테이블 만든다.
# 간단한 설문에 답을 하는 기능을 구현
## 질문 : 여름에 놀러간다면 어디에 갈래?
## 산
## 강
## 바다
## 도심 호캉스

#질문 모델 생성
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data pulished')

class Choice(models.Model):
    # 위의 QUESTION의 고유값을 받음
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
