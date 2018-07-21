import paypalrestsdk

from django.conf import settings
from django.shortcuts import redirect

def paypal_create(request, name, price, quantity, total):

    print('????????????????????????????')
    print(name)
    print(price)
    print(quantity)
    print(total)
    print(request.build_absolute_uri('/paypal/execute/'))
    print('**********estamso en el metodo de pago')
    paypalrestsdk.configure({
        'mode': settings.PAYPAL_MODE, #sandbox or live
        'client_id': settings.PAYPAL_CLIENT_ID,
        'client_secret': settings.PAYPAL_CLIENT_SECRET,
    })

    # Create payment object
    payment = paypalrestsdk.Payment({
        "intent": "sale",

        # Set payment method
        "payer": {
            "payment_method": "paypal"
        },

        # Set redirect urls
        "redirect_urls": {
            "return_url": request.build_absolute_uri('/paypal/payment/execute/'),
            "cancel_url": request.build_absolute_uri('/')
        },

        # Set transaction object
        "transactions": [{
            "item_list": {
                "items": [
                    {
                        "name": name.upper(),
                        "price": str(price),
                        "currency": "USD",
                        "quantity": quantity
                    }
                ]
            },
            "amount": {
                "total": str(total),
                "currency": "USD"
            },
            "description": "Pago por servicio turistico"
        }]
    })
    print(payment)
    if payment.create():
        # Alamacenamos payment_id en una sesion de usario
        print("Payment[%s] created successfully" % (payment.id))
        request.session['payment_id'] = payment.id
        # redirect the user to given approval url 
        for link in payment.links:
            if link.method == "REDIRECT":
                redirect_url = link.href
        return redirect_url
    else:
        print("Error while creating payment:")
        print(payment.error)
        return redirect('/error/')

def paypal_execute(request):
    payment_id = request.session.get('payment_id')
    payer_id = request.GET['PayerID']



    paypalrestsdk.configure({
        'mode': settings.PAYPAL_MODE, #sandbox or live
        'client_id': settings.PAYPAL_CLIENT_ID,
        'client_secret': settings.PAYPAL_CLIENT_SECRET,
    })

    payment = paypalrestsdk.Payment.find(payment_id)
    payment_name = payment.transactions[0].item_list.items[0].name

    print(payment)
    print(payment_name)

    if payment.execute({'payer_id': payer_id}):
        print("Payment[%s] execute successfully" % (payment.id))
        # el pago ya se concreto
        pass
    return redirect('/felicitaciones/')
