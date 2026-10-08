import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="NOVA MART POS",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# COMPLETE SUPERMARKET POS
# ============================================================

HTML = r"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>NOVA MART POS</title>

<style>

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

:root {
    --bg: #07110d;
    --panel: #0e1a15;
    --panel2: #13221b;
    --card: #101d17;
    --border: rgba(255,255,255,.08);
    --text: #f5f8f6;
    --muted: #8fa39a;
    --green: #29d391;
    --green2: #16a96f;
    --orange: #ffb13b;
    --red: #ff6262;
    --blue: #61a8ff;
}

body {
    font-family:
        Inter,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        Arial,
        sans-serif;

    min-height: 100vh;

    color: var(--text);

    background:
        radial-gradient(
            circle at 10% 0%,
            rgba(41,211,145,.10),
            transparent 28%
        ),
        radial-gradient(
            circle at 100% 80%,
            rgba(255,177,59,.07),
            transparent 28%
        ),
        var(--bg);
}

/* ============================================================
HEADER
============================================================ */

.header {

    height: 76px;

    padding: 0 28px;

    display: flex;

    align-items: center;

    justify-content: space-between;

    position: sticky;

    top: 0;

    z-index: 100;

    background:
        rgba(7,17,13,.90);

    backdrop-filter: blur(18px);

    border-bottom:
        1px solid var(--border);

}

.brand {

    display: flex;

    align-items: center;

    gap: 13px;

}

.logo {

    width: 46px;

    height: 46px;

    border-radius: 14px;

    display: grid;

    place-items: center;

    font-size: 24px;

    background:
        linear-gradient(
            135deg,
            var(--green),
            var(--green2)
        );

    box-shadow:
        0 10px 30px
        rgba(41,211,145,.22);

}

.brand h1 {

    font-size: 19px;

    font-weight: 900;

    letter-spacing: .7px;

}

.brand p {

    color: var(--muted);

    font-size: 11px;

    margin-top: 3px;

}

.status {

    display: flex;

    align-items: center;

    gap: 8px;

    padding: 9px 14px;

    border-radius: 999px;

    border:
        1px solid
        rgba(41,211,145,.20);

    background:
        rgba(41,211,145,.06);

    color: #8ce8c4;

    font-size: 11px;

    font-weight: 800;

}

.status-dot {

    width: 8px;

    height: 8px;

    border-radius: 50%;

    background: var(--green);

    box-shadow:
        0 0 14px var(--green);

    animation: pulse 1.8s infinite;

}

@keyframes pulse {

    50% {

        opacity: .4;

        transform: scale(.7);

    }

}

/* ============================================================
MAIN
============================================================ */

.main {

    max-width: 1550px;

    margin: auto;

    padding: 28px;

    display: grid;

    grid-template-columns:
        minmax(0, 1fr)
        400px;

    gap: 24px;

}

/* ============================================================
MENU
============================================================ */

.menu-panel,
.bill-panel {

    background:
        rgba(14,26,21,.90);

    border:
        1px solid var(--border);

    border-radius: 24px;

    box-shadow:
        0 20px 60px rgba(0,0,0,.30);

    overflow: hidden;

}

.menu-top {

    padding: 24px 24px 0;

}

.menu-title {

    display: flex;

    align-items: center;

    justify-content: space-between;

    gap: 20px;

    margin-bottom: 20px;

}

.menu-title h2 {

    font-size: 25px;

}

.menu-title p {

    color: var(--muted);

    font-size: 13px;

    margin-top: 5px;

}

.search {

    width: 290px;

    padding: 13px 16px;

    border-radius: 13px;

    background: #09130f;

    border:
        1px solid var(--border);

    color: white;

    outline: none;

    transition: .2s;

}

.search:focus {

    border-color:
        rgba(41,211,145,.5);

    box-shadow:
        0 0 0 4px
        rgba(41,211,145,.08);

}

.categories {

    display: flex;

    gap: 8px;

    overflow-x: auto;

    padding-bottom: 20px;

}

.category {

    border:
        1px solid var(--border);

    background: #0a1510;

    color: var(--muted);

    padding: 10px 15px;

    border-radius: 999px;

    white-space: nowrap;

    cursor: pointer;

    font-size: 12px;

    font-weight: 800;

    transition: .2s;

}

.category:hover {

    transform: translateY(-1px);

    color: white;

}

.category.active {

    color: #06110c;

    border-color: transparent;

    background:
        linear-gradient(
            135deg,
            var(--green),
            #7bf0bc
        );

}

/* ============================================================
PRODUCT GRID
============================================================ */

