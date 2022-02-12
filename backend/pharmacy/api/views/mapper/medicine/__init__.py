# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/pharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

__all__ = ["MedicineSearch"]

from .search_nearby_medicine import DisplayNearbyMedicineSearchedByUser


class MedicineSearch(DisplayNearbyMedicineSearchedByUser):
    """views.mapper.MedicineSearch"""