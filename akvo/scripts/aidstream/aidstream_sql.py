# -*- coding: utf-8 -*-

# Akvo RSR is covered by the GNU Affero General Public License.
# See more details in the license.txt file located at the root folder of the Akvo RSR module.
# For additional details on the GNU license please see < http://www.gnu.org/licenses/agpl.html >.

# SQL statements for each RSR model into which we want to import data from Aidstream.
# The identifier name for each statement is the lowercase name of ths RSR model where the data is to be used.
# This allows for direct use of the get_model helper function to create the RSR objects where the data goes.

project = """
SELECT DISTINCT
  `iati_identifier`.`text` AS `iati_activity_id`,
  `iati_document_link`.`@url` AS `current_image`,
  (SELECT DISTINCT `text` from `iati_title` WHERE `iati_title`.`@akvo_type` IS NULL AND `activity_id` = {0}) as `title`,
  (SELECT DISTINCT `text` from `iati_title` WHERE `iati_title`.`@akvo_type` = '1' AND `activity_id` = {0}) as `subtitle`,
  `iati_activity_status`.`@code` AS `status`,
  (SELECT DISTINCT `text` from `iati_description` WHERE `iati_description`.`@type` = '1' AND `iati_description`.`@akvo_type` = '5' AND `activity_id` = {0}) as project_plan_summary,
  (SELECT DISTINCT `text` from `iati_document_link/title` WHERE `iati_document_link/title`.`@akvo_type` = '1') as current_image_caption,
  (SELECT DISTINCT `text` from `iati_document_link/title` WHERE `iati_document_link/title`.`@akvo_type` = '1') as current_image_credit,
  (SELECT DISTINCT `text` from `iati_description` WHERE `iati_description`.`@type` = '2' AND `iati_description`.`@akvo_type` = '8' AND `activity_id` = {0}) as goals_overview,
  (SELECT DISTINCT `text` from `iati_description` WHERE `iati_description`.`@type` = '1' AND `iati_description`.`@akvo_type` = '9' AND `activity_id` = {0}) as current_status,
  (SELECT DISTINCT `text` from `iati_description` WHERE `iati_description`.`@type` = '1' AND `iati_description`.`@akvo_type` = '7' AND `activity_id` = {0}) as project_plan,
  (SELECT DISTINCT `text` from `iati_description` WHERE `iati_description`.`@type` = '1' AND `iati_description`.`@akvo_type` = '10' AND `activity_id` = {0}) as sustainability,
  (SELECT DISTINCT `text` from `iati_description` WHERE `iati_description`.`@type` = '3' AND `iati_description`.`@akvo_type` = '3' AND `activity_id` = {0}) as target_group,
  `iati_activity`.`@xml_lang` AS `language`,
  `iati_activity`.`@default_currency` AS `currency`,
  (SELECT DISTINCT `@iso_date` from `iati_activity_date` WHERE `iati_activity_date`.`@type` = 'start_planned' AND `activity_id` = {0}) as date_start_planned,
  (SELECT DISTINCT `@iso_date` from `iati_activity_date` WHERE `iati_activity_date`.`@type` = 'end_planned' AND `activity_id` = {0}) as date_end_planned,
  (SELECT DISTINCT `@iso_date` from `iati_activity_date` WHERE `iati_activity_date`.`@type` = 'start_actual' AND `activity_id` = {0}) as date_start_actual,
  (SELECT DISTINCT `@iso_date` from `iati_activity_date` WHERE `iati_activity_date`.`@type` = 'end_actual' AND `activity_id` = {0}) as date_end_actual,
  "Aidstream" AS `sync_owner`,
  `iati_activity`.`@hierarchy` AS `hierarchy`,
  `iati_activity_scope`.`@code` AS `project_scope`,
  `iati_capital_spend`.`@percentage` AS `capital_spend_percentage`,
  `iati_collaboration_type`.`@code` AS `collaboration_type`,
  `iati_default_aid_type`.`@code` AS `default_aid_type`,
  `iati_default_finance_type`.`@code` AS `default_finance_type`,
  `iati_default_flow_type`.`@code` AS `default_flow_type`,
  `iati_default_tied_status`.`@code` AS `default_tied_status`

FROM `iati_activity`

LEFT JOIN `iati_identifier` ON `iati_identifier`.`activity_id` = `iati_activity`.`id`
LEFT JOIN `iati_description` ON `iati_description`.`activity_id` = `iati_activity`.`id`
LEFT JOIN `iati_title` ON `iati_title`.`activity_id` = `iati_activity`.`id`
LEFT JOIN `iati_document_link` ON `iati_document_link`.`activity_id` = `iati_activity`.`id`
LEFT JOIN `iati_document_link/title` ON `iati_document_link/title`.`document_link_id` = `iati_document_link`.`id`
LEFT JOIN `iati_activity_date` ON `iati_activity_date`.`activity_id` = `iati_activity`.`id`
LEFT JOIN `iati_activity_status` ON `iati_activity_status`.`activity_id` = `iati_activity`.`id`
LEFT JOIN `iati_activity_scope` ON `iati_activity_scope`.`activity_id` = `iati_activity`.`id`
LEFT JOIN `iati_capital_spend` ON `iati_capital_spend`.`activity_id` = `iati_activity`.`id`
LEFT JOIN `iati_collaboration_type` ON `iati_collaboration_type`.`activity_id` = `iati_activity`.`id`
LEFT JOIN `iati_default_aid_type` ON `iati_default_aid_type`.`activity_id` = `iati_activity`.`id`
LEFT JOIN `iati_default_finance_type` ON `iati_default_finance_type`.`activity_id` = `iati_activity`.`id`
LEFT JOIN `iati_default_flow_type` ON `iati_default_flow_type`.`activity_id` = `iati_activity`.`id`
LEFT JOIN `iati_default_tied_status` ON `iati_default_tied_status`.`activity_id` = `iati_activity`.`id`

WHERE `iati_activity`.`id` = {0}
"""

budgetitem = """
SELECT DISTINCT
  `iati_budget`.`@type` AS type,
  `iati_budget/period_start`.`@iso_date` AS `period_start`,
  `iati_budget/period_end`.`@iso_date` AS `period_end`,
  `iati_budget/value`.`@currency` AS `currency`,
  `iati_budget/value`.`text` AS `amount`,
  `iati_budget/value`.`@akvo_type` AS `label`

FROM `iati_budget`

LEFT JOIN (
    `iati_budget/period_start`,
    `iati_budget/period_end`,
    `iati_budget/value`
)

ON (
  `iati_budget`.`id` = `iati_budget/period_start`.`budget_id` AND
  `iati_budget`.`id` = `iati_budget/period_end`.`budget_id` AND
  `iati_budget`.`id` = `iati_budget/value`.`budget_id`
)

WHERE `iati_budget`.`activity_id` = {0}
"""

projectcondition = """
SELECT DISTINCT

  `iati_conditions`.`@attached` AS	`attached`,
  `iati_conditions/condition`.`@type` AS `type`,
  `iati_conditions/condition`.`text` AS `text`

FROM `iati_conditions`

LEFT JOIN `iati_conditions/condition` ON `iati_conditions/condition`.`conditions_id` = `iati_conditions`.`id`

WHERE `iati_conditions`.`activity_id` = {0}
"""

indicatorperiod = """
SELECT DISTINCT
  `iati_result/indicator/period/period-start`.`@iso_date` AS `period_start`,
  `iati_result/indicator/period/period-end`.`@iso_date` AS `period_end`,
  `iati_result/indicator/period/target/comment`.`text` AS `target_comment`,
  `iati_result/indicator/period/target`.`@value` AS `target_value`,
  `iati_result/indicator/period/actual/comment`.`text` AS `actual_comment`,
  `iati_result/indicator/period/actual`.`@value` AS `actual_value`

FROM `iati_result/indicator/period`

LEFT JOIN `iati_result/indicator/period/period-start` ON `iati_result/indicator/period/period-start`.`period_id` = `iati_result/indicator/period`.`id`
LEFT JOIN `iati_result/indicator/period/period-end` ON `iati_result/indicator/period/period-end`.`period_id` = `iati_result/indicator/period`.`id`
LEFT JOIN `iati_result/indicator/period/target` ON `iati_result/indicator/period/target`.`period_id` = `iati_result/indicator/period`.`id`
LEFT JOIN `iati_result/indicator/period/target/comment` ON `iati_result/indicator/period/target/comment`.`target_id` = `iati_result/indicator/period/target`.`id`
LEFT JOIN `iati_result/indicator/period/actual` ON `iati_result/indicator/period/actual`.`period_id` = `iati_result/indicator/period`.`id`
LEFT JOIN `iati_result/indicator/period/actual/comment` ON `iati_result/indicator/period/actual/comment`.`actual_id` = `iati_result/indicator/period/actual`.`id`

WHERE `iati_result/indicator/period`.`indicator_id` = {0}
"""

