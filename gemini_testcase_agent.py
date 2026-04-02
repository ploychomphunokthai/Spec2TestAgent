import os
import sys
import google.generativeai as genai

# ==========================================
# 1. ตั้งค่า API Key ของ Gemini 
# ==========================================
API_KEY = os.environ.get("GEMINI_API_KEY", "")
genai.configure(api_key=API_KEY)

def read_file(filepath):
    """ฟังก์ชันผู้ช่วยสำหรับอ่านเนื้อหาในไฟล์"""
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    if filepath.strip():
        print(f"⚠️ คำเตือน: ไม่พบไฟล์ '{filepath}'")
    return ""

def main():
    print("🤖 เริ่มต้น Agent สร้าง Test Case ด้วย Gemini...")
    
    # ==========================================
    # 2. อ่าน "กฎเหล็ก" (System Instructions) ที่ตายตัว
    # ==========================================
    rule_file = "AgentForCreateTestcase.md"
    system_rules = read_file(rule_file)
    if not system_rules:
        return
    print(f"✅ อ่านกฎเกณฑ์องค์กรจาก {rule_file} สำเร็จ")

    model = genai.GenerativeModel(
        model_name = os.environ.get("MODEL", ""),
        system_instruction=system_rules
    )

    # ==========================================
    # 3. ให้ระบุไฟล์เป้าหมายที่จะให้อ่าน (Dynamic ต่อการรันแต่ละครั้ง)
    # ==========================================
    print("\n--- 📂 กำหนดไฟล์ปัจจุบันที่จะแก้ไข (ลากไฟล์มาวางใน Terminal ได้เลย) ---")
    print("* หากไม่ต้องการดูไฟล์ไหน ให้ข้ามโดยกด Enter")
    
    json_path = input("📍 1. Path ไฟล์ JSON อ้างอิง: ").strip(' \'"')
    suite_path = input("📍 2. Path ไฟล์ TestSuite: ").strip(' \'"')
    kw_path = input("📍 3. Path ไฟล์ Keywords: ").strip(' \'"')

    json_content = read_file(json_path) if json_path else "ไม่มีข้อมูล JSON อ้างอิง"
    suite_content = read_file(suite_path) if suite_path else "ไม่มีข้อมูล TestSuite อ้างอิง"
    kw_content = read_file(kw_path) if kw_path else "ไม่มีข้อมูล Keywords อ้างอิง"

    # ==========================================
    # 4. รับ Spec
    # ==========================================
    spec_input = input("\n📝 4. โปรดใส่ Spec ที่ได้จาก Jira/Confluence (พิมพ์แล้วกด Enter): \n>> ").strip()
    if not spec_input:
        print("❌ ยกเลิกการรันเพราะไม่มีคำสั่ง Spec")
        return
        
    prompt = f"""
วิเคราะห์ Spec ต่อไปนี้และทำการต่อเติมรหัส Test Case ตามกฎระเบียบที่ตั้งไว้
---
Spec ข้อกำหนดใหม่ที่ต้องทำ: 
{spec_input}
---

บริบทไฟล์ในโปรเจกต์ (สำหรับเป็นต้นแบบโครงสร้าง เลียนแบบสไตล์ และรันหมายเลข Index):
1) เนื้อหาไฟล์ JSON:
{json_content}

2) เนื้อหาไฟล์ Test Suite:
{suite_content}

3) เนื้อหาไฟล์ Keywords:
{kw_content}

(ตอบกลับเป็นโค้ดใหม่ที่ถูกต้องแบบพร้อมใช้งาน พร้อมระบุชื่อไฟล์ให้ชัดเจน)
"""

    print("\n⏳ Gemini กำลังคิดและร่าง Test Case โดยอิงจากไฟล์ของคุณ...")
    
    try:
        response = model.generate_content(prompt)
        print("\n" + "="*50)
        print("✨ ผลลัพธ์จาก Gemini Agent ✨")
        print("="*50 + "\n")
        print(response.text)
        print("\n" + "="*50)
        
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาดในการเชื่อมต่อ API: {str(e)}")

if __name__ == "__main__":
    main()
