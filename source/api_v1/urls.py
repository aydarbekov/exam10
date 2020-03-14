from django.urls import path, include

# from api_v1.views import AreaListAPIView, AddAreaFromListView, ExpertListAPIView, GetCommitteeDetails, \
#     RemoveAreaFromCommitteeView, AddIHEToCommitteeView, AddExpertFromListView, RemoveExpertFromCommitteeView

app_name = 'api_v1'


urlpatterns=[
    # path('committee/<int:pk>/', GetCommitteeDetails.as_view(), name='get_committee'),
    # path('committee/<int:pk>/ihe/add', AddIHEToCommitteeView.as_view(), name='add_ihe_to_committee'),
    # path('committee/<int:pk>/areas/', AreaListAPIView.as_view(), name='list_areas'),
    # path('committee/areas/add', AddAreaFromListView.as_view(), name='add_area_from_list'),
    # path('committee/areas/remove/<int:pk>', RemoveAreaFromCommitteeView.as_view(), name='remove_area_from_committee'),
    # path('committee/<int:pk>/experts/list/', ExpertListAPIView.as_view(), name='list_experts'),
    # path('committee/<int:pk>/experts/add', AddExpertFromListView.as_view(), name='add_expert_from_list'),
    # path('committee/<int:pk>/experts/remove', RemoveExpertFromCommitteeView.as_view(), name='remove_expert_from_committee')
]