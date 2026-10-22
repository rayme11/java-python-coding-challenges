package enterprise.qe.api;

import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import static org.junit.jupiter.api.Assertions.*;

public class ApiTest {

    @Test
    @DisplayName("GET /posts/1 should return 200 with valid JSON")
    void testGetPost() {
        Response response = RestAssured.get("https://jsonplaceholder.typicode.com/posts/1");

        assertEquals(200, response.getStatusCode(), "Should return 200 OK");
        assertTrue(response.getBody().asString().contains("title"), "Response should contain 'title'");
        assertTrue(response.getBody().asString().contains("body"), "Response should contain 'body'");
        assertTrue(response.getBody().asString().contains("userId"), "Response should contain 'userId'");

        System.out.println("API Test PASSED: GET /posts/1 returned valid response");
    }

    @Test
    @DisplayName("GET /posts/1 should contain expected fields")
    void testPostFields() {
        Response response = RestAssured.get("https://jsonplaceholder.typicode.com/posts/1");

        int userId = response.jsonPath().getInt("userId");
        int id = response.jsonPath().getInt("id");
        String title = response.jsonPath().getString("title");
        String body = response.jsonPath().getString("body");

        assertTrue(userId > 0, "userId should be positive");
        assertTrue(id > 0, "id should be positive");
        assertNotNull(title, "title should not be null");
        assertNotNull(body, "body should not be null");
        assertFalse(title.isEmpty(), "title should not be empty");
        assertFalse(body.isEmpty(), "body should not be empty");

        System.out.println("API Test PASSED: All fields present and valid");
    }

    @Test
    @DisplayName("POST /posts should create a new resource")
    void testCreatePost() {
        String requestBody = "{\"title\":\"foo\",\"body\":\"bar\",\"userId\":1}";

        Response response = RestAssured.given()
            .header("Content-Type", "application/json")
            .body(requestBody)
            .post("https://jsonplaceholder.typicode.com/posts");

        assertEquals(201, response.getStatusCode(), "Should return 201 Created");
        assertEquals("foo", response.jsonPath().getString("title"));
        assertEquals("bar", response.jsonPath().getString("body"));
        assertEquals(1, response.jsonPath().getInt("userId"));

        System.out.println("API Test PASSED: POST /posts created new resource");
    }
}
