from django.http import HttpResponse

def add_cors_headers(view_func):
    def wrapper(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)
        response['Access-Control-Allow-Origin'] = 'https://alphatech-school.vercel.app'  # Replace with your frontend domain
        response['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
        response['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
        return response
    return wrapper
