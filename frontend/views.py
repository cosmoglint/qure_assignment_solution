from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from .serializers import PeopleSerializer
from .models import People

@login_required()
def index(request, *args, **kwargs):
    return render(request, 'frontend/index.html')


def sign_up(request):
    print('!!!')
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("theree")
            user = form.save()
            login(request, user)
            return HttpResponseRedirect("/")

    context['form'] = form
    context['login_form'] = AuthenticationForm()


    return render(request, 'registration/sign_up.html', context)

@login_required()
def people_list(request):
    request_body = request.headers
    print(request_body)

    if "Cookie" in request.headers:
        value = People.objects.all()
        my_serializer = PeopleSerializer(data=value, many=True)
        if my_serializer.is_valid():
            return JsonResponse(my_serializer.data, status=200)
        # return JsonResponse(my_serializer.errors, status=400)
        return JsonResponse(my_serializer.data, safe=False, status=200)
    return JsonResponse({"data":"unautharized"}, safe=False, status=400)


@login_required()
def get_user(request):
    current_user = request.user
    current_user_name = request.user.username
    return JsonResponse({"username":current_user_name})
    # return HttpResponse("hi")
