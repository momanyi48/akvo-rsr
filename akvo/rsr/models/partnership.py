# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


from django.db import models
from django.utils.translation import ugettext_lazy as _

from ..fields import ValidXMLCharField

from .models_utils import default_aidstream_cleanup


class Partnership(models.Model):
    FIELD_PARTNER = u'field'
    FUNDING_PARTNER = u'funding'
    SPONSOR_PARTNER = u'sponsor'
    SUPPORT_PARTNER = u'support'

    PARTNER_TYPE_LIST = [FIELD_PARTNER, FUNDING_PARTNER, SPONSOR_PARTNER, SUPPORT_PARTNER, ]
    PARTNER_LABELS = [_(u'Field partner'), _(u'Funding partner'), _(u'Sponsor partner'), _(u'Support partner'), ]

    PARTNER_TYPES = zip(PARTNER_TYPE_LIST, PARTNER_LABELS)

    ALLIANCE_PARTNER = u'alliance'
    KNOWLEDGE_PARTNER = u'knowledge'
    NETWORK_PARTNER = u'network'

    PARTNER_TYPE_EXTRAS_LIST = (ALLIANCE_PARTNER, KNOWLEDGE_PARTNER, NETWORK_PARTNER)
    PARTNER_TYPE_EXTRA_LABELS = (_(u'Alliance'), _(u'Knowledge'), _(u'Network'),)

    PARTNER_TYPE_EXTRAS = zip(PARTNER_TYPE_EXTRAS_LIST, PARTNER_TYPE_EXTRA_LABELS)

    organisation = models.ForeignKey('Organisation', verbose_name=_(u'organisation'), related_name='partnerships')
    project = models.ForeignKey('Project', verbose_name=_(u'project'), related_name='partnerships')
    partner_type = ValidXMLCharField(_(u'partner type'), max_length=8, db_index=True, choices=PARTNER_TYPES,)
    funding_amount = models.DecimalField(
        _(u'funding amount'), max_digits=10, decimal_places=2,
        blank=True, null=True, db_index=True
    )
    partner_type_extra = ValidXMLCharField(
        _(u'partner type extra'), max_length=30,
        blank=True, null=True, choices=PARTNER_TYPE_EXTRAS,
    )
    iati_activity_id = ValidXMLCharField(_(u'IATI activity ID'), max_length=75, blank=True, null=True, db_index=True,)
    internal_id = ValidXMLCharField(
        _(u'Internal ID'), max_length=75, blank=True, null=True, db_index=True,
        help_text=_(u"The organisation's internal ID for the project"),
    )
    iati_url = models.URLField(
        blank=True,
        help_text=_(
            u'Please enter the URL for where the IATI Activity Id Funding details are published. '
            u'For projects directly or indirectly funded by the Dutch Government, this should be the OpenAid.nl page. '
            u'For other projects, an alternative URL can be used.'
        )
    )
    related_activity_id = ValidXMLCharField(_(u'related IATI activity ID'), max_length=50, blank=True)

    @classmethod
    def aidstream_data_cleaning(cls, data,  project=None):
        """
        helper method to "fix" data coming from aidstream
        """
        from .organisation import Organisation
        iati_2_orgaination_role = {
            '1': 'funding',
            '2': 'support',
            '3': 'support',
            '4': 'field',
        }
        data = default_aidstream_cleanup(cls, data, project)
        if data['organisation']:
           try:
               data['organisation'] = Organisation.objects.get(pk=data['organisation'])
           except:
               return None
        data['partner_type'] = iati_2_orgaination_role[data['partner_type']]
        if data['iati_url'] is None:
            data['iati_url'] = ''
        return data

    class Meta:
        app_label = 'rsr'
        verbose_name = _(u'project partner')
        verbose_name_plural = _(u'project partners')
        ordering = ['partner_type']

    def __unicode__(self):
        return self.organisation.name
