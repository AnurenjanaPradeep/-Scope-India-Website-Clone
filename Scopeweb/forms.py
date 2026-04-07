from django import forms
from .models import Registration,Category,Courses,Country
import re

class Registrationform(forms.Form):
    full_name=forms.CharField(label='Full Name (required)',widget=forms.TextInput(attrs={'class':'inpstyle'}))
    photo=forms.FileField(label='Your Photo(required)')
    dob=forms.DateField( label='Date of Birth (required)',widget=forms.NumberInput(attrs={'type':'date','class':'inpstyle'}))
    gender=forms.ChoiceField(label='Gender (required)',choices=[('Male','Male'),('Female','Female'),('Other','Other')],widget=forms.RadioSelect(attrs={'class':'radiostyle'}))
    educational_qualification=forms.CharField(required=False,label='Educational Qualification',widget=forms.TextInput(attrs={'class':'inpstyle'}))
    
    hobby=[('Drawing','Drawing'),('Singing','Singing'),('Painting','Painting'),('Dancing','Dancing')]
    hobbies=forms.MultipleChoiceField(required=False,label='Hobbies',choices=hobby,widget=forms.CheckboxSelectMultiple(attrs={'class':'radiostyle'}))
    mobile_number=forms.CharField(label='Mobile Number (required)',widget=forms.TextInput(attrs={'class':'inpstyle'}))
    email=forms.EmailField(label='Email (required)',required=True,widget=forms.TextInput(attrs={'class':'inpstyle'}))
    guardian_name=forms.CharField(required=False,label="Guardian's Name",widget=forms.TextInput(attrs={'class':'inpstyle'}))
    guardian_occu=forms.CharField(required=False,label="Guardian's Occupation",widget=forms.TextInput(attrs={'class':'inpstyle'}))
    guardian_mob=forms.CharField(label="Guardian's Mobile (required)",widget=forms.TextInput(attrs={'class':'inpstyle'}))

    Course_choice = [
         ('',
          [('default','Choose your course ')]),
        ('Software Programming Courses', [
            ('PHP Full Stack Course', '	PHP Full Stack Course'),
            ('Python Full Stack Course', 'Python Full Stack Course'),
            ('Java Full Stack Course', 'Java Full Stack Course'),
            ('.Net Core Full Stack Course', 'C#.NET  Full Stack'),
            ('MEAN Full Stack Course', 'MEAN Full Stack Course'),
            ('MERN Full Stack Course', 'MERN Full Stack Course'),
            ('Data Science & AI Course', 'Data Science & AI (Python Guru)'),
            ('Python Mastery (Python/Django/MySQL)', 'Python Mastery (Python/Django/MySQL)'),
            ('Android/iOS Mobile App Course in Google Flutter Course', 'Google Flutter Mobile App Development (iOS/Android)'),
            ('UI/UX Design Course', 'UI/UX Designing'),
        ]),
        

        ('SEO/SEM/SMM Courses', [
            
            ('Digital Marketing Master Program', 'Digital Marketing Master Program'),
        ]),
        ('Software Testing Courses', [
            ('Software Testing Advanced Course', 'Software Testing Advanced (Manual/Automation)'),
            ('ISTQB Manual Testing Course', 'Software Testing Manual (ISTQB)'),
            
        ]),
        ('Computer Networking & Server Courses', [
            
            ('	Cisco Certified Network Associate(CCNA) Course','	Cisco Certified Network Associate(CCNA) Course'),
            ('AWS Architect Associate Course','AWS Architect Associate Course'),
            ('Networking,Server,& Cloud Administration Course','Networking & Server Admin(CCNA,MCSE,Hardware)'),
            
        ]),
    ]
    career=forms.ChoiceField(choices=Course_choice,label='Choose your course (required)',widget=forms.Select(attrs={'class':'inpstyle'}))
    modee=[('Live Mode','Live Mode'),('Classroom','Classroom')]
    mode=forms.ChoiceField(label='Training Mode (required)',choices= modee,widget=forms.RadioSelect(attrs={'class':'radiostyle'}) )
    loc=[('Technopark TVM ','Technopark TVM '),('Thampanoor TVM','Thampanoor TVM'),('Kochi','Kochi'),('Nagercoil','Nagercoil'),('Online','Online')]
    scope_location=forms.ChoiceField(label='SCOPE INDIA Location (required)',choices= loc,widget=forms.RadioSelect(attrs={'class':'radio2style'}) )
    timee=[('Between 8am - 10am','Between 8am - 10am'),('Between 9am - 1pm','Between 9am - 1pm'),('Between 1pm - 6pm','Between 1pm - 6pm'),('Between 6pm - 10pm','Between 6pm - 10pm')]
    time=forms.MultipleChoiceField(label='Preferred Training Timings (required)',choices= timee,widget=forms.CheckboxSelectMultiple())
    address=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'inpstyle'}))
    country=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'inpstyle'}))   
    # state=forms.ModelChoiceField(required=False,queryset=State.objects.none(),widget=forms.Select(attrs={'class':'inpstyle'}))
    # city=forms.ModelChoiceField(required=False,queryset=City.objects.none(),widget=forms.Select(attrs={'class':'inpstyle'}))
    state=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'inpstyle'}))
    city=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'inpstyle'}))
    pin=forms.IntegerField(required=False,label='PIN/Zip Code',widget=forms.TextInput(attrs={'class':'inpstyle'}))
   


    def clean_email(self):
        value=self.cleaned_data['email']
        pattern=r'^[a-z0-9.]+@gmail\.com$'
        if re.match(pattern,value):  
        
                return value
        else:
                raise forms.ValidationError("Enter a valid email ")
    def clean_email(self):
        value=self.cleaned_data['email']
        if Registration.objects.filter(email=value).exists():
            raise forms.ValidationError("Email already exists")
        return value
        
    def clean_mobile_number(self):
        value = self.cleaned_data['mobile_number']
        pattern =r'^[0-9]{10}$'
        if re.match(pattern,value):
            return value
        else:
            raise forms.ValidationError("Enter a valid 10-digit mobile number ")

    def clean_guardian_mob(self):
            value = self.cleaned_data['guardian_mob']
            pattern =r'^[0-9]{10}$'
            if re.match(pattern, value):
                return value
            else:
                raise forms.ValidationError("Enter a valid 10-digit mobile number ")


