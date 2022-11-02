from rest_framework import serializers
from .models import Artiste
from .models import Song
from .models import Lyrics


class artisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        # fields=('firstname', 'lastname')
        fields = '__all__'


class songSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        # fields=('firstname', 'lastname')
        fields = '__all__'


class lyricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyrics
        # fields=('firstname', 'lastname')
        fields = '__all__'
