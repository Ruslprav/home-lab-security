# 🛡️ Cybersecurity Home-Lab & Automation

Проект по развертыванию защищенного стенда и разработке инструментов для мониторинга и аудита безопасности (SIEM/Vulnerability Management).

---

### 📂 Структура репозитория

#### 1. [Web Security Scanner](./scripts/web_security/web_audit.py) (New 🔥)
*   **Функционал:** Автоматизированный поиск скрытых директорий и утечек конфиденциальных файлов (.env, .git, admin) методом фаззинга.
*   **Стек:** Python (requests, os).

#### 2. [Advanced Network Scanner](./scripts/advanced_scanner/main.py) 
*   **Архитектура:** Модульное ООП-приложение для аудита портов и сбора системных метрик.
*   **Стек:** Python (socket, platform).

#### 3. [Log Analysis & Hardening](./scripts/log_monitor.py)
*   **Инструменты:** Анализатор логов на признаки Brute-force атак.
*   **Документация:** [Отчеты по защите системы и результатам тестов](./docs/).

---

### 🚀 Запуск (CLI)
```bash
# Веб-аудит (требуется pip install requests)
python scripts/web_security/web_audit.py

# Системный аудит
python scripts/advanced_scanner/main.py
