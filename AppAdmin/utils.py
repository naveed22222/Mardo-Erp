import random
import string
import datetime
from datetime import date
from django import template
from django.db import connections

from django.http import HttpResponse
from django.utils.text import slugify


def DictinctFetchAll(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall()]


# def AutoGenerateCodeForModel(model, column, code_key):
#     code = ""
#     obj = model.objects.all()
#     obj_count = len(obj)
#     if obj_count == 0:
#         code = code_key + '1'
#     else:
#         obj_latest = model.objects.latest('id')
#         get_code = (getattr(obj_latest, column)).split("-")
#         code_count = int(get_code[1]) + 1
#         auto_code = code_key + str(code_count)
#         code = auto_code
#     return code

def AutoGenerateCodeForModel(model, column, code_key):
    code = ""
    cursor = connections['default'].cursor()
    obj = model.objects.all()
    obj_count = len(obj)
    if obj_count == 0:
        code = code_key + '1'
    else:
        tbl = model._meta.db_table
        query = "SELECT SPLIT_PART(" + column + ", '-', 2)::INTEGER AS unique_code FROM " + tbl + " ORDER BY SPLIT_PART(" + column + ", '-', 2)::INTEGER DESC LIMIT 1"
        cursor.execute(query)
        query_list = DictinctFetchAll(cursor)
        get_code = query_list[0]["unique_code"]
        code_count = int(get_code) + 1
        auto_code = code_key + str(code_count)
        code = auto_code
    return code


def AutoGenerateThreeDigitNumberCodeForModel(model, column):  # 001
    code = ""
    obj = model.objects.all()
    obj_count = len(obj)
    if obj_count == 0:
        code = '001'
    else:
        obj_latest = model.objects.latest('id')
        get_code = int(getattr(obj_latest, column))

        if get_code < 9:
            code_count = "00" + str((get_code + 1))
        elif get_code >= 10 & get_code < 99:
            code_count = "0" + str((get_code + 1))
        else:
            code_count = int(get_code) + 1
        # auto_code = code_key + str(code_count)
        auto_code = str(code_count)
        code = auto_code
    return code


def AutoGenerateTwoDigitNumberCodeForModel(model, column):  # 001
    code = ""
    obj = model.objects.all()
    obj_count = len(obj)
    if obj_count == 0:
        code = '001'
    else:
        obj_latest = model.objects.latest('id')
        get_code = int(getattr(obj_latest, column))

        if get_code < 9:
            code_count = "00" + str((get_code + 1))
        elif get_code >= 10 & get_code < 99:
            code_count = "0" + str((get_code + 1))
        else:
            code_count = int(get_code) + 1
        # auto_code = code_key + str(code_count)
        auto_code = str(code_count)
        code = auto_code
    return code


def AutoGenerateThreeDigitNumberCodeForModels(model, column):  # 001
    code = ""

    cursor = connections['default'].cursor()
    query_variety = " SELECT loc_code_id || city_code_id  as combine FROM tbl_location_store"
    cursor.execute(query_variety)
    PV_List = DictinctFetchAll(cursor)

    obj = model.objects.all()
    obj_count = len(obj)
    if obj_count == 0:
        code = '001'
    else:
        obj_latest = model.objects.latest('id')
        get_code = int(getattr(obj_latest, column))

        if get_code < 9:
            code_count = "00" + str((get_code + 1))
        # elif get_code >= 10 & get_code < 99:
        #     code_count = "0" + str((get_code + 1))
        else:
            code_count = int(get_code) + 1
        # auto_code = code_key + str(code_count)
        auto_code = str(code_count)
        code = auto_code
    return code


def AutoGenerateSingleDigitNumberCodeForModel(model, column):  # 1
    code = ""
    obj = model.objects.all()
    obj_count = len(obj)
    if obj_count == 0:
        code = '1'
    else:
        obj_latest = model.objects.latest('id')
        get_code = int(getattr(obj_latest, column))
        code_count = int(get_code) + 1
        auto_code = str(code_count)
        code = auto_code
    return code


def AutoGenerateNumberCodeForModel(model, column):
    code = ""
    obj = model.objects.all()
    obj_count = len(obj)
    if obj_count == 0:
        code = '01'
    else:
        obj_latest = model.objects.latest('id')
        get_code = int(getattr(obj_latest, column))

        if get_code < 9:
            code_count = "0" + str((get_code + 1))
        else:
            code_count = int(get_code) + 1
        # auto_code = code_key + str(code_count)
        auto_code = str(code_count)
        code = auto_code
    return code


