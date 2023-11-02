from django.db import models
from django.db.models.functions import Coalesce


class CategoryManager(models.Manager):
    def with_counts(self):
        return self.annotate(num_adds=Coalesce(models.Count("adds"), 0))


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = CategoryManager()


class Adds(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    categoty = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="adds")

'''
1. Category nomi M bilan boshlanganlari

Category.objects.filter(title__istartwith="m")

2. category ichida avto so'zi qatnashganlari.
Category.objects.filter(adds__title__icontains="avto")

3. Ikkinchi 5 talik kategoriyalar.
Category.objects[:5]
     
4. 2023 yilda yaratilgan categorylar.
Category.objects.filter(created__year="2023")

5. Categorylarni oxirigi yangilanish bo'yicha tartiblab chiqish.
Category.objects.order_by("-created_at")

6. Category producti nomida matiz qatnashganlari
Category.objects.filter(adds__title="matiz")

7. Category lar ro'yxati, qaysiki producti mavjud bo'lgan.
Category.objects.filter(num_adds__gt=0)

8. Categorylar ro'yxati, 2022 yilda chiqganlari yoki nomi S harfi bilan boshlanganlari.
Category.objects.filter(created_at__year=2022, name__startswith="s")

9. Product dagi ko'rishlar sonini bittaga ortdirish, query orqali.
Category.objects.update(num_adds=F("num_adds") + 1)

10. Category nomlarini bitta bitta print qiling + har bitta categoryga tegishli bo'lgan product nomlarini bitta bita print qiling. for loop orqali
Category.objects


11. Barcha productlarni ko'rishlar sonini
Category.objects.aggregate(num_adds=Coalesce(models.Count("products"), 0))

12. Productlarda o'rtacha narx, maximal narx, minimal narx.
Category.objects.aggregate(
    avg_price=Coalesce(models.Avg("products__price"), 0),
)


13. Regionlar bor, regionlarni districtlari bor, districtlarni maktablari bor, maktablarni o'quvchilari bor.
O'quvchilarni testdan ishlagan natijalari bor.

Result:
    correct_answers = 20
    total_answers= 25
    percentage = 80

13.1 Regionlar bo'yicha o'quvchilarni o'rtacha natijalarini chiqaring.  
[{"title": "Toshkent", "student_res":81.56%}, {"title": "Sirdaryo", "student_res":87.56%}, {"title": "Jizzax", "student_res":86.56%}, {"title": "Samarqand", "student_res":87.5126%},]
13.2.Regionlarni Tumanlarini o'rtacha natijasi yuqori 3 tasini chiqarish
[{"title": "Toshkent", "tumanlar":[
    {"title":"Yunusobod", "result":67.45%}
]}, ]
13.3. O'zlashtirish natijasi yuqori bo'lgan top 3 ta maktablar tumanlar kesimida.
[{"title": "Yunusobod", "maktab":[
    {"title":"11-maktab", "result":67.45%}
]}, ]
13.4. oylar kesimida regionlarda o'zlashtirish natijasi. ( oylar kesimida degani - 12 oy (Yan, Fev,...., Dec), o'zlashtirish natijasida degani o'rtacha natija)
[
    {"title":"Yanvar", "region":[
        {"title":"Toshkent", "result":76.12%}
    ]}
]
13.5. Butun viloyatlar to'plagan ball chiqarilsin, 100-80% uchun 1 ball o'quvchiga, 80%-50% uchun 0.5 ball, undan pastiga 0 ball. Viloyatlar ballari chiqarilsin.
10 o'quvchi
2 tasi 100-80% oralig'ida=  1*2 = 2 ball
6 tasi 80%-50% uchun 0.5 * 6 = 3 ball
2 tasi 50% pas  0 ball
Region umumiy bali , 5 ball
[{"title": "Toshkent", "student_res":5}, ]
'''