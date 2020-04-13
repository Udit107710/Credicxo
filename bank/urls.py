from django.conf.urls import url, re_path
from django.urls import path
from .views import BranchDetails, AllBranches

urlpatterns = [
    path('detail/<str:ifsc>', BranchDetails.as_view(), name="ifsc-details"),
    path('branches/<str:name>/<str:city>', AllBranches.as_view(), name="city-branches"),
]