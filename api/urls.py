from django.urls import path
from . import views as v
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from rest_framework.routers import DefaultRouter,SimpleRouter

router=DefaultRouter()
router.register('stdentdetails',v.studentViewSet,basename='student')

urlpatterns = [
    path('stuinfo/<int:pk>',v.student_data),
    path('studetails/<str:pk>/',v.student_details.as_view()),
    path('mixinList/',v.ListMixinStudent.as_view()),
    path('studentDetails/<int:pk>/',v.DetailedProductMixin.as_view()),
    path('generic/',v.student_generic.as_view()),
    path('generic_D/<int:pk>/',v.generic_delete.as_view()),
    
   
 
]+router.urls
