package com.students.tests;

import org.junit.BeforeClass;
import org.junit.Test;

import com.jayway.restassured.RestAssured;
import com.jayway.restassured.response.Response;
import com.student.base.TestBase;

import static org.hamcrest.Matchers.*;
import static com.jayway.restassured.RestAssured.*;

public class StudentGetTest extends TestBase{
	

	@Test
	public void getAllStudentInformation(){
		/**
		 * given()
		 * initializations: cookies, auth, header, parameters
		 * .when()
		 * actions: GET,POST,PUT,DELETE
		 * .then()
		 * Validate status code, extract headers, extract response body
		 */
		
		Response response= given()
				.when()
				.get("/list");
		
		System.out.println(response.body().prettyPrint());
		
		//Validate status code
		given()
		.when()
		.get("/list")
		.then()
		.statusCode(200);
		
	}
	
	@Test
	public void getStudentInfo(){
		Response response= given()
				.when()
				.get("/1");
		
		//System.out.println(response.body().prettyPrint());
		
		//Validate status code
		given()
		.when()
		.get("/list")
		.then()
		.statusCode(200);

	}
	
	@Test
	public void getStudentsFromFA(){
		Response response= given()
				.param("programme", "Financial Analysis")
				.param("limit", 2)
				.when()
				.get("/list");
		
		System.out.println(response.prettyPeek());
	}

}