.products {

    padding:
        0 24px 24px;

    display: grid;

    grid-template-columns:
        repeat(
            auto-fill,
            minmax(190px, 1fr)
        );

    gap: 14px;

}

.product {

    padding: 15px;

    border-radius: 18px;

    border:
        1px solid var(--border);

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,.045),
            rgba(255,255,255,.012)
        );

    cursor: pointer;

    transition:
        transform .2s,
        border-color .2s,
        box-shadow .2s;

}

.product:hover {

    transform:
        translateY(-4px);

    border-color:
        rgba(41,211,145,.35);

    box-shadow:
        0 16px 35px
        rgba(0,0,0,.25);

}

.product-image {

    height: 105px;

    border-radius: 14px;

    display: grid;

    place-items: center;

    font-size: 49px;

    margin-bottom: 13px;

    background:
        radial-gradient(
            circle,
            rgba(41,211,145,.13),
            rgba(255,255,255,.02)
        );

}

.product-name {

    font-size: 14px;

    font-weight: 900;

    margin-bottom: 5px;

}

.product-desc {

    min-height: 30px;

    color: var(--muted);

    font-size: 11px;

    line-height: 1.4;

}

.product-bottom {

    display: flex;

    align-items: center;

    justify-content: space-between;

    margin-top: 13px;

}

.price {

    color: var(--green);

    font-size: 17px;

    font-weight: 950;

}

.add-btn {

    width: 35px;

    height: 35px;

    border: 0;

    border-radius: 11px;

    cursor: pointer;

    font-size: 21px;

    color: #06110c;

    background:
        linear-gradient(
            135deg,
            var(--green),
            #8bf2c3
        );

    transition: .2s;

}

.add-btn:hover {

    transform: scale(1.08);

}

/* ============================================================
BILL PANEL
============================================================ */

.bill-panel {

    position: sticky;

    top: 100px;

    height:
        calc(100vh - 128px);

    display: flex;

    flex-direction: column;

}

.bill-head {

    padding: 21px 22px;

    border-bottom:
        1px solid var(--border);

}

.bill-head-row {

    display: flex;

    align-items: center;

    justify-content: space-between;

}

.bill-head h2 {

    font-size: 21px;

}

.bill-number {

    color: var(--muted);

    font-size: 11px;

    margin-top: 5px;

}

.new-btn {

    padding: 9px 12px;

    border-radius: 10px;

    border:
        1px solid var(--border);

    background: #0a1510;

    color: white;

    cursor: pointer;

    font-size: 11px;

    font-weight: 800;

}

.new-btn:hover {

    border-color:
        var(--green);

}

/* ============================================================
CUSTOMER
============================================================ */

.customer {

    padding: 15px 22px;

    display: grid;

    grid-template-columns: 1fr 1fr;

    gap: 9px;

    border-bottom:
        1px solid var(--border);

}

.input {

    width: 100%;

    padding: 11px 12px;

    border-radius: 10px;

    border:
        1px solid var(--border);

    background: #09130f;

    color: white;

    outline: none;

    font-size: 12px;

}

.input:focus {

    border-color:
        rgba(41,211,145,.45);

}

/* ============================================================
CART
============================================================ */

.cart {

    flex: 1;

    overflow-y: auto;

    padding: 12px 22px;

}

.empty {

    height: 100%;

    display: grid;

    place-items: center;

    text-align: center;

    color: var(--muted);

}

.empty-icon {

    font-size: 44px;

    margin-bottom: 10px;

}

.cart-item {

    display: grid;

    grid-template-columns:
        43px 1fr auto;

    gap: 10px;

    align-items: center;

    padding: 12px 0;

    border-bottom:
        1px solid
        rgba(255,255,255,.05);

}

.cart-icon {

    width: 43px;

    height: 43px;

    display: grid;

    place-items: center;

    border-radius: 12px;

    background: #16231c;

    font-size: 21px;

}

.cart-name {

    font-size: 13px;

    font-weight: 900;

}

.cart-price {

    color: var(--muted);

    font-size: 10px;

    margin-top: 3px;

}

.qty {

    display: flex;

    align-items: center;

    gap: 7px;

    margin-top: 7px;

}

.qty button {

    width: 25px;

    height: 25px;

    border-radius: 8px;

    border:
        1px solid var(--border);

    background: #09130f;

    color: white;

    cursor: pointer;

}

.qty span {

    min-width: 17px;

    text-align: center;

    font-size: 12px;

    font-weight: 900;

}

.item-total {

    font-size: 13px;

    font-weight: 900;

}

.remove {

    margin-top: 5px;

    color: var(--red);

    background: transparent;

    border: 0;

    cursor: pointer;

    font-size: 11px;

}

/* ============================================================
SUMMARY
============================================================ */