period = """
SELECT DISTINCT
  `iati_result/indicator/period/period-start`.`@iso_date` AS `period_start`,
  `iati_result/indicator/period/period-end`.`@iso_date` AS `period_end`,
  `iati_result/indicator/period/target/comment`.`text` AS `target_comment`,
  `iati_result/indicator/period/target`.`@value` AS `target_value`,
  `iati_result/indicator/period/actual/comment`.`text` AS `actual_comment`,
  `iati_result/indicator/period/actual`.`@value` AS `actual_value`

FROM `iati_result/indicator/period`

LEFT JOIN `iati_result/indicator/period/period-start` ON `iati_result/indicator/period/period-start`.`period_id` = `iati_result/indicator/period`.`id`
LEFT JOIN `iati_result/indicator/period/period-end` ON `iati_result/indicator/period/period-end`.`period_id` = `iati_result/indicator/period`.`id`
LEFT JOIN `iati_result/indicator/period/target` ON `iati_result/indicator/period/target`.`period_id` = `iati_result/indicator/period`.`id`
LEFT JOIN `iati_result/indicator/period/target/comment` ON `iati_result/indicator/period/target/comment`.`target_id` = `iati_result/indicator/period/target`.`id`
LEFT JOIN `iati_result/indicator/period/actual` ON `iati_result/indicator/period/actual`.`period_id` = `iati_result/indicator/period`.`id`
LEFT JOIN `iati_result/indicator/period/actual/comment` ON `iati_result/indicator/period/actual/comment`.`actual_id` = `iati_result/indicator/period/actual`.`id`

WHERE `iati_result/indicator/period`.`indicator_id` = {0}
"""

# keyword = """
# SELECT DISTINCT
#   (SELECT DISTINCT `text` from `iati_description` WHERE `iati_description`.`@type` = '2' AND `iati_description`.`@akvo_type` = '8' AND `activity_id` = {0}) as `keyword`
#
# FROM `iati_description`
#
# WHERE `iati_description`.`activity_id` = {0}
# """

link = """
SELECT DISTINCT
  (SELECT DISTINCT `text` from `iati_document_link/title` WHERE `iati_document_link/title`.`@akvo_type` IS NULL AND `activity_id` = {0}) AS caption,
  `iati_document_link/category`.`@code` AS `category`,
  (SELECT DISTINCT `text` from `iati_document_link/title` WHERE `iati_document_link/title`.`@akvo_type` = '1' AND `activity_id` = {0}) AS credit,
  `iati_document_link`.`@format` AS `format`,
  `iati_document_link/language`.`text` AS `language`,
  `iati_document_link`.`@url` AS `url`


FROM `iati_document_link`

LEFT JOIN `iati_document_link/category` ON `iati_document_link/category`.`document_link_id` = `iati_document_link`.`id`
LEFT JOIN `iati_document_link/language` ON `iati_document_link/language`.`document_link_id` = `iati_document_link`.`id`
LEFT JOIN `iati_document_link/title` ON `iati_document_link/title`.`document_link_id` = `iati_document_link`.`id`


WHERE `iati_document_link`.`activity_id` = {0}
"""

partnership = """
SELECT DISTINCT
  `iati_participating_org`.`@role` AS `partner_type`,
  `iati_participating_org`.`@akvo_organsiation-id` AS `organisation`,
  `iati_other_identifier`.`@owner_ref` AS `internal_id`,
  `iati_activity`.`@linked_data_uri` AS `iati_url`

FROM `iati_activity`

LEFT JOIN `iati_participating_org` ON `iati_participating_org`.`activity_id` = `iati_activity`.`id`
LEFT JOIN `iati_other_identifier` ON `iati_other_identifier`.`activity_id` = `iati_activity`.`id`

WHERE `iati_activity`.`id` = {0}
"""

planneddisbursement = """
SELECT DISTINCT
  `iati_planned_disbursement/period_start`.`@iso_date` AS `period_end`,
  `iati_planned_disbursement/period_end`.`@iso_date` AS `period_start`,
  `iati_planned_disbursement/value`.`text` AS `value`,
  `iati_planned_disbursement/value`.`@currency` AS `currency`,
  `iati_planned_disbursement/value`.`@value_date` AS `value_date`

FROM `iati_planned_disbursement`

LEFT JOIN `iati_planned_disbursement/period_start` ON `iati_planned_disbursement/period_start`.`planned_disbursement_id` = `iati_planned_disbursement`.`id`
LEFT JOIN `iati_planned_disbursement/period_end` ON `iati_planned_disbursement/period_end`.`planned_disbursement_id` = `iati_planned_disbursement`.`id`
LEFT JOIN `iati_planned_disbursement/value` ON `iati_planned_disbursement/value`.`planned_disbursement_id` = `iati_planned_disbursement`.`id`

WHERE `iati_planned_disbursement`.`activity_id` = {0}
"""

policymarker = """
SELECT DISTINCT
  `iati_policy_marker`.`@code` AS `policy_marker`,
  `iati_policy_marker`.`@significance` AS `significance`,
  `iati_policy_marker`.`@vocabulary` AS `vocabulary`

FROM `iati_policy_marker`

WHERE `iati_policy_marker`.`activity_id` = {0}
"""


projectcontact = """
SELECT DISTINCT
  `iati_contact_info`.`@type` AS `type`,
  `iati_contact_info/email`.`text` AS `email`,
  `iati_contact_info/job_title`.`text` AS `job_title`,
  `iati_contact_info/mailing_address`.`text` AS `mailing_address`,
  `iati_contact_info/organisation`.`text` AS `organisation`,
  `iati_contact_info/person_name`.`text` AS `person_name`,
  `iati_contact_info/telephone`.`text` AS `telephone`,
  `iati_contact_info/website`.`text` AS `website`

FROM `iati_contact_info`

LEFT JOIN `iati_contact_info/email` ON `iati_contact_info/email`.`contact_info_id` = `iati_contact_info`.`id`
LEFT JOIN `iati_contact_info/job_title` ON `iati_contact_info/job_title`.`contact_info_id` = `iati_contact_info`.`id`
LEFT JOIN `iati_contact_info/mailing_address` ON `iati_contact_info/mailing_address`.`contact_info_id` = `iati_contact_info`.`id`
LEFT JOIN `iati_contact_info/organisation` ON `iati_contact_info/organisation`.`contact_info_id` = `iati_contact_info`.`id`
LEFT JOIN `iati_contact_info/person_name` ON `iati_contact_info/person_name`.`contact_info_id` = `iati_contact_info`.`id`
LEFT JOIN `iati_contact_info/telephone` ON `iati_contact_info/telephone`.`contact_info_id` = `iati_contact_info`.`id`
LEFT JOIN `iati_contact_info/website` ON `iati_contact_info/website`.`contact_info_id` = `iati_contact_info`.`id`

WHERE `iati_contact_info`.`activity_id` = {0}
"""

recipientcountry = """
SELECT DISTINCT

  `iati_recipient_country`.`@percentage` AS `percentage`,
  `iati_recipient_country`.`@code` AS `country`

FROM `iati_recipient_country`

WHERE `iati_recipient_country`.`activity_id` = {0}
"""

recipientregion = """
SELECT DISTINCT

  `iati_recipient_region`.`@percentage` AS `percentage`,
  `iati_recipient_region`.`@code` AS `region`,
  `iati_recipient_region`.`@vocabulary` AS `region_vocabulary`

FROM `iati_recipient_region`

WHERE `iati_recipient_region`.`activity_id` = {0}
"""

