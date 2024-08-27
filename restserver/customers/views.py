import traceback

# drf
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from knox.models import AuthToken

# custom
from .serializers import RegisterCustomerSerializer, LoginSerializer, CustomerSerializer
from .models import Customers


class RegisterCustomerViews(APIView):
    def post(self, request, org_id=None):
        try:
            request_data = request.data.copy()
            request_data["org_id"] = org_id

            serializer_class = RegisterCustomerSerializer(data=request_data)

            if serializer_class.is_valid():
                serializer_class.save()
                api_response = Response(serializer_class.data, status=status.HTTP_201_CREATED)
            else:
                api_response = Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)     

            return api_response
        
        except Exception as e:
            traceback.print_exc()  # Log the traceback for debugging
            return Response(
                {"status": "error", "data": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )   

class AuthenticateUser(APIView):
    
    def post(self, request, *args, **kwargs):
        try:
            serializer = LoginSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                user = serializer.validated_data['user']
                print("User Instance:", user)
                print("User Instance Type:", type(user))

                # Verify user exists and is an instance of flipopoUser
                user_data = Customers.objects.filter(email=request.data['email']).first()
                if not user_data:
                    return Response({'status': 'error', 'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
                print("Verified User Data:", user_data)
                print("Verified User Data Type:", type(user_data))

                # Confirm the user instance is of the correct model
                if not isinstance(user_data, Customers):
                    return Response({'status': 'error', 'message': 'Invalid user instance'}, status=status.HTTP_400_BAD_REQUEST)

                # Create the token
                token_instance, token = AuthToken.objects.create(user=user_data)
                print("Generated Token:", token)

                user_id = user_data.id
                # Customers.objects.filter(id=user_id).update(lastLogin=datetime.now(timezone.utc))

                is_super_admin = user_data.is_super_admin
                is_admin = user_data.is_admin
                is_customer = user_data.is_customer
                displayName = user_data.first_name
                email_id = user_data.email

                # if profileImage:
                #     profileImage = request.build_absolute_uri(user_data.profileImage.url)
                # else:
                #     profileImage = ''

                data = {
                    "status": status.HTTP_200_OK,
                    'user_id': user_id,
                    'is_super_admin': is_super_admin,
                    'is_admin': is_admin,
                    'is_customer': is_customer,
                    'displayName': displayName,
                    'emailId': email_id,
                    # 'profileImage': profileImage,
                    "message": "Logged-in Successfully",
                    "Token": token
                }

                return Response(data)

            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print( {"status": "error", "data": str(e), 'traceback': traceback.format_exc()})
            return Response(
                {"status": "error", "data": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )



class CustomerViews(APIView):

    def get(self, request, id=None, org_id=None):
        try:
            if id:
                item = Customers.objects.get(id=id)
                serializer = (item)
                return Response(
                    {"status": "success", "data": serializer.data},
                    status=status.HTTP_200_OK,
                )

            items = Customers.objects.all()
            serializer = CustomerSerializer(items, many=True)
            return Response(
                {"status": "success", "data": serializer.data}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
            {"status": "error", "data": str(e)},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )