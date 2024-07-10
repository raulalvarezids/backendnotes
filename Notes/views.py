from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]      
                
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user=user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)        
        
        