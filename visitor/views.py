from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
import hashlib

@csrf_exempt
def notify_visit(request):
    if request.method == "POST":
        visitor_ip = request.META.get('REMOTE_ADDR', 'Unknown IP')
        user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown device')

        # Combine IP + device to create a unique visitor key
        unique_visitor_key = hashlib.md5(f"{visitor_ip}_{user_agent}".encode()).hexdigest()

        # Check if visitor already notified recently (e.g. within 12 hours)
        if cache.get(unique_visitor_key):
            print(f"Duplicate visit detected: {visitor_ip}")
            return JsonResponse({"message": "Already notified recently"}, status=200)

        # Save in cache for 12 hours (43200 seconds)
        cache.set(unique_visitor_key, True, timeout=43200)

        # Send email
        send_mail(
            subject="🚀 New Unique Visitor on Your Portfolio",
            message=f"""
A new visitor just accessed your website!

📍 IP Address: {visitor_ip}
💻 Device/Browser: {user_agent}
⏰ Time: {request.META.get('DATE', 'Now')}
""",
            from_email=None,
            recipient_list=['yourgmail@gmail.com'],
            fail_silently=False,
        )

        print(f"Notification sent for visitor: {visitor_ip}")
        return JsonResponse({"message": "Email sent successfully"})

    return JsonResponse({"error": "Invalid request"}, status=400)

