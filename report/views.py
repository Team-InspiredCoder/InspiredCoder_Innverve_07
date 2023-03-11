from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import random
from django.template.loader import render_to_string
from django.template.loader import get_template
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import CustomUser
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
        
from fuzzywuzzy import fuzz
class GeneratePdf(APIView):
    
    permission_classes = []
    authentication_classes = [] 

    def post(self,request):

        user_ans =  request.data.get('user_answer')
        user_con =  request.data.get('user_confidence')

        Sample_Answer = list(user_ans.split('***'))
        confidence_list = list(user_con.split('***'))


        list_of_Accuracy_of_answer = []
        Correct_Answer_list=[
            "A function is a group of statements that together perform a task. Every C program has at least one function, which is main(), and all the most trivial programs can define additional functions. You can divide up your code into separate functions. ",
            "printf and scanf functions are inbuilt library functions in C which are available in C library by default. These functions are declared and related macros are defined in “stdio.h” which is a header file. We have to include “stdio.h” file to make use of this printf and scanf library functions. C users these functions to write and read from Input Output devices respectively.",
            "In c programming language, arrays are classified into two types. They are as follows...    Single Dimensional Array / One Dimensional Array Multi Dimensional Array Single Dimensional Array In c programming language, single dimensional arrays are used to store list of values of same datatype. In other words, single dimensional arrays are used to store a row of values. In single dimensional array, data is stored in linear form. Single dimensional arrays are also called as one-dimensional arrays, Linear Arrays or simply 1-D Arrays.",
            "Keywords are predefined, reserved words in C language and each of which is associated with specific features. These words help us to use the functionality of C language. They have special meaning to the compilers.A keyword is a reserved word. You cannot use it as a variable name, constant name, etc.",
            "scanf function is used to read input from the console or standard input of the application in C and C++ programming language. scanf() function can read different data types and assign the data into different variable types.",
            "C is Developed by Dennis Ritchie",
            "main function is the entry point of any C program. It is the point at which execution of program is started. When a C program is executed, the execution control goes directly to the main() function. Every C program have a main() function.    An operating system always calls the main function when a programmers or users execute their programming code.It is responsible for starting and ends of the program. It is a universally accepted keyword in programming language and cannot change its meaning and name.",
            "An operator is a symbol that tells the compiler to perform specific mathematical or logical functions. C language is rich in built-in operators and provides the following types of operators −    Arithmetic Operators Relational Operators  Logical Operators  Bitwise Operators Assignment Operators Misc Operators",
            "default in C is used in a switch statement to indicate the control path when no other case is selected. Hence that is why it is used, i.e. to indicate which location in the code gets control “by default”. Default is also used in C++ in switch statements and also for class member functions specifiers for compiler generated functions (and constructors) but since we’re taking about C I won’t go into why you’d need them in C++."]
       
        Questions_list=["Define Function in C ?",#1
                    "What is  the use  of printf() ?",#2
                    "Types of Array in C ?",#3
                    "Define keywords in C and give example ?",#4
                    "In C which function is used to take input from console?",#5
                    "Who Developed C Programming?",#6
                    "What is the use of main function?",#7
                    "Define Operator and State it's types?",#8
                    "what is the use of default keyword?"]#9
        
        Sample_Answer = ['Set of Instruction which perform particular task',
                        'to print the output on console',
                        'Keyword have special meaning assigned to it,int,float,char',
                        'Single Dimensional Array and Multi Dimensioanl Array',
                        'scanf is  used to take input',
                        'Dennis Ritchie',
                        'Main function is the function from where the execution of any program starts',
                        'Operator are used to perform mathematical operation Arithmetic Operator,Logical Operator',
                        'Default keyword to create '
                        ]


        current_date = date.today()
        custom_user = CustomUser.objects.filter(email="connect.siddhiraj@gmail.com").last()
        
        for j in range(len(Sample_Answer)):
            Accuracy=fuzz.ratio(Correct_Answer_list[j],Sample_Answer[j])
            print("Accuracy::",Accuracy)
            list_of_Accuracy_of_answer.append(Accuracy)
        

        confidence_list = [90,93,95,49,95,95,59,95,59]
        avg_score = sum(list_of_Accuracy_of_answer)/len(list_of_Accuracy_of_answer) ## need to do
        avg_confidence = sum(confidence_list)/len(confidence_list)


       
        res = []
        print(len(list_of_Accuracy_of_answer))
        print(len(Questions_list))
        for i in range(len(list_of_Accuracy_of_answer)):
            print(i)
            temp = {
                "sr": i+1,
                "q": Questions_list[i],
                "s": list_of_Accuracy_of_answer[i],
                "c": confidence_list[i],
            }

            res.append(temp)




        data = {'full_name':custom_user.first_name + " " + custom_user.last_name,
                'mobile_no':custom_user.mobile_number,'current_date':current_date,
                'avg_score':avg_score,'avg_confidence':avg_confidence,
                'profile_picture_link':custom_user.profile_picture,
                'rdata':res,
                'path':settings.BASE_DIR}
        print(data)
        temp, file_path = render_to_pdf(template_src,data,f'invoice')

        # return JsonResponse({"msg":"Pdf generated Successfully"})
        HttpResponse(
        file_path,
         headers={
             "Content-Type": "application/vnd.ms-excel",
             "Content-Disposition": 'attachment; filename="Report.pdf"',
         },
     )    
