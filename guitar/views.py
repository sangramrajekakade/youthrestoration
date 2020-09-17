from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView,CreateView
from .models import *
from .forms import *
from django.views import generic
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
# from django.urls import reverse_lazy

# Create your views here.
class HomePage(TemplateView):
    template_name = 'guitar/homepage.html'
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['offers'] = Offers.objects.all()
        return context


    
    # def get_context_data(self, **kwargs):
    #     context = super(HomePage, self).get_context_data(**kwargs)
    #     context['guitar'] = AboutGuitar.objects.all()
    #     return context


class VideosPage(TemplateView):
    template_name = 'guitar/videos.html'

    def get_context_data(self, **kwargs):
        context = super(VideosPage, self).get_context_data(**kwargs)
        context['videos'] = YoutubeVideos.objects.all()
        return context

class transplantdetails(ListView):
    template_name = 'guitar/abtguitar.html'
    model = AboutGuitar

    def get_context_data(self, **kwargs):
        context = super(transplantdetails, self).get_context_data(**kwargs)
        context['guitar'] = AboutGuitar.objects.all()
        return context


class Detail_Guitar(DetailView):
    model = AboutGuitar
    #template_name = 'guitar/aboutguitar_detail.html'



class Admission(TemplateView):
    template_name = 'guitar/admission.html'



class BatchesPage(ListView):
    template_name = 'guitar/batches.html'
    model = Batches
    def get_context_data(self, **kwargs):
        context = super(BatchesPage, self).get_context_data(**kwargs)
        context['Batches'] = Batches.objects.all()
        return context



# class Appointment(TemplateView):

#     template_name = 'guitar/contact.html'





class Appointment(CreateView):
    model = Appointment
    form_class = AppointmentForm
    template_name = 'guitar/contact.html'
    # def get_success_url(self):
        # return reverse_lazy('Appointment')

    def form_valid(self,ExpensesForm):
        print("saved")

        ExpensesForm.save()
        sendemail(ExpensesForm)
        return HttpResponseRedirect("/Appointment/")
    def form_invalid(self, ExpensesForm):
        print("failed")
        return self.render_to_response(self.get_context_data(form=AppointmentForm))

from django.core.mail import EmailMessage

from django.template.loader import render_to_string

from django.core.mail import EmailMultiAlternatives

def sendemail(ExpensesForm):
    print("s")
    First_name = ExpensesForm.instance.F_Name
    Last_Name = ExpensesForm.instance.L_Name
    Mobile = ExpensesForm.instance.Mobile
    email = ExpensesForm.instance.Email
    message = ExpensesForm.instance.message
    domain = "http://127.0.0.1:8000/"
    print(message)
    # message_admin = "hiiiiiiiiiiiii"+First_name
    # message_client = 'get well'
    # mail_subject = 'Activate your blog account.'
    # email = EmailMessage(mail_subject, message_admin,to=[email,'message_admin'])
    # email.send()
    
    # html_content = '<p>This is an <strong>important</strong> message.</p>'
    message_admin = render_to_string('guitar/email_tempalte_admin.html',{ "name":First_name,"Last_Name":Last_Name,"Mobile":Mobile,"email":email,"message":message})
    msg = EmailMultiAlternatives("New inquiry", "Details of new inquiry", "youth.restoration.demo@gmail.com",["youthrestoration3@gmail.com"])
    msg.attach_alternative(message_admin, "text/html")
    msg.send()


    subject, from_email, to = 'hello', 'youth.restoration.demo@gmail.com', email
    text_content = 'This is an important message.'
    # html_content = '<p>This is an <strong>important</strong> message.</p>'
    message_user = render_to_string('guitar/email_tempalte_user.html',{"name":First_name, })
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(message_user, "text/html")
    msg.send()






















class AboutPage(TemplateView):
    template_name = 'guitar/aboutus.html'


class feestructurePage(ListView):
    model = Feestructure
    template_name = 'guitar/feestructure.html'

    def get_context_data(self, **kwargs):
        context = super(feestructurePage, self).get_context_data(**kwargs)
        context['Feestructure'] = Feestructure.objects.all()
        return context


class BuyguitarPage(ListView):
    template_name = 'guitar/buyguitar.html'
    model = Buyguitar

    def get_context_data(self, **kwargs):
        context = super(BuyguitarPage, self).get_context_data(**kwargs)
        context['buyguitar'] = Buyguitar.objects.all()
        return context


class Buyguitar_details(DetailView):
    model = Buyguitar
    #template_name = 'guitar/aboutguitar_detail.html'


class PostPage(TemplateView):
    template_name = 'guitar/post.html'

    def get_context_data(self, **kwargs):
        context = super(PostPage, self).get_context_data(**kwargs)
        context['post'] = Post.objects.all()
        return context


class Post_details(DetailView):
    model = Post
    #template_name = 'guitar/aboutguitar_detail.html'

class email_tamplate(TemplateView):
    template_name = 'guitar/email_tempalte_user.html'



# class offers(ListView):
#     template_name = 'guitar/Offers.html'
#     model = Offers

#     def get_context_data(self, **kwargs):
#         context = super(transplantdetails, self).get_context_data(**kwargs)
#         context['guitar'] = AboutGuitar.objects.all()
#         return context




class Services(TemplateView):
    template_name = 'guitar/Services.html'
