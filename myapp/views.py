from rest_framework.views import Response
from rest_framework.decorators import api_view, renderer_classes


@api_view(['GET'])
def main(request):
    doc = [
        'Documention:',

    ]
    return Response(doc)
