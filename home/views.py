# from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
import sendgrid
from sendgrid import SendGridAPIClient
import os
from .serializers import *
from rest_framework.response import Response
from rest_framework import viewsets



# Create your views here.

class HomeBannerapi(viewsets.ModelViewSet):
    queryset=HomeBanner.objects.all()
    serializer_class=HomeBanner_seri


class HomePageFirstContentapi(viewsets.ModelViewSet):
    queryset=HomePageFirstContent.objects.all()
    serializer_class=HomePageFirstContent_seri

class HomePageSecondContentapi(viewsets.ModelViewSet):
    queryset=HomePageSecondContent.objects.all()
    serializer_class=HomePageFirstContent_seri

class AboutBannerapi(viewsets.ModelViewSet):
    queryset=AboutBanner.objects.all()
    serializer_class=AboutBanner_seri

class AboutPageFirstContentapi(viewsets.ModelViewSet):
    queryset=AboutPageFirstContent.objects.all()
    serializer_class=AboutPageFirstContent_seri

class AboutPageSecondContentapi(viewsets.ModelViewSet):
    queryset=AboutPageSecondContent.objects.all()
    serializer_class=AboutPageSecondContent_seri



class AboutPageThirdContentapi(viewsets.ModelViewSet):
    queryset=AboutPageThirdContent.objects.all()
    serializer_class=AboutPageThirdContent_seri

class AboutPageFourthContentapi(viewsets.ModelViewSet):
    queryset=AboutPageFourthContent.objects.all()
    serializer_class=AboutPageFourthContent_seri

class ContactBannerapi(viewsets.ModelViewSet):
    queryset=ContactBanner.objects.all()
    serializer_class=ContactBanner_seri

class ContactPageapi(viewsets.ModelViewSet):
    queryset=ContactPage.objects.all()
    serializer_class=ContactPage_seri

class socialmediaapi(viewsets.ModelViewSet):
    queryset=socialmedia.objects.all()
    serializer_class=socialmedia_seri

class ebooksapi(viewsets.ModelViewSet):
    queryset=ebooks.objects.all()
    serializer_class=ebooks_seri

class catalougeapi(viewsets.ModelViewSet):
    queryset=catalouge.objects.all()
    serializer_class=catalouge_seri

class Contactusapi(viewsets.ModelViewSet):
    queryset=Contactus.objects.all()
    serializer_class=contactus_seri


def landing(request):
    banner = HomeBanner.objects.all()
    first = HomePageFirstContent.objects.all()
    second = HomePageSecondContent.objects.all()
    cat = catalouge.objects.all()
    ebk = ebooks.objects.all()

    form = contactUsForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data


        name = form.cleaned_data.get('name')
        print(name,'name')

        email = form.cleaned_data.get('email')
        print(email,'emaaillllllllllll')
        phone = form.cleaned_data['phone']
        print(phone,'phoneeeeeeeeeeeeeeeeeeeeeeee')
        message_1 = form.cleaned_data['message']
        print(message_1,'messsssssssssssssssssss oneeeeeeeeeeeeeeeeeeeee')
        print("yes im hereeeeeeeeeeeeeeeeeee")

        # form.save()



    context={'banner':banner,
             'first':first,
             'second':second,
             'cat':cat,
             'ebk':ebk,
    }
    return render(request, 'landing.html' ,context)

def landing1(request):
    form = contactUsForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data


        name = form.cleaned_data.get('name')

        email = form.cleaned_data.get('email')
        phone = form.cleaned_data['phone']
        # message_1 = form.cleaned_data['message']

        form.save()


        # to me
        sg = sendgrid.SendGridClient('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')
        email_to = email

        message = sendgrid.Mail()
        message.add_to([email_to])
        message.set_subject(name+" - "+str(phone))

        message.add_substitution('-name-',name)
        message.set_html(' ')
        message.set_text(' ')
        message.set_from('atul.dev@dreambox.cloud')
        message.add_filter('templates', 'enable', 1)
        message.add_filter('templates', 'template_id', 'b17ee040-cd7a-48d2-a2a2-464307e66613')
        # message.add_attachment(file_= abcd, name="Invoice.pdf")
        status, msg = sg.send(message)
        print(status)
        print(msg)



        # tomeeeeeeeeeeee
        sg1 = sendgrid.SendGridClient('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')
        email_to2 = "kum.atul96@gmail.com"
        message_2 = sendgrid.Mail()
        message_2.add_to([email_to2])
        message_2.set_subject(name+" - "+str(phone))


        message_2.add_substitution('-name-',name)
        message_2.add_substitution('-email-', email)
        message_2.add_substitution('-phone-',phone)
        message_2.set_html(' ')
        message_2.set_text(' ')


        # message_2.set_text('I have a query')
        message_2.set_from('atul.dev@dreambox.cloud')
        message_2.add_filter('templates', 'enable', 1)
        message_2.add_filter('templates', 'template_id', '411274eb-8055-47a7-8e2d-e1c96d3d0a36')
        # message.add_attachment(file_= abcd, name="Invoice.pdf")
        status1, msg1 = sg1.send(message_2)
        print(status1)
        print(msg1)
    context={}
    return render(request, 'landing1.html' ,context)


