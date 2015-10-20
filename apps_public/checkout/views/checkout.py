# coding: utf-8

from django import forms
from django.core.validators import ValidationError
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from django.shortcuts import render_to_response
from formtools.wizard.views import SessionWizardView, NamedUrlSessionWizardView

from accounts.models import User
from apps_customerdata.customer.models.order import Order
from apps_productdata.mentoki_product.models.courseproduct import CourseProduct


from django import forms


class CheckoutForm1(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email',)

    def clean(self):
        """
        If somebody enters into this form ' hello ',
        the extra whitespace will be stripped.
        """
        # check wether user exists already
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
            raise ValidationError('Du bist schon bei Mentoki registriert. '
                                  'Bitte melde Dich an, bevor Du den Kurs buchst.')
        except ObjectDoesNotExist:
            pass

        # check wether user ordered this product already
        #courseproduct = get_object_or_404(C)
        try:
            #Order.objects.get(courseproduct=courseproduct)
            raise ValidationError('Du bist schon bei Mentoki registriert. '
                                  'Bitte melde Dich an, bevor Du den Kurs buchst.')
        except ObjectDoesNotExist:
            pass


        return self.cleaned_data


class CheckoutForm2(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class CheckoutForm3(forms.Form):
    message = forms.CharField(widget=forms.Textarea)


TEMPLATES = {"checkout1": "checkout/participant.html",
             "checkout2": "checkout/payment.html"}
FORMS = [("checkout1", CheckoutForm1),
         ("checkout2", CheckoutForm2)]

class CheckoutWizard(SessionWizardView):
    def get_template_names(self):
            return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        return render_to_response('done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })

    def get_context_data(self, **kwargs):
        context = super(CheckoutWizard, self).get_context_data(**kwargs)

        context['greeting'] = "Hallo"
        return context
