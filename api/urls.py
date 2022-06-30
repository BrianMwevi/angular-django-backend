from api.views import BusinessViewset
from rest_framework.routers import DefaultRouter


routes = DefaultRouter()

routes.register('businesses', BusinessViewset, basename='businesss')

urlpatterns = [

]
urlpatterns+=routes.urls