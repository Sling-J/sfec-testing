from django.db import models
from django.shortcuts import reverse

class Test(models.Model):
   name = models.CharField(max_length=100)


   def __str__(self):
      return self.name




class TextQuestion(models.Model):
   test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='text_questions')
   answer = models.TextField()

   def __str__(self):
      return 'Answer for {}. Answer - {}'.format(self.test, self.answer)



class Group(models.Model):
   name = models.CharField(max_length=100)
   slug = models.SlugField(unique=True)

   def __str__(self):
      return self.name

   def get_absolute_url(self):
      return reverse('students_url', kwargs={'slug': self.slug})


class Student(models.Model):
   full_name = models.CharField(max_length=100)
   group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
   answer = models.ManyToManyField(Test, related_name="answers")

   def __str__(self):
      return self.full_name