#rest framework import
from rest_framework.response import Response
from rest_framework import status

#app imports
from wines.models import Wine 
from subscriptions.models import SubscriptionPackage
from wineries.models import Winery
from accounts.models import Account
from bases.services.stripe.stripe import StripeAPI

#Python imports
from datetime import datetime, timedelta
from operator import itemgetter


#check error of business
class BusinessErrors:
    def exists(winery_id):
        if  not (Winery.objects.exclude(deleted_at__isnull=False).filter(id=winery_id).exists()) :
            data={
                "success":False,
                "message": "Winery don't exist! "}
            return Response(data,status= status.HTTP_400_BAD_REQUEST)


#check Account error
class AccountErrors:
    def exists(user_id):
        if not (Account.objects.filter(is_business=False).filter(id=user_id).exists()):
            data={
                "success":False,
                "message": "Account don't exist! "}
            return Response(data,status= status.HTTP_400_BAD_REQUEST)


# check error of Wine
class CategoriesErrors:

    #check type have child 
    def type_has_child(type_id):
        if Wine.objects.filter(type=type_id).exists() :
            data={
                "success":False,
                "message": "Type has child data! "}
            return Response(data,status= status.HTTP_400_BAD_REQUEST)
    
    #check style already exist
    def style_has_child(style_id):
        if Wine.objects.filter(style=style_id).exists() :
            data={
                "success":False,
                "message": "Style has child data! "}
            return Response(data,status= status.HTTP_400_BAD_REQUEST)

    #check grape already exist
    def grape_has_child(grape):
        if Wine.objects.filter(grape=grape).exists() :
            data={
                "success":False,
                "message": "Grape has child data! "}
            return Response(data,status= status.HTTP_400_BAD_REQUEST)

    #check food already exist
    def food_has_child(food):
        if Wine.objects.filter(food=food).exists() :
            data={
                "success":False,
                "message": "Food has child data! "}
            return Response(data,status=status.HTTP_400_BAD_REQUEST)
    
     #check region already exist
    def region_has_child(region):
        if Wine.objects.filter(region=region).exists() :
            data={
                "success":False,
                "message": "Region has child data! "}
            return Response(data,status= status.HTTP_400_BAD_REQUEST)
    
     #check country already exist
    def country_has_child(country):
        if Wine.objects.filter(country=country).exists() :
            data={
                "success":False,
                "message": "Country has child data! "}
            return Response(data,status= status.HTTP_400_BAD_REQUEST)


#SubscriptionCheck Errors
class SubscriptionPackageErrors:

    def exist(subs_pk_id):
        if not (SubscriptionPackage.objects.filter(id=subs_pk_id).exists()):
            data ={
                "success":False,
                "message": "Subscription Package don't exist or disable"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    
    def stripe_account_exist(stripe_account):
        if stripe_account is None:
            data ={
                "success":False,
                "message": "You don't have payment method"
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
    
    def check_winery_active(account_id):
        data = StripeAPI.subscription_search(account_id)
        if data == []:
            return None
        sorts = sorted(data,key=itemgetter('created'), reverse=True)
        if sorts[0]["status"] == "canceled":
            return None
        now = datetime.now() + timedelta(days=3)
        timestamp = datetime.timestamp(now) 
        
        due_date = sorts[0]["current_period_end"]
        print(timestamp,due_date )
        if timestamp < due_date :
            data ={
                "success":False,
                "message": "You have already subcription"
            } 
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


    def check_subscription_exists(account_id):
        data = StripeAPI.subscription_search(account_id)
        if data == []:
            data ={
                "success":False,
                "message": "You have been subcription yet "
            }
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)
      
        sorts = sorted(data,key=itemgetter('created'), reverse=True)
      
        now = datetime.now()
        timestamp = datetime.timestamp(now) 
        due_date = sorts[0]["current_period_end"]
        
        if timestamp >= due_date :
            data ={
                "success":False,
                "message": "Your subscription will expire soon!"
            } 
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)