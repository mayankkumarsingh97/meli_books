from django.db import models
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User




class State(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Capital(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='capitals')

    def __str__(self):
        return f"{self.name} ({self.state.name})"



class ImplementCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ImplementSubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(ImplementCategory, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.category.name} - {self.name}"

class AgricultureImplement(models.Model):
    id = models.AutoField(primary_key=True)  
    category = models.ForeignKey(ImplementCategory, on_delete=models.SET_NULL, null=True, blank=True)
    subcategory = models.ForeignKey(ImplementSubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    isPopular = models.BooleanField(default=False)
    isBestSeller = models.BooleanField(default=False)
    implement_type = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    working_width = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    power_required = models.IntegerField(blank=True, null=True)
    number_of_blades = models.IntegerField(blank=True, null=True)
    material_type = models.CharField(max_length=255, blank=True)
    fuel_type = models.CharField(max_length=100, blank=True)
    engine_power = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    price_negotiable = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    condition = models.CharField(max_length=100, choices=[('new', 'New'), ('used', 'Used')])
    warranty_available = models.BooleanField(default=False)
    warranty_details = models.TextField(blank=True, null=True)
    main_image = models.ImageField(upload_to='implements/')
    manual_document = models.FileField(upload_to='documents/', blank=True, null=True)
    location = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.brand} {self.name} ({self.model})"


class BlogCategory(models.Model):
    cat_id= models.AutoField(primary_key=True)
    cat_title = models.CharField(max_length=100)
    # cat_description = models.TextField()
    # url = models.CharField(max_length=100,blank=True)
    # image = models.ImageField(upload_to='blogCategory',blank=True)
    # cat_date= models.DateField()


    def __str__(self):
        return self.cat_title

class Blog(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name = "blog_cat")
    img = models.FileField(upload_to='blog', verbose_name='blog image', blank=False)
    title =models.CharField(max_length=120, null=False,default="None", blank=False,verbose_name="title")
    short_description= models.TextField(null=False,default="None", blank=False,verbose_name="short description")
    content = models.TextField(blank=True, null=True)
    pub_date = models.DateField(auto_now_add=True,blank=False,null=True)
    updated_date= models.DateTimeField(blank=True,null=True)
    Category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE,null=True, related_name = "blog_cat")
    video = models.FileField(upload_to='remyblogvideo', verbose_name='video optional', blank=True)
    slug = models.SlugField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_slug(self):
        slug = self.title
        return slugify(slug)
        

# def slug_generator(sender, instance, *args, **kwargs):
#         if not instance.slug:
#             instance.slug = unique_slug_generator(instance)

# pre_save.connect(slug_generator, sender=remmyBlog)            
        



class subscribe(models.Model):
    email = models.EmailField(max_length=70,blank=False)

    def __str__(self):
        return self.email
    
    


class ProductVideo(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='product_video/', blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    product = models.ForeignKey('AgricultureImplement', on_delete=models.CASCADE, related_name='video_benefits')
    created_by = models.ForeignKey('registration.Profile', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    
    