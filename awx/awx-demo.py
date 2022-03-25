#!/usr/bin/env python3

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
from backports import configparser
import subprocess
import inspect

from splinter import Browser

global browser
global config
global awx
global pve
global git
global xte_keydown_ctrl
global xte_key_n
global xte_key_plus
global xte_keyup_ctrl

xte_keydown_ctrl = ['xte', 'keydown Control_L']
xte_key_n        = ['xte', 'key n']
xte_key_plus     = ['xte', 'key +']
xte_keyup_ctrl   = ['xte', 'keyup Control_L']
xte_key_f11      = ['xte', 'key F11']

browser = Browser('firefox')
config = configparser.ConfigParser()
config.read('awx-demo.ini')
awx = config['awx']
pve = config['pve']
git = config['git']

def go_sleep(seconds):
    if (seconds):
        print (inspect.stack()[1][3])
        time.sleep(float(seconds))

def ssh_tunel():

    ssh_pve_tunel = ['ssh', '-qfNC', pve['ssh_tunel']]
    subprocess.call(ssh_pve_tunel)
    go_sleep(pve['time_ssh_tunel'])

    ssh_awx_tunel = ['ssh', '-qfNC', awx['ssh_tunel']]
    subprocess.call(ssh_awx_tunel)
    go_sleep(awx['time_ssh_tunel'])

def toggle_fullscreen():

    subprocess.call(xte_key_f11)

def zoom():

    subprocess.call(xte_keydown_ctrl)
    subprocess.call(xte_key_plus)
    subprocess.call(xte_keyup_ctrl)

def zoom_x6():

    for i in range(0,5):
        zoom()

def go_awx():

    browser.visit(awx['url'])
    go_sleep(awx['time_url'])

    awx_username = browser.find_by_id('pf-login-username-id')
    awx_password = browser.find_by_id('pf-login-password-id')

    if (awx_username):
      browser.fill('pf-login-username-id', awx['username'])

    if (awx_password):
      browser.fill('pf-login-password-id', awx['password'])

    awx_button = browser.find_by_css('button')
    awx_button.click()
    go_sleep(awx['time_button'])

def go_pve():

    browser.visit(pve['url'])
    go_sleep(pve['time_url'])

    pve_username = browser.find_by_name(pve['username_name'])
    pve_password = browser.find_by_name(pve['password_name'])

    if (pve_username):
      browser.fill(pve['username_name'], pve['username'])

    if (pve_password):
      browser.fill(pve['password_name'], pve['password'])

    pve_button = browser.find_by_id(pve['button_id'])
    pve_button.click()

    go_sleep(pve['time_button'])

    pve_subscription = browser.find_by_id(pve['subscription_id'])

    if (pve_subscription):
        pve_subscription.click()
        go_sleep(pve['time_subscription'])

    pve_server = browser.find_by_text(pve['server_name'])
    if (pve_server):
        pve_server.click()
        go_sleep(pve['time_server'])

    pve_summary = browser.find_by_id(pve['server_summary_id'])
    if (pve_summary):
        pve_summary.click()
        go_sleep(pve['time_summary'])

    pve_server = browser.find_by_text(pve['server_name'])
    if (pve_server):
        pve_server.click()
        go_sleep(pve['time_server'])

    pve_search = browser.find_by_text(pve['server_search_text'])
    if (pve_search):
        pve_search.click()
        go_sleep(pve['time_search'])

def go_dashboard():
    go_sleep(awx['time_dashboard'])
    dashboard_menu_link = browser.find_by_text('Dashboard')
    dashboard_menu_link.click()

def go_jobs():
    go_sleep(awx['time_jobs'])
    jobs_menu_link = browser.find_by_text('Jobs')
    jobs_menu_link.click()

def go_schedules():
    go_sleep(awx['time_schedules'])
    schedules_menu_link = browser.find_by_text('Schedules')
    schedules_menu_link.click()

def go_activity_stream():
    go_sleep(awx['time_stream'])
    activity_stream_menu_link = browser.find_by_text('Activity Stream')
    activity_stream_menu_link.click()

def go_workflow_approvals():
    go_sleep(awx['time_workflow_approvals'])
    workflow_approvals_menu_link = browser.find_by_text('Workflow Approvals')
    workflow_approvals_menu_link.click()

def go_templates():
    go_sleep(awx['time_templates'])
    templates_menu_link = browser.find_by_text('Templates')
    templates_menu_link.click()

def go_credentials():
    go_sleep(awx['time_credentials'])
    credentials_menu_link = browser.find_by_text('Credentials')
    credentials_menu_link.click()

def go_projects():
    go_sleep(awx['time_projects'])
    projects_menu_link = browser.find_by_text('Projects')
    projects_menu_link.click()

def go_inventories():
    go_sleep(awx['time_inventories'])
    inventories_menu_link = browser.find_by_text('Inventories')
    inventories_menu_link.click()

def go_hosts():
    go_sleep(awx['time_hosts'])
    hosts_menu_link = browser.find_by_text('Hosts')
    hosts_menu_link.click()

def go_organizations():
    go_sleep(awx['time_organizations'])
    organizations_menu_link = browser.find_by_text('Organizations')
    organizations_menu_link.click()

def go_users():
    go_sleep(awx['time_users'])
    users_menu_link = browser.find_by_text('Users')
    users_menu_link.click()

def go_teams():
    go_sleep(awx['time_teams'])
    teams_menu_link = browser.find_by_text('Teams')
    teams_menu_link.click()

def go_credential_types():
    go_sleep(awx['time_credential_types'])
    credential_types_menu_link = browser.find_by_text('Credential Types')
    credential_types_menu_link.click()

def go_notifications():
    go_sleep(awx['time_notifications'])
    notifications_menu_link = browser.find_by_text('Notifications')
    notifications_menu_link.click()

def go_management_jobs():
    go_sleep(awx['time_jobs'])
    management_jobs_menu_link = browser.find_by_text('Management Jobs')
    management_jobs_menu_link.click()

def go_instance_groups():
    go_sleep(awx['time_groups'])
    instance_groups_menu_link = browser.find_by_text('Instance Groups')
    instance_groups_menu_link.click()

def go_applications():
    go_sleep(awx['time_applications'])
    applications_menu_link = browser.find_by_text('Applications')
    applications_menu_link.click()

def go_settings():
    go_sleep(awx['time_settings'])
    settings_menu_link = browser.find_by_text('Settings')
    settings_menu_link.click()

def new_window():
    subprocess.call(xte_keydown_ctrl)
    subprocess.call(xte_key_n)
    subprocess.call(xte_keyup_ctrl)

toggle_fullscreen()
go_awx()
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

go_pve()
go_sleep(5)

browser.quit()
