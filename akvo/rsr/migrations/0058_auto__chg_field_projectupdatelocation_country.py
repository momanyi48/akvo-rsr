# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'ProjectUpdateLocation.country'
        db.alter_column(u'rsr_projectupdatelocation', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rsr.Country'], null=True))

    def backwards(self, orm):

        # Changing field 'ProjectUpdateLocation.country'
        db.alter_column(u'rsr_projectupdatelocation', 'country_id', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['rsr.Country']))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'rsr.benchmark': {
            'Meta': {'ordering': "('category__name', 'name__order')", 'object_name': 'Benchmark'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsr.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsr.Benchmarkname']"}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'benchmarks'", 'to': u"orm['rsr.Project']"}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        u'rsr.benchmarkname': {
            'Meta': {'ordering': "['order', 'name']", 'object_name': 'Benchmarkname'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '80'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'rsr.budgetitem': {
            'Meta': {'ordering': "('label',)", 'unique_together': "(('project', 'label'),)", 'object_name': 'BudgetItem'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'currency': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '3', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsr.BudgetItemLabel']"}),
            'other_extra': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'period_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'period_end_text': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'blank': 'True'}),
            'period_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'period_start_text': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'budget_items'", 'to': u"orm['rsr.Project']"}),
            'type': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '1', 'blank': 'True'}),
            'value_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rsr.budgetitemlabel': {
            'Meta': {'ordering': "('label',)", 'object_name': 'BudgetItemLabel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('akvo.rsr.fields.ValidXMLCharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'})
        },
        u'rsr.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            'benchmarknames': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['rsr.Benchmarkname']", 'symmetrical': 'False', 'blank': 'True'}),
            'focus_area': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'categories'", 'symmetrical': 'False', 'to': u"orm['rsr.FocusArea']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'rsr.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'continent': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '20', 'db_index': 'True'}),
            'continent_code': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '2', 'db_index': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iso_code': ('akvo.rsr.fields.ValidXMLCharField', [], {'unique': 'True', 'max_length': '2', 'db_index': 'True'}),
            'name': ('akvo.rsr.fields.ValidXMLCharField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        },
        u'rsr.countrybudgetitem': {
            'Meta': {'object_name': 'CountryBudgetItem'},
            'code': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '6', 'blank': 'True'}),
            'description': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'country_budget_items'", 'to': u"orm['rsr.Project']"}),
            'vocabulary': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '1', 'blank': 'True'})
        },
        u'rsr.focusarea': {
            'Meta': {'ordering': "['name']", 'object_name': 'FocusArea'},
            'description': ('akvo.rsr.fields.ValidXMLTextField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'link_to': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'rsr.goal': {
            'Meta': {'object_name': 'Goal'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'goals'", 'to': u"orm['rsr.Project']"}),
            'text': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'rsr.indicator': {
            'Meta': {'object_name': 'Indicator'},
            'ascending': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'baseline_comment': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'baseline_value': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'blank': 'True'}),
            'baseline_year': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '4', 'blank': 'True'}),
            'description': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'description_type': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '1', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'measure': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '1', 'blank': 'True'}),
            'result': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'indicators'", 'to': u"orm['rsr.Result']"}),
            'title': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rsr.indicatorperiod': {
            'Meta': {'object_name': 'IndicatorPeriod'},
            'actual_comment': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'actual_value': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'indicator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'periods'", 'to': u"orm['rsr.Indicator']"}),
            'period_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'period_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'target_comment': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'target_value': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'rsr.internalorganisationid': {
            'Meta': {'unique_together': "(('recording_org', 'referenced_org'),)", 'object_name': 'InternalOrganisationID'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '200'}),
            'recording_org': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'internal_ids'", 'to': u"orm['rsr.Organisation']"}),
            'referenced_org': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'reference_ids'", 'to': u"orm['rsr.Organisation']"})
        },
        u'rsr.invoice': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Invoice'},
            'amount': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'amount_received': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'bank': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '4', 'blank': 'True'}),
            'campaign_code': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '15', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'engine': ('akvo.rsr.fields.ValidXMLCharField', [], {'default': "'paypal'", 'max_length': '10'}),
            'http_referer': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ipn': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'is_anonymous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'notes': ('akvo.rsr.fields.ValidXMLTextField', [], {'default': "''", 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invoices'", 'to': u"orm['rsr.Project']"}),
            'status': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '1'}),
            'test': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'transaction_id': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        u'rsr.keyword': {
            'Meta': {'ordering': "('label',)", 'object_name': 'Keyword'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('akvo.rsr.fields.ValidXMLCharField', [], {'unique': 'True', 'max_length': '30', 'db_index': 'True'})
        },
        u'rsr.legacydata': {
            'Meta': {'object_name': 'LegacyData'},
            'iati_equivalent': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'legacy_data'", 'to': u"orm['rsr.Project']"}),
            'value': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'})
        },
        u'rsr.link': {
            'Meta': {'object_name': 'Link'},
            'caption': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50'}),
            'category': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '3', 'blank': 'True'}),
            'credit': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'blank': 'True'}),
            'format': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '1'}),
            'language': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '2', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'links'", 'to': u"orm['rsr.Project']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'rsr.minicms': {
            'Meta': {'ordering': "['-active', '-id']", 'object_name': 'MiniCMS'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'feature_box': ('akvo.rsr.fields.ValidXMLTextField', [], {'max_length': '350'}),
            'feature_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50'}),
            'lower_height': ('django.db.models.fields.IntegerField', [], {'default': '500'}),
            'top_right_box': ('akvo.rsr.fields.ValidXMLTextField', [], {'max_length': '350'})
        },
        u'rsr.molliegateway': {
            'Meta': {'object_name': 'MollieGateway'},
            'currency': ('akvo.rsr.fields.ValidXMLCharField', [], {'default': "'EUR'", 'max_length': '3'}),
            'description': ('akvo.rsr.fields.ValidXMLTextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255'}),
            'notification_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'partner_id': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '10'})
        },
        u'rsr.organisation': {
            'Meta': {'ordering': "['name']", 'object_name': 'Organisation'},
            'allow_edit': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'contact_email': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'blank': 'True'}),
            'contact_person': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '30', 'blank': 'True'}),
            'content_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsr.Organisation']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('akvo.rsr.fields.ValidXMLTextField', [], {'blank': 'True'}),
            'fax': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '20', 'blank': 'True'}),
            'iati_org_id': ('akvo.rsr.fields.ValidXMLCharField', [], {'db_index': 'True', 'max_length': '75', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_org_ids': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'recording_organisation'", 'symmetrical': 'False', 'through': u"orm['rsr.InternalOrganisationID']", 'to': u"orm['rsr.Organisation']"}),
            'language': ('akvo.rsr.fields.ValidXMLCharField', [], {'default': "'en'", 'max_length': '2'}),
            'last_modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'long_name': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '75', 'blank': 'True'}),
            'mobile': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '20', 'blank': 'True'}),
            'name': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '25', 'db_index': 'True'}),
            'new_organisation_type': ('django.db.models.fields.IntegerField', [], {'default': '22', 'db_index': 'True'}),
            'notes': ('akvo.rsr.fields.ValidXMLTextField', [], {'default': "''", 'blank': 'True'}),
            'organisation_type': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '1', 'db_index': 'True'}),
            'partner_types': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['rsr.PartnerType']", 'symmetrical': 'False'}),
            'phone': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '20', 'blank': 'True'}),
            'primary_location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsr.OrganisationLocation']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'rsr.organisationaccount': {
            'Meta': {'object_name': 'OrganisationAccount'},
            'account_level': ('akvo.rsr.fields.ValidXMLCharField', [], {'default': "'free'", 'max_length': '12'}),
            'organisation': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['rsr.Organisation']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'rsr.organisationlocation': {
            'Meta': {'ordering': "['id']", 'object_name': 'OrganisationLocation'},
            'address_1': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'address_2': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'city': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsr.Country']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('akvo.rsr.fields.LatitudeField', [], {'default': '0', 'db_index': 'True'}),
            'location_target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'null': 'True', 'to': u"orm['rsr.Organisation']"}),
            'longitude': ('akvo.rsr.fields.LongitudeField', [], {'default': '0', 'db_index': 'True'}),
            'postcode': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '10', 'blank': 'True'}),
            'state': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rsr.partnership': {
            'Meta': {'ordering': "['partner_type']", 'object_name': 'Partnership'},
            'funding_amount': ('django.db.models.fields.DecimalField', [], {'db_index': 'True', 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'iati_activity_id': ('akvo.rsr.fields.ValidXMLCharField', [], {'db_index': 'True', 'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'iati_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_id': ('akvo.rsr.fields.ValidXMLCharField', [], {'db_index': 'True', 'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'partnerships'", 'to': u"orm['rsr.Organisation']"}),
            'partner_type': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '8', 'db_index': 'True'}),
            'partner_type_extra': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'partnerships'", 'to': u"orm['rsr.Project']"}),
            'related_activity_id': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'rsr.partnersite': {
            'Meta': {'ordering': "('organisation__name',)", 'object_name': 'PartnerSite'},
            'about_box': ('akvo.rsr.fields.ValidXMLTextField', [], {'max_length': '500', 'blank': 'True'}),
            'about_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'cname': ('akvo.rsr.fields.NullCharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'custom_css': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'custom_favicon': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'custom_logo': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'custom_return_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'custom_return_url_text': ('akvo.rsr.fields.ValidXMLCharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'default_language': ('akvo.rsr.fields.ValidXMLCharField', [], {'default': "'en'", 'max_length': '5'}),
            'enabled': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'facebook_app_id': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'facebook_button': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'google_translation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hostname': ('akvo.rsr.fields.ValidXMLCharField', [], {'unique': 'True', 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'partnersites'", 'blank': 'True', 'to': u"orm['rsr.Keyword']"}),
            'last_modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'notes': ('akvo.rsr.fields.ValidXMLTextField', [], {'default': "''", 'blank': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsr.Organisation']"}),
            'partner_projects': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'twitter_button': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'ui_translation': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'rsr.partnertype': {
            'Meta': {'ordering': "('label',)", 'object_name': 'PartnerType'},
            'id': ('akvo.rsr.fields.ValidXMLCharField', [], {'unique': 'True', 'max_length': '8', 'primary_key': 'True'}),
            'label': ('akvo.rsr.fields.ValidXMLCharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'rsr.paymentgatewayselector': {
            'Meta': {'object_name': 'PaymentGatewaySelector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mollie_gateway': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['rsr.MollieGateway']"}),
            'paypal_gateway': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['rsr.PayPalGateway']"}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['rsr.Project']", 'unique': 'True'})
        },
        u'rsr.paypalgateway': {
            'Meta': {'object_name': 'PayPalGateway'},
            'account_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'currency': ('akvo.rsr.fields.ValidXMLCharField', [], {'default': "'EUR'", 'max_length': '3'}),
            'description': ('akvo.rsr.fields.ValidXMLTextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locale': ('akvo.rsr.fields.ValidXMLCharField', [], {'default': "'US'", 'max_length': '2'}),
            'name': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255'}),
            'notification_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'})
        },
        u'rsr.planneddisbursement': {
            'Meta': {'object_name': 'PlannedDisbursement'},
            'currency': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '3', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'period_end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'period_start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'planned_disbursements'", 'to': u"orm['rsr.Project']"}),
            'updated': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'value_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rsr.policymarker': {
            'Meta': {'object_name': 'PolicyMarker'},
            'description': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'policy_marker': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '2', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'policy_markers'", 'to': u"orm['rsr.Project']"}),
            'significance': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '2', 'blank': 'True'}),
            'vocabulary': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '5', 'blank': 'True'})
        },
        u'rsr.project': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Project'},
            'background': ('akvo.rsr.fields.ProjectLimitedTextField', [], {'blank': 'True'}),
            'budget': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'default': '0', 'max_digits': '10', 'blank': 'True', 'null': 'True', 'db_index': 'True'}),
            'capital_spend_percentage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'to': u"orm['rsr.Category']"}),
            'collaboration_type': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '1', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'currency': ('akvo.rsr.fields.ValidXMLCharField', [], {'default': "'EUR'", 'max_length': '3'}),
            'current_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'current_image_caption': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'blank': 'True'}),
            'current_image_credit': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'blank': 'True'}),
            'current_status': ('akvo.rsr.fields.ProjectLimitedTextField', [], {'blank': 'True'}),
            'date_end_actual': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_end_planned': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_start_actual': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_start_planned': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'default_aid_type': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '3', 'blank': 'True'}),
            'default_finance_type': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '3', 'blank': 'True'}),
            'default_flow_type': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '2', 'blank': 'True'}),
            'default_tied_status': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '1', 'blank': 'True'}),
            'donate_button': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'funds': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'default': '0', 'max_digits': '10', 'blank': 'True', 'null': 'True', 'db_index': 'True'}),
            'funds_needed': ('django.db.models.fields.DecimalField', [], {'decimal_places': '2', 'default': '0', 'max_digits': '10', 'blank': 'True', 'null': 'True', 'db_index': 'True'}),
            'goals_overview': ('akvo.rsr.fields.ProjectLimitedTextField', [], {}),
            'hierarchy': ('django.db.models.fields.PositiveIntegerField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'projects'", 'blank': 'True', 'to': u"orm['rsr.Keyword']"}),
            'language': ('akvo.rsr.fields.ValidXMLCharField', [], {'default': "'en'", 'max_length': '2'}),
            'last_modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'notes': ('akvo.rsr.fields.ValidXMLTextField', [], {'default': "''", 'blank': 'True'}),
            'partners': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'projects'", 'symmetrical': 'False', 'through': u"orm['rsr.Partnership']", 'to': u"orm['rsr.Organisation']"}),
            'primary_location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsr.ProjectLocation']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'project_plan': ('akvo.rsr.fields.ValidXMLTextField', [], {'blank': 'True'}),
            'project_plan_summary': ('akvo.rsr.fields.ProjectLimitedTextField', [], {}),
            'project_rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'project_scope': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '2', 'blank': 'True'}),
            'status': ('akvo.rsr.fields.ValidXMLCharField', [], {'default': "'N'", 'max_length': '1', 'db_index': 'True'}),
            'subtitle': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '75'}),
            'sustainability': ('akvo.rsr.fields.ValidXMLTextField', [], {}),
            'sync_owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsr.Organisation']", 'null': 'True', 'on_delete': 'models.SET_NULL'}),
            'target_group': ('akvo.rsr.fields.ProjectLimitedTextField', [], {'blank': 'True'}),
            'title': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '45', 'db_index': 'True'})
        },
        u'rsr.projectcomment': {
            'Meta': {'ordering': "('-id',)", 'object_name': 'ProjectComment'},
            'comment': ('akvo.rsr.fields.ValidXMLTextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': u"orm['rsr.Project']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'rsr.projectcondition': {
            'Meta': {'object_name': 'ProjectCondition'},
            'attached': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'conditions'", 'to': u"orm['rsr.Project']"}),
            'text': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            'type': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '1', 'blank': 'True'})
        },
        u'rsr.projectcontact': {
            'Meta': {'object_name': 'ProjectContact'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contacts'", 'null': 'True', 'to': u"orm['rsr.Country']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_title': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            'mailing_address': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'organisation': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            'person_name': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'contacts'", 'to': u"orm['rsr.Project']"}),
            'state': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            'telephone': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '15', 'blank': 'True'}),
            'type': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '1', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'rsr.projectlocation': {
            'Meta': {'ordering': "['id']", 'object_name': 'ProjectLocation'},
            'activity_description': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'address_1': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'address_2': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'administrative_code': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '25', 'blank': 'True'}),
            'administrative_level': ('django.db.models.fields.PositiveSmallIntegerField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'administrative_vocabulary': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '2', 'blank': 'True'}),
            'city': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsr.Country']"}),
            'description': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'exactness': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '1', 'blank': 'True'}),
            'feature_designation': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '5', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('akvo.rsr.fields.LatitudeField', [], {'default': '0', 'db_index': 'True'}),
            'location_class': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '1', 'blank': 'True'}),
            'location_code': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '25', 'blank': 'True'}),
            'location_reach': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '1', 'blank': 'True'}),
            'location_target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'null': 'True', 'to': u"orm['rsr.Project']"}),
            'longitude': ('akvo.rsr.fields.LongitudeField', [], {'default': '0', 'db_index': 'True'}),
            'name': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            'postcode': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '10', 'blank': 'True'}),
            'reference': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'blank': 'True'}),
            'state': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'vocabulary': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '2', 'blank': 'True'})
        },
        u'rsr.projectupdate': {
            'Meta': {'ordering': "['-id']", 'object_name': 'ProjectUpdate'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('akvo.rsr.fields.ValidXMLCharField', [], {'default': "'en'", 'max_length': '2'}),
            'last_modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'null': 'True', 'db_index': 'True', 'blank': 'True'}),
            'notes': ('akvo.rsr.fields.ValidXMLTextField', [], {'default': "''", 'blank': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'photo_caption': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '75', 'blank': 'True'}),
            'photo_credit': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '25', 'blank': 'True'}),
            'primary_location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsr.ProjectUpdateLocation']", 'null': 'True', 'on_delete': 'models.SET_NULL', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'project_updates'", 'to': u"orm['rsr.Project']"}),
            'text': ('akvo.rsr.fields.ValidXMLTextField', [], {'blank': 'True'}),
            'title': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'db_index': 'True'}),
            'update_method': ('akvo.rsr.fields.ValidXMLCharField', [], {'default': "'W'", 'max_length': '1', 'db_index': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'user_agent': ('akvo.rsr.fields.ValidXMLCharField', [], {'default': "''", 'max_length': '200', 'blank': 'True'}),
            'uuid': ('akvo.rsr.fields.ValidXMLCharField', [], {'default': "''", 'max_length': '40', 'db_index': 'True', 'blank': 'True'}),
            'video': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'video_caption': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '75', 'blank': 'True'}),
            'video_credit': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '25', 'blank': 'True'})
        },
        u'rsr.projectupdatelocation': {
            'Meta': {'ordering': "['id']", 'object_name': 'ProjectUpdateLocation'},
            'address_1': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'address_2': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'city': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsr.Country']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('akvo.rsr.fields.LatitudeField', [], {'default': '0', 'db_index': 'True'}),
            'location_target': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'locations'", 'null': 'True', 'to': u"orm['rsr.ProjectUpdate']"}),
            'longitude': ('akvo.rsr.fields.LongitudeField', [], {'default': '0', 'db_index': 'True'}),
            'postcode': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '10', 'blank': 'True'}),
            'state': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'rsr.publishingstatus': {
            'Meta': {'ordering': "('-status', 'project')", 'object_name': 'PublishingStatus'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['rsr.Project']", 'unique': 'True'}),
            'status': ('akvo.rsr.fields.ValidXMLCharField', [], {'default': "'unpublished'", 'max_length': '30'})
        },
        u'rsr.recipientcountry': {
            'Meta': {'object_name': 'RecipientCountry'},
            'country': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recipient_countries'", 'to': u"orm['rsr.Project']"}),
            'text': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'rsr.recipientregion': {
            'Meta': {'object_name': 'RecipientRegion'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recipient_regions'", 'to': u"orm['rsr.Project']"}),
            'region': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '3', 'blank': 'True'}),
            'region_vocabulary': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '1', 'blank': 'True'}),
            'text': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'rsr.result': {
            'Meta': {'object_name': 'Result'},
            'aggregation_status': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'description_type': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '1', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'results'", 'to': u"orm['rsr.Project']"}),
            'title': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'type': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '1', 'blank': 'True'})
        },
        u'rsr.sector': {
            'Meta': {'object_name': 'Sector'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'percentage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '4', 'decimal_places': '1', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sectors'", 'to': u"orm['rsr.Project']"}),
            'sector_code': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '5', 'blank': 'True'}),
            'text': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            'vocabulary': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '5', 'blank': 'True'})
        },
        u'rsr.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'aid_type': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '3', 'blank': 'True'}),
            'aid_type_text': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            'currency': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '3', 'blank': 'True'}),
            'description': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '255', 'blank': 'True'}),
            'disbursement_channel': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '1', 'blank': 'True'}),
            'disbursement_channel_text': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            'finance_type': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '3', 'blank': 'True'}),
            'finance_type_text': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            'flow_type': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '2', 'blank': 'True'}),
            'flow_type_text': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transactions'", 'to': u"orm['rsr.Project']"}),
            'provider_organisation': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            'provider_organisation_activity': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'blank': 'True'}),
            'provider_organisation_ref': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'blank': 'True'}),
            'receiver_organisation': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            'receiver_organisation_activity': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'blank': 'True'}),
            'receiver_organisation_ref': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '50', 'blank': 'True'}),
            'reference': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '25', 'blank': 'True'}),
            'tied_status': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '1', 'blank': 'True'}),
            'tied_status_text': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            'transaction_date': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'transaction_type': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '2', 'blank': 'True'}),
            'transaction_type_text': ('akvo.rsr.fields.ValidXMLCharField', [], {'max_length': '100', 'blank': 'True'}),
            'value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '1', 'blank': 'True'}),
            'value_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'rsr.userprofile': {
            'Meta': {'ordering': "['user__username']", 'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('akvo.rsr.fields.ValidXMLTextField', [], {'default': "''", 'blank': 'True'}),
            'organisation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rsr.Organisation']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'userprofile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['rsr']