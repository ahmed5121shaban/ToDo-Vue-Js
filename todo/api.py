from .serializers import TODOSerializers
from .models import TODO
from rest_framework import viewsets

class TODOViewSet(viewsets.ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOSerializers