package com.students.tests;

import static org.hamcrest.Matchers.*;

import java.util.ArrayList;

import org.junit.BeforeClass;
import org.junit.Test;

import com.jayway.restassured.RestAssured;
import com.jayway.restassured.http.ContentType;
import com.student.base.TestBase;
import com.student.model.Student;

import static com.jayway.restassured.RestAssured.*;


public class StudentPatchTest extends TestBase{
	
	@Test
	public void updateStudent(){
		ArrayList<String> courses = new ArrayList<>();
		courses.add("Python");
		courses.add("SQL");
		courses.add("Selenium");
		
		Student student = new Student();
		student.setFirstName("Delmas");
		student.setLastName("Buckley III");
		student.setEmail("patched@gmail.com");
		student.setProgramme("Computer Science");
		student.setCourses(courses);
		
		given()
		.contentType(ContentType.JSON)
		.when()
		.body(student)
		.patch("/101")
		.then()
		.statusCode(200);
		
	}


}
