# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.


from akvo.rsr.models import Indicator, IndicatorPeriod

from ..viewsets import BaseRSRViewSet
from ..serializers import IndicatorSerializer, IndicatorPeriodSerializer


class IndicatorViewSet(BaseRSRViewSet):
    """
    """
    queryset = Indicator.objects.all()
    serializer_class = IndicatorSerializer


class IndicatorPeriodViewSet(BaseRSRViewSet):
    """
    """
    queryset = IndicatorPeriod.objects.all()
    serializer_class = IndicatorPeriodSerializer
