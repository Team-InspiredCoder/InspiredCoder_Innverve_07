from django.shortcuts import render
from .access_decorators import *
# Create your views here.
import pdfkit
from datetime import date

@un_authenticated_user
def index(request):

    return render(request, 'home/index.html')

@un_authenticated_user
def register(request):

    return render(request, 'login_register/signup.html')


@un_authenticated_user
def login(request):

    return render(request, 'login_register/login.html')


@un_authenticated_user
def verifyEmail(request, action, email, name):
    
    data = {
        "action": action,
        "email": email,
        "name": name
    }

    print("\ndata :: ", data)

    return render(request, 'user_verification/otp.html', data)


@un_authenticated_user
def emailVerified(request):

    return render(request, 'user_verification/activate.html')


def interviewPreview(request):

    return render(request, 'interview/preview.html')


def interviewScreen(request):

    return render(request, 'interview/interview_page.html')

template_src = "Report/report.html"
data = {}
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


def generate_pdf(request):
    current_date = date.today()
    avg_score = None ## need to do
    avg_confidence = None ## need to do
    # question_list = request.data.get('question_list')
    # accuracy_list = request.data.get('accuracy_list')
    # confidence_list = request.data.get('question_list')
    # data = {'full_name':request.user.first_name + " " + request.user.last_name,
    #         'mobile_no':request.user.mobile_number,'current_date':current_date,
    #         'avg_score':avg_score,'avg_confidence':avg_confidence,
    #         'profile_picture_link':request.user.profile_picture}


    question = ["question 1", "question 2", "question 3"]
    score = [90, 91, 92]
    confidence = [90, 91, 92]

    res = []

    for i in range(len(question)):
        temp = {
            "sr": i+1,
            "q": question[i],
            "s": score[i],
            "c": confidence[i],
        }

        res.append(temp)


    data = {'full_name':"Pankaj Jaiswal",
            'mobile_no':'9987035170','current_date':'22-03-2022',
            'avg_score':'94.54','avg_confidence':'59.54%',
            
            # 'profile_picture_link':request.user.profile_picture
            'rdata': res,

            }


    # temp, file_path = render_to_pdf(template_src,data,'invoice.pdf')
    return render(request,'Report/report.html',data)
