#!/usr/bin/env python

# This script comes with ABSOLUTELY NO WARRANTY, use at own risk
# Copyright (C) 2021 Osiris Alejandro Gomez <osiris@gcoop.coop>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import time
import configparser
from splinter import Browser

config = configparser.ConfigParser()		
config.read('awx-demo.ini')
awx_login = config['awx_login']

global browser

browser= Browser('firefox')
browser.visit(awx_login['url'])

login_username = browser.find_by_id('pf-login-username-id')
login_password = browser.find_by_id('pf-login-password-id')

if (login_username):
  browser.fill('pf-login-username-id', awx_login['username'])

if (login_password):
  browser.fill('pf-login-password-id', awx_login['password'])

login_button = browser.find_by_css('button')
login_button.click() 

def go_dashboard():
    time.sleep(2)
    dashboard_menu_link = browser.find_by_text('Dashboard')
    dashboard_menu_link.click()

def go_jobs():
    time.sleep(2)
    jobs_menu_link = browser.find_by_text('Jobs')
    jobs_menu_link.click()

def go_schedules():
    time.sleep(2)
    schedules_menu_link = browser.find_by_text('Schedules')
    schedules_menu_link.click()

def go_activity_stream():
    time.sleep(2)
    activity_stream_menu_link = browser.find_by_text('Activity Stream')
    activity_stream_menu_link.click()

def go_workflow_approvals():
    time.sleep(2)
    workflow_approvals_menu_link = browser.find_by_text('Workflow Approvals')
    workflow_approvals_menu_link.click()

def go_templates():
    time.sleep(2)
    templates_menu_link = browser.find_by_text('Templates')
    templates_menu_link.click()

def go_credentials():
    time.sleep(2)
    credentials_menu_link = browser.find_by_text('Credentials')
    credentials_menu_link.click()

def go_projects():
    time.sleep(2)
    projects_menu_link = browser.find_by_text('Projects')
    projects_menu_link.click()

def go_inventories():
    time.sleep(2)
    inventories_menu_link = browser.find_by_text('Inventories')
    inventories_menu_link.click()

def go_hosts():
    time.sleep(2)
    hosts_menu_link = browser.find_by_text('Hosts')
    hosts_menu_link.click()

def go_organizations():
    organizations_menu_link = browser.find_by_text('Organizations')
    organizations_menu_link.click()
    time.sleep(2)

def go_users():
    time.sleep(2)
    users_menu_link = browser.find_by_text('Users')
    users_menu_link.click()

def go_teams():
    time.sleep(2)
    teams_menu_link = browser.find_by_text('Teams')
    teams_menu_link.click()

def go_credential_types():
    time.sleep(2)
    credential_types_menu_link = browser.find_by_text('Credential Types')
    credential_types_menu_link.click()

def go_notifications():
    time.sleep(2)
    notifications_menu_link = browser.find_by_text('Notifications')
    notifications_menu_link.click()

def go_management_jobs():
    time.sleep(2)
    management_jobs_menu_link = browser.find_by_text('Management Jobs')
    management_jobs_menu_link.click()

def go_instance_groups():
    time.sleep(2)
    instance_groups_menu_link = browser.find_by_text('Instance Groups')
    instance_groups_menu_link.click()

def go_applications():
    time.sleep(2)
    applications_menu_link = browser.find_by_text('Applications')
    applications_menu_link.click()

def go_settings():
    time.sleep(2)
    settings_menu_link = browser.find_by_text('Settings')
    settings_menu_link.click()

go_dashboard()
go_jobs()
go_schedules()
go_activity_stream()
go_workflow_approvals()
go_templates()
go_credentials()
go_projects()
go_inventories()
go_hosts()
go_organizations()
go_users()
go_teams()
go_credential_types()
go_notifications()
go_management_jobs()
go_instance_groups()
go_applications()
go_settings()
