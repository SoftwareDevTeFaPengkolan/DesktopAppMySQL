# DesktopAppMySQL
Aplikasi Desktop dengan Database Mysql sebagai jembatan antara Aplikasi Online dan Localhost 
cara menginstall mysql.connector
```bash
pip install mysql.connector
```
## Usage

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

print(mydb)
```
