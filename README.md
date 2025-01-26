# bank-widget
## Работа с CSV и Excel

В проект добавлена возможность чтения финансовых транзакций из файлов формата CSV и Excel.

### Пример использования:

```python
from src.file_processing.csv_handler import read_csv_file
from src.file_processing.excel_handler import read_excel_file

csv_data = read_csv_file("data/transactions.csv")
excel_data = read_excel_file("data/transactions_excel.xlsx")
