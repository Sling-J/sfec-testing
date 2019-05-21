from django.shortcuts import render, redirect
from .models import (
   Student, 
   Group, 
   Test, 
   QuestionRadio, 
   VariantRadio, 
   TextQuestion, 
   First_test_variants, 
   AnswerTest6, 
   AnswerTest8,
   Third_test_variants,
   Seventh_test_variants
)
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.utils.translation import gettext as _

def home(request):
   return render(request, 'Diplom/home.html')

def groups(request):
   groups = Group.objects.all()
   
   context = {
     'groups': groups,
   }
   return render(request, 'Diplom/groups.html', context)

def students(request, slug):
   group = Group.objects.get(slug=slug)
   students = Student.objects.filter(group=group, passed=False)

   if request.method == 'POST':
      try:
         student_id = request.POST['student']
         request.session['student_id'] = student_id
         return redirect('test_url')
      except:
         return redirect('groups_url')
   
   context = {
     'students':students,
   }
   return render(request, 'Diplom/students.html', context)




def test(request):
   # from django.utils import translation
   # # user_language = 'kk'
   # # translation.activate(user_language)
   # # request.session[translation.LANGUAGE_SESSION_KEY] = user_language

   # if translation .LANGUAGE_SESSION_KEY in request.session:
   #    del request.session[translation.LANGUAGE_SESSION_KEY]


   test1 = Test.objects.get(number=1)
   test2 = Test.objects.get(number=2)
   test3 = Test.objects.get(number=3)
   test4 = Test.objects.get(number=4)
   test5 = Test.objects.get(number=5)
   test6 = Test.objects.get(number=6)
   test7 = Test.objects.get(number=7)
   test8 = Test.objects.get(number=8)
   try:
      student = Student.objects.get(id=request.session['student_id'])
   except KeyError:
      return HttpResponse('<h1>Ошибка!</h1><p><a href="/groups/">Выберите студента!</a></p>')
   if request.method == 'POST':
      try:
         #           TEST 1
         for question in test1.questions.all():
            variantR_id = request.POST.get('first_test_variant-{}'.format(question.id))
            variantR = First_test_variants.objects.get(id=variantR_id)
            variantR.owner.add(student)

         #           TEST 2 
         answer = request.POST.get('T2')
         TextQuestion.objects.create(owner=student, test=test2, answer=answer)

         #           TEST 3
         variant_id = request.POST.get('T3')
         variant = Third_test_variants.objects.get(id=variant_id)
         variant.owner.add(student)


         #           TEST 4
         for question in test4.questions.all():
            variantR_id = request.POST.get('variants-{}'.format(question.id))
            variantR = VariantRadio.objects.get(id=variantR_id)
            variantR.owner.add(student)

         #           TEST 5
         answer = request.POST.get('T5')
         TextQuestion.objects.create(owner=student, test=test5, answer=answer)

         #           TEST 6
         answers = request.POST.getlist('answer_number_t6')
         for answer in answers:
            AnswerTest6.objects.create(owner=student, answer=answer)

         #           TEST 7
         variant_id = request.POST.get('T7')
         variant = Seventh_test_variants.objects.get(id=variant_id)
         variant.owner.add(student)

         #         TEST 8
         answers = request.POST.getlist('answer_number_t8')
         for answer in answers:
            AnswerTest8.objects.create(owner=student, answer=answer)

         student.passed = True
         student.save()
         del request.session['student_id']
         messages.success(request, f'Сіз сынақты сәтті өткіздіңіз!')
         return redirect('home_url')
      except:
         error_message = _('Сіз барлық сұрақтарға жауап берген жоқсыз')
         messages.error(request, f'{error_message}')
         return redirect('test_url')


   title = _('Сынақ парақшасы')
   return render(request, 'Diplom/test.html', context={
      'test1': test1,
      'test3': test3,
      'test4': test4,
      'test6': test6,
      'test7': test7,
      'test8': test8,
      'title': title,
   })
   


@login_required()
def answers(request):
   groups = Group.objects.all()
   test6 = Test.objects.get(number=6)
   test8 = Test.objects.get(number=8)
   context = {
      'groups': groups,
      'test6': test6,
      'test8': test8,
   }
   return render(request, 'Diplom/answers.html', context)