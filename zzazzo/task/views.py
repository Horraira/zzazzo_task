from django.views.generic import ListView, CreateView
from .forms import *
from .models import User
from django.shortcuts import redirect, reverse, render


class TaskListView(ListView):
    model = Payment
    template_name = 'report/user_input.html'
    context_object_name = 'payment'


class PurchaseDetailsAddView(CreateView):
    template_name = 'report/input_form.html'
    form_class = UserForm
    purchase_form_class = PurchaseForm
    payment_form_class = PaymentForm
    success_url = '/report/'

    def post(self,
             request,
             *args,
             **kwargs):
        form = self.form_class(request.POST, request.FILES)
        purchase_form = self.purchase_form_class(request.POST, prefix='purchase_form')
        payment_form = self.payment_form_class(request.POST, prefix='payment_form')

        if form.is_valid() and purchase_form.is_valid():
            userInstance = form.save()
            purchase = purchase_form.save(commit=False)
            payment = payment_form.save(commit=False)
            purchase.user = userInstance
            payment.user = userInstance
            purchase.save()
            payment.purchase = purchase
            payment.save()
            return redirect('/report/')

        if not purchase_form.is_valid():
            print("purchase_form")
            print(purchase_form.errors.as_data())
            return render(request, self.template_name)

        if not payment_form.is_valid():
            print("payment_form")
            print(purchase_form.errors.as_data())
            return render(request, self.template_name)

    def get(self,
            request,
            *args,
            **kwargs):
        form = self.form_class(**self.get_form_kwargs())
        purchase_form = self.purchase_form_class(prefix='purchase_form')
        payment_form = self.payment_form_class(prefix='payment_form')
        return render(request, self.template_name, {'form': form,
                                                    'purchase_form': purchase_form,
                                                    'payment_form': payment_form})
