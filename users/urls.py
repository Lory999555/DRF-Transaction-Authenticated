from django.urls import path
from .views import CreateUserView, ListUsersView, DeleteUserView, CustomTokenObtainPairView, UserDetailView

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='user-create'),
    path('list/', ListUsersView.as_view(), name='user-list'),
    path('delete/<int:pk>/', DeleteUserView.as_view(), name='user-delete'),
    path('token/', CustomTokenObtainPairView.as_view(), name='api-token-auth'),
     path('me/', UserDetailView.as_view(), name='user-detail'),
]
