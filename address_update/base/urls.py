"""address_update URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from .views import auth, dashboard
urlpatterns = [
    path('login',auth.login,name='login'),
    path('register',auth.register,name='register')
    path('/api/aadhar-user/dashboard/home',dashboard.landlord_dashboard,name='landlord_dashboard')
    path('/api/aadhar-user/dashboard/request_details',dashboard.landlord_request_details,name='landlord_request_details')
    path('/api/aadhar-user/dashboard/handle_request_consent',dashboard.handle_request_after_consent,name='handle_request'),
    # path('user/dashboard/home',dashboard.dashboardhome,name='dashboardhome')
]