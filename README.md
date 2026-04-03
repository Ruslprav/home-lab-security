# 🛡️ Cybersecurity Home-Lab & Automation

Проект по развертыванию защищенной ИТ-инфраструктуры и разработке инструментов для мониторинга безопасности (SIEM/Vulnerability Management).

---

### 📂 Структура репозитория

#### 1. [Advanced Security Scanner](./scripts/advanced_scanner/main.py) (New 🚀)
*   **Архитектура:** Модульное приложение (ООП) с разделением логики.
*   **Функционал:** Сбор системных метрик ОС (`utils.py`) + многопоточное сканирование портов (`scanner.py`).
*   **Стек:** Python (socket, sys, platform).

#### 2. [Security Scripts](./scripts/)
*   **`log_monitor.py`**: Автоматический поиск признаков Brute-force атак в логах.
*   **`port_scanner.py`**: Базовый аудит сетевых интерфейсов.

#### 3. [Infrastructure & Hardening](./docs/hardening_check.txt)
*   **Конфигурация:** Описание настройки Ubuntu Server (UFW, SSH Hardening).
*   **Отчеты:** [Результаты сканирования и анализа инцидентов](./docs/).

---

### 🚀 Запуск инструментов
```bash
# Продвинутый аудит системы и сети
python scripts/advanced_scanner/main.py

# Базовый анализатор логов
python scripts/log_monitor.py
