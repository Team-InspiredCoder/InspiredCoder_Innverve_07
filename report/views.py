from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import random
from django.template.loader import render_to_string
from django.template.loader import get_template
from rest_framework.response import Response
from rest_framework.views import APIView
from interview.models import InterviewTest
import pdfkit
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import date
# Create your views here.
from django.conf import settings
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives

template_src = "Report/report.html"
data = {}
global file_path
def render_to_pdf(template_src, context, file_name="invoice"):
    file_path = f'{file_name}_{str(random.randint(100000, 9999999))}.pdf'
    template = get_template(template_src)
    html = template.render(context)
    options = {
        'page-height': '270mm',
        'page-width': '185mm',
    }

    config = pdfkit.configuration(wkhtmltopdf=r'C:\Users\admin\Downloads\wkhtmltox\bin\wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html, r'media/' + file_path, options=options,configuration=config) # new
    
    # print(f'pdf:{pdf}')
    return pdf,file_path
        

class GeneratePdf(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication] 

    def post(self,request):  
        current_date = date.today()
        avg_score = None ## need to do
        avg_confidence = None ## need to do
        question_list = request.data.get('question_list')
        accuracy_list = request.data.get('accuracy_list')
        confidence_list = request.data.get('question_list')

        data = {'full_name':request.user.first_name + " " + request.user.last_name,
                'mobile_no':request.user.mobile_number,'current_date':current_date,
                'avg_score':avg_score,'avg_confidence':avg_confidence,
                'profile_picture_link':request.user.profile_picture,
                'path':settings.BASE_DIR}
        temp, file_path = render_to_pdf(template_src,data,f'invoice')

        return JsonResponse({"msg":"Pdf generated Successfully"})
    
