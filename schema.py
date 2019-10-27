import graphene
import json
from datetime import datetime


class User(graphene.ObjectType):
    id = graphene.ID()
    username = graphene.String()
    created_at = graphene.DateTime()

mockusers = [User(id="1", username="Dima", created_at=datetime.now()), User(id="2", username="Priv", created_at=datetime.now())]

class Query(graphene.ObjectType):
    users = graphene.List(User, limit = graphene.Int())
    hello = graphene.String()
    is_admin = graphene.Boolean()

    def resolve_hello(self, info):
        return "world"

    def resolve_is_admin(self, info):
        return True

    def resolve_users(self, info, limit): 
        return mockusers[:limit]

schema = graphene.Schema(query=Query)

result = schema.execute(
    '''
    {
        users(limit:1) {
            id
            username
            createdAt
        }
    }
    '''
)

dictResult = dict(result.data.items())
jsonResult = json.dumps(dictResult)

print(jsonResult)