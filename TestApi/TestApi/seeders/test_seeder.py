from api.models import Patient
from tests.models import Test
from results.models import Result
import random

def seed():

    
    # test names to populate db
    names = [
        'John',
        'Bill',
        'Larry',
    ]

    if (Patient.objects.filter(name=names[0]).exists()):
        return

    # test tests to populate db
    tests = [
        'nash',
        'ckd'
    ]

    # populate patients 
    for name in names:
        cur = Patient(name=name, weight=100)
        cur.save()

    # populate tests for each patient
    for name in names:
        for test in tests:
            patient = Patient.objects.get(name=name)
            cur = Test(test_name=test, patient=patient)
            cur.save()

    tests_qs = Test.objects.all()  # querystring of all tests

    # create result for each test
    for test in tests_qs:
        res = random.randint(0, 20)  # create random test result in range from 0 -> 20 
        res_db = Result(result=res, patient=test.patient, test=test)
        res_db.save()

