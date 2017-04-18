# coding: utf-8
"""
 Service to manage scheduled and conditional reporting via notifications
"""
import json
import os
import time

import MySQLdb
import unicodecsv as csv
from datetime import datetime
import base_service
import config
import utils


class ReportNotifier(base_service.BaseService):
    """
    Main class for managing the reports
    """
    inst = None

    def __init__(self):
        ReportNotifier.inst = self
        super(ReportNotifier, self).__init__()

        # The pretty name of the service
        self.pretty_name = "Report Notifier"
        # Whether the service is enabled
        self.enabled = True
        # Whether to run more than once
        self.loop = True
        # The amount of time to sleep in seconds
        self.sleep_time = 60

        self.sql_rn_conn = None
        self.rn_db = 'Report_Notifier'
        self.query_table = 'query'
        self.report_table = 'report'
        self.schedule_table = 'schedule'

        self.initialize()

    pass

    def setup(self):
        """
        Set initial variables before the run loop starts
        """
        self.sql_rn_conn = self.connect_to_sql(self.sql_rn_conn, self.rn_db, True)

        pass

    def run(self):
        """
        Runs every X seconds, the main run loop
        """
        last_run = self.find_last_run_ingest("ReportNotifier")
        last_personcourse = self.find_last_run_ingest("PersonCourse")

        if self.finished_ingestion("PersonCourse") and \
                        last_run < last_personcourse:

            reports = self.get_report_schedule()
            for report in reports:
                report_files = []
                # run the conditional reports - they don't have dates
                if report['trigger'] == 'CONDITIONAL':
                    print ("Running Conditional Report: " + report['report_name'])
                    # get queries
                    queries = self.get_query(report_code=report['report_code'])
                    for dbquery in queries:
                        # its conditional so run it
                        if dbquery['type'] == report['trigger']:
                            # execute the conditional query and get data
                            data = self.get_results(query=dbquery['query'])
                            if len(data) > 0:
                                # export the file
                                report_file = self.report2csv(report['report_code'], data)
                                report_files.append(report_file)
                            else:
                                print("No Data (report not sent): " + dbquery['description'])

                    # send the email and file if we have files
                    if len(report_files) > 0:
                        print("Sending Email: " + dbquery['description'])
                        email_data = json.loads(report['email'])

                        for path in report_files:
                            file_list = """<blockquote><blockquote>{0}</blockquote></blockquote>""".format(os.path.basename(path))

                        html = "{0} <br/><br/>" \
                               "The following report (attached) was generated by AdX Analytics on {1}: <br/> " \
                               "<blockquote><strong>{2}</strong></blockquote> " \
                               "<blockquote>Attached files:</blockquote> " \
                               "{3}<br/><br/>" \
                               "{4}".format(email_data['msg_leader'], str(datetime.now().strftime("%d/%m/%Y")),
                                            dbquery['description'], file_list, email_data['msg_sig'])
                        # to = email_data['to_email']
                        if "dev" in report_file:
                            # send only to from address
                            to = [email_data['from_email']]
                        else:
                            to = email_data['to_email']
                        # send the email
                        utils.send_mail(send_from=email_data['from_email'],
                                        send_to=to,
                                        cc_to=email_data['cc_email'],
                                        subject=report['report_name'] + ' - ' + str(datetime.now()),
                                        text=html,
                                        files=report_files)
                else:
                    # run the CALENDAR reports
                    pass

            utils.log("FINISHED REPORT NOTIFIER")
            self.save_run_ingest()
        pass

    @staticmethod
    def report2csv(report_code, data):
        """
        Generates a CSV file for report
        :return filename
        """
        print "Exporting CSV: " + report_code

        backup_path = config.EXPORT_PATH
        current_time = time.strftime('%Y%m%d-%H%M%S')
        backup_prefix = report_code + "_" + current_time
        backup_file = os.path.join(backup_path, backup_prefix.lower() + ".csv")

        with open(backup_file, "wb") as csv_file:
            writer = csv.DictWriter(csv_file, data[0].keys(), dialect='excel', delimiter=',', encoding='utf-8')
            writer.writeheader()
            # write utf-8 data
            for d in data:
                writer.writerow(dict((k, v.encode('utf-8')) for k, v in d.iteritems()))

        return backup_file

    def get_results(self, **kwargs):
        """ 
        Retrieves the data from queries 
        :return data in a dict 
        """
        cursor = self.sql_rn_conn.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(kwargs['query'])
        data = cursor.fetchall()
        cursor.close()

        return data

    def get_query(self, **kwargs):
        """ 
        Retrieves the relevant queries to be processed 
        :return queries in a dict 
        """
        query = "SELECT * FROM " + self.query_table + \
                " WHERE `report_report_code` = '" + kwargs['report_code'] + \
                "' ORDER BY `sequence` ;"
        cursor = self.sql_rn_conn.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)
        queries = cursor.fetchall()
        cursor.close()

        return queries

    def get_report_schedule(self):
        """ 
        Retrieves the relevant reports to be processed 
        :return reports in a dict 
        """
        query = "SELECT * FROM " + self.report_table + " WHERE active = 1"
        cursor = self.sql_rn_conn.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute(query)
        reports = cursor.fetchall()
        cursor.close()

        return reports


def get_files(path):
    """ 
    Returns a list of files that the service will ingest 
    :param path: The path of the files 
    :return: An array of file paths 
    """
    print path
    required_files = []
    return required_files


def name():
    """ 
    The name of the service class
    :return Name of service class
    """
    return "ReportNotifier"


def service():
    """
    Returns an instance of the service
    :return An instance of the class
    """
    return ReportNotifier()
