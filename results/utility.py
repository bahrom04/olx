from django.db.models import Avg, F
from .models import Students, Regions, Districts, Schools
from django.db import models


def average_student_results():
    return Students.objects.aggregate(avg_result=Avg("correct_answer"))


def average_school_results():
    return Students.objects.values("school").annotate(avg_result=Avg("correct_answer"))


def average_district_results():
    top_school_results = Schools.objects.annotate(
    result=models.Avg(models.F('student__correct_answers')
                      * 100 / models.F('student__total_answers'))
    ).order_by('-result')[:3]
    

def average_region_results():
    # 13.1 
    average_result = Regions.objects.select_related('region').values('region__title').annotate(
        student=models.Avg(models.F('region__district__school__student__correct_answers')
                           * 100 / models.F('region__district__school__student__total_answers'))
    )
    top_region_results = Regions.objects.order_by('-average_result')[:3]


    # 13.5
    student_correct_answers = Students.objects.aggregate(avg_result=Avg("correct_answer")

    )
    region_points = Regions.objects.annotate(
    student_res=models.Sum(models.Case(models.When(
                student_correct_answers / models.F('student__total_answers') >= 0.8, 1.0,
                models.When(student_correct_answers / models.F('student__total_answers') >= 0.5, 0.5, default=0
                ), 
                output_field=models.FloatField()
            ),
            output_field=models.FloatField()
        )
    )
)


def calculate_average_results(request):
    region_results = Regions.objects.annotate(
        average_result=Avg('district__school__student__correct_answers')
                       / Avg('district__school__student__total_answers')
    ).values('title', 'average_result')

    results_list = [
        {"title": result['title'], "student_res": result['average_result'] * 100}
        for result in region_results
    ]

