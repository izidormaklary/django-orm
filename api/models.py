from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=255, default="Your street")
    house_number = models.CharField(max_length=60, default="Your house")
    zip_code = models.CharField(max_length=60, default="Your zip")
    city = models.CharField(max_length=255, default="Your city")

    def __str__(self):
        return "{} {} {} {}".format(
            self.street,
            self.house_number,
            self.zip_code,
            self.city
        )

    class Meta:
        abstract = True


class Teacher(Address):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=256)

    def __str__(self):
        return self.firstName + " " + self.lastName

    def json(self):
        return [{
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
        }]


class Student(Address):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=256)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstName + " " + self.lastName

    def json(self):
        return ({
            'firstName': self.firstName,
            'lastName': self.lastName,
            'email': self.email,
        })

