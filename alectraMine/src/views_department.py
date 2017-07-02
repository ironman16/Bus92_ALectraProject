from flask import render_template, url_for, request
from src.models import cursor

#--------------departments handler-------------------------------    
def departmentsPrinter():
    
    command = """SELECT {departments}.dept_id, {departments}.dept_name, {departments}.warranty, {departments}.dept_phone, {departments}.dept_manager
    FROM {departments}
    """.format( departments = "departments")
    cursor.execute(command)
    departments_data = cursor.fetchall()
    
    return render_template('departments.html', departments_data = departments_data, URL = url_for('departmentsPrinter'))