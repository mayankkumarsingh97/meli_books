from django.db import models
from django.forms import ModelForm
# Create your models here.
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save

# Create your models here.

class HomeBanner(models.Model):
    id=models.AutoField(primary_key=True)
    bannername = models.CharField(max_length=200, blank=False, verbose_name='Banner Name')
    first_banner = models.ImageField(upload_to='img/', blank=False, verbose_name='First Banner 4928*3264')
    first_banner_heading = models.CharField(max_length=200, blank=False, verbose_name='First Banner Heading')
    first_banner_paragraph = models.CharField(max_length=200, blank=False, verbose_name='First Banner Paragraph')
    second_banner = models.ImageField(upload_to='img/', blank=True, verbose_name='Second Banner 4928*3264')
    second_banner_heading = models.CharField(max_length=200, blank=True, verbose_name='Second Banner Heading')
    second_banner_paragraph = models.CharField(max_length=200, blank=True, verbose_name='Second Banner Paragraph')
    third_banner = models.ImageField(upload_to='img/', blank=True, verbose_name='Third Banner 4928*3264')
    third_banner_heading = models.CharField(max_length=200, blank=True, verbose_name='Third Banner Heading')
    third_banner_paragraph = models.CharField(max_length=200, blank=True, verbose_name='Third Banner Paragraph')


    def __str__(self):
        return self.bannername


class HomePageFirstContent(models.Model):
    id=models.AutoField(primary_key=True)
    contentname = models.CharField(max_length=1000, blank=True, verbose_name='ContentName')
    heading = models.CharField(max_length=1000, blank=True, verbose_name='Heading')
    paragraph = models.CharField(max_length=1000, blank=True, verbose_name='Paragraph')
    first_img = models.ImageField(upload_to='img/', blank=True, verbose_name='First Image Size 3861*2574')
    second_img = models.ImageField(upload_to='img/', blank=True, verbose_name='Second Image Size 3861*2574')
    second_heading = models.CharField(max_length=1000, blank=True, verbose_name='Second Heading')
    second_paragraph = models.CharField(max_length=1000, blank=True, verbose_name='Second Paragraph')
    third_paragraph = models.CharField(max_length=1000, blank=True, verbose_name='Third Paragraph')
    fourth_paragraph = models.CharField(max_length=1000, blank=True, verbose_name='Fourth Paragraph')
    left_img = models.ImageField(upload_to='img/', blank=True, verbose_name='Left Image Size 3861*2574')



    def __str__(self):
        return self.contentname



class HomePageSecondContent(models.Model):
    id=models.AutoField(primary_key=True)
    contentname = models.CharField(max_length=1000, blank=True, verbose_name='ContentName')
    heading = models.CharField(max_length=1000, blank=True, verbose_name='Heading')
    small_heading = models.CharField(max_length=1000, blank=True, verbose_name='Small Heading')
    paragraph = models.CharField(max_length=1000, blank=True, verbose_name='Paragraph')
    left_img = models.ImageField(upload_to='img/', blank=True,verbose_name='First Image Size 408*531')
    point_1 = models.CharField(max_length=1000, blank=True, verbose_name='Point 1')
    point_2 = models.CharField(max_length=1000, blank=True, verbose_name='Point 2')
    point_3 = models.CharField(max_length=1000, blank=True, verbose_name='Point 3')
    point_4 = models.CharField(max_length=1000, blank=True, verbose_name='Point 4')
    point_5 = models.CharField(max_length=1000, blank=True, verbose_name='Point 5')
    point_6 = models.CharField(max_length=1000, blank=True, verbose_name='Point 6')
    point_7 = models.CharField(max_length=1000, blank=True, verbose_name='Point 7')
    second_small_heading = models.CharField(max_length=1000, blank=True, verbose_name='Small Heading')
    second_paragraph = models.CharField(max_length=1000, blank=True, verbose_name='Paragraph')
    right_img = models.ImageField(upload_to='img/', blank=True,verbose_name='Second Image Size 408*531')
    second_point_1 = models.CharField(max_length=1000, blank=True, verbose_name='Point 1')
    second_point_2 = models.CharField(max_length=1000, blank=True, verbose_name='Point 2')
    second_point_3 = models.CharField(max_length=1000, blank=True, verbose_name='Point 3')
    second_point_4 = models.CharField(max_length=1000, blank=True, verbose_name='Point 4')
    second_point_5 = models.CharField(max_length=1000, blank=True, verbose_name='Point 5')
    second_point_6 = models.CharField(max_length=1000, blank=True, verbose_name='Point 6')
    second_point_7 = models.CharField(max_length=1000, blank=True, verbose_name='Point 7')
    second_point_8 = models.CharField(max_length=1000, blank=True, verbose_name='Point 8')
    second_point_9 = models.CharField(max_length=1000, blank=True, verbose_name='Point 9')
    second_point_10 = models.CharField(max_length=1000, blank=True, verbose_name='Point 10')
    def __str__(self):
        return self.contentname


