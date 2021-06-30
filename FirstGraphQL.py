from graphene import ObjectType, String
import graphene
import json

    """[summary]

    Returns:
        [type]: [description]
    """
class Query(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    isStaff = graphene.Boolean()

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_isStaff(self, info):
        return True

schema = graphene.Schema(query=Query, auto_camelcase= True)

result = schema.execute(
    '''
    {
        isStaff
    }
    '''
)
items = dict(result.data.items())
print(json.dumps(items, indent=4))