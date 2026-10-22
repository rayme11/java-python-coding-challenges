package enterprise.qe.gates;

public class ReleaseQualityGate {
    public static boolean isReleaseReady(int failedTests, double coverage, int criticalBugs, double avgResponseTime) {
        if (failedTests > 0) return false;
        if (coverage < 80.0) return false;
        if (criticalBugs > 0) return false;
        if (avgResponseTime > 2000) return false;
        return true;
    }
    
    public static void main(String[] args) {
        boolean ready = isReleaseReady(0, 85.5, 0, 1500);
        System.out.println("Release Ready: " + ready);
    }
}