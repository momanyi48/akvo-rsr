# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


from rest_framework import serializers

from akvo.rsr.models import Indicator, IndicatorPeriod

from .rsr_serializer import BaseRSRSerializer


class IndicatorSerializer(BaseRSRSerializer):

    class Meta:
        model = Indicator


class IndicatorPeriodSerializer(BaseRSRSerializer):

    class Meta:
        model = IndicatorPeriod
