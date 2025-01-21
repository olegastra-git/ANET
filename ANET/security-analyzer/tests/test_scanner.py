import unittest
from src.scanner.network_scanner import NetworkScanner
from src.scanner.vulnerability_checker import VulnerabilityChecker

class TestNetworkScanner(unittest.TestCase):
    def test_scan(self):
        scanner = NetworkScanner()
        result = scanner.scan()
        self.assertIsInstance(result, list)

class TestVulnerabilityChecker(unittest.TestCase):
    def test_check_vulnerabilities(self):
        checker = VulnerabilityChecker()
        vulnerabilities = checker.check_vulnerabilities()
        self.assertIsInstance(vulnerabilities, list)

if __name__ == '__main__':
    unittest.main()