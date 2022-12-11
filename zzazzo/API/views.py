from rest_framework import generics
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import paymentSerializers, userDetailSerializers
from rest_framework.views import APIView
from oscar.core.loading import get_model
from rest_framework.permissions import IsAuthenticated

Payment = get_model('task', 'Payment')
User = get_model('task', 'User')


class paymentListView(APIView):
    def get(self,
            request,
            format=None):
        snippet = Payment.objects.all()
        serializer = paymentSerializers(snippet, many=True)
        return Response(serializer.data)


class paymentDetailApiView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = paymentSerializers


class userDetailApiView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = userDetailSerializers
