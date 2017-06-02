## Pythonic rendition of Udemy course REST API testing with
##     REST Assured and POSTMAN
## 2017-06-01, D. Robert Buckley, III

import requests
import unittest

class TestRESTAPICmds(unittest.TestCase):
    def setUp(self):
    	# initialize urls and sample data
    	self.baseurl = "http://localhost:8085"
    	self.posturl = "/student"
    	self.listurl = "/student/list"

    	self.student = {
    		'firstName': 'Robert',
    		'lastName':  'Buckley',
    		'email':     'sample@gmail.com',
    		'programme': 'Computer Science',
    		'courses':   ['Python', 'REST API', 'SQL']
    	}


    def tearDown(self):
    	pass

    def get_last_student_id(self):
    	# return 'id' of last student in list
    	r = requests.get(self.baseurl + self.listurl)
    	student_id = r.json()[-1]['id']
    	return student_id

    def test_get_all_student_info(self):
    	# GET entire student list
    	# Validate status code
    	# Validate initial expected list size
    	expected_db_size = 100

    	r = requests.get(self.baseurl + self.listurl)
    	self.assertEqual(r.status_code, requests.codes.ok)
    	self.assertEqual(len(r.json()), expected_db_size)

    def test_get_first_student(self):
    	# GET first student info
    	# Validate status code
    	# Validate initial expected value
    	expected_firstName = 'Vernon'

    	r = requests.get(self.baseurl + self.posturl + "/1")
    	self.assertEqual(r.status_code, requests.codes.ok)
    	self.assertEqual(r.json()['firstName'], expected_firstName)

    def test_get_students_from_FA(self):
    	# GET all students where 'programme' == 'Financial Analysis'
    	# Validate status code
    	# Validate expected collection size
    	# Validate expected 'programme' field
    	expected_length = 10
    	expected_programme = "Financial Analysis"
    	search_params = "?programme=" + expected_programme

    	r = requests.get(self.baseurl + self.listurl + search_params)
    	self.assertEqual(r.status_code, requests.codes.ok)
    	self.assertEqual(len(r.json()), expected_length)
    	self.assertEqual(r.json()[0]['programme'], expected_programme)

    def test_post_new_student(self):
    	# POST new student info
    	# Validate status code

    	r = requests.post(self.baseurl + self.posturl, json=self.student)
    	self.assertEqual(r.status_code, requests.codes.created)

    def test_put_updated_student(self):
    	# PUT updated student info
    	# Validate status code
    	# Validate updated student field
    	updated_email = 'example@hotmail.com'
    	updated_student = self.student
    	updated_student['email'] = updated_email

    	# get student id from last student in list
    	student_id = self.get_last_student_id()

    	r = requests.put(self.baseurl + self.posturl + "/" + str(student_id), json=updated_student)
    	self.assertEqual(r.status_code, requests.codes.ok)

    	r = requests.get(self.baseurl + self.posturl + "/" + str(student_id))
    	self.assertEqual(r.json()['email'], updated_email)

    def test_patch_updated_email(self):
    	# PATCH updated email info to last student
    	# Validate status code
    	# Validate new email info
    	updated_email = {'email': 'example2@yahoo.com'}

    	# get student id from last student in list
    	student_id = self.get_last_student_id()

    	r = requests.patch(self.baseurl + self.posturl + "/" + str(student_id), json=updated_email)
    	self.assertEqual(r.status_code, requests.codes.ok)

    	r = requests.get(self.baseurl + self.posturl + "/" + str(student_id))
    	self.assertEqual(r.json()['email'], updated_email['email'])

    def test_delete_last_student(self):
    	# DELETE last student in list
    	# Validate status code
    	# Validate student id deleted
    	# Validate decrease in student list size

    	student_id = self.get_last_student_id()
    	r = requests.get(self.baseurl + self.listurl)
    	previous_list_size = len(r.json())

    	r = requests.delete(self.baseurl + self.posturl + "/" + str(student_id))
    	self.assertEqual(r.status_code, requests.codes.no_content)

    	r = requests.get(self.baseurl + self.listurl)
    	self.assertLess(len(r.json()), previous_list_size)


if __name__ == "__main__":
	unittest.main()
