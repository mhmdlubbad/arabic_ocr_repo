#!/usr/bin/env python3
"""
برنامج استخراج النص من ملفات PDF العربية
Arabic PDF OCR Script

هذا البرنامج يستخرج النص من ملفات PDF العربية باستخدام Tesseract OCR مع دعم اللغة العربية
This script extracts text from Arabic PDFs using Tesseract OCR with Arabic language support.
"""

import os
import tempfile
from pathlib import Path
import argparse
from pdf2image import convert_from_path
import pytesseract
from tqdm import tqdm

def extract_text_from_pdf(pdf_path, output_file=None, language='ara', dpi=300, max_pages=None):
    """
    استخراج النص من ملف PDF باستخدام Tesseract OCR مع دعم اللغة العربية
    Extract text from a PDF file using Tesseract OCR with Arabic language support.
    
    المعاملات (Args):
        pdf_path (str): مسار ملف PDF | Path to the PDF file
        output_file (str, optional): مسار لحفظ النص المستخرج. إذا كان None، يتم الطباعة على وحدة التحكم
                                    | Path to save the extracted text. If None, prints to console.
        language (str, optional): لغة التعرف الضوئي. الافتراضي هو 'ara' للعربية
                                 | Language for OCR. Default is 'ara' for Arabic.
        dpi (int, optional): دقة تحويل PDF إلى صورة. القيم الأعلى تعطي جودة أفضل لكن معالجة أبطأ
                            | DPI for PDF to image conversion. Higher values give better quality but slower processing.
        max_pages (int, optional): الحد الأقصى لعدد الصفحات للمعالجة. إذا كان None، تتم معالجة جميع الصفحات
                                  | Maximum number of pages to process. If None, processes all pages.
    
    العائد (Returns):
        str: النص المستخرج | Extracted text
    """
    # إنشاء دليل مؤقت لتخزين الصور | Create a temporary directory to store the images
    with tempfile.TemporaryDirectory() as temp_dir:
        print(f"جاري تحويل PDF إلى صور... (قد يستغرق وقتًا طويلاً للملفات الكبيرة)")
        print(f"Converting PDF to images... (This may take a while for large files)")
        
        # تحويل PDF إلى صور | Convert PDF to images
        images = convert_from_path(
            pdf_path, 
            dpi=dpi,
            output_folder=temp_dir,
            fmt="jpeg",
            grayscale=True,
            thread_count=os.cpu_count()
        )
        
        print(f"تم استخراج {len(images)} صفحة من ملف PDF.")
        print(f"Extracted {len(images)} pages from the PDF.")
        
        # تحديد عدد الصفحات إذا تم تحديد max_pages | Limit the number of pages if max_pages is specified
        if max_pages is not None and max_pages > 0:
            images = images[:max_pages]
            print(f"معالجة {len(images)} صفحات الأولى فقط.")
            print(f"Processing only the first {len(images)} pages.")
        
        # استخراج النص من كل صورة | Extract text from each image
        full_text = ""
        for i, image in enumerate(tqdm(images, desc="معالجة الصفحات | Processing pages")):
            # إعدادات Pytesseract للغة العربية | Pytesseract configuration for Arabic
            config = f'--psm 6 -l {language}'
            
            # استخراج النص من الصورة | Extract text from image
            text = pytesseract.image_to_string(image, config=config)
            
            # إضافة رقم الصفحة والنص المستخرج | Add page number and extracted text
            full_text += f"\n\n--- الصفحة {i+1} | Page {i+1} ---\n\n{text}"
        
        # حفظ أو طباعة النص المستخرج | Save or print the extracted text
        if output_file:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(full_text)
            print(f"تم حفظ النص المستخرج في {output_file}")
            print(f"Extracted text saved to {output_file}")
        
        return full_text

def main():
    """
    الدالة الرئيسية للبرنامج | Main function of the script
    """
    parser = argparse.ArgumentParser(description='استخراج النص من ملفات PDF العربية باستخدام OCR | Extract text from Arabic PDFs using OCR')
    parser.add_argument('pdf_path', help='مسار ملف PDF | Path to the PDF file')
    parser.add_argument('-o', '--output', help='مسار لحفظ النص المستخرج. إذا لم يتم تقديمه، يتم الطباعة على وحدة التحكم | Path to save the extracted text. If not provided, prints to console.')
    parser.add_argument('-l', '--language', default='ara', help='لغة التعرف الضوئي. الافتراضي هو "ara" للعربية | Language for OCR. Default is "ara" for Arabic.')
    parser.add_argument('-d', '--dpi', type=int, default=300, help='دقة تحويل PDF إلى صورة. الافتراضي هو 300 | DPI for PDF to image conversion. Default is 300.')
    parser.add_argument('-p', '--max-pages', type=int, help='الحد الأقصى لعدد الصفحات للمعالجة. إذا لم يتم تقديمه، تتم معالجة جميع الصفحات | Maximum number of pages to process. If not provided, processes all pages.')
    
    args = parser.parse_args()
    
    # التحقق مما إذا كان ملف PDF موجودًا | Check if the PDF file exists
    if not os.path.isfile(args.pdf_path):
        print(f"خطأ: الملف {args.pdf_path} غير موجود.")
        print(f"Error: The file {args.pdf_path} does not exist.")
        return
    
    # استخراج النص من PDF | Extract text from the PDF
    if not args.output:
        text = extract_text_from_pdf(args.pdf_path, language=args.language, dpi=args.dpi, max_pages=args.max_pages)
        print("\nالنص المستخرج | Extracted Text:")
        print("-" * 50)
        print(text)
    else:
        extract_text_from_pdf(args.pdf_path, args.output, args.language, args.dpi, args.max_pages)

if __name__ == "__main__":
    main()
