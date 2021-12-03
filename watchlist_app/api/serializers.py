from django.db import models
from django.db.models import fields
from rest_framework import serializers
from ..models import Review, StreamPlatform, WatchList


class ReviewSerilaizer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerilaizer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = '__all__'


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def validate(self, data):

#         if(data['name'] == data['descrption'] ):
#             return serializers.ValidationError("Title and description cannot be same")
#         return data

#     def validate_name(self, value):
#         if(len(value)<2):
#             return serializers.ValidationError("Name is too small")
#         return value

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         return instance