.summary {

    padding: 17px 22px;

    border-top:
        1px solid var(--border);

}

.summary-row {

    display: flex;

    justify-content: space-between;

    color: var(--muted);

    font-size: 12px;

    margin-bottom: 9px;

}

.discount-row {

    display: flex;

    gap: 7px;

    margin:
        8px 0 14px;

}

.discount-input {

    flex: 1;

    padding: 10px;

    border-radius: 10px;

    background: #09130f;

    border:
        1px solid var(--border);

    color: white;

    outline: none;

}

.discount-btn {

    padding: 0 13px;

    border-radius: 10px;

    border:
        1px solid
        rgba(41,211,145,.18);

    background:
        rgba(41,211,145,.07);

    color: #86e9bf;

    cursor: pointer;

    font-size: 11px;

    font-weight: 900;

}

.total {

    display: flex;

    align-items: center;

    justify-content: space-between;

    padding-top: 12px;

    border-top:
        1px dashed
        rgba(255,255,255,.1);

}

.total span:first-child {

    font-weight: 900;

}

.total-value {

    color: var(--green);

    font-size: 25px;

    font-weight: 950;

}

/* ============================================================
PAYMENT
============================================================ */

.payment {

    padding:
        0 22px 17px;

}

.payment-title {

    color: var(--muted);

    font-size: 11px;

    margin-bottom: 8px;

}

.payment-methods {

    display: grid;

    grid-template-columns:
        repeat(3,1fr);

    gap: 7px;

}

.pay-btn {

    padding: 10px 5px;

    border-radius: 10px;

    background: #09130f;

    border:
        1px solid var(--border);

    color: var(--muted);

    cursor: pointer;

    font-size: 11px;

    font-weight: 800;

}

.pay-btn.active {

    color: white;

    border-color:
        rgba(41,211,145,.45);

    background:
        rgba(41,211,145,.10);

}

.cash-box {

    margin-top: 8px;

}

.change {

    min-height: 15px;

    color: #82e6bb;

    font-size: 11px;

    margin-top: 6px;

}

/* ============================================================
PRINT
============================================================ */

.print-btn {

    margin:
        0 22px 22px;

    padding: 14px;

    border: 0;

    border-radius: 13px;

    cursor: pointer;

    color: #06110c;

    background:
        linear-gradient(
            135deg,
            var(--green),
            #83efbd
        );

    font-size: 14px;

    font-weight: 950;

    box-shadow:
        0 10px 30px
        rgba(41,211,145,.16);

    transition: .2s;

}

.print-btn:hover {

    transform:
        translateY(-2px);

}

/* ============================================================
RECEIPT
============================================================ */

.receipt-print {

    display: none;

}

/* ============================================================
RESPONSIVE
============================================================ */

@media(max-width: 1050px) {

    .main {

        grid-template-columns: 1fr;

    }

    .bill-panel {

        position: relative;

        top: 0;

        height: auto;

        min-height: 650px;

    }

}

@media(max-width: 650px) {

    .header {

        padding: 0 14px;

    }

    .status {

        display: none;

    }

    .main {

        padding: 10px;

    }

    .menu-top {

        padding:
            18px 14px 0;

    }

    .menu-title {

        display: block;

    }

    .search {

        width: 100%;

        margin-top: 14px;

    }

    .products {

        padding:
            0 14px 14px;

        grid-template-columns:
            repeat(2,1fr);

        gap: 9px;

    }

    .product {

        padding: 10px;

    }

    .product-image {

        height: 80px;

        font-size: 37px;

    }

    .product-desc {

        display: none;

    }

    .customer {

        grid-template-columns: 1fr;

    }

}

/* ============================================================
PRINT STYLE
============================================================ */

@media print {

    body {

        background: white !important;

    }

    .header,
    .main {

        display: none !important;

    }

    .receipt-print {

        display: block !important;

        width: 80mm;

        margin: auto;

        background: white;

        color: black;

        font-family: Arial, sans-serif;

        font-size: 11px;

    }

    .receipt-title {

        text-align: center;

        font-size: 19px;

        font-weight: 900;

    }

    .receipt-subtitle {

        text-align: center;

        font-size: 9px;

        margin-top: 3px;

    }

    .receipt-line {

        border-top:
            1px dashed black;

        margin: 8px 0;

    }

    .receipt-info {

        font-size: 10px;

        line-height: 1.55;

    }

    .receipt-item {

        display: flex;

        justify-content: space-between;

        gap: 8px;

        margin: 5px 0;

    }

    .receipt-item-name {

        flex: 1;

    }

    .receipt-summary div {

        display: flex;

        justify-content: space-between;

        margin: 4px 0;

    }

    .receipt-total {

        font-size: 16px;

        font-weight: 900;

        margin-top: 7px;

    }

    .receipt-thanks {

        text-align: center;

        font-weight: 900;

        margin-top: 14px;

    }

    @page {

        size: 80mm auto;

        margin: 0;

    }

}

