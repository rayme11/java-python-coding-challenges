package enterprise.qe.api;

import io.restassured.RestAssured;
import io.restassured.response.Response;

/**
 * API Test Example - Real REST Assured library for HTTP API testing.
 */
public class ApiTestExample {
    public static void main(String[] args) {
        try {
            System.out.println("Calling https://jsonplaceholder.typicode.com/posts/1...");

            Response response = RestAssured.get("https://jsonplaceholder.typicode.com/posts/1");

            int statusCode = response.getStatusCode();
            String body = response.getBody().asString();

            System.out.println("Status Code: " + statusCode);
            System.out.println("Response Body: " + body);

            if (statusCode == 200 && body.contains("title")) {
                System.out.println("Test PASSED: API returned 200 with valid JSON");
            } else {
                System.out.println("Test FAILED: Unexpected response");
            }

        } catch (Exception e) {
            System.err.println("Test ERROR: " + e.getMessage());
        }
    }
}