relatedproject = """
SELECT DISTINCT

  `iati_related_activity`.`@type` AS `relation`,
  `iati_related_activity`.`@ref` AS `related_project`

FROM `iati_related_activity`

WHERE `iati_related_activity`.`activity_id` = {0}
"""

result = """
SELECT DISTINCT
  `iati_result`.`@type` AS `type`,
  `iati_result/title`.`text` AS `title`,
  `iati_result/description`.`text` AS `description`


FROM `iati_result`

LEFT JOIN `iati_result/title` ON `iati_result/title`.`result_id` = `iati_result`.`id`
LEFT JOIN `iati_result/description` ON `iati_result/description`.`result_id` = `iati_result`.`id`

WHERE `iati_result`.`activity_id` = {0}
"""

sector = """
SELECT DISTINCT

  `iati_sector`.`@code` AS	`sector_code`,
  `iati_sector`.`@percentage` AS `percentage`,
  `iati_sector`.`@vocabulary` AS `vocabulary`

FROM `iati_sector`

WHERE `iati_sector`.`activity_id` = {0}
"""

transaction = """
SELECT DISTINCT

  `iati_transaction/aid_type`.`@code` AS	`aid_type`,
  `iati_transaction/value`.`@currency` AS `currency`,
  `iati_transaction/description`.`text` AS `description`,
  `iati_transaction/disbursement_channel`.`@code` AS `disbursement_channel`,
  `iati_transaction/finance_type`.`@code` AS	`finance_type`,
  `iati_transaction/flow_type`.`@code` AS `flow_type`,
  `iati_transaction/provider_org`.`text` AS `provider_organisation`,
  `iati_transaction/provider_org`.`@provider_activity_id` AS `provider_organisation_activity`,
  `iati_transaction/provider_org`.`@ref` AS `provider_organisation_ref`,
  `iati_transaction/receiver_org`.`text` AS `receiver_organisation`,
  `iati_transaction/receiver_org`.`@receiver_activity_id` AS `receiver_organisation_activity`,
  `iati_transaction/receiver_org`.`@ref` AS `receiver_organisation_ref`,
  `iati_transaction`.`@ref` AS `reference`,
  `iati_transaction/tied_status`.`@code`	AS `tied_status`,
  `iati_transaction/transaction_date`.`@iso_date` AS `transaction_date`,
  `iati_transaction/transaction_type`.`@code` AS `transaction_type`,
  `iati_transaction/value`.`text` AS `value`,
  `iati_transaction/value`.`@value_date` AS `value_date`

FROM `iati_transaction`

LEFT JOIN `iati_transaction/aid_type` ON `iati_transaction/aid_type`.`transaction_id` = `iati_transaction`.`id`
LEFT JOIN `iati_transaction/value` ON `iati_transaction/value`.`transaction_id` = `iati_transaction`.`id`
LEFT JOIN `iati_transaction/description` ON `iati_transaction/description`.`transaction_id` = `iati_transaction`.`id`
LEFT JOIN `iati_transaction/disbursement_channel` ON `iati_transaction/disbursement_channel`.`transaction_id` = `iati_transaction`.`id`
LEFT JOIN `iati_transaction/finance_type` ON `iati_transaction/finance_type`.`transaction_id` = `iati_transaction`.`id`
LEFT JOIN `iati_transaction/flow_type` ON `iati_transaction/flow_type`.`transaction_id` = `iati_transaction`.`id`
LEFT JOIN `iati_transaction/provider_org` ON `iati_transaction/provider_org`.`transaction_id` = `iati_transaction`.`id`
LEFT JOIN `iati_transaction/receiver_org` ON `iati_transaction/receiver_org`.`transaction_id` = `iati_transaction`.`id`
LEFT JOIN `iati_transaction/tied_status` ON `iati_transaction/tied_status`.`transaction_id` = `iati_transaction`.`id`
LEFT JOIN `iati_transaction/transaction_date` ON `iati_transaction/transaction_date`.`transaction_id` = `iati_transaction`.`id`
LEFT JOIN `iati_transaction/transaction_type` ON `iati_transaction/transaction_type`.`transaction_id` = `iati_transaction`.`id`

WHERE `iati_transaction`.`activity_id` = {0}
"""
