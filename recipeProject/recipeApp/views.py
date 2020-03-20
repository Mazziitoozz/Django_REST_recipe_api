from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag,Ingredient,Recipe

from recipeApp import serializers


class BaseRecipeAttrViewSet(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.ListModelMixin):
    "Here we should put which is common to the following viewsets like permissions, filter and save the info"
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for the current authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """Create a new ingredient"""
        return serializer.save(user=self.request.user)

class IngredientViewSet(BaseRecipeAttrViewSet):
    """ Manage the ingredients in the db"""
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer

class TagViewSet(BaseRecipeAttrViewSet):
    """Manage tags in the database"""
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer

'''
Previous code before reduce the amount
class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,mixins.CreateModelMixin):

    """Manage tags in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer
    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
        
    def perform_create(self, serializer):
        """Create a new ingredient"""
        serializer.save(user=self.request.user)

class IngredientViewSet(viewsets.GenericViewSet, mixins.ListModelMixin,mixins.CreateModelMixin):
    """ Manage the ingredients in the db"""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """Create a new ingredient"""

        return serializer.save(user=self.request.user)
'''
class RecipeViewSet(viewsets.ModelViewSet):
    """"Manage Recipe, we use modelViewset because we want all the actions not only list and create"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Recipe.objects.all()
    serializer_class=serializers.RecipeSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
    def get_serializer_class(self):
        """Return appropiate serializer class, Here we add the logic depending on the action that we decide to use"""
        
        if self.action == 'retrieve':
            return serializers.RecipeDetailSerializer

        return self.serializer_class
    
    def perform_create(self, serializer):
        """Create a new recipe"""
        serializer.save(user=self.request.user)