import graphene
import json
from datetime import datetime

"""
    GraphQL Mutation
    Mutation is used to Update or Delete the data

"""


class User(graphene.ObjectType):
    id = graphene.ID()
    userName = graphene.String()
    lastLogin = graphene.DateTime(required=False)


class Query(graphene.ObjectType):
    users = graphene.List(User, first=graphene.Int())

    def resolve_users(self, info, first):
        return [
            User(userName='Tuhin', lastLogin=datetime.now()),
            User(userName='Wrik', lastLogin=datetime.now()),
            User(userName='Arti', lastLogin=datetime.now())
        ][:first]


class CreateUser(graphene.Mutation):
    class Arguments:
        userName = graphene.String()
    user = graphene.Field(User)

    def mutate(self, info, userName):
        user = User(userName=userName)
        return CreateUser(user=user)


class Mutations(graphene.ObjectType):
    createUser = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)

result = schema.execute(
    '''
    mutation createUser ($userName : String){
        createUser(userName: $userName){
            user{
                userName
            }
        }
    }
    ''',
    variable_values={'userName': 'Tuhin'}
)

items = dict(result.data.items())
print(json.dumps(items, indent=4))
