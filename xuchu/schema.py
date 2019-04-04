from django.contrib.auth.models import User as UserModel
from graphene_django import DjangoObjectType
import graphene

class User(DjangoObjectType):
    class Meta:
        model = UserModel

class Hero(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()


class Query(graphene.ObjectType):
    users = graphene.List(User)
    hero = graphene.Field(Hero)

    @graphene.resolve_only_args
    def resolve_users(self):
        return UserModel.objects.all()
    @graphene.resolve_only_args
    def resolve_hero(self):
        return Hero(id=1, name="xuchu")
schema = graphene.Schema(query=Query)
