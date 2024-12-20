
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryListCreateView, CategoryViewSet, ProductViewSet, OrderViewSet, ReviewViewSet, ProductListCreateView, ProductDetailView
from . import views

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]