</style>

</head>


<body>

<!-- ============================================================
HEADER
============================================================ -->

<header class="header">

    <div class="brand">

        <div class="logo">
            🛒
        </div>

        <div>

            <h1>NOVA MART</h1>

            <p>
                Super Market • Point of Sale
            </p>

        </div>

    </div>


    <div class="status">

        <span class="status-dot"></span>

        POS ONLINE

    </div>

</header>


<!-- ============================================================
MAIN
============================================================ -->

<main class="main">


<section class="menu-panel">

    <div class="menu-top">

        <div class="menu-title">

            <div>

                <h2>
                    Products
                </h2>

                <p>
                    Select products to add them to the bill.
                </p>

            </div>


            <input
                id="search"
                class="search"
                placeholder="🔎 Search products..."
            >

        </div>


        <div class="categories">

            <button
                class="category active"
                data-category="All">

                All

            </button>


            <button
                class="category"
                data-category="Grocery">

                🛒 Grocery

            </button>


            <button
                class="category"
                data-category="Fruits">

                🍎 Fruits

            </button>


            <button
                class="category"
                data-category="Vegetables">

                🥦 Vegetables

            </button>


            <button
                class="category"
                data-category="Dairy">

                🥛 Dairy

            </button>


            <button
                class="category"
                data-category="Bakery">

                🍞 Bakery

            </button>


            <button
                class="category"
                data-category="Drinks">

                🥤 Drinks

            </button>


            <button
                class="category"
                data-category="Snacks">

                🍪 Snacks

            </button>


            <button
                class="category"
                data-category="Personal Care">

                🧴 Personal

            </button>

        </div>

    </div>


    <div
        id="products"
        class="products">
    </div>

</section>


<!-- ============================================================
BILL
============================================================ -->

<section class="bill-panel">


    <div class="bill-head">

        <div class="bill-head-row">

            <div>

                <h2>
                    Current Bill
                </h2>

                <div
                    id="billNumber"
                    class="bill-number">
                </div>

            </div>


            <button
                class="new-btn"
                onclick="newBill()">

                + New Bill

            </button>

        </div>

    </div>


    <div class="customer">

        <input
            id="customerName"
            class="input"
            placeholder="Customer name">

        <input
            id="customerPhone"
            class="input"
            placeholder="Phone number">

    </div>


    <div
        id="cart"
        class="cart">
    </div>


    <div class="summary">


        <div class="summary-row">

            <span>
                Subtotal
            </span>

            <span id="subtotal">
                ₹0.00
            </span>

        </div>


        <div class="summary-row">

            <span>
                Tax (5%)
            </span>

            <span id="tax">
                ₹0.00
            </span>

        </div>


        <div class="summary-row">

            <span>
                Discount
            </span>

            <span id="discount">
                -₹0.00
            </span>

        </div>


        <div class="discount-row">

            <input
                id="discountInput"
                class="discount-input"
                type="number"
                min="0"
                placeholder="Discount ₹">

            <button
                class="discount-btn"
                onclick="applyDiscount()">

                APPLY

            </button>

        </div>


        <div class="total">

            <span>
                TOTAL
            </span>

            <span
                id="total"
                class="total-value">

                ₹0.00

            </span>

        </div>

    </div>


    <div class="payment">

        <div class="payment-title">

            Payment Method

        </div>


        <div class="payment-methods">

            <button
                class="pay-btn active"
                data-pay="Cash">

                💵 Cash

            </button>


            <button
                class="pay-btn"
                data-pay="Card">

                💳 Card

            </button>


            <button
                class="pay-btn"
                data-pay="UPI">

                📱 UPI

            </button>

        </div>


        <div
            id="cashBox"
            class="cash-box">

            <input
                id="cashReceived"
                class="input"
                type="number"
                min="0"
                placeholder="Cash received">

            <div
                id="change"
                class="change">
            </div>

        </div>

    </div>


    <button
        class="print-btn"
        onclick="printBill()">

        🖨️ PRINT RECEIPT

    </button>


</section>

</main>


<!-- ============================================================
RECEIPT
============================================================ -->

