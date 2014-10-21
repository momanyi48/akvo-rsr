# -*- coding: utf-8 -*-

"""Akvo RSR is covered by the GNU Affero General Public License.
See more details in the license.txt file located at the root folder of the
Akvo RSR module. For additional details on the GNU license please
see < http://www.gnu.org/licenses/agpl.html >.
"""
from akvo.rsr.models import Organisation
from django.shortcuts import get_object_or_404, render


def directory(request):
    context = {'organisations': Organisation.objects.all()}
    return render(request, 'organisation_directory.html', context)


def main(request, organisation_id):
    context = {'o': get_object_or_404(Organisation, pk=organisation_id)}
    return render(request, 'organisation_main.html', context)