from rest_framework import serializers


class JavaCodeSerializer(serializers.Serializer):
    title = serializers.CharField()
    files = serializers.ListField(
        child=serializers.CharField()
    )
    _hash = serializers.CharField()
    _type = serializers.CharField()
    version = serializers.CharField()


class ReconDataSerializer(serializers.Serializer):
    pass


class RecentScansSerializer(serializers.Serializer):
    pass


class RecentScansSerializer(serializers.Serializer):
    pass

