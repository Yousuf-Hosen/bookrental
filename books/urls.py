from django.urls import path
from .views import (Book_Title_List_View,
                    BookTitleDetailView,
                    BookDetailView,
                    BookDeleteView
)

app_name='books'
# urls 'app_name:name'  in this case {% urls 'books:detail' %}
urlpatterns = [
    path('',Book_Title_List_View.as_view(),{'letter' : None},name='main'),
    path('<str:letter>/',Book_Title_List_View.as_view(),name='main'),
    path('<str:letter>/<slug>/',BookTitleDetailView.as_view(),name='detail'),
    path('<str:letter>/<slug>/<str:book_id>/',BookDetailView.as_view(),name='detail-book'),
    path('<str:letter>/<slug>/<str:book_id>/delete/',BookDeleteView.as_view(),name='delete-book'),
    
    # path('<str:slug>/',book_title_detail_view),
]


