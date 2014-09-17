from django.conf import settings
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models import get_app, get_models
from django.db.models.signals import post_syncdb
from akvo.utils import RSR_REST_USER

if "akvo.rsr" in settings.INSTALLED_APPS:
    from akvo.rsr import models as rsr
    def create_limited_change_permissions(sender, **kwargs):
        print "Adding RSR limited permissions"
        print
        models = [
            rsr.Organisation, rsr.Project, rsr.UserProfile, rsr.PartnerSite
        ]
        for model in models:
            opts = model._meta
            model_name = opts.object_name.lower()
            permission, created = Permission.objects.get_or_create(
                codename=u"rsr_limited_change_%s" % model_name,
                defaults={
                    'name': u'RSR limited change %s' % model_name,
                    'content_type_id': ContentType.objects.get_for_model(model).id,
                }
            )
            if created:
                print 'Created RSR limited change %s Permission' % model_name
            else:
                print 'RSR limited change %s Permission already exists in the database' % model_name

    post_syncdb.connect(create_limited_change_permissions, sender=rsr)

    def create_rest_user_permissions(sender, **kwargs):
        """ This is a temporary permission for blanket DRF API access
        """
        # TODO: replace this with granular permissions for the DRF API
        app = get_app('rsr')
        for model in get_models(app):
            opts = model._meta
            model_name = opts.object_name.lower()
            permission, created = Permission.objects.get_or_create(
                codename="{}_{}".format(RSR_REST_USER, model_name),
                defaults={
                    'name': u'RSR rest API user',
                    'content_type_id': ContentType.objects.get_for_model(model).id,
                }
            )
            if created:
                print 'Created RSR rest API user Permission for {}'.format(model_name)
            else:
                print 'RSR rest API user Permission for {} already exists in the database'.format(model_name)


    post_syncdb.connect(create_rest_user_permissions, sender=rsr)
