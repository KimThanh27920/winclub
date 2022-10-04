from django.urls import path
from .views import (CategoriesAPIView,
                     TypeGuestAPIView,
                     StyleGuestAPIView,
                      GrapeGuestAPIView,
                      FoodGuestAPIView,
                       RegionGuestAPIView,
                        CountryGuestAPIView)


urlpatterns = [
    path('', CategoriesAPIView.as_view(), name="categories-guest-view"),
    path("types/", TypeGuestAPIView.as_view(),name="types_guest"),
    path("styles/", StyleGuestAPIView.as_view(),name="styles_guest" ),
    path("grapes/",GrapeGuestAPIView.as_view(),name="grapes_guest" ),
    path("foods/",FoodGuestAPIView.as_view(),name="foods_guest" ),
    path("region/", RegionGuestAPIView.as_view(),name="region_guest"),
    path("countries/", CountryGuestAPIView.as_view(),name="countries_guest" ),
]
