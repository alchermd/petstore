from django.contrib import messages


def logout_message(sender, user, request, **kwargs):
    messages.error(request, "You have been logged out.")


def login_message(sender, user, request, **kwargs):
    messages.success(request, "You are now logged in.")
