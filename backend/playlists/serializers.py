from rest_framework import serializers
from .models import Playlist

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'

'''
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
'''
