package enterprise.qe;

public class QualityEngine {
    public static boolean evaluateQualityGate(int totalTests, int failedTests, double coveragePercentage, double minCoverageRequired) {
        if (failedTests > 0) {
            return false;
        }
        if (coveragePercentage < minCoverageRequired) {
            return false;
        }
        return true;
    }
}
