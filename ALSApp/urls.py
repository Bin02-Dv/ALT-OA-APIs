from django.urls import path
from .views import SignUpView, LoginView, UserView, LogoutView, AllUserView, CourseView, AllCoursesView

urlpatterns = [
    # Authentication
    path('user/signup', SignUpView.as_view()),
    path('user/login', LoginView.as_view()),
    path('user/logout', LogoutView.as_view()),
    path('user/', UserView.as_view()),
    path('', AllUserView.as_view()),

    # Course Upload

    path('user/course/upload', CourseView.as_view()),
    path('user/course', AllCoursesView.as_view()),
]