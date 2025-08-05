from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Page
from .forms import CEORegisterForm, PageForm, RecruitmentRequestForm
from django.contrib import messages


# Vista para listar páginas del blog
def page_list(request):
    pages = Page.objects.all().order_by('-date')
    return render(request, 'core/page_list.html', {'pages': pages})

# Vista para ver el detalle de una página
def page_detail(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    return render(request, 'core/page_detail.html', {'page': page})

def register_ceo(request):
    if request.method == 'POST':
        form = CEORegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ ¡Registro exitoso! Iniciá sesión para continuar.')
            return redirect('login')
    else:
        form = CEORegisterForm()
    return render(request, 'core/register.html', {'form': form})


# Vista principal luego del login
@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

# Vista para crear una nueva página del blog
@login_required
def create_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            page = form.save(commit=False)
            page.author = request.user
            page.save()
            return redirect('page_list')
    else:
        form = PageForm()
    return render(request, 'core/page_form.html', {'form': form})

# Vista para editar una página existente
@login_required
def edit_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect('page_list')
    else:
        form = PageForm(instance=page)
    return render(request, 'core/page_form.html', {'form': form})

# Vista para confirmar y eliminar una página
@login_required
def delete_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    if request.method == 'POST':
        page.delete()
        return redirect('page_list')
    return render(request, 'core/page_confirm_delete.html', {'page': page})

# Vista para crear una solicitud de reclutamiento por parte del CEO
@login_required
def recruitment_request_view(request):
    if request.method == 'POST':
        form = RecruitmentRequestForm(request.POST)
        if form.is_valid():
            recruitment_request = form.save(commit=False)
            recruitment_request.user = request.user
            recruitment_request.save()
            return redirect('dashboard')
    else:
        form = RecruitmentRequestForm()
    return render(request, 'core/recruitment_request_form.html', {'form': form})

# Vista para la home (landing)
def home(request):
    return render(request, 'core/home.html')
