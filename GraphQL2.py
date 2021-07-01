import graphene
import json
from datetime import datetime

"""
    GraphQL schema with parameters

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


schema = graphene.Schema(query=Query)

result = schema.execute(
    '''
    {
      users (first : 1){
          userName
          lastLogin
      }
    }
    '''

)

items = dict(result.data.items())
print(json.dumps(items, indent=4))
