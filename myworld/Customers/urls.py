from django.urls import include, path
from rest_framework import routers
from . import views
customerRouter = routers.SimpleRouter()
productRouter = routers.SimpleRouter()
customerRouter.register(r'Customer', views.CustomerViewSet)
productRouter.register(r'Products', views.ProductsViewSet)
urlpatterns = [
    path('', include(customerRouter.urls)),
    path('', include(productRouter.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]