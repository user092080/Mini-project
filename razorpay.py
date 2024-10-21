
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import razorpay
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse

# Initialize Razorpay client
razorpay_client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def initiate_payment(request):
    if request.method == 'POST':
        order_amount = 50000  # Amount in paise (50000 = ₹500.00)
        order_currency = 'INR'
        order_receipt = 'order_rcptid_11'

        # Razorpay order creation
        razorpay_order = razorpay_client.order.create({
            "amount": order_amount,
            "currency": order_currency,
            "receipt": order_receipt,
            "payment_capture": "1"
        })

        # Pass the order details and your Key ID to the HTML template
        context = {
            'razorpay_order_id': razorpay_order['id'],
            'razorpay_key': settings.RAZORPAY_KEY_ID,
            'amount': order_amount,  # in paise
            'currency': order_currency,
        }
        return render(request, 'main/razorpay_checkout.html', context)

    return render(request, 'main/razorpay_form.html')  # A page to initiate the payment


@csrf_exempt
def razorpay_callback(request):
    if request.method == 'POST':
        razorpay_payment_id = request.POST.get('razorpay_payment_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')

        # Verify the payment signature (optional, but recommended)
        params_dict = {
            'razorpay_order_id': razorpay_order_id,
            'razorpay_payment_id': razorpay_payment_id,
        }

        try:
            # Here you can add the verification logic if needed
            # For now, let's just assume it's verified

            # Fetch the order using the order_id
            order = Orders.objects.filter(order_id=razorpay_order_id).first()
            if order:
                # Update the order status and payment details
                order.payment_id = razorpay_payment_id  # Store payment ID if needed
                order.status = 'Completed'  # Update order status
                order.save()

                messages.success(request, 'Payment was successful! Your order has been placed.')
                return redirect(reverse('myorders'))  # Redirect to myorders page
            else:
                messages.error(request, 'Order not found.')
                return redirect(reverse('myorders'))  # Redirect to myorders page

        except Exception as e:
            messages.error(request, f'Payment verification failed: {str(e)}')
            return redirect(reverse('myorders'))  # Redirect to myorders page

    return JsonResponse({"status": "Invalid request!"})
