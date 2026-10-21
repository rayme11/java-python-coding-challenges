package enterprise.qe;

public class QualityEngineTest {
    public static void main(String[] args) {
        System.out.println("Running Enterprise Quality Engine Tests...");

        // Test 1: Passing Quality Gate
        boolean result1 = QualityEngine.evaluateQualityGate(100, 0, 85.5, 80.0);
        assert result1 == true : "Test 1 Failed: Should pass quality gate";

        // Test 2: Failing due to test failures
        boolean result2 = QualityEngine.evaluateQualityGate(100, 2, 85.5, 80.0);
        assert result2 == false : "Test 2 Failed: Should fail due to test failures";

        // Test 3: Failing due to low coverage
        boolean result3 = QualityEngine.evaluateQualityGate(100, 0, 75.0, 80.0);
        assert result3 == false : "Test 3 Failed: Should fail due to insufficient coverage";

        System.out.println("All Enterprise Quality Engine Tests Passed Successfully!");
    }
}
