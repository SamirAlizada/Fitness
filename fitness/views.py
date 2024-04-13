from django.shortcuts import render, redirect
from .forms import StudentForm

def student_register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_register')  # Öğrenci kaydı başarıyla oluşturulduktan sonra yönlendirilecek sayfanın adını belirtin
    else:
        form = StudentForm()
    return render(request, 'student_register.html', {'form': form})
