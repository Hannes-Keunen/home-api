from rest_framework import serializers

from .models import Device, StateTemplate, StateTemplateField

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'address', 'state_template']


class TemplateFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateTemplateField
        fields = ['name', 'type']


class TemplateSerializer(serializers.ModelSerializer):
    fields = TemplateFieldSerializer(many = True)

    class Meta:
        model = StateTemplate
        fields = ['id', 'name', 'fields']

    def create(self, validated_data):
        fields = validated_data.pop('fields')
        template = StateTemplate.objects.create(**validated_data)

        for i, field in enumerate(fields):
            StateTemplateField.objects.create(template=template, ordinal=i, **field)

        return template

    def update(self, instance, validated_data):
        fields = validated_data.pop('fields')

        instance.name = validated_data.get('name', instance.name)
        instance.save()

        StateTemplateField.objects.filter(template=instance).delete()
        for i, field in enumerate(fields):
            StateTemplateField.objects.create(template=instance, ordinal=i, **field)

        return instance
