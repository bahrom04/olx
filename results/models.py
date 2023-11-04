from django.db import models

# Create your models here.
class Regions(models.Model):
    title = models.CharField(max_length=100)
    

    def __str__(self):
        return self.title


class Districts(models.Model):
    title = models.CharField(max_length=100)

    region = models.ForeignKey(Regions, on_delete=models.CASCADE, related_name="districts")

    def __str__(self):
        return self.title


class Schools(models.Model):
    title = models.CharField(max_length=100)

    district = models.ForeignKey(Districts, on_delete=models.CASCADE, related_name="schools")

    def __str__(self):
        return self.title


class Students(models.Model):
    title = models.CharField(max_length=100)
    correct_answer = models.PositiveIntegerField()
    total_answer = models.PositiveIntegerField()

    school = models.ForeignKey(Schools, on_delete=models.CASCADE, related_name="students")

    def __str__(self):
        return self.title
    

class MonthResult(models.Model):
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    result = models.FloatField()











