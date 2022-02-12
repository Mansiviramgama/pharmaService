# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from random import random
from django.contrib.auth.models import User


from rest_framework.test import  APITestCase

from pharmacy.api.tests.setup import Service


class SearchMedicalShop(APITestCase):
    def setUp(self):
        self.factory, self.client, self.header = Service.setup_auth_user(self)


    def test_setup(self):
        print("Setup")
        print(self.factory, self.client, self.header)
        pass        
