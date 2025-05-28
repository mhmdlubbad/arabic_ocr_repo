# Arabic PDF OCR Tool | أداة استخراج النص من ملفات PDF العربية

<div dir="rtl">

## نظرة عامة
هذه أداة بسيطة وفعالة لاستخراج النص من ملفات PDF العربية باستخدام تقنية التعرف الضوئي على الحروف (OCR). تعتمد الأداة على مكتبة Tesseract OCR مع دعم اللغة العربية.

</div>

## Overview
This is a simple and effective tool for extracting text from Arabic PDF files using Optical Character Recognition (OCR) technology. The tool relies on the Tesseract OCR library with Arabic language support.

<div dir="rtl">

## المتطلبات المسبقة
قبل استخدام هذه الأداة، تحتاج إلى تثبيت:

1. **Python 3.6+**: لغة البرمجة الأساسية.
2. **Poppler**: مكتبة تستخدم لتحويل ملفات PDF إلى صور.
3. **Tesseract OCR**: محرك التعرف الضوئي على الحروف مع حزمة اللغة العربية.
4. **مكتبات Python**: المحددة في ملف `requirements.txt`.

</div>

## Prerequisites
Before using this tool, you need to install:

1. **Python 3.6+**: The primary programming language.
2. **Poppler**: A library used for converting PDF files to images.
3. **Tesseract OCR**: The OCR engine with the Arabic language package.
4. **Python libraries**: Specified in the `requirements.txt` file.

<div dir="rtl">

## دليل التثبيت

