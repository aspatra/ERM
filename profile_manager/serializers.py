from rest_framework.serializers import Serializer, CharField, DateTimeField


class UserProfileSerilalizer(Serializer):
    """Serializer class for User Profile model class"""
    EmailID = CharField(max_length=50,source='email_id')
    username = CharField(max_length=50,required=False, source='username')
    password = CharField(max_length=50,required=False, source='password')
    UserAddress = CharField(max_length=100,required=False, source='address')
    created_at = DateTimeField(required=False)
    updated_at = DateTimeField(required=False)


    def validate(self, attrs):
        """
        Validation method for User profile serializer
        :param attrs:
        :return:
        """
        pass

    def create(self, validated_data):
        """
        Create a record in database
        :param validated_data:
        :return:
        """
        return self.create(**validated_data)