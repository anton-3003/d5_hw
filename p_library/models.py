from django.db import models


# модель издательства: название
class Publisher(models.Model):
    pub_name = models.TextField()

    def __str__(self):
        return self.pub_name


# модель автора: Ф.И., год рождения, страна
class Author(models.Model):
    full_name = models.TextField(verbose_name="Имя")
    birth_year = models.SmallIntegerField(verbose_name="Год рождения")
    country = models.CharField(verbose_name="Страна", max_length=2)

    def __str__(self):
        return "{}".format(self.full_name)


# модель книги: международный код, название, описание, год "создания", автор, количество экз., цена, издательство

class Book(models.Model):
    ISBN = models.CharField(verbose_name="Международный код", max_length=13)
    title = models.TextField(verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    year_release = models.SmallIntegerField(verbose_name="Год издания")
    copy_count = models.SmallIntegerField(verbose_name="Количество экз.")
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Цена")
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE,
                               related_name="book_author",
                               verbose_name="Автор",
                               null=True)
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.DO_NOTHING,
                                  null=True,
                                  related_name="books",
                                  verbose_name="Издательство")

    # friend_take = models.ForeignKey(Friend,
    #                                 on_delete=models.DO_NOTHING,
    #                                 related_name='taked',
    #                                 verbose_name='Книга у ',
    #                                 null=True)

    def __str__(self):
        return self.title


# модель друга: Ф.И., телефон, эл.почта
class Friend(models.Model):
    name = models.CharField(max_length=50, verbose_name="Имя")
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")
    e_mail = models.EmailField(max_length=50, verbose_name="Эл.почта")
    book = models.ForeignKey(Book,
                             on_delete=models.DO_NOTHING,
                             null=True,
                             verbose_name="Книга",
                             related_name="book", )

    def __str__(self):
        return self.name