<div
    id="receiptPrint"
    class="receipt-print">

    <div class="receipt-title">
        NOVA MART
    </div>

    <div class="receipt-subtitle">
        Super Market • Quality Everyday
    </div>

    <div class="receipt-line"></div>

    <div
        id="receiptInfo"
        class="receipt-info">
    </div>

    <div class="receipt-line"></div>

    <div
        id="receiptItems">
    </div>

    <div class="receipt-line"></div>

    <div
        id="receiptSummary"
        class="receipt-summary">
    </div>

    <div class="receipt-line"></div>

    <div
        id="receiptPayment"
        class="receipt-info">
    </div>

    <div class="receipt-thanks">
        Thank you for shopping with us! ❤️
    </div>

</div>


<script>

/* ============================================================
PRODUCT DATA
============================================================ */

const products = [

    {
        id: 1,
        name: "Basmati Rice 5kg",
        category: "Grocery",
        price: 499,
        icon: "🍚",
        desc: "Premium long grain basmati rice."
    },

    {
        id: 2,
        name: "Wheat Flour 5kg",
        category: "Grocery",
        price: 280,
        icon: "🌾",
        desc: "Fresh quality wheat flour."
    },

    {
        id: 3,
        name: "Cooking Oil 1L",
        category: "Grocery",
        price: 145,
        icon: "🫗",
        desc: "Refined cooking oil."
    },

    {
        id: 4,
        name: "Sugar 1kg",
        category: "Grocery",
        price: 52,
        icon: "🍬",
        desc: "Premium white sugar."
    },

    {
        id: 5,
        name: "Salt 1kg",
        category: "Grocery",
        price: 25,
        icon: "🧂",
        desc: "Iodized cooking salt."
    },

    {
        id: 6,
        name: "Red Apples 1kg",
        category: "Fruits",
        price: 180,
        icon: "🍎",
        desc: "Fresh red apples."
    },

    {
        id: 7,
        name: "Banana 1kg",
        category: "Fruits",
        price: 65,
        icon: "🍌",
        desc: "Fresh ripe bananas."
    },

    {
        id: 8,
        name: "Oranges 1kg",
        category: "Fruits",
        price: 110,
        icon: "🍊",
        desc: "Juicy fresh oranges."
    },

    {
        id: 9,
        name: "Watermelon",
        category: "Fruits",
        price: 80,
        icon: "🍉",
        desc: "Fresh sweet watermelon."
    },

    {
        id: 10,
        name: "Tomato 1kg",
        category: "Vegetables",
        price: 55,
        icon: "🍅",
        desc: "Fresh red tomatoes."
    },

    {
        id: 11,
        name: "Potato 1kg",
        category: "Vegetables",
        price: 48,
        icon: "🥔",
        desc: "Fresh farm potatoes."
    },

    {
        id: 12,
        name: "Carrot 1kg",
        category: "Vegetables",
        price: 70,
        icon: "🥕",
        desc: "Fresh crunchy carrots."
    },

    {
        id: 13,
        name: "Broccoli",
        category: "Vegetables",
        price: 90,
        icon: "🥦",
        desc: "Fresh green broccoli."
    },

    {
        id: 14,
        name: "Fresh Milk 1L",
        category: "Dairy",
        price: 65,
        icon: "🥛",
        desc: "Fresh full cream milk."
    },

    {
        id: 15,
        name: "Cheese 200g",
        category: "Dairy",
        price: 150,
        icon: "🧀",
        desc: "Creamy processed cheese."
    },

    {
        id: 16,
        name: "Butter 500g",
        category: "Dairy",
        price: 260,
        icon: "🧈",
        desc: "Smooth creamy butter."
    },

    {
        id: 17,
        name: "Bread",
        category: "Bakery",
        price: 45,
        icon: "🍞",
        desc: "Fresh soft bakery bread."
    },

    {
        id: 18,
        name: "Croissant",
        category: "Bakery",
        price: 70,
        icon: "🥐",
        desc: "Buttery French croissant."
    },

    {
        id: 19,
        name: "Chocolate Cake",
        category: "Bakery",
        price: 320,
        icon: "🍰",
        desc: "Rich chocolate cake."
    },

    {
        id: 20,
        name: "Mineral Water",
        category: "Drinks",
        price: 20,
        icon: "💧",
        desc: "Pure drinking water."
    },

    {
        id: 21,
        name: "Orange Juice",
        category: "Drinks",
        price: 90,
        icon: "🧃",
        desc: "Refreshing orange juice."
    },

    {
        id: 22,
        name: "Cola",
        category: "Drinks",
        price: 45,
        icon: "🥤",
        desc: "Chilled soft drink."
    },

    {
        id: 23,
        name: "Potato Chips",
        category: "Snacks",
        price: 40,
        icon: "🥔",
        desc: "Crispy potato chips."
    },

    {
        id: 24,
        name: "Cookies",
        category: "Snacks",
        price: 65,
        icon: "🍪",
        desc: "Crunchy chocolate cookies."
    },

    {
        id: 25,
        name: "Chocolate Bar",
        category: "Snacks",
        price: 50,
        icon: "🍫",
        desc: "Smooth milk chocolate."
    },

    {
        id: 26,
        name: "Shampoo",
        category: "Personal Care",
        price: 210,
        icon: "🧴",
        desc: "Daily care shampoo."
    },

    {
        id: 27,
        name: "Bath Soap",
        category: "Personal Care",
        price: 45,
        icon: "🧼",
        desc: "Gentle bathing soap."
    },

    {
        id: 28,
        name: "Toothpaste",
        category: "Personal Care",
        price: 110,
        icon: "🪥",
        desc: "Fresh mint toothpaste."
    }

];


