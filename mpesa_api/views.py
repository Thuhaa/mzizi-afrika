from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import requests
from requests.auth import HTTPBasicAuth
import json
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword
from django.views.decorators.csrf import csrf_exempt
from .models import MpesaPayment
from cart.cart import Cart
from shop.models import Order, CurrentBuyer
import random
from django.contrib import messages
import os

def getAccessToken(request):
    consumer_key = os.environ['MPESA_CONSUMER_KEY']
    consumer_secret = os.environ['MPESA_CONSUMER_SECRET']
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)



def lipa_na_mpesa_online(request):

    cart = Cart(request)

    items_in_cart = []
    for bag in cart:
        items_in_cart.append(bag['bag'])
        print(bag['bag'])
    number_of_items_in_cart = len(items_in_cart)

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        city = request.POST.get('city')
        bags_ordered = items_in_cart
        transaction_id = random.randint(1111111111,9999999999)
        total_amount = cart.get_total_price()

        order = Order.objects.create(first_name=first_name, last_name=last_name,
            phone = phone_number, city=city, transaction_id=transaction_id, 
            bags_ordered=bags_ordered, total_amount=total_amount)

        order.save()

        messages.success(request, ('Order has been placed successfully. We will confirm your payment and deliver in a few hours'))

    total = cart.get_total_price()
    price = int(total)
    current_buyer = CurrentBuyer.objects.all()
    pay_to = order.phone
    print(pay_to)
    
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": "Bearer %s" % access_token}
    request = {
        "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
        "Password": LipanaMpesaPpassword.decode_password,
        "Timestamp": LipanaMpesaPpassword.lipa_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": price, # replace with the total amount including the shipping costs
        "PartyA": 254792127575,#pay_to,  # replace with your phone number to get stk push
        "PartyB": LipanaMpesaPpassword.Business_short_code,
        "PhoneNumber": 254792127575,#pay_to,  # replace with your phone number to get stk push
        "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
        "AccountReference": "Mzizi Afrika",
        "TransactionDesc": "Testing stk push"
    }
    cart.clear()
    response = requests.post(api_url, json=request, headers=headers)
    return HttpResponseRedirect('/')




@csrf_exempt
def register_urls(request):
    access_token = MpesaAccessToken.validated_mpesa_access_token
    api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": LipanaMpesaPpassword.Test_c2b_shortcode,
               "ResponseType": "Completed",
               "ConfirmationURL": "https://fdd8a2893ba4.ngrok.io//api/v1/c2b/confirmation",
               "ValidationURL": "https://fdd8a2893ba4.ngrok.io//api/v1/c2b/validation"}
    response = requests.post(api_url, json=options, headers=headers)
    return HttpResponse(response.text)
@csrf_exempt
def call_back(request):
    pass
@csrf_exempt
def validation(request):
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))
@csrf_exempt
def confirmation(request):
    mpesa_body =request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    payment = MpesaPayment(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['LastName'],
        middle_name=mpesa_payment['MiddleName'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        amount=mpesa_payment['TransAmount'],
        reference=mpesa_payment['BillRefNumber'],
        organization_balance=mpesa_payment['OrgAccountBalance'],
        type=mpesa_payment['TransactionType'],
    )
    payment.save()
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))