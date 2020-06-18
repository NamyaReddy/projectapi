from flask_restful import Resource,reqparse
from db import query

class Logreg(Resource):
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('email',type=str,required=True,help="email required")
        parser.add_argument('password',type=str,required=True,help="password required")
        data=parser.parse_args()
        try:
           x= query(f"""select * from team12.logreg where email='{data['email']}' and password='{data['password']}'""",return_json=False)
           if len(x)>0:
               return query(f"""select * from team12.logreg where email='{data['email']}' and password='{data['password']}'""")
           else:
               return {"message":"login unsuccessfull"}
        except:
            return {"message":"error"},500