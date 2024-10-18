"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# myproject/urls.py
from django.http import HttpResponse
from django.urls import path

def kubernetes_page(request):
    html_content = """
    <html>
    <head>
        <title>Kubernetes and Ingress</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
            }
            h1 {
                font-size: 48px;  /* Large font size */
                font-weight: bold; /* Bold text */
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h1>Implementing Kubernetes and Ingress</h1>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('', kubernetes_page),  # Set this to the homepage
]