def MonthCheckingEndDate(date):
    end_date = ""
    date_part = date.split("-")
    month = int(date_part[1])

    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10:
        # print("Valid Month with 31 days")
        if int(date_part[2]) == 31:
            end_date = datetime.date(int(date_part[0]), int(date_part[1]) + 1, 1)
        else:
            end_date = datetime.date(int(date_part[0]), int(date_part[1]), int(date_part[2]) + 1)

    elif month == 4 or month == 6 or month == 9 or month == 11:
        # print("Valid Month with 30 days")
        if int(date_part[2]) == 30:
            end_date = datetime.date(int(date_part[0]), int(date_part[1]) + 1, 1)
        else:
            end_date = datetime.date(int(date_part[0]), int(date_part[1]), int(date_part[2]) + 1)

    elif month == 2:
        # print("Valid Month with 29 days")
        if int(date_part[2]) == 28:
            end_date = datetime.date(int(date_part[0]), 3, 1)
        else:
            end_date = datetime.date(int(date_part[0]), int(date_part[1]), int(date_part[2]) + 1)

    elif month == 12:
        # print("Valid Month with 29 days")
        if int(date_part[2]) == 31:
            end_date = datetime.date(int(date_part[0]) + 1, 1, 1)
        else:
            end_date = datetime.date(int(date_part[0]), int(date_part[1]), int(date_part[2]) + 1)

    return end_date


def BackLimitStartDate1(date):
    start_date = ""
    date_part = date.split("-")
    month = int(date_part[1])

    if month == 1 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        # print("Valid Month with 31 days")
        if int(date_part[2]) == 1:
            start_date = datetime.date(int(date_part[0]), int(date_part[1]) - 1, 30)
        else:
            start_date = datetime.date(int(date_part[0]), int(date_part[1]), int(date_part[2]) - 1)

    elif month == 4 or month == 6 or month == 9 or month == 11:
        # print("Valid Month with 30 days")
        if int(date_part[2]) == 1:
            start_date = datetime.date(int(date_part[0]), int(date_part[1]) - 1, 31)
        else:
            start_date = datetime.date(int(date_part[0]), int(date_part[1]), int(date_part[2]) - 1)

    elif month == 3:
        # print("Valid Month with 29 days")
        if int(date_part[2]) == 1:
            start_date = datetime.date(int(date_part[0]), 2, 28)
        else:
            start_date = datetime.date(int(date_part[0]), int(date_part[1]), int(date_part[2]) - 1)

    return start_date


def BackLimitStartDate3(select_date):
    start_date = ""
    date_part = select_date.split("-")
    year = int(date_part[0])
    month = int(date_part[1])
    day = int(date_part[2])

    format_str = '%Y-%m-%d'
    current_date = datetime.datetime.now().strftime(format_str)
    d_part = current_date.split("-")
    curr_year = int(d_part[0])
    curr_month = int(d_part[1])
    curr_day = int(d_part[2])

    see_selected_date = date(year, month, day)
    get_current_date = date(curr_year, curr_month, curr_day)
    date_diff = get_current_date - see_selected_date
    get_day_diff = date_diff.days

    start_date = datetime.date(int(date_part[0]), int(date_part[1]), int(date_part[2]))
    if get_day_diff > 3:
        if month == 3:
            if day == 1:
                start_date = datetime.date(int(date_part[0]), int(date_part[1]), 27)
            elif day == 2:
                start_date = datetime.date(int(date_part[0]), int(date_part[1]), 28)
            elif day == 3:
                start_date = datetime.date(int(date_part[0]), int(date_part[1]), 28)
            else:
                start_date = datetime.date(int(date_part[0]), int(date_part[1]), int(date_part[2]) - 3)
        else:
            if day == 1:
                start_date = datetime.date(int(date_part[0]), int(date_part[1]) - 1, 29)
            elif day == 2:
                start_date = datetime.date(int(date_part[0]), int(date_part[1]) - 1, 30)
            elif day == 3:
                start_date = datetime.date(int(date_part[0]), int(date_part[1]) - 1, 30)
            else:
                start_date = datetime.date(int(date_part[0]), int(date_part[1]), int(date_part[2]) - 3)

    return start_date


def calculateAge(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def days_between(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    d3 = (d2 - d1).days
    return d3
