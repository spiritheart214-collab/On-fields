from django.db import models

#FAQ
#-------------------------------------------------------------
class FAQ(models.Model):
    questions = models.CharField('Вопрос', max_length=100)
    answer = models.TextField('Ответ', max_length=500)
    
    class Meta:
        ordering = ["questions"]
        verbose_name = "ЧЗВ"
        verbose_name_plural = "ЧЗВ"
    
    def __str__(self):
        return self.questions