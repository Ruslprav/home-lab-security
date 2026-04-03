# 🛡️ Cybersecurity Home-Lab & Automation

Репозиторий содержит описание конфигурации защищенного стенда и инструменты для автоматизации анализа безопасности (SIEM/Vulnerability Management).

---

### 📂 Структура проекта

#### 1. [Infrastructure Setup](./docs/hardening_check.txt)
*   **Среда:** Ubuntu Server + Windows 10 (Изолированный сегмент).
*   **Hardening:** Настройка UFW, аутентификация по SSH-ключам, минимизация портов.
*   **Цель:** Отработка навыков администрирования и защиты узлов.

#### 2. [Automation Scripts](./scripts/)
В папке `scripts` находятся инструменты на Python:
*   **`log_monitor.py`**: Анализатор логов на признаки Brute-force атак.
*   **`port_scanner.py`**: Скрипт для аудита открытых TCP-портов.

---

### 🚀 Быстрый запуск (CLI)
```bash
# Клонирование репозитория
git clone https://github.com

# Запуск сканера портов
python3 scripts/port_scanner.py
