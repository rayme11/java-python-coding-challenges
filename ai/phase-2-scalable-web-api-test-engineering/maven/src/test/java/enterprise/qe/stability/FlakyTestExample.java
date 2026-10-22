package enterprise.qe.stability;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Stability Test Example - Real JUnit 5 with retry logic for flaky test scenarios.
 */
public class FlakyTestExample {

    @Test
    @DisplayName("Test with retry logic for flaky scenarios")
    void testWithRetry() {
        int maxRetries = 3;
        boolean success = false;

        for (int i = 0; i < maxRetries; i++) {
            try {
                success = executeUnstableTest();
                if (success) {
                    System.out.println("Test PASSED on attempt " + (i + 1));
                    return;
                }
            } catch (Exception e) {
                System.out.println("Attempt " + (i + 1) + " failed: " + e.getMessage());
            }
        }

        if (!success) {
            fail("Test FAILED after " + maxRetries + " retries");
        }
    }

    @Test
    @DisplayName("Verify retry counter does not exceed maximum")
    void testRetryCounterLimit() {
        int maxRetries = 5;
        int attempts = 0;

        for (int i = 0; i < maxRetries; i++) {
            attempts++;
            if (Math.random() > 0.5) break;
        }

        assertTrue(attempts <= maxRetries, "Should not exceed max retries");
        System.out.println("Retry counter test completed in " + attempts + " attempts");
    }

    private boolean executeUnstableTest() {
        // Simulates a flaky test that passes 70% of the time
        return Math.random() > 0.3;
    }
}
