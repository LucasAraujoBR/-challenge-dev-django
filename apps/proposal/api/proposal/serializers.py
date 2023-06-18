from rest_framework import serializers
from apps.proposal.models.proposal import ProposalModel


class ProposalSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = ProposalModel
        fields = '__all__'


class FieldsFullSerializer(serializers.Serializer):
    
    
    id = serializers.IntegerField()
    label = serializers.CharField(required=False)
    slug = serializers.SlugField()
    
    
class ProposalFullSerializer(serializers.Serializer):
    
    
    id = serializers.IntegerField()
    proposal_situation = serializers.CharField(required=False)
    title = serializers.CharField(required=False)
    slug = serializers.SlugField()
    description = serializers.CharField(required=False)
    field = serializers.SerializerMethodField(required=False, method_name='get_field_data')
    
    class Meta:
        model = ProposalModel
    

    def get_field_data(self, obj: ProposalModel):
        
        fields = obj.field.all()
        serialized_field = []
        
        for field in fields:
            serialized_fields = FieldsFullSerializer(field).data
            serialized_field.append(serialized_fields)

        return serialized_field

