
from rest_framework.views import APIView

from rest_framework.response import Response

class BooksListCreateView(APIView):

    def get(self,request,*args,**kwargs):

        context={"message":"listing all books"}

        return Response(data=context)
    
    def post(self,request,*args,**kwargs):

        context={"message":"creating a new book object"}

        return Response(data=context)
    
class BookRetrieveUpdateDestroyView(APIView):

    def get(self,request,*args,**kwargs):

        context={"message":"fecth a specific book detail"}

        return Response(data=context)
    
    def put(self,request,*args,**kwargs):

        context={"message":"logic for updating a book"}

        return Response(data=context)
    
    def delete(self,request,*args,**kwargs):

        context={"message":"logic for deleting a book"}

        return Response(data=context)
    
# API =>enables communication between two software application

#http_request
#   url:
#   method:[GET,POST,PUT,PATCH,DELETE]
#   body
#   headers 

# JSON => format for transfering data

# DRF
# rest_framework>views>APIView
# rest_framework>resonse>Response => python_native_type=> JSON
