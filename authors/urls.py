from django.urls import path
from . views import AuthorListView,AuthorCreateView, AuthorUpdateView, AuthorDeleteView

urlpatterns = [
    path('', AuthorListView.as_view()),
    path('create/', AuthorCreateView.as_view(), name='create'),
    path('update/<int:pk>/', AuthorUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', AuthorDeleteView.as_view(), name='delete'),
]
