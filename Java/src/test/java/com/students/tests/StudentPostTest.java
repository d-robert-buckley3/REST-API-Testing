package com.students.tests;

import com.jayway.restassured.RestAssured;
import com.jayway.restassured.http.ContentType;
import com.jayway.restassured.response.Response;
import com.student.base.TestBase;
import com.student.model.Student;

import static org.hamcrest.Matchers.*;

import java.util.ArrayList;

import org.junit.BeforeClass;
import org.junit.Test;

import static com.jayway.restassured.RestAssured.*;


public class StudentPostTest extends TestBase{
	
	@Test
	public void createNewStudent(){
		ArrayList<String> courses = new ArrayList<>();
		courses.add("Python");
		courses.add("SQL");
		
		Student student = new Student();
		student.setFirstName("Robert");
		student.setLastName("Buckley");
		student.setEmail("sample@gmail.com");
		student.setProgramme("Computer Science");
		student.setCourses(courses);
		
		given()
		.contentType(ContentType.JSON)
		.when()
		.body(student)
		.post()
		.then()
		.statusCode(201);
		
	}



}