def landing2(request):
    form = contactUsForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data


        name = form.cleaned_data.get('name')

        email = form.cleaned_data.get('email')
        phone = form.cleaned_data['phone']
        # message_1 = form.cleaned_data['message']

        form.save()


        # to me
        sg = sendgrid.SendGridClient('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')
        email_to = email

        message = sendgrid.Mail()
        message.add_to([email_to])
        message.set_subject(name+" - "+str(phone))

        message.add_substitution('-name-',name)
        message.set_html(' ')
        message.set_text(' ')
        message.set_from('atul.dev@dreambox.cloud')
        message.add_filter('templates', 'enable', 1)
        message.add_filter('templates', 'template_id', 'b17ee040-cd7a-48d2-a2a2-464307e66613')
        # message.add_attachment(file_= abcd, name="Invoice.pdf")
        status, msg = sg.send(message)
        print(status)
        print(msg)



        # tomeeeeeeeeeeee
        sg1 = sendgrid.SendGridClient('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')
        email_to2 = "kum.atul96@gmail.com"
        message_2 = sendgrid.Mail()
        message_2.add_to([email_to2])
        message_2.set_subject(name+" - "+str(phone))


        message_2.add_substitution('-name-',name)
        message_2.add_substitution('-email-', email)
        message_2.add_substitution('-phone-',phone)
        message_2.set_html(' ')
        message_2.set_text(' ')


        # message_2.set_text('I have a query')
        message_2.set_from('atul.dev@dreambox.cloud')
        message_2.add_filter('templates', 'enable', 1)
        message_2.add_filter('templates', 'template_id', '411274eb-8055-47a7-8e2d-e1c96d3d0a36')
        # message.add_attachment(file_= abcd, name="Invoice.pdf")
        status1, msg1 = sg1.send(message_2)
        print(status1)
        print(msg1)
    context={}
    return render(request, 'landing2.html' ,context)


def aboutus(request):
    banner = AboutBanner.objects.all()
    first = AboutPageFirstContent.objects.all()
    second = AboutPageSecondContent.objects.all()
    third = AboutPageThirdContent.objects.all()
    fourth = AboutPageFourthContent.objects.all()
    social = socialmedia.objects.all()
    cat = catalouge.objects.all()
    ebk = ebooks.objects.all()
    context={'banner':banner,
             'first':first,
             'third':third,
             'fourth':fourth,
             'social':social,
             'cat':cat,
             'ebk':ebk,
    }
    return render(request, 'about-us.html' ,context)


def contactus(request):
    banner = ContactBanner.objects.all()
    cont = ContactPage.objects.all()
    cat = catalouge.objects.all()
    ebk = ebooks.objects.all()

    form = contactUsForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data


        name = form.cleaned_data.get('name')

        email = form.cleaned_data.get('email')
        phone = form.cleaned_data['phone']
        # message_1 = form.cleaned_data['message']

        form.save()


        # to me
        sg = sendgrid.SendGridClient('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')
        email_to = email

        message = sendgrid.Mail()
        message.add_to([email_to])
        message.set_subject(name+" - "+str(phone))

        message.add_substitution('-name-',name)
        message.set_html(' ')
        message.set_text(' ')
        message.set_from('atul.dev@dreambox.cloud')
        message.add_filter('templates', 'enable', 1)
        message.add_filter('templates', 'template_id', 'b17ee040-cd7a-48d2-a2a2-464307e66613')
        # message.add_attachment(file_= abcd, name="Invoice.pdf")
        status, msg = sg.send(message)
        print(status)
        print(msg)



        # tomeeeeeeeeeeee
        sg1 = sendgrid.SendGridClient('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')
        email_to2 = "kum.atul96@gmail.com"
        message_2 = sendgrid.Mail()
        message_2.add_to([email_to2])
        message_2.set_subject(name+" - "+str(phone))


        message_2.add_substitution('-name-',name)
        message_2.add_substitution('-email-', email)
        message_2.add_substitution('-phone-',phone)
        message_2.set_html(' ')
        message_2.set_text(' ')


        # message_2.set_text('I have a query')
        message_2.set_from('atul.dev@dreambox.cloud')
        message_2.add_filter('templates', 'enable', 1)
        message_2.add_filter('templates', 'template_id', '411274eb-8055-47a7-8e2d-e1c96d3d0a36')
        # message.add_attachment(file_= abcd, name="Invoice.pdf")
        status1, msg1 = sg1.send(message_2)
        print(status1)
        print(msg1)
    context={'banner':banner,
    'cont':cont,
    'cat':cat,
    'ebk':ebk,}
    return render(request, 'contact-us.html' ,context)


def category(request):
    context={}
    return render(request, 'category.html' ,context)

def product(request):
    context={}
    return render(request, 'product.html' ,context)