class AboutBanner(models.Model):
    id=models.AutoField(primary_key=True)
    bannername = models.CharField(max_length=200, blank=True, verbose_name='Banner Name')
    about_banner = models.ImageField(upload_to='img/', blank=True, verbose_name='Banner Size 1440*961')
    def __str__(self):
        return self.bannername


class AboutPageFirstContent(models.Model):
    id=models.AutoField(primary_key=True)
    contentname = models.CharField(max_length=1000, blank=True, verbose_name='ContentName')
    heading = models.CharField(max_length=1000, blank=True, verbose_name='Heading')
    paragraph = models.CharField(max_length=1000, blank=True, verbose_name='Paragraph')
    first_small_heading = models.CharField(max_length=1000, blank=True, verbose_name='First Small Heading')
    first_paragraph = models.CharField(max_length=1000, blank=True, verbose_name='First Paragraph')
    second_small_heading = models.CharField(max_length=1000, blank=True, verbose_name='Second Small Heading')
    second_paragraph = models.CharField(max_length=1000, blank=True, verbose_name='Second Paragraph')
    third_small_heading = models.CharField(max_length=1000, blank=True, verbose_name='Third Small Heading')
    third_paragraph = models.CharField(max_length=1000, blank=True, verbose_name='Third Paragraph')

    def __str__(self):
        return self.contentname

class AboutPageSecondContent(models.Model):
    id=models.AutoField(primary_key=True)
    contentname = models.CharField(max_length=1000, blank=True, verbose_name='ContentName')
    heading = models.CharField(max_length=1000, blank=True, verbose_name='Heading')
    paragraph = models.CharField(max_length=1000, blank=True, verbose_name='Paragraph')
    first_small_heading = models.CharField(max_length=1000, blank=True, verbose_name='First Small Heading')
    first_paragraph = models.CharField(max_length=1000, blank=True, verbose_name='First Paragraph')
    second_small_heading = models.CharField(max_length=1000, blank=True, verbose_name='Second Small Heading')
    second_paragraph = models.CharField(max_length=1000, blank=True, verbose_name='Second Paragraph')
    third_small_heading = models.CharField(max_length=1000, blank=True, verbose_name='Third Small Heading')
    third_paragraph = models.CharField(max_length=1000, blank=True, verbose_name='Third Paragraph')
    left_img = models.ImageField(upload_to='img/', blank=True,  verbose_name='Left image Size 996*696')
    img_heading = models.CharField(max_length=1000, blank=True, verbose_name='Img Heading')
    img_paragraph = models.CharField(max_length=1000, blank=True, verbose_name='Img Paragraph')

    def __str__(self):
        return self.contentname


class AboutPageThirdContent(models.Model):
    id=models.AutoField(primary_key=True)
    contentname = models.CharField(max_length=1000, blank=True, verbose_name='ContentName')
    first_small_heading = models.CharField(max_length=1000, blank=True, verbose_name='First Small Heading')
    first_paragraph = models.CharField(max_length=1000, blank=True, verbose_name='First Paragraph')
    second_small_heading = models.CharField(max_length=1000, blank=True, verbose_name='Second Small Heading')
    second_paragraph = models.CharField(max_length=1000, blank=True, verbose_name='Second Paragraph')
    third_small_heading = models.CharField(max_length=1000, blank=True, verbose_name='Third Small Heading')
    third_paragraph = models.CharField(max_length=1000, blank=True, verbose_name='Third Paragraph')
    right_img = models.ImageField(upload_to='img/', blank=True, verbose_name='Right image Size 1000*750')
    img_heading = models.CharField(max_length=1000, blank=True, verbose_name='Img Heading')
    img_paragraph = models.CharField(max_length=1000, blank=True, verbose_name='Img Paragraph')

    def __str__(self):
        return self.contentname

