from rest_framework import generics, response, status, permissions
from rest_framework_simplejwt import authentication

from wines.models import Wine
from .serializers import CartSerializer, CartDetailSerializer
from ..models import Cart, CartDetail



class CartListCreate(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):        
        return super().get_queryset()
    
    def get_serializer_class(self):
        return super().get_serializer_class()
    
    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)
        
    def create(self, request, *args, **kwargs):
        user = request.user.id
        
        for cart_detail in request.data:
            wine = cart_detail.get("wine")
            winery = cart_detail.get("winery")
            quantity = cart_detail.get("quantity")
            print(cart_detail)
            cart = Cart.objects.filter(winery=winery, account=user)
            if(cart.exists()):
                print("da ton tai")
                print(cart[0].id)
                wine_object = Wine.objects.filter(id = wine)
                CartDetail_Object = CartDetail.objects.update_or_create(
                    wine = wine_object[0],
                    quantity = quantity,
                    cart = cart[0]
                )
                print(CartDetail_Object)
                # cart[0].quantity = cart[0].quantity + quantity
                # ob = cart[0].save()
                # print(ob)
            else:
                cart_data = {
                    "winery": winery,
                    "account": user
                }
                
                print(cart_data)
                print("hello")
                # serializer = self.get_serializer(data=request.data)
                serializer = self.get_serializer(data=cart_data)
                serializer.is_valid(raise_exception=True)
                # self.perform_create(serializer)
                serializer.save()
            
        # headers = self.get_success_headers(serializer.data)
        
        return response.Response(data="helloworld", status=status.HTTP_201_CREATED)