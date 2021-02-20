from rest_framework import serializers
from subdivisions.models import Subdivision
from workers.models import Worker, Dismissal_list
from users.models import CustomUser


class RecursiveSerializer(serializers.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class SubdivisionCreatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subdivision
        fields = '__all__'

    def create(self, validated_data):
        subdivision, _ = Subdivision.objects.update_or_create(
            name=validated_data.get('name', None),
            abbreviation=validated_data.get('abbreviation', None), 
            defaults={'parent':validated_data.get("parent")}
        )
        return subdivision


class SubdivisionSerializer(serializers.ModelSerializer):

    children = RecursiveSerializer(many=True)
    
    class Meta:
        model = Subdivision
        fields = ('name', 'abbreviation', 'children')


class WorkerCreatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = '__all__'

    def create(self, validated_data):
        worker, _ = Worker.objects.update_or_create(
            name=validated_data.get('name', None), 
            defaults={
                'user_name':validated_data.get("user_name"),
                'subdivision':validated_data.get("subdivision"), 
                'position':validated_data.get("position"),
                'recruitment_date':validated_data.get("recruitment_date"),
                'dismissal_point':validated_data.get("dismissal_point")
                }
        )
        return worker



class WorkerDetalSerializer(serializers.ModelSerializer):

    user_name = serializers.SlugRelatedField(slug_field='username', read_only=True)
    subdivision = serializers.SlugRelatedField(slug_field='name', read_only=True)
 
    class Meta:
        model = Worker
        fields = ('name', 'user_name', 'subdivision', 'position', 'recruitment_date', 'dismissal_point')


class SubWorkerSerializer(serializers.ModelSerializer):

    user_name = serializers.SlugRelatedField(slug_field='email', read_only=True)

    class Meta:
        model = Worker
        fields = ('name', 'user_name')


class DismissalCreatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dismissal_list
        fields = '__all__'


class DismissalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dismissal_list
        fields = ('dismissal_date')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('password', 'username', 'email', 'fullname')


class UserCreatSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'