/* ============================================================
STATE
============================================================ */

let cart = [];

let discountAmount = 0;

let paymentMethod = "Cash";

let billNumber =
    "NM-" +
    Date.now()
        .toString()
        .slice(-7);


/* ============================================================
ELEMENTS
============================================================ */

const productsEl =
    document.getElementById(
        "products"
    );

const cartEl =
    document.getElementById(
        "cart"
    );

const searchEl =
    document.getElementById(
        "search"
    );

const billNumberEl =
    document.getElementById(
        "billNumber"
    );

const customerNameEl =
    document.getElementById(
        "customerName"
    );

const customerPhoneEl =
    document.getElementById(
        "customerPhone"
    );

const subtotalEl =
    document.getElementById(
        "subtotal"
    );

const taxEl =
    document.getElementById(
        "tax"
    );

const discountEl =
    document.getElementById(
        "discount"
    );

const totalEl =
    document.getElementById(
        "total"
    );

const cashReceivedEl =
    document.getElementById(
        "cashReceived"
    );

const changeEl =
    document.getElementById(
        "change"
    );

const cashBox =
    document.getElementById(
        "cashBox"
    );


billNumberEl.textContent =
    "Bill #" + billNumber;


/* ============================================================
MONEY
============================================================ */

function money(value) {

    return "₹" +
        Number(value).toLocaleString(
            "en-IN",
            {
                minimumFractionDigits: 2,
                maximumFractionDigits: 2
            }
        );

}


/* ============================================================
RENDER PRODUCTS
============================================================ */

function renderProducts(
    category = "All",
    search = ""
) {

    const filtered =
        products.filter(item => {

            const categoryMatch =
                category === "All" ||
                item.category === category;

            const searchMatch =
                item.name
                    .toLowerCase()
                    .includes(
                        search.toLowerCase()
                    );

            return (
                categoryMatch &&
                searchMatch
            );

        });


    if (!filtered.length) {

        productsEl.innerHTML = `

            <div style="
                grid-column:1/-1;
                padding:50px;
                text-align:center;
                color:#8fa39a;
            ">

                🔎

                <div style="
                    margin-top:10px;
                    font-weight:800;
                ">
                    No products found
                </div>

            </div>

        `;

        return;

    }


    productsEl.innerHTML =
        filtered.map(item => `

            <article
                class="product"
                onclick="addToCart(${item.id})">

                <div class="product-image">
                    ${item.icon}
                </div>

                <div class="product-name">
                    ${item.name}
                </div>

                <div class="product-desc">
                    ${item.desc}
                </div>

                <div class="product-bottom">

                    <div class="price">
                        ${money(item.price)}
                    </div>

                    <button
                        class="add-btn"
                        onclick="
                            event.stopPropagation();
                            addToCart(${item.id});
                        ">

                        +

                    </button>

                </div>

            </article>

        `).join("");

}


/* ============================================================
ADD
============================================================ */

function addToCart(id) {

    const product =
        products.find(
            item => item.id === id
        );

    if (!product) return;


    const existing =
        cart.find(
            item => item.id === id
        );


    if (existing) {

        existing.qty++;

    } else {

        cart.push({
            ...product,
            qty: 1
        });

    }


    renderCart();

}


/* ============================================================
QUANTITY
============================================================ */

function changeQty(
    id,
    amount
) {

    const item =
        cart.find(
            x => x.id === id
        );

    if (!item) return;


    item.qty += amount;


    if (item.qty <= 0) {

        cart =
            cart.filter(
                x => x.id !== id
            );

    }


    renderCart();

}


/* ============================================================
REMOVE
============================================================ */

function removeItem(id) {

    cart =
        cart.filter(
            item => item.id !== id
        );

    renderCart();

}


/* ============================================================
CART
============================================================ */

