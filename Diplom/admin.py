from django.contrib import admin
from .models import (
   
   Student, 
   Test, 
   TextQuestion, 
   Group,
   VariantRadio, 
   QuestionRadio, 
   First_test_variants, NumberQuestion, 
   AnswerTest6,
   AnswerTest8,
   Third_test_variants,
   Seventh_test_variants
)
admin.site.register(Student)
admin.site.register(Test)
admin.site.register(TextQuestion)
admin.site.register(Group)

admin.site.register(QuestionRadio)
admin.site.register(VariantRadio)
admin.site.register(First_test_variants)

admin.site.register(NumberQuestion)
admin.site.register(AnswerTest6)
admin.site.register(AnswerTest8)
admin.site.register(Third_test_variants)
admin.site.register(Seventh_test_variants)