package enterprise.qe.stability;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import static org.junit.jupiter.api.Assertions.*;

/**
 * Stability and flaky test handling examples.
 */
public class StabilityTest {

    @Test
    @DisplayName("Retry logic handles flaky test scenarios")
    void testRetryLogic() {
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
    @DisplayName("Retry counter does not exceed maximum")
    void testRetryCounterLimit() {
        int maxRetries = 5;
        int attempts = 0;

        for (int i = 0; i < maxRetries; i++) {
            attempts++;
            if (Math.random() > 0.5) break;
        }

        assertTrue(attempts <= maxRetries, "Should not exceed max retries");
        System.out.println("Stability Test PASSED: Completed in " + attempts + " attempts");
    }

    @Test
    @DisplayName("Stable test always passes")
    void testStable() {
        assertTrue(true, "Stable test should always pass");
        System.out.println("Stability Test PASSED: Stable test executed");
    }

    private boolean executeUnstableTest() {
        return Math.random() > 0.3;
    }
}
