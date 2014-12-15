# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import ugettext_lazy as _

from ..fields import ValidXMLCharField
from ..iati.codelists import codelists_v104 as codelists

from .models_utils import default_aidstream_cleanup


class RecipientRegion(models.Model):
    project = models.ForeignKey('Project', verbose_name=u'project', related_name='recipient_regions')
    region = ValidXMLCharField(_(u'region'), blank=True, max_length=3, choices=codelists.REGION)
    region_vocabulary = ValidXMLCharField(
        _(u'region vocabulary'), blank=True, max_length=1, choices=codelists.REGION_VOCABULARY
    )
    percentage = models.DecimalField(_(u'percentage'), blank=True, null=True, max_digits=4, decimal_places=1,
                                     validators=[MaxValueValidator(100), MinValueValidator(0)])
    text = ValidXMLCharField(_(u'region description'), blank=True, max_length=50, help_text=_(u'(max 50 characters)'))

    @classmethod
    def aidstream_data_cleaning(cls, data,  project=None):
        """
        helper method to "fix" data coming from aidstream
        """
        data = default_aidstream_cleanup(cls, data, project)
        return data

    class Meta:
        app_label = 'rsr'
        verbose_name = _(u'recipient region')
        verbose_name_plural = _(u'recipient regions')
