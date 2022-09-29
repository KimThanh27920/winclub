from rest_framework import generics, response, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt import authentication

from wines.models import Wine
from .serializers import CartSerializer, CartDetailSerializer, ListCartSerializer, CartDetailUpdateSerializer
from ..models import Cart, CartDetail

# from bases.permissions.rolecheck import IsOwner



class CartListCreate(generics.ListCreateAPIView):    
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]      
    serializer_class = ListCartSerializer
    pagination_class = None
    # queryset = Cart.objects.all()
    
    def get_queryset(self):
        self.queryset = Cart.objects.filter(account=self.request.user)              
        return super().get_queryset()    
    
    def get_serializer_class(self):
        if(self.request.method == "POST"):
            self.serializer_class = CartSerializer                      
        return super().get_serializer_class()
                                          
    def create(self, request, *args, **kwargs): # error when first create cart_detail will none
        user = request.user.id    
        data_return = []    
        for cart_detail in request.data:
            # cart_temp = []
            # cart_detail = []            
            wine_id = cart_detail.get("wine")
            quantity = cart_detail.get("quantity")
            if(quantity < 1):                 
                return response.Response(data={"quantity": ["Invalid quantity"]}, status=status.HTTP_400_BAD_REQUEST)
            
            data = Wine.objects.get(id = wine_id)
            winery_id = data.winery.id
            # Check Cart exist, create or get  
            cart = Cart.objects.filter(winery=winery_id, account=user)    
            if not (cart.exists()):
                cart_data = {
                    "winery": winery_id,
                    "account": user
                }
                serializer = self.get_serializer(data=cart_data)
                serializer.is_valid(raise_exception=True)
                instance_cart = serializer.save() 
                cart_id = instance_cart.id  
                    
            else:
                instance_cart = cart[0]
                cart_id = instance_cart.id   
            
            # cart_temp.append(instance_cart)
            # Check Cart Detail exist, create or update
            cart_detail = CartDetail.objects.filter(cart=cart_id, wine=wine_id)
            
            if(cart_detail.exists()):
                quantity = quantity + cart_detail[0].quantity
                ob_cart_detail = {
                    "quantity": quantity                    
                }
                serializer_cart_detail = CartDetailSerializer(cart_detail[0],data = ob_cart_detail, partial=True)
                
                if serializer_cart_detail.is_valid(raise_exception=True):
                    serializer_cart_detail.save()  
                
            else: 
                ob_cart_detail = {
                    "quantity": quantity,
                    "cart": cart_id,
                    "wine": wine_id                 
                }
                serializer_cart_detail = CartDetailSerializer(data = ob_cart_detail)
                if serializer_cart_detail.is_valid(raise_exception=True):
                    serializer_cart_detail.save()  
                    
        return response.Response(status=status.HTTP_200_OK)
    
    
class CartRetrieve(generics.RetrieveUpdateDestroyAPIView):    
    serializer_class = ListCartSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated] 
    lookup_url_kwarg = 'cart_id' 
        
    def get_queryset(self):
        self.queryset = Cart.objects.filter(account=self.request.user.id)
        return super().get_queryset()
    
    def get_serializer_class(self):
        if(self.request.method == "PUT"):
            self.serializer_class = CartDetailUpdateSerializer 
                               
        return super().get_serializer_class()
    
    def get_object(self):
        if(self.request.method == "PUT"):
            cart_id = self.kwargs.get(self.lookup_url_kwarg)
            id = self.request.data.get("cart_detail")
            obj = CartDetail.objects.filter(id=id, cart=cart_id) #check cart_detail of cart            , cart=self.kwargs.get(self.lookup_url_kwarg)
            if(obj.exists()):
                return obj[0]
        
            return Response(data={"detail": "Not found"},status=status.HTTP_404_NOT_FOUND)
        
        return super().get_object()   
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        try: 
            if(instance.status_code == 404):
                return instance
        except:
            pass
        
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)