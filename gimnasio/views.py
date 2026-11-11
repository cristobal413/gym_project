from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import ImplementoGym, TipoEquipamiento
from .forms import ImplementoGymForm

# 1. Catálogo público con optimización ORM obligatoria (select_related)
class ImplementoListView(ListView):
    model = ImplementoGym
    template_name = 'gimnasio/catalogo.html'
    context_object_name = 'implementos'
    paginate_by = 6

    def get_queryset(self):
        # OPTIMIZACIÓN OBLIGATORIA: Evita el problema N+1 mediante select_related
        queryset = ImplementoGym.objects.select_related('tipo').all()
        tipo_id = self.request.GET.get('tipo')
        if tipo_id:
            queryset = queryset.filter(tipo_id=tipo_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipos'] = TipoEquipamiento.objects.all()
        context['tipo_seleccionado'] = self.request.GET.get('tipo')
        return context

# 2. Detalle individual (Ficha)
class ImplementoDetailView(DetailView):
    model = ImplementoGym
    template_name = 'gimnasio/implemento_detail.html'
    context_object_name = 'implemento'

# 3. Creación protegida con Mixins y Mensajes Flash
class ImplementoCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ImplementoGym
    form_class = ImplementoGymForm
    template_name = 'gimnasio/implemento_form.html'
    success_url = reverse_lazy('catalogo_implementos')
    success_message = '¡El implemento "%(nombre)s" fue registrado exitosamente!'

# 4. Edición protegida
class ImplementoUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ImplementoGym
    form_class = ImplementoGymForm
    template_name = 'gimnasio/implemento_form.html'
    success_url = reverse_lazy('catalogo_implementos')
    success_message = '¡El implemento "%(nombre)s" fue actualizado correctamente!'

# 5. Eliminación protegida
class ImplementoDeleteView(LoginRequiredMixin, DeleteView):
    model = ImplementoGym
    template_name = 'gimnasio/implemento_confirm_delete.html'
    success_url = reverse_lazy('catalogo_implementos')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(request, f'El implemento "{obj.nombre}" fue eliminado correctamente.')
        return super().delete(request, *args, **kwargs)