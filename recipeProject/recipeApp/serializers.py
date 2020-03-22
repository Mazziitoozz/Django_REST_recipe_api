from rest_framework import serializers

from core.models import Tag,Ingredient,Recipe


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag object"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_Fields = ('id',)

class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for Ingredient object"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_Fields = ('id',)

class RecipeSerializer(serializers.ModelSerializer):
    """ Serialize a recipe"""
    'Ingredient and Tag are primary keys from other tables, we set many=True because is many to many'
   
    ingredients = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Ingredient.objects.all()
    )
    tags = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Tag.objects.all()
    )

    class Meta:
        model = Recipe
        fields = (
            'id', 'title', 'ingredients', 'tags', 'time_minutes', 'price',
            'link',
        )
        read_only_fields = ('id',)
class RecipeDetailSerializer(RecipeSerializer):
    """We reuse the code from the previous serializers, but we are going to overwrite some things"""
    ingredients = IngredientSerializer(many=True,read_only=True)
    tags = TagSerializer(many=True,read_only=True)
    # create this structure
        # {
        #     "id": 1,
        #     "title": "Vegan  key lime pie",
        #     "ingredients": [
        #         3
        #     ],
        #     "tags": [
        #         8
        #     ],
        #     "time_minutes": 60,
        #     "price": "15.00",
        #     "link": ""
        # }

class RecipeImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to recipe"""

    class Meta:
        model = Recipe
        fields = ('id', 'image')
        read_only_fields = ('id',)

 