from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register('inquiry', views.InquiryViewSet)
router.register('inquiry/(<id>)/questions', views.QuestionViewSet, basename='questions')
router.register('inquiry/(<id>)/questions/(<question_pk>)/choices', views.ChoiceViewSet, basename='choices')
router.register('active_inquiry', views.ActiveInquiryListViewSet)
router.register('inquiry/(<id>)/questions/(<question_pk>)/answers', views.AnswerCreateViewSet, basename='answers')
router.register('my_inquiry', views.UserIdInquiryListViewSet, basename='list_userid_inquiry')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
