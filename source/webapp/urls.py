from django.urls import path

from webapp.views import IndexView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('committee/create/', CommitteeCreateView.as_view(), name='committee_create'),
    # path('university/', UniversityIndexView.as_view(), name='university'),
    # path('university/add/', UniversityCreateView.as_view(), name='university_create'),
    # path('university/<int:pk>/delete/', UniversityDeleteView.as_view(), name='university_delete'),
    # path('university/<int:pk>/update/', UniversityUpdateView.as_view(), name='university_update'),
    # path('accreditation/list/', AccreditationListView.as_view(), name='accreditation_list'),
    # path('accreditation/add/', AccreditationCreateView.as_view(), name='accreditation_create'),
    # path('accreditation/<int:pk>/update/', AccreditationUpdateView.as_view(), name='accreditation_update'),
    # path('accreditation/<int:pk>/delete/', AccreditationDeleteView.as_view(), name='accreditation_delete'),
    # path('black_list/', BlackList.as_view(), name='black_list'),
    # path('black_list_del/<int:pk>/', DeleteFromBL.as_view(), name='black_list_del'),
    # path('expert/list/<str:type>/', ExpertListView.as_view(), name='expert_list'),
    # path('expert/create/', ExpertCreate.as_view(), name='expert_create'),
    # path('expert/<int:pk>/', ExpertDetail.as_view(), name='expert_detail'),
    # path('expert/<int:pk>/update/', ExpertUpdate.as_view(), name='expert_update'),
    # path('expert/<int:pk>/delete/', ExpertDeleteView.as_view(), name='expert_delete'),
    # path('training/list/', TrainingListView.as_view(), name='training_list'),
    # path('training/create/', TrainingCreateView.as_view(), name='training_create'),
    # path('training/<int:pk>/delete/', TrainingDeleteView.as_view(), name='training_delete'),
    # path('training/<int:pk>/update/', TrainingUpdateView.as_view(), name='training_update'),
    # path('sendlink/', SendLinkView.as_view(), name='sendlink'),
    # path('expertlink/<token>', ExpertLinkView.as_view(), name='expertlink'),
    # path('expert/<int:pk>/resume/', DownloadExpertResume.as_view(), name='download')
    # path('expertlink/creation_choice/', ExpertCreationChoice.as_view(), name='expert_creation_choice'),

]
