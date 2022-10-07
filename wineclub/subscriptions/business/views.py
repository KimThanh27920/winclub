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
from bases.services.stripe.stripe import  StripeAPI
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
        error = SubscriptionPackageErrors.check_winery_active(self.request.user.id)
        if error is not None:
            return error
            
        error1 = SubscriptionPackageErrors.stripe_account_exist(stripe_account)
        if error1 is not None:
            return error1

        error = SubscriptionPackageErrors.exist(subs_pk_id)
        if error is not None:
            return error
        subs_pk = SubscriptionPackage.objects.get(id=subs_pk_id)
        price_id = subs_pk.price_id
        
        subscription = StripeAPI.subscription_checkout(stripe_account,price_id, self.request.user.id )
     
        if subscription["status"] == "Failed" :
            error = {
                "error": "Can't checkout! Because you don't have payment method",
                "status" : False
            }
            return Response(data=error, status=status.HTTP_400_BAD_REQUEST)
        
        if subscription["status"] == "active" :
            Winery.objects.filter(account=self.request.user.id).update(is_active=True)
       
        return Response(data=subscription, status=status.HTTP_200_OK)


#Subcsription cancel
class SubscriptionCancel(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsBusiness]
    
    def post(self, request, *args, **kwargs):
        user = Account.objects.get(id = self.request.user.id)
       
        stripe_account = user.stripe_account
        error = SubscriptionPackageErrors.check_subscription_exists(self.request.user.id)
        if error is not None:
            return error
        
        subscription = StripeAPI.cancel(self.request.user.id)
        
        if subscription["status"] == "Failed" :
            error = {
                "error": "Can't cancel! You may or may not have canceled! If you didn't cancel before, please repeat in a few minutes!",
                "status" : False
            }
            return Response(data=error, status=status.HTTP_400_BAD_REQUEST)

        if subscription["status"] == "canceled" :
            Winery.objects.filter(account=self.request.user.id).update(is_active=False)
       
        return Response(data=subscription, status=status.HTTP_200_OK)