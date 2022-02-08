from django.urls import path

from . import views

app_name = 'after'
urlpatterns = [
    path("after_index/", views.After_indexViews.as_view(), name="after_index"),
    path("after_mypage/", views.After_MypageViews.as_view(), name="after_mypage"),
    path("after_inquiry/", views.After_InquiryView.as_view(), name="after_inquiry")
]