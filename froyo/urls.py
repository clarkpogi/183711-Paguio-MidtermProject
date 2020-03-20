"""thegoodplace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from .views import IngredientsCreateFormView, IngredientsDetailView, IngredientsListView, IngredientsUpdateFormView, OrdersCreateFormView, OrdersDetailView, OrdersListView

urlpatterns = [
    url(r'^ingredients_create_form$',IngredientsCreateFormView.as_view(),name='ICF'),
    url(r'^ingredients_detail$',IngredientsDetailView.as_view(),name='ID'),
    url(r'^ingredients_list$', IngredientsListView.as_view(), name='IL'),
    url(r'^ingredients_update_form$',IngredientsUpdateFormView.as_view(),name='IUF'),
    url(r'^orders_create_form$',OrdersCreateFormView.as_view(),name='OCF'),
    url(r'^orders_detail$',OrdersDetailView.as_view(),name='OD'),
    url(r'^orders_list$',OrdersListView.as_view(),name='OL'),
    
]
