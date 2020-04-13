import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_200_OK
from django.shortcuts import get_object_or_404

from .models import Bank, Branch
from .serializers import BranchSerializer, BankSerializer

class BranchDetails(APIView):

    def get(self, request: Request, ifsc: str) -> Response:
        branch = get_object_or_404(Branch, ifsc=ifsc)
        bank = Bank.objects.get(id=branch.bank_id)

        data = BranchSerializer(branch).data
        data["name"] = bank.name

        return Response(data)


class AllBranches(APIView):

    def get(self, request, name, city):
        bank = get_object_or_404(Bank, name=name)
        branches = Branch.objects.filter(bank_id=bank.id, city=city)

        serializers = BranchSerializer(branches, many=True)
        data = serializers.data[:]
        for d in data:
            d['name'] = bank.name
        
        return Response(data)
