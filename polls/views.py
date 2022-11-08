from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from polls.utils import generate_order_id


# Create your views here.

@api_view(['GET'])
@permission_classes((IsAuthenticated, IsAdminUser))
def cc_avenue_request(request):
    order_id = request.REQUEST.get("Order_Id")
    if not order_id:
        order_id = generate_order_id()

    return Response()
