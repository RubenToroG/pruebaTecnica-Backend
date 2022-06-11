from rest_framework.serializers import ModelSerializer
from api.models import Company

class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'