# rest framework import
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
#app import
from bases.permissions.business import IsBusiness
from rest_framework.permissions import IsAuthenticated
from bases.errors.errors import SubscriptionPackageErrors
from subscriptions.models import SubscriptionPackage
from service.stripe.stripe_api import  StripeAPI
from accounts.models import Account
from wineries.models import Winery

#Subcsription checkout
class Subscription(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsBusiness]
    
    def post(self, request, *args, **kwargs):
        subs_pk_id = request.data["subscription_package"]
        user = Account.objects.get(id = self.request.user.id)
        
        stripe_account = user.stripe_account
        
        error1 = SubscriptionPackageErrors.stripe_account_exist(stripe_account)
        if error1 is not None:
            return error1

        error = SubscriptionPackageErrors.exist(subs_pk_id)
        if error is not None:
            return error
        subs_pk = SubscriptionPackage.objects.get(id=subs_pk_id)
        price_id = subs_pk.price_id
        
        subscription = StripeAPI.subscription_checkout(stripe_account,price_id )
        
        # print(subscription)
        
        # if subscription == False :
        #     error = {
        #         "message": "Can't checkout! Because you don't have payment method",
        #         "status" : False
        #     }
        #     return Response(data=error, status=status.HTTP_400_BAD_REQUEST)
        
        if subscription["status"] == "active" :
            
            Winery.objects.filter(account=self.request.user.id).update(is_active=True)
       
        return Response(data=subscription, status=status.HTTP_200_OK)