from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import forms
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe


# Displays user with contact us form to enter information
def contact(request):
    if request.method == 'GET':
        form = forms.ContactForm()
    else:
        # Once user has sent form, data is then cleaned for security purposes
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # If successful, contact us form is sent to admin email
            try:
                send_mail(subject, message, email, ['n.dawson3@newcastle.ac.uk'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('support:success')
    return render(request, "email.html", {'form': form})


def success(request):
    return render(request, "success.html")


def donate(request):
    return render(request, "donate.html")


# View to handle XHR request for Stripe donations
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


# Event handler to button's click event.
@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            # Create new Checkout Session for the order, redirecting user to appropriate page
            # if donation is successful or not
            checkout_session = stripe.checkout.Session.create(
                success_url='https://127.0.0.1:8000/' + 'support/d_success',
                cancel_url='https://127.0.0.1:8000/' + 'support/d_cancelled',
                payment_method_types=['card'],
                mode='payment',
                # Donation item information to be displayed to user
                line_items=[
                    {
                        'name': 'Plant a tree',
                        'quantity': 1,
                        'currency': 'gbp',
                        'amount': '500',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})


def d_success(request):
    return render(request, "d_success.html")


def d_cancelled(request):
    return render(request, "d_cancelled.html")
