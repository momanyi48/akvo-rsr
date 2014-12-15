# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


from django.db import models

# Custom manager based on http://www.djangosnippets.org/snippets/562/ and http://simonwillison.net/2008/May/1/orm/
from akvo.rsr.fields import ValidXMLCharField, ValidXMLTextField, ProjectLimitedTextField


class QuerySetManager(models.Manager):
    def get_queryset(self):
        return self.model.QuerySet(self.model)

    def __getattr__(self, attr, *args):
        try:
            return getattr(self.__class__, attr, *args)
        except AttributeError:
            return getattr(self.get_queryset(), attr, *args)


class OrganisationsQuerySetManager(QuerySetManager):
    def get_queryset(self):
        return self.model.OrganisationsQuerySet(self.model)

def default_aidstream_cleanup(cls, data, project):
    for name, val in data.items():
        if project:
            data['project'] = project
        model_field = cls._meta.get_field(name)
        if val is None:
            if type(model_field) in [ValidXMLCharField, ValidXMLTextField, ProjectLimitedTextField]:
                data[name] = ''
            # TODO: fix dates...
            if type(model_field) in [models.DateField, models.DateTimeField]:
                data[name] = '2000-01-01'
    return data
