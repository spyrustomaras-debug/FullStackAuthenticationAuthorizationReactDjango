from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import CustomUser
from .serializers import UserRegisterSerializer
from .serializers import ProjectSerializer
from .permissions import IsWorkerOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import Project
from rest_framework import viewsets
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# User Registration
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]
    
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsWorkerOrReadOnly]

    def perform_create(self, serializer):
        # Assign the currently logged-in user as the creator
        serializer.save(created_by=self.request.user)

