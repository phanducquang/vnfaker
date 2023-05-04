import random
from datetime import datetime
from datetime import timedelta
from datetime import tzinfo
from typing import Optional

from unidecode import unidecode

from .commonUtils import CommonUtils, str_clean, change_year, date_time_ad


class Generator:

    def __init__(self):
        self.__religion_value = None
        self.__username_value = None
        self.__email_value = None
        self.__district_name = None
        self.__ward_name = None
        self.__province_name = None
        self.__known_location_value = None
        self.__name_value = None
        self.__last_name_value = None
        self.__mid_name_value = None
        self.__nickname_value = None
        self.__sentences_value = None
        self.__id_number_value = None
        self.__occupation_value = None
        self.__company_value = None
        self.__birth_date = None
        self.__gender_value = None
        self.__address_value = None
        self.__phone = None
        self.__full_name = None

    def gender(self):
        if self.__gender_value is None:
            self.__gender_value = random.choice([1, 2])
        return self.__gender_value

    def fullname(self):
        if self.__full_name is None:
            if self.__gender_value is None:
                self.gender()
            self.__last_name_value = random.choice(CommonUtils.lastNames)
            if self.__gender_value:  # man
                self.__mid_name_value = random.choice(CommonUtils.maleMidNames)
                self.__name_value = random.choice(CommonUtils.maleNames)
                self.__full_name = "{} {} {}".format(self.__last_name_value, self.__mid_name_value, self.__name_value)
            else:
                self.__mid_name_value = random.choice(CommonUtils.femaleMidNames)
                self.__name_value = random.choice(CommonUtils.femaleNames)
                self.__full_name = "{} {} {}".format(self.__last_name_value, self.__mid_name_value, self.__name_value)
        return self.__full_name

    def middle_name(self):
        if self.__full_name is None:
            self.fullname()
        return self.__mid_name_value

    def last_name(self):
        if self.__full_name is None:
            self.fullname()
        return self.__last_name_value

    def name(self):
        if self.__full_name is None:
            self.fullname()
        return self.__name_value

    def nickname(self, number_of_nick: int = 3):
        if self.__nickname_value is None:
            if number_of_nick > 10:
                number_of_nick = 10
            if self.__full_name is None:
                self.fullname()
            nickname = ["{} {}".format(self.__mid_name_value, self.__name_value),
                        "{} {}".format(self.__name_value, self.__last_name_value),
                        "{} {}".format(self.__last_name_value, self.__name_value),
                        unidecode(str_clean(self.__name_value)).lower(),
                        unidecode(str_clean(self.__mid_name_value + self.__name_value)).lower(),
                        unidecode(str_clean(
                            self.__mid_name_value + self.__name_value + random.randint(1, 999).__str__())).lower(),
                        unidecode(str_clean(self.__name_value + self.__last_name_value)).lower(),
                        unidecode(str_clean(
                            self.__name_value + self.__last_name_value + random.randint(1, 999).__str__())).lower(),
                        unidecode(str_clean(self.__last_name_value + self.__name_value)).lower(),
                        unidecode(str_clean(
                            self.__last_name_value + self.__name_value + random.randint(1, 999).__str__())).lower(),
                        unidecode(str_clean(
                            self.__name_value + self.__name_value + random.randint(1, 999).__str__())).lower()]
            nickname_value_set = [random.choice(nickname) for _ in range(random.randint(1, number_of_nick))]
            self.__nickname_value = list(set(nickname_value_set))
        return self.__nickname_value

    def email(self):
        if self.__email_value is None:
            if self.__full_name is None:
                self.fullname()
            self.__email_value = "{}@{}".format(unidecode(str_clean(self.__full_name)).lower(),
                                                random.choice(CommonUtils.domainEmail))
        return self.__email_value

    def username(self):
        if self.__username_value is None:
            if self.__nickname_value is None:
                self.nickname()
            self.__username_value = random.choice(self.__nickname_value)
        return self.__username_value

    def mobile_phone(self):
        if self.__phone is None:
            list_phone_start = [
                '086', '096', '097', '098', '032', '033', '034', '035', '036', '037', '038', '039', '090', '093', '091',
                '094',
                '083', '084', '085',
            ]
            start = random.choice(list_phone_start)
            # random 7 number from 0000000 to 9999999
            end = random.randint(0000000, 9999999)
            self.__phone = start + str(end)
        return self.__phone

    def date_of_birth(
            self,
            tz_info: Optional[tzinfo] = None,
            minimum_age: int = 0,
            maximum_age: int = 115,
            timestamp: bool = True,
    ):
        """
        Generate a random date of birth represented as a Timestamp or Date object,
        constrained by optional tz_info and minimum_age and maximum_age and timestamp
        parameters.

        :param tz_info: Defaults to None.
        :param minimum_age: Defaults to 0.
        :param maximum_age: Defaults to 115.
        :param timestamp: Defaults to True.

        :example: 852051600000 Or Date('1997-01-01')
        :return: Timestamp(Default) Or Date
        """
        if self.__birth_date is None:
            if not isinstance(minimum_age, int):
                raise TypeError("minimum_age must be an integer.")

            if not isinstance(maximum_age, int):
                raise TypeError("maximum_age must be an integer.")

            if maximum_age < 0:
                raise ValueError("maximum_age must be greater than or equal to zero.")

            if minimum_age < 0:
                raise ValueError("minimum_age must be greater than or equal to zero.")

            if minimum_age > maximum_age:
                raise ValueError("minimum_age must be less than or equal to maximum_age.")

            # In order to return the full range of possible dates of birth, add one
            # year to the potential age cap and subtract one day if we land on the
            # boundary.

            now = datetime.now(tz_info).date()
            start_date = change_year(now, -(maximum_age + 1))
            end_date = change_year(now, -minimum_age)

            dob_temp = date_time_ad(tzinfo=tz_info, start_datetime=start_date, end_datetime=end_date).date()

            self.__birth_date = dob_temp if dob_temp != start_date else dob_temp + timedelta(days=1)
        if timestamp:
            return datetime.fromisoformat(self.__birth_date.isoformat()).timestamp() * 1000
        return self.__birth_date

    def address(self):
        if self.__address_value is None:
            address_value_obj = random.choice(CommonUtils.address)
            self.__province_name = address_value_obj.get("__province_name")
            self.__ward_name = address_value_obj.get("__ward_name")
            self.__district_name = address_value_obj.get("__district_name")
            self.__address_value = "{}, {}, {}".format(self.__ward_name,
                                                       self.__district_name,
                                                       self.__province_name)
        return self.__address_value

    def address_province(self):
        if self.__address_value is None:
            self.address()
        return self.__province_name

    def address_district(self):
        if self.__address_value is None:
            self.address()
        return self.__district_name

    def address_ward(self):
        if self.__address_value is None:
            self.address()
        return self.__ward_name

    def company(self):
        if self.__company_value is None:
            self.__company_value = random.choice(CommonUtils.companyNames)
        return self.__company_value

    def known_location(self):
        if self.__known_location_value is None:
            self.__known_location_value = [random.choice(CommonUtils.address).get("__province_name") for _ in
                                           range(random.randint(1, 5))]
        return self.__known_location_value

    def occupation(self):
        if self.__occupation_value is None:
            self.__occupation_value = random.choice(CommonUtils.occupationNames)
        return self.__occupation_value

    def id_number(self, number_of_id):
        if self.__id_number_value is None:
            number = '0123456789'
            self.__id_number_value = "".join([random.choice(number) for _ in range(number_of_id)])
        return self.__id_number_value

    def sentences(self):
        if self.__sentences_value is None:
            sentences_value_temp = [random.choice(CommonUtils.sentencesValue) for _ in range(random.randint(1, 3))]
            self.__sentences_value = ". ".join(sentences_value_temp) + "."
        return self.__sentences_value

    def religion(self):
        if self.__religion_value is None:
            self.__religion_value = random.choice(CommonUtils.religionNames)
        return self.__religion_value
