from collections import OrderedDict
from datetime import datetime

import numpy as np


def date_to_days(date: str) -> int:
    date_struct = datetime.strptime(date, "%Y-%m-%d")
    days_from_now = (datetime.now() - date_struct).days
    return days_from_now


def boolean_value_to_number(value: str) -> int:
    return 0 if value == 'false' else 1


class DiagnosisRequest:

    def __init__(self, request):
        request.pop('nama')
        self.request = OrderedDict()
        self.request['tanggalLahir'] = date_to_days(request['tanggalLahir'])
        self.request['jenisKelamin'] = int((request['jenisKelamin']))
        self.request['tinggiBadan'] = int(request['tinggiBadan'])
        self.request['beratBadan'] = float(request['beratBadan'])
        self.request['tekananSistolik'] = int(request['tekananSistolik'])
        self.request['tekananDiastolik'] = int(request['tekananDiastolik'])
        self.request['tingkatKolesterol'] = int(request['tingkatKolesterol'])
        self.request['tingkatGlukosa'] = int(request['tingkatGlukosa'])
        self.request['isMerokok'] = boolean_value_to_number(request['isMerokok'])
        self.request['isPeminum'] = boolean_value_to_number(request['isPeminum'])
        self.request['isOlahraga'] = boolean_value_to_number(request['isOlahraga'])

    def to_np_array(self):
        number_features = len(self.request.keys())
        array = np.empty(shape=(1, number_features))
        feature_values = list(self.request.values())
        array[0] = np.asarray(feature_values, dtype=np.float64)
        return array



