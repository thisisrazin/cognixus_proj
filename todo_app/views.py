from rest_framework import status, generics
from rest_framework.response import Response
from .models import TODO
from .serializers import TODOSerializer

# STILL NEED TO DEPLOY THIS PROJECT TO DOCKER

class TODOListCreateAPIView(generics.ListCreateAPIView):
    queryset=TODO.objects.all()
    serializer_class=TODOSerializer

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers=self.get_success_headers(serializer.data)
            return Response(
                {   
                    'pk': serializer.data['pk'],
                    'msg': 'TODO item added successfully'
                }, 
                status=status.HTTP_200_OK, headers=headers
            )
        if not serializer.is_valid(raise_exception=False):
            return Response(
                {'msg': 'Failed to add TODO item'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

class TODOUpdateAPIView(generics.UpdateAPIView):
    queryset=TODO.objects.all()
    serializer_class=TODOSerializer
    lookup_field='pk'

    def patch(self, request, *args, **kwargs):
        serializer=self.get_serializer(
            self.get_object(), 
            data=request.data, 
            partial=True
        )
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(
                {
                    'pk': f"{self.get_object().pk}", 
                    'patched_data': request.data
                }, 
                status=status.HTTP_200_OK
            )
        if not serializer.is_valid(raise_exception=False):
            return Response(
                {'msg': 'patch failed'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

class TODODestroyAPIView(generics.DestroyAPIView):
    queryset=TODO.objects.all()
    serializer_class=TODOSerializer
    lookup_field='pk'

    def destroy(self, request, *args, **kwargs):
        pk=self.kwargs['pk']
        instance=self.get_object()
        self.perform_destroy(instance)
        return Response(
            {
                'pk': f"{pk}", 
                'msg': 'TODO item deleted successfully'
            }, 
            status=status.HTTP_200_OK
        )



