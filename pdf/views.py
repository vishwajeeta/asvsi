from django.http import FileResponse
import os
from django.contrib.auth.decorators import login_required
 
@login_required(login_url='signin')  
def pdf(request):
    filepath = os.path.join('static', 'hii.pdf')
    return FileResponse(open(filepath, 'rb'), content_type='application/pdf')