
-- 1. Total sales summary
SELECT
    COUNT(*) AS total_orders,
    SUM(quantity) AS total_items_sold,
    SUM(total_sales) AS total_revenue
FROM `bright-eon-515118-r5.retail_sales_dw.fact_sales`;


-- 2. Product-wise revenue
SELECT
    p.product_name,
    SUM(f.total_sales) AS total_revenue
FROM `bright-eon-515118-r5.retail_sales_dw.fact_sales` f
JOIN `bright-eon-515118-r5.retail_sales_dw.dim_product` p
    ON f.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_revenue DESC;


-- 3. Monthly revenue
SELECT
    d.year,
    d.month,
    SUM(f.total_sales) AS monthly_revenue,
    COUNT(DISTINCT f.order_id) AS total_orders
FROM `bright-eon-515118-r5.retail_sales_dw.fact_sales` f
JOIN `bright-eon-515118-r5.retail_sales_dw.dim_date` d
    ON f.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY d.year, d.month;
