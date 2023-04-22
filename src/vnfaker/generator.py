import random
from datetime import datetime
from datetime import timedelta
from datetime import tzinfo
from typing import Optional

from unidecode import unidecode

from .commonUtils import CommonUtils, str_clean, change_year, date_time_ad


class Generator:

    def __init__(self):
        self.email_value = None
        self.district_name = None
        self.ward_name = None
        self.province_name = None
        self.known_location_value = None
        self.name_value = None
        self.last_name_value = None
        self.mid_name_value = None
        self.nickname_value = None
        self.sentences_value = None
        self.id_number_value = None
        self.occupation_value = None
        self.company_value = None
        self.birth_date = None
        self.gender_value = None
        self.address_value = None
        self.phone = None
        self.full_name = None

    def gender(self):
        if self.gender_value is None:
            self.gender_value = random.choice([1, 2])
        return self.gender_value

    def fullname(self):
        if self.full_name is None:
            if self.gender_value is None:
                self.gender()
            self.last_name_value = random.choice(CommonUtils.lastNames)
            if self.gender_value:  # man
                self.mid_name_value = random.choice(CommonUtils.maleMidNames)
                self.name_value = random.choice(CommonUtils.maleNames)
                self.full_name = "{} {} {}".format(self.last_name_value, self.mid_name_value, self.name_value)
            else:
                self.mid_name_value = random.choice(CommonUtils.femaleMidNames)
                self.name_value = random.choice(CommonUtils.femaleNames)
                self.full_name = "{} {} {}".format(self.last_name_value, self.mid_name_value, self.name_value)
        return self.full_name

    def middle_name(self):
        if self.full_name is None:
            self.fullname()
        return self.mid_name_value

    def last_name(self):
        if self.full_name is None:
            self.fullname()
        return self.last_name_value

    def name(self):
        if self.full_name is None:
            self.fullname()
        return self.name_value

    def nickname(self, number_of_nick: int = 3):
        if self.nickname_value is None:
            if number_of_nick > 10:
                number_of_nick = 10
            if self.full_name is None:
                self.fullname()
            nickname = ["{} {}".format(self.mid_name_value, self.name_value),
                        "{} {}".format(self.name_value, self.last_name_value),
                        "{} {}".format(self.last_name_value, self.name_value),
                        unidecode(str_clean(self.name_value)).lower(),
                        unidecode(str_clean(self.mid_name_value + self.name_value)).lower(),
                        unidecode(str_clean(self.mid_name_value + self.name_value + random.randint(1, 999).__str__())).lower(),
                        unidecode(str_clean(self.name_value + self.last_name_value)).lower(),
                        unidecode(str_clean(self.name_value + self.last_name_value + random.randint(1, 999).__str__())).lower(),
                        unidecode(str_clean(self.last_name_value + self.name_value)).lower(),
                        unidecode(str_clean(self.last_name_value + self.name_value + random.randint(1, 999).__str__())).lower(),
                        unidecode(str_clean(self.name_value + self.name_value + random.randint(1, 999).__str__())).lower()]
            nickname_value_set = [random.choice(nickname) for _ in range(random.randint(1, number_of_nick))]
            self.nickname_value = list(set(nickname_value_set))
        return self.nickname_value

    def email(self):
        if self.email_value is None:
            if self.full_name is None:
                self.fullname()
            self.email_value = "{}@{}".format(unidecode(str_clean(self.full_name)).lower(), random.choice(CommonUtils.domainEmail))
        return self.email_value

    def username(self):
        if self.username_value is None:
            if self.nickname_value is None:
                self.nickname()
            self.username_value = random.choice(self.nickname_value)
        return self.username_value

    def mobile_phone(self):
        if self.phone is None:
            list_phone_start = [
                '086', '096', '097', '098', '032', '033', '034', '035', '036', '037', '038', '039', '090', '093', '091',
                '094',
                '083', '084', '085',
            ]
            start = random.choice(list_phone_start)
            # random 7 number from 0000000 to 9999999
            end = random.randint(0000000, 9999999)
            self.phone = start + str(end)
        return self.phone

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
        if self.birth_date is None:
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

            self.birth_date = dob_temp if dob_temp != start_date else dob_temp + timedelta(days=1)
        if timestamp:
            return datetime.fromisoformat(self.birth_date.isoformat()).timestamp() * 1000
        return self.birth_date

    def address(self):
        if self.address_value is None:
            address_value_obj = random.choice(CommonUtils.address)
            self.province_name = address_value_obj.get("province_name")
            self.ward_name = address_value_obj.get("ward_name")
            self.district_name = address_value_obj.get("district_name")
            self.address_value = "{}, {}, {}".format(self.ward_name,
                                                     self.district_name,
                                                     self.province_name)
        return self.address_value

    def address_province(self):
        if self.address_value is None:
            self.address()
        return self.province_name

    def address_district(self):
        if self.address_value is None:
            self.address()
        return self.district_name

    def address_ward(self):
        if self.address_value is None:
            self.address()
        return self.ward_name

    def company(self):
        if self.company_value is None:
            self.company_value = random.choice(CommonUtils.companyNames)
        return self.company_value

    def known_location(self):
        if self.known_location_value is None:
            self.known_location_value = [random.choice(CommonUtils.address).get("province_name") for _ in
                                         range(random.randint(1, 5))]
        return self.known_location_value

    def occupation(self):
        if self.occupation_value is None:
            self.occupation_value = random.choice(CommonUtils.occupationNames)
        return self.occupation_value

    def id_number(self, number_of_id):
        if self.id_number_value is None:
            number = '0123456789'
            self.id_number_value = "".join([random.choice(number) for _ in range(number_of_id)])
        return self.id_number_value

    def sentences(self):
        if self.sentences_value is None:
            sentences_value_temp = [random.choice(CommonUtils.sentencesValue) for _ in range(random.randint(1, 3))]
            self.sentences_value = ". ".join(sentences_value_temp) + "."
        return self.sentences_value
