from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CourseCertificationMapping
from .serializers import CourseCertificationMappingSerializer

class CourseCertificationMappingListView(APIView):

    def get(self, request):
        queryset = CourseCertificationMapping.objects.all()
        vendor_id = request.query_params.get('vendor_id')
        if vendor_id:
            queryset = queryset.filter(vendor__id=vendor_id)
        serializer = CourseCertificationMappingSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CourseCertificationMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseCertificationMappingDetailView(APIView):

    def get_object(self, pk):
        try:
            return CourseCertificationMapping.objects.get(pk=pk)
        except CourseCertificationMapping.DoesNotExist:
            return None

    def get(self, request, pk):
        mapping = self.get_object(pk)
        if mapping is None:
            return Response({'error': 'Mapping not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseCertificationMappingSerializer(mapping)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        mapping = self.get_object(pk)
        if mapping is None:
            return Response({'error': 'Mapping not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseCertificationMappingSerializer(mapping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        mapping = self.get_object(pk)
        if mapping is None:
            return Response({'error': 'Mapping not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseCertificationMappingSerializer(mapping, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        mapping = self.get_object(pk)
        if mapping is None:
            return Response({'error': 'Mapping not found'}, status=status.HTTP_404_NOT_FOUND)
        mapping.delete()
        return Response({'message': 'Mapping deleted successfully'}, status=status.HTTP_200_OK)