# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

# This script imports an IATI activity from Aidstream using a direct database connection.
# For that it needs a connecion setting similar to this:
# DATABASES['aidstream'] = {
#     'ENGINE': 'django.db.backends.mysql',
#     'NAME': 'aidstream',
#     'USER': 'root',
#     'PASSWORD': 'password',
#     'HOST': 'mysql.localdev.akvo.org',
#     'PORT': '',
# }

import os
from datetime import date
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'akvo.settings'
from akvo import settings

from django.db import connections
from django.db.models import get_model

import aidstream_sql

from aidstream_sql import project

def dict_fetch_all(cursor):
    "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def aidstream_sql_for_one_model(sql, param):
    cursor = connections['aidstream'].cursor()
    cursor.execute(sql.format(param))
    rows = dict_fetch_all(cursor)
    return rows

def main(iadstream_id):
    """
    This function imports data for one RSR model at a time.

    For each model, first the call to the Aidstream database is made to fetch the raw data.
    The data is returned as a list of dicts.

    The data is processed using each model's version of the aidstream_data_cleaning() method. This method in turn calls
    the utils' function default_aidstream_cleanup() to set the project FK to the project object created (except for the
    project itself of course), sets all "string fields" to '' if the data is None and all date(time) fields to
    2000-01-01 if None.
     aidstream_data_cleaning() then proceeds with any special cases implemented for the particular model.

    It starts with the Project model and then continues with all other models for which there is a SQL
    statement defined in aidstream_sql. The Project object created is used for the project FK in all other
    models.
    """

    # TODO: implement updating of an existing RSR project
    # get the project model data
    rows = aidstream_sql_for_one_model(project, iadstream_id)
    project_data = rows[0]
    rsr_obj = get_model('rsr', 'project')
    project_data = rsr_obj.aidstream_data_cleaning(project_data)

    p = rsr_obj.objects.create(**project_data)

    # since the identifiers of the aidstream SQL are the RSR model names we can iterate over them and use them to create
    # the RSR models using get_model()
    for model, sql in aidstream_sql.__dict__.iteritems():
        # duck the built in items and 'project'
        if isinstance(sql, str) and not model.startswith('_') and model != 'project':
            rows = aidstream_sql_for_one_model(sql, iadstream_id)
            rsr_obj = get_model('rsr', model)
            for row in rows:
                row = rsr_obj.aidstream_data_cleaning(row, p)
                if row:
                    rsr_obj.objects.create(**row)


if __name__ == '__main__':
    AIDSTREAM_ID = 1234
    main(AIDSTREAM_ID)