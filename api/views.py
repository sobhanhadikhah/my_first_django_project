from .models import Blog
from .serializers import BlogSerializer,RegisterSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
from drf_yasg.utils import swagger_auto_schema

class BlogView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(
        security=[{'Bearer': []}]  # Specify the security scheme here
    )
    
   
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]
    def get(self, request,pk=None):
        if pk:
            blog = Blog.objects.get(pk=pk)
            serializer = BlogSerializer(blog)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        else:
            blogs = Blog.objects.all()
            serializer = BlogSerializer(blogs, many=True)
            return Response(data=serializer.data,status=status.HTTP_200_OK)
    @swagger_auto_schema(request_body=BlogSerializer)
    def post(self,request):
        
        
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_200_OK)
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        blog = Blog.objects.get(pk=pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # This will create the user if validation passes
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 