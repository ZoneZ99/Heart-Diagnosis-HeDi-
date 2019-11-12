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
        request['tanggalLahir'] = date_to_days(request['tanggalLahir'])
        request['gender'] = int(request['gender'])
        request['tinggiBadan'] = int(request['tinggiBadan'])
        request['beratBadan'] = int(request['beratBadan'])
        request['tekananSistolik'] = int(request['tekananSistolik'])
        request['tekananDiastolik'] = int(request['tekananDiastolik'])
        request['tingkatKolesterol'] = int(request['tingkatKolesterol'])
        request['tingkatGlukosa'] = int(request['tingkatGlukosa'])
        request['isMerokok'] = boolean_value_to_number(request['isMerokok'])
        request['isPeminum'] = boolean_value_to_number(request['isPeminum'])
        request['isOlahraga'] = boolean_value_to_number(request['isOlahraga'])
        self.request = request

    def to_np_array(self):
        number_features = len(self.request.keys())
        array = np.empty(shape=(1, number_features))
        feature_values = list(self.request.values())
        array[0] = np.asarray(feature_values, dtype=np.float64)
        return array



