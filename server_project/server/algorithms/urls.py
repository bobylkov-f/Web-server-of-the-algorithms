from django.conf.urls import patterns, url

from algorithms import views

urlpatterns = patterns("",
                       url(r"^$", views.index, name="index"),
                       url(r"add_algorithm/$", views.add_algorithm, name="add_algorithm"),
                       url(r"update_algorithm_page/([-\w]+)$", views.update_algorithm_page, name="update_algorithm"),
                       url(r"update_algorithm/$", views.update_algorithm, name="update_algorithm"),
                       url(r"submit_algorithm/$", views.submit_algorithm, name="submit_algorithm"),
                       url(r"register/$", views.register, name="register"),
                       url(r"login/$", views.login, name="login"),
                       url(r"logout/$", views.logout, name="logout"),
                       url(r"run_existing_algo/([-\w]+)$", views.run_existing_algo, name="run_existing_algo"),
                       url(r'^([-\w]+)$', views.alg_details, name="alg_details"),
                       url(r'^([-\w]+)/description/$', views.alg_description, name="alg_details"))
