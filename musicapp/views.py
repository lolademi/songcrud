from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Artiste, Song, Lyrics
from .serializers import artisteSerializer, songSerializer, lyricsSerializer


class artisteList(APIView):
    def get(self, request):
        artiste1 = Artiste.objects.all()
        serializer = artisteSerializer(artiste1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class songList(APIView):
    def get(self, request):
        song1 = Song.objects.all()
        serializer = songSerializer(song1, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class lyricsList(APIView):
    def get(self, request):
        lyrics1 = Lyrics.objects.all()
        serializer = lyricsSerializer(lyrics1, many=True)
        return Response(serializer.data)

    def post(self):
        pass
