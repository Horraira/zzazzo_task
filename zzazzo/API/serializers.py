from rest_framework import serializers
from oscar.core.loading import get_model

User = get_model('task', 'User')
Purchase = get_model('task', 'Purchase')
Payment = get_model('task', 'Payment')


class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class purchaseSerializers(serializers.ModelSerializer):
    user = userSerializers

    class Meta:
        model = Purchase
        fields = '__all__'
        # depth = 1


class paymentSerializers(serializers.ModelSerializer):
    purchase = purchaseSerializers

    class Meta:
        model = Payment
        fields = '__all__'
        depth = 1


class userDetailSerializers(serializers.ModelSerializer):
    purchase = purchaseSerializers
    payment = paymentSerializers

    class Meta:
        model = User
        fields = ('payment',)
        depth = 3
