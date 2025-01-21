# Этот файл является точкой входа для программы анализа уязвимости и контроля утечек информации в локальной сети.

from scanner.network_scanner import NetworkScanner
from scanner.vulnerability_checker import VulnerabilityChecker
from analyzer.data_analyzer import DataAnalyzer
from analyzer.leak_detector import LeakDetector

def main():
    # Инициализация компонентов
    network_scanner = NetworkScanner()
    vulnerability_checker = VulnerabilityChecker()
    data_analyzer = DataAnalyzer()
    leak_detector = LeakDetector()

    # Запуск сканирования сети
    network_data = network_scanner.scan()
    
    # Проверка на уязвимости
    vulnerabilities = vulnerability_checker.check(network_data)
    
    # Анализ данных
    analysis_results = data_analyzer.analyze(vulnerabilities)
    
    # Обнаружение утечек
    leaks = leak_detector.detect(analysis_results)

    # Вывод результатов
    print("Результаты анализа:")
    print(analysis_results)
    print("Обнаруженные утечки:")
    print(leaks)

if __name__ == "__main__":
    main()