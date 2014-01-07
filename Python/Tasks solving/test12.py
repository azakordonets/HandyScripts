__author__ = 'vova'

import sys
import os

sys.path.append(os.path.dirname(__file__) + '/../../')
import pytest
import requests
from util import api
from util import mysql_api as mysql
from util import functions
import random
from resources import myconfig


@pytest.mark.delivery
class TestGlobalPolicy:
    """This case performs global policy verification"""
    host = myconfig.HOST[7:]
    db_port = "3306"
    base = "bb_console"
    db_user = "root"
    db_pass = "ep3z3ena"

    def setup_class(self):

        # logging into the system, and storing global variable SESSION
        api.get_session()
        api.clear_mysql()
        self.metadata = "{\"targeting\":{\"dayparts\":[],\"daypart_utc\":true,\"geo_targets\":[],\"gender\":[],\"education\":[],\"incomeGroup\":[],\"maritalStatus\":[],\"employmentSector\":[],\"language\":[],\"ageGroup\":[],\"categories\":[\"29\"],\"categories_ext\":[{\"children\":\"0\",\"id\":\"29\",\"name\":\"Dating\",\"parentId\":\"28\",\"parentName\":\"Society\",\"tier\":\"2\"}]},\"targeting_shared\":{\"geo_no_targeting_all\":false,\"geo_targets\":[],\"gender\":[],\"education\":[],\"incomeGroup\":[],\"maritalStatus\":[],\"employmentSector\":[],\"language\":[],\"ageGroup\":[],\"categories\":[\"29\"],\"categories_ext\":[{\"children\":\"0\",\"id\":\"29\",\"name\":\"Dating\",\"parentId\":\"28\",\"parentName\":\"Society\",\"tier\":\"2\"}],\"categories_no_targeting_all\":false}}"

    def teardown_class(self):

        # closing connection to database and switching back to default account
        api.mysql().close()
        api.account().change_account(id_part='accountId=1')

    @pytest.mark.skipif("False")
    def test_global_policy(self):

        # # creating needed entities
        accountId = api.create_default_entities().create_default_account(categories=[28, 29])['accountId']
        r = api.account().activate(id_part='?accountId=' + str(accountId))
        assert r.status_code == 200
        r = api.account().change_account(id_part='accountId=' + str(accountId))
        assert r.status_code == 200
        orderId = api.create_default_entities().create_default_order(budget=2000)['orderId']
        lineItemId = api.create_default_entities().create_default_line_item(order_id=orderId,
                                                                            metadata=self.metadata)['lineItemId']
        r = api.create_default_entities().create_default_creative(order_id=orderId, line_item_id=lineItemId,
                                                                  metadata=self.metadata)
        #Executing order
        ioId = api.order().execute(orderId)

        # importing data into SOLR
        functions.Functions().import_data_into_solr()
        requests.get(myconfig.RESOURCE_CACHE_FLUSH)
        #get our global policy rules in JSON format
        rules = self.get_categories_table()
        #go through all rules and make sure that ads are not getting delivered
        self.make_request_with_rules(rules, accountId, lineItemId)

    def get_categories_table(self):
        #This method will take all global policy rules from DB and will convert them into a json object
        mysqlIstance = mysql.MySqlDB(host=self.host, user=self.db_user, password=self.db_pass, database=self.base)
        rules_from_mysql = mysqlIstance.return_query_result("select * from `global_policy`;")
        rules_in_json_format = []
        for item in rules_from_mysql:
            rule = {"rule_id": item[0], "country_id": item[1], "age_limit": item[2], "category_id": item[3],
                    "description": item[4]}
            rules_in_json_format.append(rule)
        return rules_in_json_format

    def test(self):
        table = self.get_categories_table()
        print table

    # def make_request_with_rules(self, rules_dict, account_id, lineItemId):
    #     #we have json dictionary will all rules
    #     #we go through each rule and verify that for each country id ad is not getting delivered
    #     #for specific category id
    #     for rule in rules_dict:
    #         #define main parameters for request
    #         #If value is None, then we replace it with default
    #         country_ids = rule.get("country_id").split(" ") if rule.get("country_id") is not None else ['US']
    #         age_limit = rule.get("age_limit") if rule.get('age_limit') is not None else 25
    #         category_id = rule.get("category_id")
    #         #for every category we update our account to make sure that it has only currently needed category
    #         r = functions.Functions().update_account(account_id, categories=[category_id])
    #         #now we go through each rule and make sure that ads are not getting delivered
    #         for country in country_ids:
    #             outer_data_incl = "{\n \"app\":\"BBM\",\n \"appver\":\"2345\",\n \"channels\":[\"channel\"],\n \"blocked\":[],\n \"device\":{\n \"device\":\"9910\",\n  \"time\":\"Sat, 07 Sep 2002 00:00:01 +0300\",\n  \"platform\":\"blackberry\",\n  \"sw\" : 640,\n  \"sh\" : 480\n },\n \"demo\":[\"age/" + str(age_limit) + "\",\"country/" + str(country) + "\",\"gender/male\"],\n \"tastes\":[\"Society/Dating\"]\n}"
    #             r = api.ad().direct_request(outer_data_incl, params={},
    #                                         additions='?uid=' + str(random.randint(100000, 999999)) + '&type=SPAU',
    #                                         id_part='&pid=' + lineItemId, to_json=False)
    #             print r.text
    #             assert r.status_code != 200


if __name__ == '__main__':
    pytest.main([__file__, "-v"])



