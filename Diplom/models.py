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
   hint = models.CharField(max_length=200)

   def __str__(self):
      return self.text


class VariantRadio(models.Model):
   text = models.CharField(max_length=200)
   question = models.ForeignKey(QuestionRadio, on_delete=models.CASCADE, related_name='variants')


   def __str__(self):
      return 'Variant of {}. Variant - {}'.format(self.question, self.text)




#               TEST 6, TEST 8
class NumberQuestion(models.Model):
   test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='number_questions')
   text = models.CharField(max_length=200)

   def __str__(self):
      return self.text



class Student(models.Model):
   full_name = models.CharField(max_length=100)
   group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
   answer_of_TEST4 =  models.ManyToManyField(VariantRadio, related_name="students", blank=True)
   passed = models.BooleanField(default=False)

   
   def __str__(self):
      return self.full_name

#              TEST 2, TEST 3, TEST 5, TEST 7 
class TextQuestion(models.Model):
   owner = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="TextAnswers")
   test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='text_questions')
   answer = models.TextField()

   def __str__(self):
      return 'Answer for {}. Answer - {}'.format(self.test, self.answer)



class AnswerTest6(models.Model):
   owner = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="Test6Answers")
   answer = models.IntegerField(blank=True)

   def __str__(self):
      return 'Answer - {}'.format(self.answer)


class AnswerTest8(models.Model):
   owner = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="Test8Answers")
   answer = models.IntegerField(blank=True)

   def __str__(self):
      return 'Answer - {}'.format(self.answer)



#              TEST 1
class First_test_variants(models.Model):
   test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='first_test_variants', blank=True)
   variant = models.CharField(max_length=1)
   owner = models.ManyToManyField(Student, related_name='first_test_answer', blank=True)

   def __str__(self):
      return 'Variant of {}. Variant - {}'.format(self.test, self.variant)