class AboutPageFourthContent(models.Model):
    id=models.AutoField(primary_key=True)
    contentname = models.CharField(max_length=1000, blank=True, verbose_name='ContentName')
    heading = models.CharField(max_length=1000, blank=True, verbose_name='Heading')
    paragraph = models.CharField(max_length=1000, blank=True, verbose_name='Paragraph')
    img_1 = models.ImageField(upload_to='img/', blank=True, verbose_name='First image Size 408*531')
    img_2 = models.ImageField(upload_to='img/', blank=True, verbose_name='Second image Size 408*531')
    img_3 = models.ImageField(upload_to='img/', blank=True, verbose_name='Third image Size 408*531')
    img_4 = models.ImageField(upload_to='img/', blank=True, verbose_name='Fourth image Size 730*250')
    img_5 = models.ImageField(upload_to='img/', blank=True, verbose_name='Fifth image Size 730*250')

    link_1 = models.CharField(max_length=200, blank=True, verbose_name='link_1')
    link_2 = models.CharField(max_length=200, blank=True, verbose_name='link_2')
    link_3 = models.CharField(max_length=200, blank=True, verbose_name='link_3')
    link_4 = models.CharField(max_length=200, blank=True, verbose_name='link_4')
    link_5 = models.CharField(max_length=200, blank=True, verbose_name='link_5')



    def __str__(self):
        return self.contentname

class ContactBanner(models.Model):
    id=models.AutoField(primary_key=True)
    bannername = models.CharField(max_length=200, blank=True, verbose_name='Banner Name')
    contact_banner = models.ImageField(upload_to='img/', blank=True, verbose_name='Banner image Size 1440*960')
    def __str__(self):
        return self.bannername


class ContactPage(models.Model):
    id=models.AutoField(primary_key=True)
    address = models.CharField(max_length=200, blank=True, verbose_name='Office Address')
    marketing_phone = models.CharField(max_length=200, blank=True, verbose_name='Marketing Person Phone Number')
    marketing_email = models.CharField(max_length=200, blank=True, verbose_name='Marketing Person Email')
    production_phone = models.CharField(max_length=200, blank=True, verbose_name='Production Person Phone Number')
    production_email = models.CharField(max_length=200, blank=True, verbose_name='Production Person Phone Number')



    def __str__(self):
        return self.address


class socialmedia(models.Model):
    id=models.AutoField(primary_key=True)
    social = models.CharField(max_length=200, blank=True, verbose_name='Social Media')
    facebook = models.CharField(max_length=200, blank=True, verbose_name='Facebook')
    instagram = models.CharField(max_length=200, blank=True, verbose_name='Instagram')
    youtube = models.CharField(max_length=200, blank=True, verbose_name='Youtube')
    twitter = models.CharField(max_length=200, blank=True, verbose_name='Twitter')
    def __str__(self):
        return self.social


class ebooks(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, verbose_name='Ebook Name')
    ebook = models.CharField(max_length=200, blank=True, verbose_name='Ebook Url')



    def __str__(self):
        return self.name

class catalouge(models.Model):
    id=models.AutoField(primary_key=True)
    cat = models.CharField(max_length=200, blank=True, verbose_name='Name')
    cat_pdf = models.FileField(upload_to='catalouge/', null=True, )



    def __str__(self):
        return self.cat



class Contactus(models.Model):
    name = models.CharField(max_length=200, blank=True, verbose_name='Name')
    email = models.CharField(max_length=200, blank=True, verbose_name='Email')
    phone = models.CharField(max_length=17, blank=True, verbose_name='phone')
    message = models.TextField(max_length=200, blank=True, verbose_name='Message')

    def __str__(self):
        return self.name

class contactUsForm(ModelForm):
    class Meta:
        model = Contactus
        fields = [ 'name', 'email', 'phone', 'message']
