from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # path("", views.index, name="index"),
    # path("<int:question_id>/", views.detail, name="detail"),
    # # ex: /polls/5/results/
    # path("<int:question_id>/results/", views.results, name="results"),
    # path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    # path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),

    # IndexView - shows list of questions
    path("", views.IndexView.as_view(), name="index"),
    
    # DetailView - shows details for a specific question
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    
    # ResultsView - shows voting results
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    
    # vote() - still typically a function-based view
    path("<int:question_id>/vote/", views.vote, name="vote"),
]