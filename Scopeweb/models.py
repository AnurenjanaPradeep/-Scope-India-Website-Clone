from django.db import models

# Create your models here.
#courses
class Category(models.Model):
    category_name=models.CharField(max_length=100,primary_key=True)
    class Meta:
        verbose_name_plural="Category"
    def __str__(self):
        return self.category_name
class Courses(models.Model):
    course_name=models.CharField(max_length=100)
    duration=models.CharField(max_length=30,db_default='6 Months')
    fee=models.BigIntegerField(default= 42000)
    category_name=models.ForeignKey(Category,on_delete=models.CASCADE,null=True) 
    class Meta:
        verbose_name_plural="Courses"
    def __str__(self):
        return self.course_name
    
#registration 
class Registration(models.Model):
    full_name=models.CharField(max_length=100)
    photo=models.FileField(upload_to='documents',null=True)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=50)
    educational_qualification=models.CharField(max_length=50,null=True)
    hobbies=models.CharField(max_length=50,null=True)
    mobile_no=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    guardian_name=models.CharField(max_length=100,null=True)
    guardian_occupation=models.CharField(max_length=100,null=True)
    guardian_phone=models.CharField(max_length=100,null=True)
    choose_course=models.ManyToManyField(Courses, blank=True)
    training_mode=models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    timing=models.CharField(max_length=50)
    address=models.TextField(null=True)
    country=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)
    pin_code=models.CharField(max_length=50,null=True)
    password=models.CharField(max_length=8,default="NA",null=True)
    confirm_password=models.CharField(max_length=8,default="NA",null=True)
    existing_password=models.CharField(max_length=8,default="NA",null=True)
    otp_db=models.CharField(max_length=5,default="NA",null=True)
    remember_me=models.CharField(max_length=10,default="False",null=True)
    

# COUNTRY
class Country(models.Model):
    name=models.CharField(primary_key=True, max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural="Country"

# class State(models.Model):
#     country=models.ForeignKey(Country,on_delete=models.CASCADE)    
#     state_name=models.CharField(primary_key=True,max_length=100)
#     def __str__(self):
#         return self.state_name    

# class City(models.Model):
#     State=models.ForeignKey(State,on_delete=models.CASCADE)    
#     city_name=models.CharField(primary_key=True,max_length=100)
#     def __str__(self):
#         return self.city_name   



