import json


from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from apps.proposal.models.answers import AnswersModel
from django.views.decorators.csrf import csrf_exempt


from apps.proposal.models.proposal import ProposalModel
from apps.proposal.api.proposal.serializers import ProposalFullSerializer, ProposalSerializer
from tasks import start_queue




class ResponseAPIView(generics.RetrieveAPIView, generics.CreateAPIView):
    queryset = ProposalModel.objects.all()
    serializer_class = ProposalSerializer
    lookup_field = 'pk'
    
    
    def get(self, request, pk, *args, **kwargs):
        
        obj_proposal = ProposalModel.objects.filter(pk=pk).first()
        if obj_proposal:
            
            data = ProposalFullSerializer(obj_proposal).data
            return Response(data)
        
        return Response({"details": "pk not registered in the database"}, status=status.HTTP_404_NOT_FOUND)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        
        id = None
        received_json_data = request.data if request.data else None
        if 'id' in received_json_data:
            
            id = int(received_json_data['id'])
        if received_json_data:
            
            answer = AnswersModel(value=received_json_data)
            start_queue(id)
            answer.save()
            
            return Response({'success': True, 'message': 'Reply created successfully.'},status=200)
        else:
            return Response({'success': False, 'message': 'All fields must be provided.'},status=400)

            
        
        
    