from django.db import models

class Customerdata(models.Model):
    first_name=models.CharField(max_length=300)
    last_name=models.CharField(max_length=300)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=300)




    @staticmethod
    def get_customer_email(email):
        try:
            return Customerdata.objects.get(email=email)

        except:
            return False

    def register(self):
        self.save()






