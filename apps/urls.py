from django.urls import path

from apps.views import UserProfileUpdateView, CustomLoginView, RegisterView, users_list, UserDeleteView

urlpatterns = [
    path('update/', UserProfileUpdateView.as_view(), name='update'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('delete/', UserDeleteView.as_view(), name='delete'),
    path('', users_list, name='users_list'),

    ]