from rest_framework import serializers
from. models import Type, CheckList, ListInput

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'
        
class CheckListSerializer(serializers.ModelSerializer):
    title = TypeSerializer(read_only=True)
    # title = serializers.StringRelatedField()
    class Meta:
        model = CheckList
        fields = '__all__'

class ListInputSerializer(serializers.ModelSerializer):
    answer = serializers.BooleanField(allow_null=True, default=None)
    # title = CheckListSerializer(read_only=True)
    question_text = CheckListSerializer(read_only=True)
    # title = serializers.StringRelatedField()
    # question_text = serializers.StringRelatedField()
    class Meta:
        model = ListInput
        fields = '__all__'

# class HistorySerializer(serializers.ModelSerializer):
#     # title = serializers.StringRelatedField()
#     # question_date = serializers.StringRelatedField()
#     class Meta:
#         model = History
#         fields = '__all__'