class updateform(forms.Form):
    full_name=forms.CharField(label='Full Name (required)',widget=forms.TextInput(attrs={'class':'inpstyle'}))
   
    dob=forms.DateField( label='Date of Birth (required)',widget=forms.NumberInput(attrs={'type':'date','class':'inpstyle'}))
    gender=forms.ChoiceField(label='Gender (required)',choices=[('Male','Male'),('Female','Female'),('Other','Other')],widget=forms.RadioSelect(attrs={'class':'radiostyle'}))
    educational_qualification=forms.CharField(required=False,label='Educational Qualification',widget=forms.TextInput(attrs={'class':'inpstyle'}))
    
    hobby=[('Drawing','Drawing'),('Singing','Singing'),('Painting','Painting'),('Dancing','Dancing')]
    hobbies=forms.MultipleChoiceField(required=False,label='Hobbies',choices=hobby,widget=forms.CheckboxSelectMultiple(attrs={'class':'radiostyle'}))
    mobile_number=forms.CharField(label='Mobile Number (required)',widget=forms.TextInput(attrs={'class':'inpstyle'}))
    email=forms.EmailField(label='Email (required)',required=True,widget=forms.TextInput(attrs={'class':'inpstyle'}))
    guardian_name=forms.CharField(required=False,label="Guardian's Name",widget=forms.TextInput(attrs={'class':'inpstyle'}))
    guardian_occu=forms.CharField(required=False,label="Guardian's Occupation",widget=forms.TextInput(attrs={'class':'inpstyle'}))
    guardian_mob=forms.CharField(required=False,label="Guardian's Mobile",widget=forms.TextInput(attrs={'class':'inpstyle'}))

    Course_choice = [
         ('',
          [('default','Choose your course ')]),
        ('Software Programming Courses', [
            ('PHP Full Stack Course', '	PHP Full Stack Course'),
            ('Python Full Stack Course', 'Python Full Stack Course'),
            ('Java Full Stack Course', 'Java Full Stack Course'),
            ('.Net Core Full Stack Course', 'C#.NET  Full Stack'),
            ('MEAN Full Stack Course', 'MEAN Full Stack Course'),
            ('MERN Full Stack Course', 'MERN Full Stack Course'),
            ('Data Science & AI Course', 'Data Science & AI (Python Guru)'),
            ('Python Mastery (Python/Django/MySQL)', 'Python Mastery (Python/Django/MySQL)'),
            ('Android/iOS Mobile App Course in Google Flutter Course', 'Google Flutter Mobile App Development (iOS/Android)'),
            ('UI/UX Design Course', 'UI/UX Designing'),
        ]),
        

        ('SEO/SEM/SMM Courses', [
            
            ('Digital Marketing Master Program', 'Digital Marketing Master Program'),
        ]),
        ('Software Testing Courses', [
            ('Software Testing Advanced Course', 'Software Testing Advanced (Manual/Automation)'),
            ('ISTQB Manual Testing Course', 'Software Testing Manual (ISTQB)'),
            
        ]),
        ('Computer Networking & Server Courses', [
            
            ('	Cisco Certified Network Associate(CCNA) Course','	Cisco Certified Network Associate(CCNA) Course'),
            ('AWS Architect Associate Course','AWS Architect Associate Course'),
            ('Networking,Server,& Cloud Administration Course','Networking & Server Admin(CCNA,MCSE,Hardware)'),
            
        ]),
    ]
    # career=forms.ChoiceField(choices=Course_choice,label='Choose your course (required)',widget=forms.Select(attrs={'class':'inpstyle'}))
    modee=[('Live Mode','Live Mode'),('Classroom','Classroom')]
    mode=forms.ChoiceField(label='Training Mode (required)',choices= modee,widget=forms.RadioSelect(attrs={'class':'radiostyle'}) )
    loc=[('Technopark TVM ','Technopark TVM '),('Thampanoor TVM','Thampanoor TVM'),('Kochi','Kochi'),('Nagercoil','Nagercoil'),('Online','Online')]
    scope_location=forms.ChoiceField(label='SCOPE INDIA Location (required)',choices= loc,widget=forms.RadioSelect(attrs={'class':'radio2style'}) )
    timee=[('Between 8am - 10am','Between 8am - 10am'),('Between 9am - 1pm','Between 9am - 1pm'),('Between 1pm - 6pm','Between 1pm - 6pm'),('Between 6pm - 10pm','Between 6pm - 10pm')]
    time=forms.MultipleChoiceField(label='Preferred Training Timings (required)',choices= timee,widget=forms.CheckboxSelectMultiple())
    address=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'inpstyle'}))
    country=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'inpstyle'})) 
    # state=forms.ModelChoiceField(required=False,queryset=State.objects.none(),widget=forms.Select(attrs={'class':'inpstyle'}))
    # city=forms.ModelChoiceField(required=False,queryset=City.objects.none(),widget=forms.Select(attrs={'class':'inpstyle'}))
    state=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'inpstyle'}))
    city=forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'inpstyle'}))
    pin=forms.IntegerField(required=False,label='PIN/Zip Code',widget=forms.TextInput(attrs={'class':'inpstyle'}))
    photo=forms.FileField(required=False ,label='Your Photo')
    # password=forms.CharField(required=False,widget=forms.PasswordInput(attrs={'class':'inpstyle'}))
    # confirm_password=forms.CharField(required=False,widget=forms.PasswordInput(attrs={'class':'inpstyle'}))


    def clean_email(self):
        value=self.cleaned_data['email']
        pattern=r'^[a-z0-9.]+@gmail\.com$'
        if re.match(pattern,value):  
        
                return value
        else:
                raise forms.ValidationError("Enter a valid email ")
        
    def clean_mobile_number(self):
        value = self.cleaned_data['mobile_number']
        pattern =r'^[0-9]{10}$'
        if re.match(pattern,value):
            return value
        else:
            raise forms.ValidationError("Enter a valid 10-digit mobile number ")

    def clean_guardian_mob(self):
            value = self.cleaned_data['guardian_mob']
            pattern =r'^[0-9]{10}$'
            if re.match(pattern, value):
                return value
            else:
                raise forms.ValidationError("Enter a valid 10-digit mobile number ")
    # def clean_password(self):
    #         value= self.cleaned_data['password']

class pass_updateform(forms.Form):
    epassword=forms.CharField(label="Existing Password",required=False,widget=forms.PasswordInput(attrs={'class':'inpstyle'}))  
    password=forms.CharField(required=False,widget=forms.PasswordInput(attrs={'class':'inpstyle'}))
    cpassword=forms.CharField(label="Confirm Password",required=False,widget=forms.PasswordInput(attrs={'class':'inpstyle'}))          


     


