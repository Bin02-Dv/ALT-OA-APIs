from rest_framework import serializers
from .models import AuthApiModel, Course

class AuthApiModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthApiModel
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'state', 'phone_number', 'invitation_code']
        extra_kwargs = {
            'password': {'write_only': False}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class CourseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'instructor', 'instructor_full_name', 'course_title', 'course_description', 'course_price', 'course_banner', 'course_slide', 'course_video']
        