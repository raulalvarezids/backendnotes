from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Note
from .serializers import NoteSerializer
from rest_framework.authentication import TokenAuthentication


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated] 
    authentication_classes = [TokenAuthentication]
        
                
    def get_queryset(self):
        user = self.request.user        
        return self.queryset.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)        
        
        