function renderCart() {

    if (!cart.length) {

        cartEl.innerHTML = `

            <div class="empty">

                <div>

                    <div class="empty-icon">
                        🛒
                    </div>

                    <div>
                        Cart is empty
                    </div>

                    <div style="
                        margin-top:5px;
                        font-size:11px;
                    ">
                        Add products to start billing.
                    </div>

                </div>

            </div>

        `;

        updateSummary();

        return;

    }


    cartEl.innerHTML =
        cart.map(item => `

            <div class="cart-item">

                <div class="cart-icon">
                    ${item.icon}
                </div>

                <div>

                    <div class="cart-name">
                        ${item.name}
                    </div>

                    <div class="cart-price">
                        ${money(item.price)}
                    </div>

                    <div class="qty">

                        <button
                            onclick="
                                changeQty(
                                    ${item.id},
                                    -1
                                )
                            ">

                            −

                        </button>

                        <span>
                            ${item.qty}
                        </span>

                        <button
                            onclick="
                                changeQty(
                                    ${item.id},
                                    1
                                )
                            ">

                            +

                        </button>

                    </div>

                </div>


                <div style="
                    text-align:right;
                ">

                    <div class="item-total">
                        ${money(
                            item.price *
                            item.qty
                        )}
                    </div>

                    <button
                        class="remove"
                        onclick="
                            removeItem(
                                ${item.id}
                            )
                        ">

                        Remove

                    </button>

                </div>

            </div>

        `).join("");


    updateSummary();

}


/* ============================================================
TOTAL
============================================================ */

function calculateSubtotal() {

    return cart.reduce(
        (sum, item) =>
            sum +
            item.price *
            item.qty,
        0
    );

}


function calculateTax() {

    return calculateSubtotal() * 0.05;

}


function calculateTotal() {

    return Math.max(
        0,
        calculateSubtotal() +
        calculateTax() -
        discountAmount
    );

}


/* ============================================================
SUMMARY
============================================================ */

function updateSummary() {

    const subtotal =
        calculateSubtotal();

    const tax =
        calculateTax();

    const total =
        calculateTotal();


    subtotalEl.textContent =
        money(subtotal);

    taxEl.textContent =
        money(tax);

    discountEl.textContent =
        "-" +
        money(discountAmount);

    totalEl.textContent =
        money(total);


    updateChange(total);

}


/* ============================================================
DISCOUNT
============================================================ */

function applyDiscount() {

    const value =
        Number(
            document.getElementById(
                "discountInput"
            ).value
        );


    discountAmount =
        Math.max(
            0,
            Number.isFinite(value)
                ? value
                : 0
        );


    updateSummary();

}


/* ============================================================
PAYMENT
============================================================ */

document
    .querySelectorAll(".pay-btn")
    .forEach(button => {

        button.addEventListener(
            "click",
            () => {

                document
                    .querySelectorAll(
                        ".pay-btn"
                    )
                    .forEach(
                        btn =>
                            btn.classList
                                .remove(
                                    "active"
                                )
                    );


                button.classList.add(
                    "active"
                );


                paymentMethod =
                    button.dataset.pay;


                if (
                    paymentMethod ===
                    "Cash"
                ) {

                    cashBox.style.display =
                        "block";

                } else {

                    cashBox.style.display =
                        "none";

                    changeEl.textContent =
                        "";

                }

            }
        );

    });


/* ============================================================
CHANGE
============================================================ */

cashReceivedEl.addEventListener(
    "input",
    () => {

        updateChange(
            calculateTotal()
        );

    }
);


function updateChange(total) {

    if (
        paymentMethod !==
        "Cash"
    ) {

        changeEl.textContent =
            "";

        return;

    }


    const cash =
        Number(
            cashReceivedEl.value
        );


    if (!cash) {

        changeEl.textContent =
            "Enter cash received.";

        return;

    }


    const difference =
        cash - total;


    if (difference >= 0) {

        changeEl.textContent =
            "Change: " +
            money(difference);

    } else {

        changeEl.textContent =
            "Remaining: " +
            money(
                Math.abs(difference)
            );

    }

}


/* ============================================================
CATEGORIES
============================================================ */

let currentCategory =
    "All";


document
    .querySelectorAll(".category")
    .forEach(button => {

        button.addEventListener(
            "click",
            () => {

                document
                    .querySelectorAll(
                        ".category"
                    )
                    .forEach(
                        btn =>
                            btn.classList
                                .remove(
                                    "active"
                                )
                    );


                button.classList.add(
                    "active"
                );


                currentCategory =
                    button.dataset.category;


                renderProducts(
                    currentCategory,
                    searchEl.value
                );

            }
        );

    });


/* ============================================================
SEARCH
============================================================ */

