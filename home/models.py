# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Survey(models.Model):

    #__Survey_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    #__Survey_FIELDS__END

    class Meta:
        verbose_name        = _("Survey")
        verbose_name_plural = _("Survey")


class User(models.Model):

    #__User_FIELDS__
    id = models.IntegerField(null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Question(models.Model):

    #__Question_FIELDS__
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255, null=True, blank=True)
    question_type = models.CharField(max_length=255, null=True, blank=True)

    #__Question_FIELDS__END

    class Meta:
        verbose_name        = _("Question")
        verbose_name_plural = _("Question")


class Answer(models.Model):

    #__Answer_FIELDS__
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text_answer = models.TextField(max_length=255, null=True, blank=True)
    number_answer = models.IntegerField(null=True, blank=True)
    bool_answer = models.BooleanField()

    #__Answer_FIELDS__END

    class Meta:
        verbose_name        = _("Answer")
        verbose_name_plural = _("Answer")



#__MODELS__END
