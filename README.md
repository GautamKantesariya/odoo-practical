# 🚀 Odoo Custom Module Assignment

### 📌 Developed by: **Gautam Kantesariya**

---

## 🧩 Module Overview

This custom module extends core Odoo functionality to enhance operations across Sales, Inventory, Manufacturing, and Purchase modules. It includes several usability improvements, automated workflows, and UI enhancements following Odoo best practices and coding standards.

---

## ✅ Features & Requirements

### 🔍 Partner Reference Enhancements
- All **Many2one** partner fields across the module will now support search by **Ref**.
- Display format for partner fields:  
  `PARTNER NAME [REF]`

![m2m partner](https://res.cloudinary.com/dxbzrvpb7/image/upload/v1746471022/01_dgyhna.png)

### 🏷️ Tags Management
- **All tags** from the **Sale Order** are automatically copied to the **Delivery Orders**.
- Tag search is enabled on **Delivery Orders**.
- In **Delivery Orders**:
  - Tags field visibility in **List View** is optional (configurable via Studio or XML).
  - Tags field in **Form View** is visible **only if it contains values**.
  
![sale order form](https://res.cloudinary.com/dxbzrvpb7/image/upload/v1746471021/02_oi5iqp.png)

![delivery form](https://res.cloudinary.com/dxbzrvpb7/image/upload/v1746471021/03_smsm0f.png)

![Invisible in delivery form](https://res.cloudinary.com/dxbzrvpb7/image/upload/v1746471022/06_o4tmvj.png)

![Search with Tagd in delivery](https://res.cloudinary.com/dxbzrvpb7/image/upload/v1746471023/17_t1sqcz.png)


### 🏭 Manufacturing Enhancements
- After confirming a **Manufacturing Order** created from a **Sale Order**, changing the **quantity** is **not allowed**.

![read only manufacture](https://res.cloudinary.com/dxbzrvpb7/image/upload/v1746471022/07_lk21gk.png)

![modify manufacture order](https://res.cloudinary.com/dxbzrvpb7/image/upload/v1746471022/08_g36ut9.png)


### 🛒 Purchase Enhancements
- **Purchase Orders** generated from **procurements** are **split by product category**.

![purchase order](https://res.cloudinary.com/dxbzrvpb7/image/upload/v1746471023/09_hcybpe.png)

![Created PO 1](https://res.cloudinary.com/dxbzrvpb7/image/upload/v1746471022/10_onnl6a.png)

![Created PO 2](https://res.cloudinary.com/dxbzrvpb7/image/upload/v1746471023/11_hwll2d.png)


### 📧 Automation
- When a **Delivery Order** is **delivered**, an **automated action** sends an email notification to the **Salesperson** of the associated **Sale Order**.

![Automated Action in Delivery](https://res.cloudinary.com/dxbzrvpb7/image/upload/v1746471023/12_nbeeya.png)

### 🧾 Category Uniqueness
- Product **Category names must be unique**. Duplicate names are not allowed.
![Unque Name](https://res.cloudinary.com/dxbzrvpb7/image/upload/v1746471021/13_zo52o1.png)


### 🧠 New UI Widget
- Introduced a custom **Char field widget** that allows users to **copy content to clipboard** with one click.

![Widget List](https://res.cloudinary.com/dxbzrvpb7/image/upload/v1746471021/14_j5b2dk.png)

![Widget Form](https://res.cloudinary.com/dxbzrvpb7/image/upload/v1746471022/15_xel7ib.png)


### 🔎 Default Search Filter
- Replaces default **"My Quotations"** filter with **"Sales Orders"** to show only confirmed and done orders by default.

![Default Filter SO](https://res.cloudinary.com/dxbzrvpb7/image/upload/v1746471023/16_pljudq.png)

---

## 🛠️ Technical Standards

- ✅ Clean and readable code
- ✅ Consistent naming conventions and file structure
- ✅ Fully compatible with Odoo best practices
- ✅ Tested with Odoo 18

---

## 📂 Repository Structure

```plaintext
odoo-practical/
├── gautam_prac_odoo18/
│   ├── data/
│   ├── models/
│   ├── static/
│   │   └── src/
│   │       └── widget/
│   │           └── char_copy_clipboard/
|   |
│   ├── views/
│   ├── __init__.py
│   ├── __manifest__.py
│
├── README.md

