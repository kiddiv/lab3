from django.db import models
from django.urls import reverse
class Departments(models.Model):
    name = models.CharField("Назва кафедри", max_length=200)
    head = models.CharField("Завідувач кафедри", max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = "Кафедра"
        verbose_name_plural = "Кафедри"

    def __str__(self):
        return self.name

class Programs(models.Model):
    title = models.CharField('Назва спеціальності', max_length=200)
    code = models.CharField('Код спеціальності', max_length=10, unique=True)
    description = models.TextField('Опис спеціальності')
    coordinator = models.ForeignKey(
        'Teachers',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='coordinated_programs',
        verbose_name='Координатор набору'
    )
    disciplines = models.TextField('Список дисциплін', blank=True)
    department = models.ForeignKey(
        'Departments',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='programs',
        verbose_name='Кафедра'
    )

    class Meta:
        verbose_name = 'Спеціальність'
        verbose_name_plural = 'Спеціальності'
        ordering = ['code', 'title']

    def __str__(self):
        return f"{self.title} ({self.code})"

    def get_disciplines_list(self):
        if self.disciplines:
            return [d.strip() for d in self.disciplines.replace('\n', ',').split(',')]
        return []


class Teachers(models.Model):
    full_name = models.CharField("Ім'я", max_length=200)
    position = models.CharField("Посада", max_length=100)
    degree = models.CharField("Ступінь", max_length=100, blank=True, null=True)
    email = models.EmailField("Email", blank=True, null=True)
    phone = models.CharField("Телефон", max_length=50, blank=True, null=True)
    department = models.ForeignKey(
        'Departments',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='teachers',
        verbose_name='Кафедра'
    )

    class Meta:
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"

    def __str__(self):
        return self.full_name
class HomePage(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    description = models.TextField("Опис факультету")

    def __str__(self):
        return self.title

