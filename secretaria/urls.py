from django.urls import path

from secretaria import views

urlpatterns = [
    path("api/v1/listar_estudantes", views.estudantes_list),
    path("api/v1/detalhe_estudante/<int:pk>/", views.estudantes_details),
    path("api/v1/filtar_estudante/", views.estudante_filter),
    path("api/v1/novo_estudante", views.estudante_create),
    path("api/v1/editar_estudante/<int:pk>/", views.estudante_edit),
    path("api/v1/apagar_estudante/<int:pk>/", views.estudante_delete),
]
