from django.urls import path
from .import views
urlpatterns = [
    path('',views.HomePage,name='homepage'),
    path('portfoli_single/<int:id>',views.PortfolioSingleView,name='singleportfolio')
]
