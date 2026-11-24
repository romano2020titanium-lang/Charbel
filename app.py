import os
import sys
import webview

def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

if __name__ == '__main__':
    html_file = get_resource_path('index.html')
    # مسار لحفظ بيانات التطبيق (المهام والخدمات) بشكل دائم على الجهاز
    storage_dir = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'HolyFamilyPlanner')
    
    window = webview.create_window(
        title='كنيسة العائلة المقدسة — المخطط التنفيذي الأسبوعي',
        url=f'file:///{html_file}',
        width=1280,
        height=800,
        min_size=(900, 600)
    )
    
    # private_mode=False يضمن عدم مسح المهام المحفوظة عند إغلاق البرنامج
    webview.start(private_mode=False, storage_path=storage_dir)