searchEl.addEventListener(
    "input",
    () => {

        renderProducts(
            currentCategory,
            searchEl.value
        );

    }
);


/* ============================================================
NEW BILL
============================================================ */

function newBill() {

    if (
        cart.length &&
        !confirm(
            "Start a new bill? Current bill will be cleared."
        )
    ) {

        return;

    }


    cart = [];

    discountAmount = 0;

    paymentMethod = "Cash";


    document.getElementById(
        "discountInput"
    ).value = "";


    cashReceivedEl.value = "";


    customerNameEl.value = "";

    customerPhoneEl.value = "";


    billNumber =
        "NM-" +
        Date.now()
            .toString()
            .slice(-7);


    billNumberEl.textContent =
        "Bill #" + billNumber;


    document
        .querySelectorAll(
            ".pay-btn"
        )
        .forEach(
            btn =>
                btn.classList
                    .remove("active")
        );


    document
        .querySelector(
            '[data-pay="Cash"]'
        )
        .classList.add(
            "active"
        );


    cashBox.style.display =
        "block";


    renderCart();

}


/* ============================================================
RECEIPT
============================================================ */

function prepareReceipt() {

    const name =
        customerNameEl.value.trim() ||
        "Walk-in Customer";


    const phone =
        customerPhoneEl.value.trim() ||
        "-";


    const now =
        new Date();


    const date =
        now.toLocaleDateString(
            "en-IN"
        );


    const time =
        now.toLocaleTimeString(
            "en-IN",
            {
                hour: "2-digit",
                minute: "2-digit"
            }
        );


    document.getElementById(
        "receiptInfo"
    ).innerHTML = `

        <div>
            Bill: ${billNumber}
        </div>

        <div>
            Date: ${date}
        </div>

        <div>
            Time: ${time}
        </div>

        <div>
            Customer: ${name}
        </div>

        <div>
            Phone: ${phone}
        </div>

    `;


    document.getElementById(
        "receiptItems"
    ).innerHTML =
        cart.map(
            item => `

                <div class="receipt-item">

                    <span
                        class="receipt-item-name">

                        ${item.name}
                        × ${item.qty}

                    </span>

                    <span>

                        ${money(
                            item.price *
                            item.qty
                        )}

                    </span>

                </div>

            `
        ).join("");


    const subtotal =
        calculateSubtotal();

    const tax =
        calculateTax();

    const total =
        calculateTotal();


    document.getElementById(
        "receiptSummary"
    ).innerHTML = `

        <div>
            <span>Subtotal</span>
            <span>
                ${money(subtotal)}
            </span>
        </div>

        <div>
            <span>Tax 5%</span>
            <span>
                ${money(tax)}
            </span>
        </div>

        <div>
            <span>Discount</span>
            <span>
                -${money(discountAmount)}
            </span>
        </div>

        <div
            class="receipt-total"
            style="
                display:flex;
                justify-content:space-between;
            ">

            <span>TOTAL</span>

            <span>
                ${money(total)}
            </span>

        </div>

    `;


    let payment =
        "Payment: " +
        paymentMethod;


    if (
        paymentMethod ===
        "Cash"
    ) {

        const cash =
            Number(
                cashReceivedEl.value
            );


        const change =
            Math.max(
                0,
                cash - total
            );


        payment += `

            <br>
            Cash: ${money(cash)}

            <br>
            Change: ${money(change)}

        `;

    }


    document.getElementById(
        "receiptPayment"
    ).innerHTML =
        payment;

}


/* ============================================================
PRINT BILL
============================================================ */

function printBill() {

    if (!cart.length) {

        alert(
            "Please add products before printing."
        );

        return;

    }


    const total =
        calculateTotal();


    if (
        paymentMethod ===
        "Cash"
    ) {

        const cash =
            Number(
                cashReceivedEl.value
            );


        if (cash < total) {

            alert(
                "Cash received is less than the total."
            );

            return;

        }

    }


    prepareReceipt();


    setTimeout(
        () => window.print(),
        100
    );

}


/* ============================================================
KEYBOARD SHORTCUTS
============================================================ */

document.addEventListener(
    "keydown",
    event => {

        if (
            event.key === "F2"
        ) {

            event.preventDefault();

            newBill();

        }


        if (
            event.ctrlKey &&
            event.key.toLowerCase() === "p"
        ) {

            event.preventDefault();

            printBill();

        }

    }
);


/* ============================================================
START
============================================================ */

renderProducts();

renderCart();

</script>

</body>
</html>
"""


# ============================================================
# STREAMLIT
# ============================================================

components.html(
    HTML,
    height=1200,
    scrolling=True
)
