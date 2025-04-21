import os
import pandas as pd
from pathlib import Path

def read_latest_csv(data_folder: str) -> dict:
    """
    آخرین فایل CSV را از پوشه داده‌ها می‌خواند و داده‌ها را به فرمت مشخص شده برمی‌گرداند
    
    Args:
        data_folder (str): مسیر پوشه حاوی فایل‌های CSV
        
    Returns:
        dict: دیکشنری حاوی اطلاعات مکان و داده‌ها
    """
    # تبدیل مسیر به Path object
    data_path = Path(data_folder)
    
    # پیدا کردن تمام فایل‌های CSV
    csv_files = list(data_path.glob('*.csv'))
    
    if not csv_files:
        raise FileNotFoundError(f"could not found any csv file in {data_folder}")
    
    # پیدا کردن آخرین فایل بر اساس زمان تغییر
    latest_file = max(csv_files, key=lambda x: x.stat().st_mtime)
    
    # خواندن فایل CSV
    df = pd.read_csv(latest_file)
    
    # استخراج نام ستون‌ها
    datetime = df.columns[0]
    hail = df.columns[1]
    
    # ایجاد لیست جفت‌های DateTime و MaxHail
    data_pairs = []
    for dt, h in zip(df[datetime], df[hail]):
        data_pairs.append({
            'DateTime': dt,
            'MaxHail': h
        })
    
    # ایجاد دیکشنری با ساختار مورد نظر
    # result = {
    #     'data': data_pairs
    # }
    
    return data_pairs 