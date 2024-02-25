from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.utils.decorators import method_decorator
from .models import Car, Order

@method_decorator(login_required, name='dispatch')
class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object 
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    
@login_required
def buy_now(request, car_id):
    car = Car.objects.get(pk=car_id)
    existing_order = Order.objects.filter(user=request.user, car=car).first()

    if existing_order:
        existing_order.quantity += 1
        existing_order.save()
    else:
        Order.objects.create(user=request.user, car=car)
    car.quantity -= 1
    car.save()
    return redirect('profile')