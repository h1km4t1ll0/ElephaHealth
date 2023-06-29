from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from django.http import HttpResponse, HttpRequest
from rest_framework.permissions import IsAuthenticated
from .models import User
from .permissions import IsOwnerProfileOrReadOnly
from .serializers import userProfileSerializer


def homepage(request: HttpRequest) -> HttpResponse:
    html = "ElephaHealth homepage"
    return HttpResponse(html)


class UserProfileListCreateView(ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user)


class userProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=userProfileSerializer
    permission_classes=[IsOwnerProfileOrReadOnly,IsAuthenticated]

# def register_request(request: HttpRequest) -> HttpResponse:
#     if request.method == 'POST':
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration successful! Welcome!")
#             return redirect("homepage")
#         messages.error(request, "Invalid information. Unsuccessful registration.")
#     form = NewUserForm()
#     return render(request=request, template_name="register.html", context={"register_form": form})
#
#
# def login_request(request: HttpRequest) -> HttpResponse:
#     if request.method == "POST":
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('email')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.info(request, f"You are now logged in as {email}.")
#                 return redirect("homepage")
#             else:
#                 messages.error(request, "Invalid username or password.")
#         else:
#             messages.error(request, "Invalid username or password.")
#     form = AuthenticationForm()
#     return render(request=request, template_name="login.html", context={"login_form": form})
