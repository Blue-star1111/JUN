import requests
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import serializers
from. models import Type, CheckList, ImageDetect
from django.conf import settings
from django.core.files import File
import os
from django.utils import timezone
from PIL import Image
import io

class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'

class CheckListSerializer(serializers.ModelSerializer):
    title = TypeSerializer(read_only=True)
    # title = serializers.StringRelatedField()
    answer = serializers.BooleanField(allow_null=True, default=None)

    class Meta:
        model = CheckList
        fields = '__all__'
        # fields = ['answer', 'bigo']

    def update(self, instance, validated_data):
        instance.answer = validated_data.get('answer', instance.answer)
        instance.bigo = validated_data.get('bigo', instance.bigo)
        instance.save()

        return instance


class ImageDetectSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()

    class Meta:
        model = ImageDetect
        fields = ['image']
    
    parser_classes = (MultiPartParser, FormParser)

    def create(self, validated_data):
        image = ImageDetect.objects.create(**validated_data)
        path = validated_data['image']
        print(path)
        # path =  settings.MEDIA_ROOT + '/' + str(validated_data['image'])
        file_path = settings.MEDIA_ROOT + "/yolov5/images/" + str(path)
        files = {'file': open(file_path, 'rb')}
        print(files)
        response = requests.post("http://127.0.0.1:8001/object-to-image", files=files)
        print(type(response.content), path)
        # # os.remove(file_path)
        
        print('step1')
        
        # 장고 안에 폴더 추가
        file_name = os.path.join(settings.MEDIA_ROOT+"/yolov5/images/",
                         timezone.now().strftime('%Y_%m_%d_%H_%M_%S.jpg'))
        print('step2')                 
        
        with open(file_name, 'wb') as f:
            content = response.content
            # data = content.encode('utf-8')
            resp = f.write(content)
            # img = Image.open(io.BytesIO(content))
            print(resp)
            f.close()
        print('step3')
        print(file_name)

        img = {'image': open(file_name, 'rb')}
        requests.post("http://127.0.0.1:8000/image/", files=img)
        print('step4')
        return image

        
        # image.delete(save=False)
        # image.save(file_name, File(img))
# class HistorySerializer(serializers.ModelSerializer):

#     class Meta:
#         model = History
#         fields = '__all__'
