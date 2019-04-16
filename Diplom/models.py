from django.db import models
from django.shortcuts import reverse


class Test(models.Model):
   name = models.CharField(max_length=100)
   number = models.IntegerField()

   def __str__(self):
      return 'Test {}. {}'.format(self.number, self.name)


class Group(models.Model):
   name = models.CharField(max_length=100)
   slug = models.SlugField(unique=True)

   def __str__(self):
      return self.name

   def get_absolute_url(self):
      return reverse('students_url', kwargs={'slug': self.slug})


#                 TEST 4
class QuestionRadio(models.Model):
   test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='questions', blank=True)
   text = models.CharField(max_length=200)
   hint = models.CharField(max_length=200, blank=True)

   def __str__(self):
      return self.text



#               TEST 6, TEST 8
class NumberQuestion(models.Model):
   test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='number_questions')
   text = models.CharField(max_length=200)
   correct_answer = models.CharField(max_length=200, blank=True)

   def __str__(self):
      return self.text



class Student(models.Model):
   full_name = models.CharField(max_length=100)
   group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
   passed = models.BooleanField(default=False)

   
   def __str__(self):
      return self.full_name

#              TEST 2, TEST 5
class TextQuestion(models.Model):
   owner = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="TextAnswers")
   test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='text_questions')
   answer = models.TextField()

   def __str__(self):
      return '{}. Студенттің жауабы: - {}'.format(self.test, self.answer)



class AnswerTest6(models.Model):
   owner = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="Test6Answers")
   answer = models.IntegerField(blank=True)

   def __str__(self):
      return str(self.answer)


class AnswerTest8(models.Model):
   owner = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="Test8Answers")
   answer = models.IntegerField(blank=True)

   def __str__(self):
      return str(self.answer)



class VariantRadio(models.Model):
   text = models.CharField(max_length=200)
   question = models.ForeignKey(QuestionRadio, on_delete=models.CASCADE, related_name='variants')
   owner =  models.ManyToManyField(Student, related_name="answer_of_TEST4", blank=True)
   correct_answer = models.CharField(max_length=200, blank=True)

   def __str__(self):
      return '{}. Студенттің жауабы - {}'.format(self.question, self.text)



#              TEST 1
class First_test_variants(models.Model):
   text = models.CharField(max_length=200)
   question = models.ForeignKey(QuestionRadio, on_delete=models.CASCADE, related_name='first_test_variant')
   owner =  models.ManyToManyField(Student, related_name="answer_of_TEST1", blank=True)
   correct_answer = models.CharField(max_length=200, blank=True)

   def __str__(self):
      return '{} {}'.format(self.question, self.text)



class Third_test_variants(models.Model):
   test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='third_test_variant')
   text = models.CharField(max_length=200)
   owner = models.ManyToManyField(Student, related_name="third_test_variant", blank=True)
   correct_answer = models.CharField(max_length=200, blank=True)


   def __str__(self):
      return self.text


class Seventh_test_variants(models.Model):
   test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='seventh_test_variant')
   text = models.CharField(max_length=200)
   owner = models.ManyToManyField(Student, related_name="seventh_test_variant", blank=True)
   correct_answer = models.CharField(max_length=200, blank=True)

   def __str__(self):
      return self.text