### 1. تثبيت Python
قم بتحميل وتثبيت Python من [الموقع الرسمي](https://www.python.org/downloads/).

### 2. تثبيت Poppler

#### نظام ماك (macOS):
```bash
brew install poppler
```

#### نظام لينكس (Linux):
```bash
sudo apt-get install poppler-utils
```

#### نظام ويندوز (Windows):
قم بتحميل الملفات التنفيذية من [هنا](https://github.com/oschwartz10612/poppler-windows/releases/) وإضافة المسار إلى متغيرات البيئة PATH.

### 3. تثبيت Tesseract OCR

#### نظام ماك (macOS):
```bash
brew install tesseract
brew install tesseract-lang  # لتثبيت حزم اللغات بما فيها العربية
```

#### نظام لينكس (Linux):
```bash
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-ara  # لتثبيت حزمة اللغة العربية
```

#### نظام ويندوز (Windows):
قم بتحميل وتثبيت Tesseract من [هنا](https://github.com/UB-Mannheim/tesseract/wiki) وتأكد من اختيار حزمة اللغة العربية أثناء التثبيت.

### 4. إعداد بيئة Python الافتراضية (اختياري ولكن موصى به)
```bash
# إنشاء البيئة الافتراضية
python3 -m venv arabic_ocr_env

# تفعيل البيئة الافتراضية
# على نظام ماك/لينكس
source arabic_ocr_env/bin/activate
# على نظام ويندوز
arabic_ocr_env\Scripts\activate
```

### 5. تثبيت مكتبات Python المطلوبة
```bash
pip install -r requirements.txt
```

</div>

## Installation Guide

### 1. Install Python
Download and install Python from the [official website](https://www.python.org/downloads/).

### 2. Install Poppler

#### macOS:
```bash
brew install poppler
```

#### Linux:
```bash
sudo apt-get install poppler-utils
```

#### Windows:
Download the binaries from [here](https://github.com/oschwartz10612/poppler-windows/releases/) and add the path to the PATH environment variables.

### 3. Install Tesseract OCR

#### macOS:
```bash
brew install tesseract
brew install tesseract-lang  # To install language packages including Arabic
```

#### Linux:
```bash
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-ara  # To install the Arabic language package
```

#### Windows:
Download and install Tesseract from [here](https://github.com/UB-Mannheim/tesseract/wiki) and make sure to select the Arabic language package during installation.

### 4. Set up a Python Virtual Environment (Optional but Recommended)
```bash
# Create the virtual environment
python3 -m venv arabic_ocr_env

# Activate the virtual environment
# On macOS/Linux
source arabic_ocr_env/bin/activate
# On Windows
arabic_ocr_env\Scripts\activate
```

### 5. Install Required Python Libraries
```bash
pip install -r requirements.txt
```

<div dir="rtl">

## كيفية الاستخدام

### الاستخدام الأساسي:
استخراج النص من ملف PDF وطباعته على وحدة التحكم:
```bash
python arabic_ocr.py "مسار/إلى/الملف.pdf"
```

### حفظ النص المستخرج إلى ملف:
```bash
python arabic_ocr.py "مسار/إلى/الملف.pdf" -o "النص_المستخرج.txt"
```

### معالجة عدد محدد من الصفحات فقط:
```bash
python arabic_ocr.py "مسار/إلى/الملف.pdf" -p 10 -o "النص_المستخرج.txt"
```

### تحسين جودة التعرف عن طريق زيادة دقة الصورة:
```bash
python arabic_ocr.py "مسار/إلى/الملف.pdf" -d 400 -o "النص_المستخرج.txt"
```

### الخيارات المتاحة:
- `-o, --output`: مسار لحفظ النص المستخرج
- `-l, --language`: لغة التعرف الضوئي (الافتراضي: 'ara' للعربية)
- `-d, --dpi`: دقة تحويل PDF إلى صورة (الافتراضي: 300)
- `-p, --max-pages`: الحد الأقصى لعدد الصفحات للمعالجة

</div>

## How to Use

### Basic Usage:
Extract text from a PDF file and print it to the console:
```bash
python arabic_ocr.py "path/to/file.pdf"
```

### Save the Extracted Text to a File:
```bash
python arabic_ocr.py "path/to/file.pdf" -o "extracted_text.txt"
```

### Process Only a Specific Number of Pages:
```bash
python arabic_ocr.py "path/to/file.pdf" -p 10 -o "extracted_text.txt"
```

### Improve Recognition Quality by Increasing Image Resolution:
```bash
python arabic_ocr.py "path/to/file.pdf" -d 400 -o "extracted_text.txt"
```

### Available Options:
- `-o, --output`: Path to save the extracted text
- `-l, --language`: Language for OCR (default: 'ara' for Arabic)
- `-d, --dpi`: DPI for PDF to image conversion (default: 300)
- `-p, --max-pages`: Maximum number of pages to process

<div dir="rtl">

## نصائح لتحسين دقة التعرف الضوئي

1. **استخدم دقة أعلى**: زيادة قيمة DPI (مثل 400 أو 600) قد تحسن الدقة على حساب الأداء.
2. **ملفات PDF عالية الجودة**: كلما كانت جودة ملف PDF أفضل، كانت نتائج التعرف الضوئي أدق.
3. **صفحات فردية**: إذا كان لديك مشاكل في الدقة، جرب معالجة صفحات فردية بدلاً من الملف الكامل.
4. **تعديل قيمة PSM**: يمكنك تعديل وضع تجزئة الصفحة (PSM) في الكود إذا كان لديك نتائج غير مرضية.

</div>

## Tips for Improving OCR Accuracy

1. **Use Higher Resolution**: Increasing the DPI value (like 400 or 600) can improve accuracy at the expense of performance.
2. **High-Quality PDFs**: The better the quality of the PDF file, the more accurate the OCR results.
3. **Individual Pages**: If you're having accuracy issues, try processing individual pages instead of the entire file.
4. **Adjust PSM Value**: You can modify the Page Segmentation Mode (PSM) in the code if you're getting unsatisfactory results.

<div dir="rtl">

## استكشاف الأخطاء وإصلاحها

### مشكلة: خطأ "No module named 'pdf2image'"
**الحل**: تأكد من تثبيت المكتبات المطلوبة باستخدام `pip install -r requirements.txt`.

### مشكلة: خطأ "Unable to get page count. Is poppler installed and in PATH?"
**الحل**: تأكد من تثبيت Poppler وإضافته إلى متغيرات البيئة PATH.

### مشكلة: خطأ "TesseractNotFoundError: tesseract is not installed or not in PATH"
**الحل**: تأكد من تثبيت Tesseract وإضافته إلى متغيرات البيئة PATH.

### مشكلة: نتائج OCR ضعيفة أو غير دقيقة
**الحل**: حاول زيادة قيمة DPI، وتأكد من تثبيت حزمة اللغة العربية الصحيحة، وتحقق من جودة ملف PDF الأصلي.

</div>

## Troubleshooting

### Problem: Error "No module named 'pdf2image'"
**Solution**: Make sure you have installed the required libraries using `pip install -r requirements.txt`.

### Problem: Error "Unable to get page count. Is poppler installed and in PATH?"
**Solution**: Make sure Poppler is installed and added to the PATH environment variables.

### Problem: Error "TesseractNotFoundError: tesseract is not installed or not in PATH"
**Solution**: Make sure Tesseract is installed and added to the PATH environment variables.

### Problem: Poor or inaccurate OCR results
**Solution**: Try increasing the DPI value, make sure the correct Arabic language package is installed, and check the quality of the original PDF file.

<div dir="rtl">

## المساهمة
نرحب بالمساهمات! إذا كنت ترغب في تحسين هذه الأداة، يرجى إنشاء fork للمشروع وتقديم pull request.

</div>

## Contributing
Contributions are welcome! If you'd like to improve this tool, please fork the project and submit a pull request.

<div dir="rtl">

## الترخيص
هذا المشروع مرخص تحت رخصة MIT - انظر ملف LICENSE للتفاصيل.

</div>

## License
This project is licensed under the MIT License - see the LICENSE file for details.
