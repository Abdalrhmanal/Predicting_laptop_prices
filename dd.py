import pandas as pd

# قم بتحديد مسار ملف الإكسل
excel_file_path = 'comp_encoded.xlsx'

# قراءة ملف الإكسل إلى DataFrame
df = pd.read_excel(excel_file_path)

# تحديد مسار ملف الـ CSV الذي تريد حفظه
csv_file_path = 'comp_encoded.csv'

# حفظ DataFrame كملف CSV
df.to_csv(csv_file_path, index=False)

print(f'تم تحويل {excel_file_path} إلى {csv_file_path}')
