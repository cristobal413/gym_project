from django.urls import path
from .views import (
    ImplementoListView,
    ImplementoDetailView,
    ImplementoCreateView,
    ImplementoUpdateView,
    ImplementoDeleteView,
)

urlpatterns = [
    path('', ImplementoListView.as_view(), name='catalogo_implementos'),
    path('implemento/<int:pk>/', ImplementoDetailView.as_view(), name='implemento_detail'),
    path('implemento/nuevo/', ImplementoCreateView.as_view(), name='implemento_create'),
    path('implemento/<int:pk>/editar/', ImplementoUpdateView.as_view(), name='implemento_update'),
    path('implemento/<int:pk>/eliminar/', ImplementoDeleteView.as_view(), name='implemento_delete'),
]